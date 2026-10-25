// Botón de arrepentimiento (Res. SCI 424/2020): POST /arrepentimiento/enviar verifica el pago en Mercado Pago,
// registra la solicitud en D1, revoca la descarga y ordena el reembolso total. Sin intervención humana.
const PLAZO_DIAS = 10;
const api = (env) => env.MP_API || "https://api.mercadopago.com";
const json = (o, status = 200) => Response.json(o, { status, headers: { "cache-control": "no-store" } });

let listo;
function db(env) {
  listo ||= env.DB.prepare("CREATE TABLE IF NOT EXISTS arrepentimientos (pago TEXT PRIMARY KEY, codigo TEXT NOT NULL, nombre TEXT, email TEXT, motivo TEXT, reembolso TEXT NOT NULL, created INTEGER NOT NULL)").run()
    .catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

// true si el pago fue revocado por arrepentimiento (la descarga y los créditos quedan desactivados).
export async function revocado(env, id) {
  if (!env.DB) return false;
  try {
    const d = await db(env);
    return !!(await d.prepare("SELECT 1 FROM arrepentimientos WHERE pago=?").bind(String(id)).first());
  } catch { return false; }
}

const limpio = (v, n) => String(v || "").replace(/[\u0000-\u001f<>]/g, " ").trim().slice(0, n);

async function reembolsar(env, pago) {
  try {
    const r = await fetch(`${api(env)}/v1/payments/${pago}/refunds`, {
      method: "POST",
      headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}`, "content-type": "application/json", "X-Idempotency-Key": `arrep-${pago}` },
      body: "{}",
    });
    return r.ok;
  } catch { return false; }
}

// Si el pago era de una suscripción de QR, da de baja la suscripción para que no cobre el mes siguiente.
async function bajaQR(env, d, ref) {
  try {
    const fila = await d.prepare("SELECT preapproval FROM qr WHERE id=?").bind(ref).first();
    if (!fila?.preapproval) return;
    await fetch(`${api(env)}/preapproval/${fila.preapproval}`, {
      method: "PUT",
      headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}`, "content-type": "application/json" },
      body: JSON.stringify({ status: "cancelled" }),
    });
  } catch {}
}

const fechaAR = (t) => new Date(t * 1000).toLocaleString("es-AR", { timeZone: "America/Argentina/Buenos_Aires" });
const fin = (fila) => ({ ok: true, codigo: fila.codigo, fecha: fechaAR(fila.created), mensaje: fila.reembolso === "ordenado" ? "Registramos tu arrepentimiento. El reembolso total ya fue ordenado a Mercado Pago y la descarga quedó desactivada. Guardá el código de constancia." : "Registramos tu arrepentimiento y desactivamos la descarga. El reembolso no se pudo ordenar en este momento: volvé a enviar el formulario con el mismo código de pago en unos minutos y se reintenta solo." });

export async function manejarLegal(req, env, refsValidas) {
  const url = new URL(req.url);
  if (url.pathname !== "/arrepentimiento/enviar") return null;
  if (req.method !== "POST") return json({ ok: false, mensaje: "Método no permitido." }, 405);
  if (!env.DB) return json({ ok: false, mensaje: "Servicio no disponible. Probá de nuevo más tarde." }, 503);
  const b = await req.json().catch(() => ({}));
  if (b.web) return json({ ok: true, mensaje: "Recibido." });
  const pago = limpio(b.pago, 20).replace(/\s/g, "");
  const nombre = limpio(b.nombre, 120);
  if (!/^\d{5,20}$/.test(pago)) return json({ ok: false, mensaje: "Ingresá el código de pago de Mercado Pago (solo números)." }, 400);
  if (nombre.length < 3) return json({ ok: false, mensaje: "Ingresá tu nombre y apellido." }, 400);
  const email = limpio(b.email, 120);
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ ok: false, mensaje: "El email no es válido." }, 400);

  const d = await db(env);
  let fila = await d.prepare("SELECT * FROM arrepentimientos WHERE pago=?").bind(pago).first();
  if (!fila) {
    let p;
    try {
      const r = await fetch(`${api(env)}/v1/payments/${pago}`, { headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}` } });
      if (r.ok) p = await r.json();
    } catch {}
    const propio = p && (refsValidas.includes(p.external_reference) || (await d.prepare("SELECT 1 FROM qr WHERE id=?").bind(String(p.external_reference)).first().catch(() => null)));
    if (!p || !propio || p.status !== "approved") return json({ ok: false, mensaje: "No encontramos un pago aprobado con ese código. Revisalo en tu comprobante de Mercado Pago." }, 404);
    if (Date.now() - Date.parse(p.date_approved) > PLAZO_DIAS * 864e5) return json({ ok: false, mensaje: "Pasaron más de 10 días corridos desde el pago, así que ya no corre el plazo de arrepentimiento. Te quedan el reclamo ante Defensa del Consumidor y la baja de la suscripción desde Mercado Pago." }, 410);
    const codigo = "ARR-" + crypto.randomUUID().slice(0, 8).toUpperCase();
    const ahora = Math.floor(Date.now() / 1000);
    await d.prepare("INSERT OR IGNORE INTO arrepentimientos (pago,codigo,nombre,email,motivo,reembolso,created) VALUES (?,?,?,?,?,?,?)").bind(pago, codigo, nombre, email, limpio(b.motivo, 300), "pendiente", ahora).run();
    await bajaQR(env, d, String(p.external_reference));
    fila = await d.prepare("SELECT * FROM arrepentimientos WHERE pago=?").bind(pago).first();
  }
  if (fila.reembolso !== "ordenado" && env.ARREP_REEMBOLSO !== "0" && (await reembolsar(env, pago))) {
    await d.prepare("UPDATE arrepentimientos SET reembolso='ordenado' WHERE pago=?").bind(pago).run();
    fila.reembolso = "ordenado";
  }
  return json(fin(fila));
}
