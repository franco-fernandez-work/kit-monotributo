// QR dinámicos con suscripción de Mercado Pago (preapproval, ARS). D1 guarda QR y escaneos.
// /q/<id> redirige mientras la suscripción esté autorizada; el panel se maneja con un enlace secreto (sin mails ni soporte).
import qrcode from "./vendor/qrcode.cjs";

const PRECIO = 2999;
const REFRESCO = 3600; // s entre consultas a MP por QR
const DOH = "https://security.cloudflare-dns.com/dns-query";
const ACORTADORES = /(^|\.)(bit\.ly|tinyurl\.com|t\.co|goo\.gl|is\.gd|cutt\.ly|rb\.gy|shorturl\.at|ow\.ly|buff\.ly|t\.ly|rebrand\.ly|tiny\.cc|s\.id|v\.gd|qrco\.de|qr\.io)$/i;
const api = (env) => env.MP_API || "https://api.mercadopago.com";

const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);
const ahora = () => Math.floor(Date.now() / 1000);
const rand = (n) => btoa(String.fromCharCode(...crypto.getRandomValues(new Uint8Array(n)))).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");

let listo;
function db(env) {
  listo ||= env.DB.batch([
    env.DB.prepare("CREATE TABLE IF NOT EXISTS qr (id TEXT PRIMARY KEY, token TEXT UNIQUE NOT NULL, email TEXT NOT NULL, dest TEXT NOT NULL, preapproval TEXT, st TEXT NOT NULL DEFAULT 'pending', st_at INTEGER NOT NULL DEFAULT 0, created INTEGER NOT NULL)"),
    env.DB.prepare("CREATE TABLE IF NOT EXISTS scans (id TEXT NOT NULL, day TEXT NOT NULL, country TEXT NOT NULL, n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY (id, day, country))"),
  ]).catch((e) => { listo = null; throw e; });
  return listo.then(() => env.DB);
}

// ---------- filtro de destinos ----------
async function dohBloqueado(host) {
  // El DNS de seguridad de Cloudflare responde 0.0.0.0 para malware y phishing conocidos.
  const r = await fetch(`${DOH}?name=${encodeURIComponent(host)}&type=A`, { headers: { accept: "application/dns-json" }, cf: { cacheTtl: 300, cacheEverything: true } });
  if (!r.ok) throw new Error("doh");
  const j = await r.json();
  if (j.Status === 3) return "nx";
  return (j.Answer || []).some((a) => a.data === "0.0.0.0") ? "bloqueado" : "ok";
}

