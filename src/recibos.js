import { revocado } from "./legal.js";
// Créditos del generador de recibos y presupuestos: cada pago aprobado de Mercado Pago (ref recibos2026) da 10 documentos.
// D1 guarda cuántos se usaron por pago. El PDF se arma en el navegador; el servidor solo descuenta el crédito.
const REF = "recibos2026", PRECIO = 990, CREDITOS = 10;
const api = (env) => env.MP_API || "https://api.mercadopago.com";
const json = (o, status = 200) => Response.json(o, { status, headers: { "cache-control": "no-store" } });

let listo;
function db(env) {
  listo ||= env.DB.prepare("CREATE TABLE IF NOT EXISTS creditos (pago TEXT PRIMARY KEY, total INTEGER NOT NULL, usados INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL)").run()
    .catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

async function pagoOk(env, id) {
  try {
    const r = await fetch(`${api(env)}/v1/payments/${id}`, { headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}` } });
    if (!r.ok) return false;
    const p = await r.json();
    return p.external_reference === REF && p.status === "approved" && p.transaction_amount >= PRECIO;
  } catch { return false; }
}

// Devuelve { id, restan } o null si el pago no existe o no está aprobado.
async function pack(env, d, id) {
  if (await revocado(env, id)) return null;
  let row = await d.prepare("SELECT total, usados FROM creditos WHERE pago=?").bind(id).first();
  if (!row) {
    if (!(await pagoOk(env, id))) return null;
    await d.prepare("INSERT OR IGNORE INTO creditos (pago,total,usados,created) VALUES (?,?,0,?)").bind(id, CREDITOS, Math.floor(Date.now() / 1000)).run();
    row = await d.prepare("SELECT total, usados FROM creditos WHERE pago=?").bind(id).first();
  }
  return { id, restan: row.total - row.usados };
}

const ids = (v) => [...new Set(String(v || "").split(",").filter((x) => /^\d{1,20}$/.test(x)))].slice(0, 20);

export async function manejarRecibos(req, env) {
  const url = new URL(req.url);
  if (!url.pathname.startsWith("/recibos/api/")) return null;
  if (!env.DB) return json({ error: "Servicio no disponible" }, 503);
  const d = await db(env);

  if (url.pathname === "/recibos/api/saldo" && req.method === "GET") {
    const packs = (await Promise.all(ids(url.searchParams.get("ids")).map((i) => pack(env, d, i)))).filter(Boolean);
    return json({ saldo: packs.reduce((s, p) => s + p.restan, 0), packs });
  }

  if (url.pathname === "/recibos/api/usar" && req.method === "POST") {
    const body = await req.json().catch(() => ({}));
    for (const i of ids((body.ids || []).join?.(",") ?? "")) {
      const p = await pack(env, d, i);
      if (!p || p.restan <= 0) continue;
      const r = await d.prepare("UPDATE creditos SET usados=usados+1 WHERE pago=? AND usados<total").bind(i).run();
      if (r.meta.changes) {
        const packs = (await Promise.all(ids((body.ids || []).join(",")).map((x) => pack(env, d, x)))).filter(Boolean);
        return json({ ok: true, saldo: packs.reduce((s, q) => s + q.restan, 0) });
      }
    }
    return json({ ok: false, error: "Sin créditos" }, 402);
  }
  return json({ error: "No encontrado" }, 404);
}
