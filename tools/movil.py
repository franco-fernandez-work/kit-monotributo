"""Experiencia en teléfonos: CSS final (gana por orden sobre el resto) y posproceso del HTML.
build_site.main() llama a post(pub) al final, después de seo_boost.post. No cambia contenido ni SEO:
solo envuelve tablas, agrega inputmode a campos numéricos, enlace de salto, CTA fija de compra y el script que centra el tema activo del menú."""
import glob, html, json, os, re

CSS = r"""
/* ===== móvil (último bloque: pisa a los anteriores) ===== */
:root{--celeste-txt:#1d6aa8;--gut-i:max(20px,env(safe-area-inset-left,0px));--gut-d:max(20px,env(safe-area-inset-right,0px))}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--celeste-txt:#7ab6e6}}
:root[data-theme="dark"]{--celeste-txt:#7ab6e6}
body{overflow-wrap:break-word;-webkit-tap-highlight-color:color-mix(in srgb,var(--celeste) 25%,transparent)}
.saltar{position:absolute;left:12px;top:-60px;z-index:50;background:var(--tinta);color:var(--papel);padding:12px 16px;border-radius:4px;font-weight:700;text-decoration:none}
.saltar:focus{top:12px}
main:focus{outline:none}
/* contraste: el celeste de la marca queda para fondos, bordes y textos grandes; el texto chico usa celeste-txt */
a:hover{color:var(--celeste-txt)}
.puntos .num,.marca i,.r2quien h3,.modelos li::before,.indice li::before,.pasosauto h3,.link,td.cat{color:var(--celeste-txt)}
.marca i{border-color:var(--celeste-txt)}
.escala-barra span.on{background:var(--celeste-txt);color:#fff}
.sello{border-color:var(--celeste-txt);color:var(--celeste-txt)}.sello.alerta{border-color:var(--sello);color:var(--sello)}
.boton{min-height:52px;justify-content:center}
.boton:focus-visible{outline-offset:3px}
.campo input[type=date],.campo input[type=month]{min-width:0;width:100%;font:600 18px var(--f-num);min-height:52px}
.campo .entrada{min-height:52px}
.campo select{min-height:50px}
.fila2>*,.campo,.entrada{min-width:0}
.datos div{flex-wrap:wrap}
.datos dd{white-space:normal}
.avisolegal{color:#10263d}
:root[data-theme="dark"] .avisolegal{background:#2a1a1f;color:var(--tinta)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .avisolegal{background:#2a1a1f;color:var(--tinta)}}
/* tablas: sombra de borde al deslizar y primera columna fija */
.tabla-wrap{overflow-x:auto;overscroll-behavior-x:contain;-webkit-overflow-scrolling:touch;
  background:linear-gradient(90deg,var(--hoja) 30%,transparent) 0 0/36px 100% no-repeat local,linear-gradient(270deg,var(--hoja) 30%,transparent) 100% 0/36px 100% no-repeat local,linear-gradient(90deg,rgba(16,38,61,.22),transparent) 0 0/12px 100% no-repeat scroll,linear-gradient(270deg,rgba(16,38,61,.22),transparent) 100% 0/12px 100% no-repeat scroll,var(--hoja)}
.tabla-wrap:focus-visible{outline-offset:-3px}
th:first-child,td:first-child{position:sticky;left:0;z-index:1;background:var(--hoja)}
@media (max-width:760px){
  body{font-size:17px;line-height:1.62}
  .wrap{padding-left:var(--gut-i);padding-right:var(--gut-d)}
  main.wrap{padding-block:28px 0}
  h1{font-size:clamp(29px,8.6vw,40px);line-height:1.1}
  h2{font-size:clamp(23px,6.6vw,28px);margin:40px 0 12px}
  h3{font-size:18px}
  .bajada{font-size:18px;margin-top:14px}
  .lectura,.lectura p,.lectura li{max-width:none}
  .lectura li{margin:8px 0}
  .nota{font-size:14.5px}
  .etiqueta{font-size:12px}
  /* encabezado y menú por tema: cintas que se deslizan, no 4 renglones de enlaces */
  .top .wrap{flex-direction:column;align-items:stretch;flex-wrap:nowrap;gap:2px;padding-block:10px 4px}
  .marca{min-height:44px}
  .menu,.submenu{flex-wrap:nowrap;overflow-x:auto;gap:8px;margin:0 calc(-1 * var(--gut-d)) 0 calc(-1 * var(--gut-i));padding:2px var(--gut-d) 8px var(--gut-i);scrollbar-width:none;scroll-snap-type:x proximity;overscroll-behavior-x:contain;-webkit-overflow-scrolling:touch;
    -webkit-mask-image:linear-gradient(90deg,transparent 0,#000 14px,#000 calc(100% - 30px),transparent);mask-image:linear-gradient(90deg,transparent 0,#000 14px,#000 calc(100% - 30px),transparent)}
  .menu::-webkit-scrollbar,.submenu::-webkit-scrollbar{display:none}
  .menu a,.submenu a{flex:none;scroll-snap-align:center;display:inline-flex;align-items:center;min-height:44px;padding:0 16px;border:1px solid var(--linea);border-radius:999px;background:var(--hoja);color:var(--tinta);text-decoration:none;font-size:15px;white-space:nowrap}
  .menu a[aria-current],.menu a[aria-current="page"]{background:var(--tinta);color:var(--papel);border-color:var(--tinta);text-decoration:none}
  .submenu{font-size:14px;margin-top:0}
  .submenu a{min-height:40px;padding:0 14px;color:var(--tinta-2);font-size:14px;background:transparent}
  .menu .arrep{border-color:var(--sello);color:var(--sello);font-weight:700;padding:0 16px}
  /* comprobante y calculadora */
  .comp-cab{padding:14px 16px}
  .comp-cuerpo{padding:16px 16px 20px}
  .campo label{font-size:16px;margin-bottom:8px}
  .campo input{font-size:20px;min-height:52px;padding:12px}
  .campo select{font-size:17px;padding:12px}
  .resultado{grid-template-columns:1fr;justify-items:center;gap:14px}
  .resultado .datos{justify-self:stretch;width:100%}
  .sello{width:auto;min-width:92px;height:92px;border-radius:46px;padding-inline:16px;max-width:100%}
  .sello b{white-space:nowrap}
  #sello #r-tot,#sello #r-mes{font-size:clamp(26px,8.5vw,38px)!important}
  .sello small{font-size:10px}
  .datos{font-size:16px}
  .datos div{padding-bottom:6px}
  .estado{font-size:16px}
  .escala-barra span{font-size:11px}
  .escala-pie{font-size:11.5px}
  /* tablas */
  table{font-size:14.5px;min-width:480px}
  th{font-size:11.5px;padding:10px 10px}
  td{padding:10px}
  th:first-child,td:first-child{box-shadow:1px 0 0 var(--linea)}
  td:first-child:not(.cat){font-family:var(--f-texto);font-size:15px;line-height:1.35}
  /* botones y ofertas */
  .boton{display:flex;width:100%;justify-content:space-between;gap:10px;padding:15px 18px;font-size:17px}
  .boton .num{padding-left:12px;white-space:nowrap}
  .oferta{margin-top:40px;padding:20px 18px;gap:20px}
  .oferta .compra{justify-items:stretch}
  .oferta .nota{font-size:14.5px}
  .compra .nota:last-child{padding-block:8px;display:inline-block}
  .oferta ul{padding-left:20px}
  /* enlaces de listas y pie con zona táctil */
  .migas{font-size:14.5px;margin:12px 0 6px;line-height:1.7}
  .migas a{display:inline-block;padding-block:10px}
  .mas-leer li,.indice li{margin:0}
  .mas-leer li a{display:inline-block;padding-block:9px}
  .indice li a{display:inline-block;padding-block:6px}
  .fuentes li a{display:inline-block;padding-block:6px}
  .pie{margin-top:56px}
  .pie .wrap{padding-block:20px 28px;font-size:14.5px}
  .pie .legal{gap:0 20px}
  .pie .legal a{display:inline-flex;align-items:center;min-height:44px}
  .pie .arrep{padding:0 12px;min-height:40px;margin-block:2px}
  /* generadores y formularios */
  .gen .campo input,.gen .campo textarea,.gen .campo select,.arr-form input,.arr-form select,.arr-form textarea{font-size:16px;min-height:48px;padding:12px}
  .gen .campo textarea{min-height:96px}
  .tipos{gap:10px}
  .tipos button{min-height:44px;padding:10px 16px;font-size:15px}
  .itemrow{grid-template-columns:1fr 1fr 44px;gap:8px}
  .itemrow>:first-child{grid-column:1/-1}
  .itemrow button{min-height:44px;min-width:44px}
  .link{min-height:44px;padding:0 4px}
  .copiar{gap:12px}
  .copiar .boton{width:100%}
  .hoja-carta,.hoja-prev{position:static;min-height:0;padding:18px 16px}
  .hoja-carta{font-size:14.5px}
  .r2chk label{padding:14px;font-size:16px;min-height:52px}
  .r2chk input{width:24px;height:24px;margin-top:1px}
  .r2res{padding:16px}
  .r2res .fil{font-size:16px}
  .r2quien,.modelos,.pasosauto{grid-template-columns:1fr}
  .heroe{gap:24px}
  .mensaje{padding-block:36px}
  .mensaje .boton{margin-top:6px}
  .precio-grande{font-size:38px}
  .tapa{max-width:300px;margin-inline:auto}
  /* CTA fija: entra después de leer un rato y se va cuando aparece la oferta, un campo con teclado o el pie */
  .cta-fija{position:fixed;left:0;right:0;bottom:0;z-index:30;display:flex;align-items:center;gap:12px;padding:10px var(--gut-d) calc(10px + env(safe-area-inset-bottom,0px)) var(--gut-i);background:var(--hoja);border-top:1px solid var(--linea);box-shadow:0 -8px 24px -12px rgba(16,38,61,.35);transform:translateY(0);transition:transform .2s}
  .cta-fija[hidden]{display:flex;transform:translateY(110%);visibility:hidden;transition:transform .2s,visibility 0s .2s}
  .cta-fija .cta-nombre{flex:1;min-width:0;font:700 14px/1.25 var(--f-texto);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
  .cta-fija .boton{width:auto;flex:none;min-height:48px;padding:0 16px;font-size:16px}
  body.con-cta{padding-bottom:calc(76px + env(safe-area-inset-bottom,0px))}
}
@media (max-width:360px){
  h1{font-size:28px}
  .campo input{font-size:19px}
  .cta-fija .cta-nombre{display:none}
  .cta-fija .boton{flex:1;justify-content:space-between}
}
@media (min-width:761px){.cta-fija{display:none}}
/* teléfono en horizontal: poca altura */
@media (max-height:500px) and (orientation:landscape){
  main.wrap{padding-block:18px 0}
  .top .wrap{padding-block:6px 0}
  .menu a,.submenu a{min-height:40px}
  .marca{min-height:36px}
  .sello{width:76px;height:76px}.sello b{font-size:40px}
  .cta-fija{padding-block:6px calc(6px + env(safe-area-inset-bottom,0px))}
  .cta-fija .boton{min-height:42px}
  .cta-fija .cta-nombre{-webkit-line-clamp:1}
  body.con-cta{padding-bottom:calc(60px + env(safe-area-inset-bottom,0px))}
  .oferta{margin-top:32px}
}
"""

