// Redirecciones de los QR dinámicos, aisladas de la tienda: si un destino hace que Google marque este host,
// kit-monotributo.*.workers.dev no se ve afectado. Solo lee D1 (el estado de la suscripción lo mantiene el cron del worker
// principal) y no tiene token de Mercado Pago. Revalida el destino en cada redirección (DNS de seguridad y Safe Browsing si hay SB_KEY).
const DOH = "https://security.cloudflare-dns.com/dns-query";
const SB_TTL = 3600;

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const pagina = (titulo, texto, status) =>
  new Response(`<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>${esc(titulo)}</title><style>body{font:18px/1.5 system-ui,sans-serif;max-width:560px;margin:12vh auto;padding:0 20px;color:#222}a{color:#0a58ca}</style></head><body><h1>${esc(titulo)}</h1><p>${esc(texto)}</p></body></html>`,
    { status, headers: { "content-type": "text/html; charset=utf-8", "x-robots-tag": "noindex", "cache-control": "no-store", "referrer-policy": "no-referrer" } });

let listo;
function db(env) {
  listo ||= env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS qr (id TEXT PRIMARY KEY, token TEXT UNIQUE NOT NULL, email TEXT NOT NULL, dest TEXT NOT NULL, preapproval TEXT, st TEXT NOT NULL DEFAULT 'pending', st_at INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS scans (id TEXT NOT NULL, day TEXT NOT NULL, country TEXT NOT NULL, n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY (id, day, country))"),
  ]).catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

async function dohBloqueado(host) {
  const r = await fetch(`${DOH}?name=${encodeURIComponent(host)}&type=A`, { headers: { accept: "application/dns-json" }, cf: { cacheTtl: 300, cacheEverything: true } });
  if (!r.ok) throw new Error("doh");
  const j = await r.json();
  return (j.Answer || []).some((a) => a.data === "0.0.0.0");
}

// Safe Browsing con caché de 1 h por destino (Cache API, sin costo).
async function sbBloqueado(env, destino) {
  if (!env.SB_KEY) return false;
  const clave = new Request("https://sb-cache.invalid/" + encodeURIComponent(destino));
  const cache = caches.default;
  const hit = await cache.match(clave);
  if (hit) return (await hit.text()) === "1";
  const r = await fetch(`https://safebrowsing.googleapis.com/v4/threatMatches:find?key=${env.SB_KEY}`, {
    method: "POST",
    body: JSON.stringify({
      client: { clientId: "qr-dinamicos", clientVersion: "1" },
      threatInfo: { threatTypes: ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"], platformTypes: ["ANY_PLATFORM"], threatEntryTypes: ["URL"], threatEntries: [{ url: destino }] },
    }),
  }).catch(() => null);
  if (!r?.ok) return false;
  const malo = !!(await r.json()).matches?.length;
  await cache.put(clave, new Response(malo ? "1" : "0", { headers: { "cache-control": `max-age=${SB_TTL}` } }));
  return malo;
}

export default {
  async fetch(req, env, ctx) {
    const url = new URL(req.url);
    const m = url.pathname.match(/^\/q\/([A-Za-z0-9_-]{6,20})$/);
    if (url.pathname === "/robots.txt") return new Response("User-agent: *\nDisallow: /\n", { headers: { "content-type": "text/plain" } });
    if (!m) return pagina("No encontrado", "Esta dirección solo redirige códigos QR.", 404);
    if (!env.DB) return pagina("Servicio no disponible", "El servicio de QR todavía no está configurado.", 503);
    const d = await db(env);
    const rec = await d.prepare("SELECT id, dest, st FROM qr WHERE id=?").bind(m[1]).first();
    if (!rec) return pagina("QR no válido", "Este código no existe.", 404);
    if (rec.st !== "authorized") return pagina("Este QR está inactivo", "El dueño del código canceló su suscripción, así que ya no redirige.", 410);
    try {
      if ((await dohBloqueado(new URL(rec.dest).hostname)) || (await sbBloqueado(env, rec.dest)))
        return pagina("Destino bloqueado", "Este QR apunta a un sitio marcado como peligroso, así que lo detuvimos para protegerte.", 451);
    } catch {}
    const dia = new Date().toISOString().slice(0, 10);
    const pais = req.cf?.country || "XX";
    ctx.waitUntil(d.prepare("INSERT INTO scans (id, day, country, n) VALUES (?,?,?,1) ON CONFLICT(id,day,country) DO UPDATE SET n=n+1").bind(rec.id, dia, pais).run());
    return new Response(null, { status: 302, headers: { location: rec.dest, "cache-control": "no-store", "referrer-policy": "no-referrer", "x-robots-tag": "noindex" } });
  },
};
