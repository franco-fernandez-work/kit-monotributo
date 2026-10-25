// Pedidos de documentos y herramientas: el visitante describe lo que necesita, sin email ni respuesta.
// D1 guarda el pedido; los parecidos suman un voto en vez de duplicarse. Lectura privada en /pedidos/admin?k=PEDIDOS_KEY.
const MAX_PEDIDOS = 5000, POR_HORA = 5;
const json = (o, status = 200) => Response.json(o, { status, headers: { "cache-control": "no-store" } });
const limpio = (v, n) => String(v || "").replace(/[\u0000-\u001f<>]/g, " ").replace(/\s+/g, " ").trim().slice(0, n);
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);
const TIPOS = ["documento", "planilla", "calculadora", "otro"];
const VACIAS = new Set("para como cual cuando donde esta este esto estos que con una uno unos unas los las del por mas muy sin sobre desde hasta quiero necesito busco hacer tener algo modelo".split(" "));

let listo;
function db(env) {
  listo ||= env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS pedidos (id INTEGER PRIMARY KEY AUTOINCREMENT, texto TEXT NOT NULL, tipo TEXT NOT NULL, clave TEXT NOT NULL, votos INTEGER NOT NULL DEFAULT 1, created INTEGER NOT NULL, ultimo INTEGER NOT NULL)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS pedidos_votos (pedido INTEGER NOT NULL, ip TEXT NOT NULL, created INTEGER NOT NULL, PRIMARY KEY (pedido, ip))"),
  ]).catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

const palabras = (t) => new Set(t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9 ]/g, " ").split(" ").filter((w) => w.length > 3 && !VACIAS.has(w)));
const parecido = (a, b) => { let i = 0; for (const w of a) if (b.has(w)) i++; return i / (a.size + b.size - i || 1); };
async function hash(s) { const b = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s)); return [...new Uint8Array(b)].slice(0, 12).map((x) => x.toString(16).padStart(2, "0")).join(""); }

async function enviar(req, env) {
  if (req.method !== "POST") return json({ ok: false, mensaje: "Método no permitido." }, 405);
  if (!env.DB) return json({ ok: false, mensaje: "Servicio no disponible. Probá de nuevo más tarde." }, 503);
  const b = await req.json().catch(() => ({}));
  if (b.web) return json({ ok: true, mensaje: "Recibido." });
  if (Date.now() - Number(b.t) < 3000) return json({ ok: false, mensaje: "Fue muy rápido. Probá de nuevo." }, 429);
  const texto = limpio(b.texto, 400);
  if (texto.length < 15) return json({ ok: false, mensaje: "Contanos un poco más: qué documento o herramienta necesitás y para qué (mínimo 15 caracteres)." }, 400);
  if (/https?:|www\.|@/i.test(texto)) return json({ ok: false, mensaje: "Describí lo que necesitás sin enlaces ni emails." }, 400);
  const tipo = TIPOS.includes(b.tipo) ? b.tipo : "otro";
  const clave = [...palabras(texto)];
  if (clave.length < 2) return json({ ok: false, mensaje: "Describí con más detalle lo que necesitás." }, 400);

  const d = await db(env);
  const ip = await hash((req.headers.get("cf-connecting-ip") || "?") + (env.PEDIDOS_KEY || "sal"));
  const ahora = Math.floor(Date.now() / 1000);
  const n = await d.prepare("SELECT COUNT(*) c FROM pedidos_votos WHERE ip=? AND created>?").bind(ip, ahora - 3600).first();
  if (n.c >= POR_HORA) return json({ ok: false, mensaje: "Ya mandaste varios pedidos. Probá de nuevo en un rato." }, 429);

  const { results } = await d.prepare("SELECT id, clave FROM pedidos ORDER BY ultimo DESC LIMIT 500").all();
  const mios = new Set(clave);
  let par = null, mejor = 0.5;
  for (const r of results) { const s = parecido(mios, new Set(r.clave.split(" "))); if (s >= mejor) { mejor = s; par = r.id; } }
  if (par) {
    const v = await d.prepare("INSERT OR IGNORE INTO pedidos_votos (pedido,ip,created) VALUES (?,?,?)").bind(par, ip, ahora).run();
    if (v.meta.changes) await d.prepare("UPDATE pedidos SET votos=votos+1, ultimo=? WHERE id=?").bind(ahora, par).run();
    return json({ ok: true, mensaje: "Ya había un pedido parecido y sumamos tu voto. Los pedidos con más votos se hacen primero." });
  }
  const tot = await d.prepare("SELECT COUNT(*) c FROM pedidos").first();
  if (tot.c >= MAX_PEDIDOS) return json({ ok: false, mensaje: "Estamos recibiendo muchos pedidos. Probá más adelante." }, 503);
  const r = await d.prepare("INSERT INTO pedidos (texto,tipo,clave,votos,created,ultimo) VALUES (?,?,?,1,?,?)").bind(texto, tipo, clave.join(" "), ahora, ahora).run();
  await d.prepare("INSERT OR IGNORE INTO pedidos_votos (pedido,ip,created) VALUES (?,?,?)").bind(r.meta.last_row_id, ip, ahora).run();
  return json({ ok: true, mensaje: "Pedido registrado. No respondemos de forma personal: si sale un producto parecido, lo vas a ver publicado en el sitio." });
}

async function admin(url, env) {
  const k = url.searchParams.get("k") || "";
  const nada = () => new Response("No encontrado", { status: 404 });
  if (!env.PEDIDOS_KEY || k.length !== env.PEDIDOS_KEY.length) return nada();
  let dif = 0;
  for (let i = 0; i < k.length; i++) dif |= k.charCodeAt(i) ^ env.PEDIDOS_KEY.charCodeAt(i);
  if (dif) return nada();
  const d = await db(env);
  const { results } = await d.prepare("SELECT id, texto, tipo, votos, created, ultimo FROM pedidos ORDER BY votos DESC, ultimo DESC LIMIT 1000").all();
  const h = { "cache-control": "no-store", "x-robots-tag": "noindex" };
  if (url.searchParams.get("fmt") === "json") return Response.json(results, { headers: h });
  const f = (t) => new Date(t * 1000).toISOString().slice(0, 10);
  const filas = results.map((r) => `<tr><td>${r.votos}</td><td>${esc(r.tipo)}</td><td>${esc(r.texto)}</td><td>${f(r.created)}</td></tr>`).join("");
  return new Response(`<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><title>Pedidos</title><style>body{font:15px system-ui;margin:20px}td,th{border-bottom:1px solid #ccc;padding:6px 10px;text-align:left}</style><h1>Pedidos (${results.length})</h1><table><tr><th>Votos</th><th>Tipo</th><th>Pedido</th><th>Fecha</th></tr>${filas}</table>`, { headers: { ...h, "content-type": "text/html; charset=utf-8" } });
}

export async function manejarPedidos(req, env) {
  const url = new URL(req.url);
  if (url.pathname === "/pedidos/enviar") return enviar(req, env);
  if (url.pathname === "/pedidos/admin" && req.method === "GET") return env.DB ? admin(url, env) : new Response("No encontrado", { status: 404 });
  return null;
}