JS = r"""<script>
(function(){
function centrar(n){var a=n&&n.querySelector('[aria-current]');if(a&&n.scrollWidth>n.clientWidth)n.scrollLeft=Math.max(0,a.offsetLeft-(n.clientWidth-a.offsetWidth)/2)}
document.querySelectorAll('.menu').forEach(centrar);
var o=document.querySelector('.oferta a.boton[href^="/comprar"]');if(!o)return;
var t=o.closest('.oferta').querySelector('h2'),n=o.querySelector('.num');
var b=document.createElement('div');b.className='cta-fija';b.hidden=true;
var s=document.createElement('span');s.className='cta-nombre';s.textContent=t?t.textContent:'';
var a=document.createElement('a');a.className='boton';a.href=o.getAttribute('href');a.innerHTML='Comprar'+(n?' <span class="num">'+n.textContent+'</span>':'');
b.appendChild(s);b.appendChild(a);document.body.appendChild(b);document.body.classList.add('con-cta');
var enOferta=false,enPie=false,campo=false,mq=matchMedia('(max-width:760px)');
function ver(){b.hidden=!(mq.matches&&!enOferta&&!enPie&&!campo&&scrollY>420)}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.target.classList.contains('oferta'))enOferta=e.isIntersecting;else enPie=e.isIntersecting});ver()});
document.querySelectorAll('.oferta,.pie').forEach(function(x){io.observe(x)})}
document.addEventListener('focusin',function(e){if(/^(INPUT|SELECT|TEXTAREA)$/.test(e.target.tagName)){campo=true;ver()}});
document.addEventListener('focusout',function(){campo=false;setTimeout(ver,50)});
addEventListener('scroll',ver,{passive:true});mq.addEventListener&&mq.addEventListener('change',ver);ver();
})();
</script>"""


