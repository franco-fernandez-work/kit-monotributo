// Límites de uso sin servicios externos: contadores en D1 (ventana fija desde el primer pedido), caché de pagos inexistentes
// y registro de descargas por pago. Si D1 falla, los límites se saltan (no se bloquea una compra por un error propio).
let listo;
function db(env) {
  listo ||= env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS limites (k TEXT PRIMARY KEY, n INTEGER NOT NULL, hasta INTEGER NOT NULL)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS descargas (pago TEXT PRIMARY KEY, n INTEGER NOT NULL, primera INTEGER NOT NULL, ultima INTEGER NOT NULL)"),
  ]).catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

const ahora = () => Math.floor(Date.now() / 1000);
async function hash(s) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)); return [...new Uint8Array(b)].slice(0, 12).map((x) => x.toString(16).padStart(2, "0")).join(""); }

// true si la clave superó `max` pedidos dentro de `seg` segundos.
export async function limitarClave(env, clave, max, seg) {
  if (!env.DB) return false;
  try {
    const d = await db(env);
    const t = ahora();
    const r = await d.prepare("INSERT INTO limites (k,n,hasta) VALUES (?,1,?) ON CONFLICT(k) DO UPDATE SET n=CASE WHEN hasta<? THEN 1 ELSE n+1 END, hasta=CASE WHEN hasta<? THEN ? ELSE hasta END RETURNING n")
      .bind(clave, t + seg, t, t, t + seg).first();
    if (Math.random() < 0.02) await d.prepare("DELETE FROM limites WHERE hasta<?").bind(t).run();
    return r.n > max;
  } catch { return false; }
}

// Límite por IP (hash con sal; no se guarda la IP).
export async function limitar(env, req, nombre, max, seg) {
  const ip = await hash((req.headers.get("cf-connecting-ip") || "?") + (env.PEDIDOS_KEY || "sal"));
  return limitarClave(env, `${nombre}:${ip}`, max, seg);
}

// Caché de pagos que Mercado Pago dijo que no existen (evita repetir la consulta con el token de Franco).
export async function pagoInexistente(env, id) {
  if (!env.DB) return false;
  try {
    const d = await db(env);
    return !!(await d.prepare("SELECT 1 FROM limites WHERE k=? AND hasta>?").bind(`neg:${id}`, ahora()).first());
  } catch { return false; }
}
export async function marcarInexistente(env, id) {
  if (!env.DB) return;
  try {
    const d = await db(env);
    await d.prepare("INSERT INTO limites (k,n,hasta) VALUES (?,1,?) ON CONFLICT(k) DO UPDATE SET hasta=excluded.hasta").bind(`neg:${id}`, ahora() + 600).run();
  } catch {}
}

export const MAX_DESCARGAS = 5;

// Registra una descarga del pago. Devuelve false si ya se llegó al tope.
export async function registrarDescarga(env, pago) {
  if (!env.DB) return true;
  try {
    const d = await db(env);
    const t = ahora();
    const r = await d.prepare("INSERT INTO descargas (pago,n,primera,ultima) VALUES (?,1,?,?) ON CONFLICT(pago) DO UPDATE SET n=n+1, ultima=excluded.ultima WHERE n<? RETURNING n")
      .bind(String(pago), t, t, MAX_DESCARGAS).first();
    return !!r;
  } catch { return true; }
}

// true si el pago ya descargó el archivo o usó créditos del generador de recibos.
export async function yaDescargo(env, pago) {
  if (!env.DB) return false;
  const d = await db(env);
  if (await d.prepare("SELECT 1 FROM descargas WHERE pago=?").bind(String(pago)).first()) return true;
  try {
    return !!(await d.prepare("SELECT 1 FROM creditos WHERE pago=? AND usados>0").bind(String(pago)).first());
  } catch { return false; }
}