async function sbBloqueado(env, url) {
  if (!env.SB_KEY) return false;
  const r = await fetch(`https://safebrowsing.googleapis.com/v4/threatMatches:find?key=${env.SB_KEY}`, {
    method: "POST",
    body: JSON.stringify({
      client: { clientId: "qr-dinamicos", clientVersion: "1" },
      threatInfo: { threatTypes: ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE"], platformTypes: ["ANY_PLATFORM"], threatEntryTypes: ["URL"], threatEntries: [{ url }] },
    }),
  }).catch(() => null);
  if (!r?.ok) return false;
  const j = await r.json();
  return !!j.matches?.length;
}

// Devuelve { url } con la URL normalizada o { error }.
async function validarDestino(env, raw, origin) {
  let u;
  try { u = new URL(String(raw || "").trim()); } catch { return { error: "Escribí una dirección completa, por ejemplo https://tuweb.com/menu" }; }
  const host = u.hostname.toLowerCase();
  if (!/^https?:$/.test(u.protocol)) return { error: "Solo se aceptan direcciones http o https." };
  if (u.href.length > 2000) return { error: "La dirección es demasiado larga." };
  if (u.username || u.password) return { error: "La dirección no puede incluir usuario ni contraseña." };
  if (!host.includes(".") || /^[\d.]+$/.test(host) || host.includes(":") || host.startsWith("[") || host === "localhost" || /\.(local|internal|localhost|onion)$/.test(host)) return { error: "Usá un dominio público, no una IP ni una dirección local." };
  if (host === new URL(origin).hostname) return { error: "El destino no puede ser este mismo sitio." };
  if (ACORTADORES.test(host)) return { error: "No se aceptan acortadores ni otros generadores de QR como destino." };
  if (host.split(".").some((p) => p.startsWith("xn--"))) return { error: "No se aceptan dominios con caracteres internacionales camuflados." };
  let v;
  try { v = await dohBloqueado(host); } catch { return { error: "No pudimos verificar el destino ahora. Probá de nuevo en unos minutos." }; }
  if (v === "nx") return { error: "Ese dominio no existe. Revisá que esté bien escrito." };
  if (v === "bloqueado" || (await sbBloqueado(env, u.href))) return { error: "Ese destino figura como sitio peligroso (malware o phishing), así que no podemos crear el QR." };
  return { url: u.href };
}

// ---------- suscripción ----------
async function estadoMP(env, rec) {
  if (!rec.preapproval) return rec.st;
  try {
    const r = await fetch(`${api(env)}/preapproval/${rec.preapproval}`, { headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}` } });
    if (!r.ok) return null;
    const p = await r.json();
    if (p.external_reference !== rec.id) return null;
    return p.status;
  } catch { return null; }
}

async function refrescar(env, rec, forzar) {
  if (!forzar && ahora() - rec.st_at < REFRESCO) return rec;
  const st = await estadoMP(env, rec);
  if (st && st !== rec.st) rec.st = st;
  if (st) {
    rec.st_at = ahora();
    await (await db(env)).prepare("UPDATE qr SET st=?, st_at=? WHERE id=?").bind(rec.st, rec.st_at, rec.id).run();
  }
  return rec;
}

// ---------- vistas ----------
const FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;700&family=Bricolage+Grotesque:opsz,wght@12..96,700&family=JetBrains+Mono:wght@600&display=swap">';
const CSS = `<style>
.qr-h{display:grid;grid-template-columns:1.1fr .9fr;gap:44px;align-items:center}
@media(max-width:860px){.qr-h{grid-template-columns:1fr}}
.qr-h>*{min-width:0}
.tarjeta{background:var(--hoja);border:1px solid var(--linea);border-radius:4px;padding:26px}
.tarjeta h2,.tarjeta h3{margin-top:0}
label{display:block;font:600 12px/1.2 var(--f-num);letter-spacing:.1em;text-transform:uppercase;color:var(--tinta-2);margin:18px 0 6px}
input[type=url],input[type=email]{width:100%;font:17px var(--f-texto);padding:12px 14px;border:1.5px solid var(--linea);border-radius:3px;background:var(--papel);color:var(--tinta)}
input:focus{border-color:var(--celeste);outline:none;box-shadow:0 0 0 3px var(--celeste-suave)}
button.boton,a.boton{display:inline-block;margin-top:20px;font:700 17px var(--f-texto);padding:13px 26px;border:0;border-radius:3px;background:var(--tinta);color:var(--hoja);cursor:pointer;text-decoration:none}
button.boton:hover,a.boton:hover{background:var(--celeste);color:#fff}
a.boton.sec,button.sec{background:transparent;color:var(--tinta);border:1.5px solid var(--tinta)}
.precio{font:700 44px/1 var(--f-display)}.precio small{font:400 16px var(--f-texto);color:var(--tinta-2)}
.qrbox{background:#fff;padding:14px;border-radius:4px;border:1px solid var(--linea);max-width:300px}
.qrbox svg{display:block;width:100%;height:auto}
.err{border-left:4px solid var(--sello);background:var(--hoja);padding:12px 16px;margin:0 0 20px;color:var(--sello)}
.estado{display:inline-block;font:600 12px var(--f-num);letter-spacing:.1em;text-transform:uppercase;padding:5px 10px;border-radius:2px}
.estado.on{background:var(--celeste-suave);color:var(--ok)}.estado.off{background:var(--hoja);border:1px solid var(--sello);color:var(--sello)}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:20px}
.barras{display:flex;align-items:flex-end;gap:3px;height:90px;margin-top:14px}
.barras i{flex:1;background:var(--celeste);min-height:2px;border-radius:2px 2px 0 0}
.kpi{font:700 38px/1 var(--f-display)}
.sec2{margin-top:44px}.sec2 h2{margin-top:0}
.sec2 .grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:20px}
table{width:100%;border-collapse:collapse;font-size:15px}td,th{text-align:left;padding:6px 0;border-bottom:1px solid var(--linea)}td:last-child,th:last-child{text-align:right}
</style>`;

function pagina({ titulo, desc = "", cuerpo, indexar = false, status = 200, extra = "" }) {
  return new Response(
    `<!doctype html><html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>${esc(titulo)}</title>${desc ? `<meta name="description" content="${esc(desc)}">` : ""}${indexar ? "" : '<meta name="robots" content="noindex">'}<meta name="referrer" content="no-referrer">${FONTS}<link rel="stylesheet" href="/estilo.css">${CSS}</head><body><header class="top"><div class="wrap"><a class="marca" href="/qr"><i>QR</i>QR dinámicos</a><nav class="menu"><a href="/qr#precio">Precio</a><a href="/qr#faq">Preguntas</a><a href="/">Planillas</a></nav></div></header><main class="wrap">${cuerpo}</main><footer class="wrap" style="padding-block:48px;color:var(--tinta-2);font-size:14px">Cobro por Mercado Pago. Podés cancelar cuando quieras desde tu cuenta de Mercado Pago, sin mensajes ni trámites.</footer>${extra}</body></html>`,
    { status, headers: { "content-type": "text/html; charset=utf-8", "referrer-policy": "no-referrer", "cache-control": "private, no-store" } }
  );
}

function svgQR(texto, scalable = true) {
  const q = qrcode(0, "M");
  q.addData(texto);
  q.make();
  return q.createSvgTag({ cellSize: 6, margin: 0, scalable });
}

const fmt = (n) => "$" + n.toLocaleString("es-AR");

function landing(origin, error = "", valores = {}) {
  const demo = svgQR(origin + "/qr");
  const cuerpo = `
<div class="qr-h">
  <div>
    <span class="etiqueta">QR dinámicos · sin letra chica</span>
    <h1>Un QR que podés cambiar después de imprimirlo.</h1>
    <p class="bajada">Cambiá el destino cuando quieras sin reimprimir, mirá cuántas veces lo escanean y pagá ${fmt(PRECIO)} por mes. Si cancelás, el QR deja de funcionar y se acabó: nada de rehenes, nada de cobros escondidos.</p>
    <ul class="puntos">
      <li><span class="num">01</span><span><b>Alta en dos minutos.</b> Pegás la dirección, pagás con Mercado Pago y descargás el QR.</span></li>
      <li><span class="num">02</span><span><b>Editable y con estadísticas.</b> Escaneos por día y por país, y destino editable las veces que quieras.</span></li>
      <li><span class="num">03</span><span><b>Sin cuenta ni contraseña.</b> Tu panel es un enlace privado que se guarda en favoritos.</span></li>
      <li><span class="num">04</span><span><b>Sin sorpresas.</b> El QR sigue activo mientras la suscripción esté vigente.</span></li>
    </ul>
  </div>
  <div class="tarjeta" id="alta">
    <span class="etiqueta">Crear mi QR</span>
    ${error ? `<p class="err">${esc(error)}</p>` : ""}
    <form method="post" action="/qr/alta">
      <label for="u">Adónde lleva el QR</label>
      <input id="u" name="url" type="url" required placeholder="https://tuweb.com/menu" value="${esc(valores.url || "")}" autocomplete="off">
      <label for="e">Tu email (para Mercado Pago)</label>
      <input id="e" name="email" type="email" required placeholder="vos@correo.com" value="${esc(valores.email || "")}" autocomplete="email">
      <button class="boton" type="submit">Suscribirme por ${fmt(PRECIO)}/mes</button>
      <p class="nota" style="margin-top:14px">Te llevamos a Mercado Pago para autorizar el cobro mensual. Al volver, tu QR ya está listo.</p>
    </form>
  </div>
</div>
<section class="sec2" id="precio">
  <h2>Un solo plan, todo incluido</h2>
  <div class="grid3">
    <div class="tarjeta"><div class="precio">${fmt(PRECIO)}<small> / mes</small></div><p class="nota">Pesos argentinos, cobro automático con Mercado Pago. Cancelás cuando quieras.</p></div>
    <div class="tarjeta"><h3>Qué incluye</h3><p class="nota">Un QR dinámico, escaneos ilimitados, cambio de destino ilimitado y estadísticas diarias.</p></div>
    <div class="tarjeta"><h3>Mismo QR siempre</h3><p class="nota">El código impreso no cambia nunca. Lo que cambia es adónde te lleva.</p><div class="qrbox" style="max-width:120px;padding:8px;margin-top:8px">${demo}</div></div>
  </div>
</section>
<section class="sec2 lectura" id="faq">
  <h2>Preguntas frecuentes</h2>
  <h3>¿Qué pasa si cancelo?</h3><p>Cancelás desde Mercado Pago y el QR deja de redirigir. Si querés volver a activarlo, creás una suscripción nueva.</p>
  <h3>¿Qué pasa si pierdo el enlace del panel?</h3><p>Es tu llave: guardalo en favoritos o en un gestor de contraseñas. Por seguridad no hay forma de recuperarlo, porque no hay cuentas ni contraseñas.</p>
  <h3>¿Qué destinos no se aceptan?</h3><p>Sitios marcados como malware o phishing, acortadores de links, direcciones IP o locales. Si un destino pasa a figurar como peligroso, el QR deja de redirigir.</p>
  <h3>¿Cómo se cobra?</h3><p>Mercado Pago cobra ${fmt(PRECIO)} por mes a tu medio de pago. Nosotros nunca vemos los datos de tu tarjeta.</p>
</section>`;
  return pagina({
    titulo: "QR dinámicos editables sin vencimiento | Argentina",
    desc: `Creá un QR dinámico: cambiás el destino sin reimprimir, ves las estadísticas de escaneos y pagás ${fmt(PRECIO)} por mes con Mercado Pago. Sin letra chica.`,
    cuerpo, indexar: true,
  });
}

function mensaje(titulo, texto, status = 200, boton = ["Volver", "/qr"]) {
  return pagina({ titulo, status, cuerpo: `<div class="mensaje lectura"><h1>${esc(titulo)}</h1><p>${texto}</p><a class="boton" href="${boton[1]}">${esc(boton[0])}</a></div>` });
}

async function panel(env, req, rec, error = "", ok = "") {
  const origin = new URL(req.url).origin;
  const d = await db(env);
  const activo = rec.st === "authorized";
  const desde = new Date(Date.now() - 29 * 864e5).toISOString().slice(0, 10);
  const { results: filas } = await d.prepare("SELECT day, country, n FROM scans WHERE id=? AND day>=?").bind(rec.id, desde).all();
  const { results: tot } = await d.prepare("SELECT COALESCE(SUM(n),0) AS n FROM scans WHERE id=?").bind(rec.id).all();
  const porDia = {}, porPais = {};
  for (const f of filas) { porDia[f.day] = (porDia[f.day] || 0) + f.n; porPais[f.country] = (porPais[f.country] || 0) + f.n; }
  const dias = Array.from({ length: 30 }, (_, i) => new Date(Date.now() - (29 - i) * 864e5).toISOString().slice(0, 10));
  const max = Math.max(1, ...dias.map((x) => porDia[x] || 0));
  const barras = dias.map((x) => `<i title="${x}: ${porDia[x] || 0}" style="height:${Math.max(2, ((porDia[x] || 0) / max) * 100)}%"></i>`).join("");
  const mes = dias.reduce((a, x) => a + (porDia[x] || 0), 0);
  const paises = Object.entries(porPais).sort((a, b) => b[1] - a[1]).slice(0, 6).map(([c, n]) => `<tr><td>${esc(c)}</td><td class="num">${n}</td></tr>`).join("") || '<tr><td colspan="2" class="nota">Todavía no hay escaneos.</td></tr>';
  const qrUrl = `${origin}/q/${rec.id}`;
  const cuerpo = `
<span class="etiqueta">Tu panel privado · guardalo en favoritos</span>
<h1>Tu QR dinámico</h1>
<p style="margin-top:14px"><span class="estado ${activo ? "on" : "off"}">${activo ? "Activo" : rec.st === "pending" ? "Esperando el pago" : rec.st === "paused" ? "Suscripción en pausa" : "Suscripción cancelada"}</span></p>
${error ? `<p class="err">${esc(error)}</p>` : ""}${ok ? `<p class="nota" style="color:var(--ok)">${esc(ok)}</p>` : ""}
${activo ? "" : `<div class="tarjeta" style="margin-top:20px"><p>Este QR ${rec.st === "pending" ? "se activa cuando autorices el pago mensual en Mercado Pago" : "no redirige porque la suscripción no está vigente"}. ${rec.st === "pending" ? "Si ya pagaste, recargá esta página en un minuto." : "Para volver a usarlo creá una suscripción nueva."}</p><a class="boton" href="/qr#alta">Crear una suscripción nueva</a></div>`}
<div class="grid2">
  <div class="tarjeta">
    <span class="etiqueta">Tu código</span>
    <div class="qrbox" id="qrbox">${svgQR(qrUrl)}</div>
    <p class="nota" style="margin-top:12px">Imprimilo así: el código no cambia nunca, aunque cambies el destino.<br><span class="num">${esc(qrUrl)}</span></p>
    <button class="boton sec" type="button" id="dl-png">Descargar PNG</button> <button class="boton sec" type="button" id="dl-svg">Descargar SVG</button>
  </div>
  <div class="tarjeta">
    <span class="etiqueta">Destino</span>
    <form method="post" action="/qr/editar">
      <input type="hidden" name="t" value="${esc(rec.token)}">
      <label for="d">Adónde lleva ahora</label>
      <input id="d" name="url" type="url" required value="${esc(rec.dest)}" autocomplete="off">
      <button class="boton" type="submit">Guardar destino</button>
    </form>
    <p class="nota" style="margin-top:16px">Para cancelar, entrá a Mercado Pago, Suscripciones, y cancelá “QR dinámicos”. El QR se apaga solo.</p>
  </div>
</div>
<div class="grid2">
  <div class="tarjeta"><span class="etiqueta">Escaneos</span><div class="kpi num">${tot[0].n}</div><p class="nota">en total · ${mes} en los últimos 30 días</p><div class="barras" aria-label="Escaneos por día, últimos 30 días">${barras}</div></div>
  <div class="tarjeta"><span class="etiqueta">Países (30 días)</span><table>${paises}</table></div>
</div>`;
  const script = `<script>
(function(){var b=document.getElementById('qrbox'),s=b.querySelector('svg');
function dl(n,h){var a=document.createElement('a');a.download=n;a.href=h;document.body.appendChild(a);a.click();a.remove()}
document.getElementById('dl-svg').onclick=function(){var c=s.cloneNode(true);c.setAttribute('xmlns','http://www.w3.org/2000/svg');c.insertAdjacentHTML('afterbegin','<rect width="100%" height="100%" fill="#fff"/>');dl('qr.svg','data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(c)))};
document.getElementById('dl-png').onclick=function(){var c=s.cloneNode(true);c.setAttribute('xmlns','http://www.w3.org/2000/svg');var vb=c.getAttribute('viewBox').split(' ').map(Number),n=vb[2],z=Math.ceil(1200/n),m=4*z*0+0;
c.setAttribute('width',n*z);c.setAttribute('height',n*z);var i=new Image();i.onload=function(){var k=document.createElement('canvas'),p=Math.round(n*z*0.06);k.width=k.height=n*z+p*2;var x=k.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,k.width,k.height);x.imageSmoothingEnabled=false;x.drawImage(i,p,p);dl('qr.png',k.toDataURL('image/png'))};
i.src='data:image/svg+xml;charset=utf-8,'+encodeURIComponent(new XMLSerializer().serializeToString(c))};})();
</script>`;
  return pagina({ titulo: "Tu QR dinámico", cuerpo, extra: script });
}

// ---------- ruteo ----------
export async function manejarQR(req, env, ctx) {
  const url = new URL(req.url);
  const p = url.pathname;
  if (!(p === "/qr" || p.startsWith("/qr/") || p.startsWith("/q/"))) return null;
  if (!env.DB) return mensaje("Servicio no disponible", "El servicio de QR todavía no está configurado.", 503);
  const d = await db(env);

  if (p.startsWith("/q/")) {
    const id = p.slice(3);
    if (!/^[A-Za-z0-9_-]{6,20}$/.test(id)) return mensaje("QR no válido", "Este código no existe.", 404);
    let rec = await d.prepare("SELECT * FROM qr WHERE id=?").bind(id).first();
    if (!rec) return mensaje("QR no válido", "Este código no existe.", 404);
    rec = await refrescar(env, rec, false);
    if (rec.st !== "authorized") return mensaje("Este QR está inactivo", "El dueño del código canceló su suscripción, así que ya no redirige.", 410, ["Crear mi propio QR", "/qr"]);
    // revalidación periódica del destino contra el DNS de seguridad
    try {
      const host = new URL(rec.dest).hostname;
      if ((await dohBloqueado(host)) === "bloqueado") return mensaje("Destino bloqueado", "Este QR apunta a un sitio marcado como peligroso, así que lo detuvimos para protegerte.", 451);
    } catch {}
    const dia = new Date().toISOString().slice(0, 10);
    const pais = req.cf?.country || "XX";
    ctx.waitUntil(d.prepare("INSERT INTO scans (id, day, country, n) VALUES (?,?,?,1) ON CONFLICT(id,day,country) DO UPDATE SET n=n+1").bind(id, dia, pais).run());
    return new Response(null, { status: 302, headers: { location: rec.dest, "cache-control": "no-store", "referrer-policy": "no-referrer" } });
  }

  if (p === "/qr" && req.method === "GET") return landing(url.origin, url.searchParams.get("e") ? "Hubo un problema con el pago. Probá de nuevo." : "");

  if (p === "/qr/alta" && req.method === "POST") {
    const f = await req.formData().catch(() => null);
    const email = String(f?.get("email") || "").trim().toLowerCase();
    const valores = { url: String(f?.get("url") || ""), email };
    if (!/^[^\s@]{1,64}@[^\s@]{1,190}\.[^\s@]{2,}$/.test(email)) return landing(url.origin, "Revisá el email.", valores);
    const v = await validarDestino(env, valores.url, url.origin);
    if (v.error) return landing(url.origin, v.error, valores);
    await d.prepare("DELETE FROM qr WHERE st='pending' AND created<?").bind(ahora() - 3 * 86400).run();
    const id = rand(6), token = rand(24);
    const r = await fetch(`${api(env)}/preapproval`, {
      method: "POST",
      headers: { Authorization: `Bearer ${env.MP_ACCESS_TOKEN}`, "content-type": "application/json" },
      body: JSON.stringify({
        reason: "QR dinámicos (suscripción mensual)",
        external_reference: id,
        payer_email: email,
        back_url: `${url.origin}/qr/panel?t=${token}`,
        status: "pending",
        auto_recurring: { frequency: 1, frequency_type: "months", transaction_amount: PRECIO, currency_id: "ARS" },
      }),
    }).catch(() => null);
    if (!r?.ok) return landing(url.origin, "No pudimos abrir Mercado Pago. Probá de nuevo en unos minutos.", valores);
    const pre = await r.json();
    await d.prepare("INSERT INTO qr (id, token, email, dest, preapproval, st, st_at, created) VALUES (?,?,?,?,?,?,?,?)").bind(id, token, email, v.url, pre.id, "pending", ahora(), ahora()).run();
    return Response.redirect(pre.init_point, 303);
  }

  if (p === "/qr/panel" && req.method === "GET") {
    const t = url.searchParams.get("t") || "";
    let rec = /^[A-Za-z0-9_-]{20,40}$/.test(t) ? await d.prepare("SELECT * FROM qr WHERE token=?").bind(t).first() : null;
    if (!rec) return mensaje("Enlace no válido", "No encontramos ese panel. Revisá que hayas copiado el enlace completo.", 404);
    rec = await refrescar(env, rec, true);
    return panel(env, req, rec, "", url.searchParams.get("ok") ? "Destino actualizado." : "");
  }

  if (p === "/qr/editar" && req.method === "POST") {
    const f = await req.formData().catch(() => null);
    const t = String(f?.get("t") || "");
    let rec = /^[A-Za-z0-9_-]{20,40}$/.test(t) ? await d.prepare("SELECT * FROM qr WHERE token=?").bind(t).first() : null;
    if (!rec) return mensaje("Enlace no válido", "No encontramos ese panel.", 404);
    const v = await validarDestino(env, f.get("url"), url.origin);
    if (v.error) return panel(env, req, rec, v.error);
    await d.prepare("UPDATE qr SET dest=? WHERE id=?").bind(v.url, rec.id).run();
    return Response.redirect(`${url.origin}/qr/panel?t=${t}&ok=1`, 303);
  }

  return mensaje("No encontrado", "Esa página no existe.", 404);
}