TEMAS_JS = r"""(function(){
var T=window.TEMAS||{},menu=document.querySelector('nav.menu');if(!menu)return;
var actual=location.pathname.replace(/\.html$/,'')||'/';
function sub(){var n=document.querySelector('nav.submenu');if(!n){n=document.createElement('nav');n.className='submenu';n.setAttribute('aria-label','En este tema');menu.parentNode.insertBefore(n,menu.nextSibling)}return n}
menu.addEventListener('click',function(e){var a=e.target.closest('a[href^="/guias#"]');if(!a||e.metaKey||e.ctrlKey||e.shiftKey)return;
var k=a.getAttribute('href').split('#')[1],l=T[k];if(!l)return;e.preventDefault();
menu.querySelectorAll('a[aria-current]').forEach(function(x){x.removeAttribute('aria-current')});a.setAttribute('aria-current','true');
var n=sub();n.innerHTML='';n.setAttribute('aria-label','En este tema: '+a.textContent);
l.forEach(function(it){var b=document.createElement('a');b.href=it[0];b.textContent=it[1];if(it[0]===actual)b.setAttribute('aria-current','page');n.appendChild(b)});
n.scrollLeft=0;a.scrollIntoView&&a.scrollIntoView({block:'nearest',inline:'center'})});
})();"""

def _temas(pub):
    """temas.js: pages de cada tema (de /guias) con la etiqueta corta del submenú, para que tocar un tema cambie las burbujas sin salir de la página."""
    lab = {}
    for p in glob.glob(os.path.join(pub, "*.html")):
        h = open(p, encoding="utf-8").read()
        m = re.search(r'<nav class="submenu"[^>]*>(.*?)</nav>', h, re.S)
        if m:
            for href, t in re.findall(r'<a href="([^"]+)">(.*?)</a>', m.group(1)):
                lab[href] = html.unescape(t)
    g = os.path.join(pub, "guias.html")
    if not os.path.exists(g):
        return
    T = {}
    for k, body in re.findall(r'<h2 id="(\w+)">.*?</h2><ul>(.*?)</ul>', open(g, encoding="utf-8").read(), re.S):
        its = []
        for href, t in re.findall(r'<li><a href="([^"]+)">(.*?)</a>', body)[:10]:
            t = html.unescape(re.sub(r"<[^>]+>", "", t)).lstrip("¿")
            t = lab.get(href) or (t if len(t) <= 34 else t[:32].rsplit(" ", 1)[0] + "…")
            its.append([href, t])
        T[k] = its
    open(os.path.join(pub, "temas.js"), "w", encoding="utf-8").write("window.TEMAS=" + json.dumps(T, ensure_ascii=False, separators=(",", ":")) + ";\n" + TEMAS_JS)

# campos que piden teclado numérico (id/data-k que contienen estas palabras)
NUM = re.compile(r'(monto|precio|sena|seña|importe|sueldo|costo|valor|total|km|anio|año|dni|cuit|cuil|cantidad|dias|horas|meses|edad|hijos|metros|m2|ambientes|stock|unidades)', re.I)

def _inputs(h):
    def f(m):
        tag = m.group(0)
        if "inputmode" in tag or re.search(r'type="(date|month|email|checkbox|radio|hidden|number|tel|url|password)"', tag):
            return tag
        ident = " ".join(re.findall(r'(?:id|data-k|name)="([^"]*)"', tag))
        if NUM.search(ident):
            return tag[:-1] + ' inputmode="numeric" enterkeyhint="done">'
        return tag
    return re.sub(r"<input\b[^>]*>", f, h)

def _tablas(h):
    """Tablas sueltas: envueltas para que deslicen en vez de ensanchar la página; las ya envueltas ganan foco por teclado."""
    h = h.replace('<div class="tabla-wrap">', '<div class="tabla-wrap" tabindex="0" role="region" aria-label="Tabla: deslizá para ver más columnas">')
    partes = re.split(r'(<div class="tabla-wrap"[^>]*>.*?</table>\s*</div>)', h, flags=re.S)
    for i in range(0, len(partes), 2):
        partes[i] = re.sub(r"(<table\b.*?</table>)", r'<div class="tabla-wrap" tabindex="0" role="region" aria-label="Tabla: deslizá para ver más columnas">\1</div>', partes[i], flags=re.S)
    return "".join(partes)

def _post_html(h):
    if "cta-fija" in h:
        return h
    h = _inputs(h)
    h = _tablas(h)
    h = h.replace("<body>", '<body><a class="saltar" href="#contenido">Saltar al contenido</a>', 1)
    h = h.replace('<main class="wrap">', '<main class="wrap" id="contenido" tabindex="-1">', 1)
    return h.replace("</body>", JS + '<script src="/temas.js" defer></script></body>', 1) if "</body>" in h else h

def post(pub):
    _temas(pub)
    n = 0
    for p in glob.glob(os.path.join(pub, "*.html")):
        h = open(p, encoding="utf-8").read()
        if "<main" not in h:
            continue
        h2 = _post_html(h)
        if h2 != h:
            open(p, "w", encoding="utf-8").write(h2)
            n += 1
    css = os.path.join(pub, "estilo.css")
    s = open(css, encoding="utf-8").read()
    if "/* ===== móvil" not in s:
        open(css, "a", encoding="utf-8").write("\n" + CSS)
    return n
