"""Genera todas las páginas de public/ con un diseño común. Correr: python3 tools/build_site.py"""
import os, json

BASE = "https://kit-monotributo.fernandezfrancowork.workers.dev"
PUB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
HOY = "2026-10-24"

CATS = [("A",12009410.45,49527.18,49527.18),("B",17595182.74,56379.08,56379.08),("C",24670494.31,66020.12,64530.58),
("D",30628651.43,84612.93,82564.81),("E",36028231.33,119811.45,108267.51),("F",45151659.41,150784.21,129930.65),
("G",53995798.87,230312.94,158815.05),("H",81924660.37,522706.68,317895.01),("I",91699761.90,963747.86,474992.78),
("J",105012519.20,1167299.76,580793.69),("K",126610838.75,1614446.04,702103.24)]

def ars(n, dec=True):
    s = f"{n:,.2f}" if dec else f"{n:,.0f}"
    return "$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;600;700&family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=JetBrains+Mono:wght@500;600&display=swap">'

CSS = r"""/* Concepto: un comprobante fiscal. Papel frío, tinta azul marino, celeste de sello con mesura, números en mono como en una factura. */
:root{
  --papel:#f5f7f9; --hoja:#ffffff; --tinta:#10263d; --tinta-2:#4b5e72; --linea:#d6dfe8;
  --celeste:#3f8fcf; --celeste-suave:#e6f1fa; --sello:#b3343c; --ok:#2e7650;
  --f-display:"Bricolage Grotesque","Arial Narrow",system-ui,sans-serif;
  --f-texto:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-num:"JetBrains Mono",ui-monospace,"Cascadia Mono",Consolas,monospace;
  color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--papel:#0b1520;--hoja:#11202e;--tinta:#e6edf5;--tinta-2:#9db0c3;--linea:#22374b;--celeste:#7ab6e6;--celeste-suave:#14304a;--sello:#e46970;--ok:#6cc08f;color-scheme:dark}}
:root[data-theme="dark"]{--papel:#0b1520;--hoja:#11202e;--tinta:#e6edf5;--tinta-2:#9db0c3;--linea:#22374b;--celeste:#7ab6e6;--celeste-suave:#14304a;--sello:#e46970;--ok:#6cc08f;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--papel);color:var(--tinta);font:17px/1.6 var(--f-texto);-webkit-text-size-adjust:100%}
a{color:inherit;text-decoration-color:var(--celeste);text-underline-offset:3px;text-decoration-thickness:2px}
a:hover{color:var(--celeste)}
:focus-visible{outline:3px solid var(--celeste);outline-offset:2px}
.wrap{max-width:1060px;margin:0 auto;padding-left:max(20px,env(safe-area-inset-left,0px));padding-right:max(20px,env(safe-area-inset-right,0px))}
.top{border-bottom:1px solid var(--linea);background:var(--hoja)}
.top .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:10px 28px;padding-block:14px}
.marca{display:flex;align-items:center;gap:10px;font:700 18px/1 var(--f-display);text-decoration:none;letter-spacing:-.01em}
.marca i{width:30px;height:30px;border-radius:50%;border:2px solid var(--celeste);display:grid;place-items:center;font:600 12px/1 var(--f-num);font-style:normal;color:var(--celeste)}
.menu{display:flex;flex-wrap:wrap;gap:4px 20px;font-size:15px}
.menu a{text-decoration:none;color:var(--tinta-2)}
.menu a:hover,.menu a[aria-current="page"]{color:var(--tinta);text-decoration:underline;text-decoration-color:var(--celeste)}
h1,h2,h3{font-family:var(--f-display);line-height:1.08;letter-spacing:-.02em;text-wrap:balance;margin:0}
h1{font-size:clamp(34px,5.2vw,56px)}
h2{font-size:clamp(24px,3vw,32px);margin:60px 0 14px}
h3{font-size:19px;margin:0 0 6px}
p{margin:0 0 14px}
.etiqueta{display:block;font:600 12px/1.2 var(--f-num);letter-spacing:.12em;text-transform:uppercase;color:var(--tinta-2);margin-bottom:12px}
.num{font-family:var(--f-num);font-variant-numeric:tabular-nums}
.bajada{font-size:19px;color:var(--tinta-2);max-width:52ch;margin-top:16px}
.lectura{max-width:68ch}
.lectura li{margin:6px 0}
.nota{color:var(--tinta-2);font-size:14px}
main.wrap{padding-block:44px 0}
/* héroe */
.heroe{display:grid;grid-template-columns:1fr 1.05fr;gap:40px;align-items:start}
@media (max-width:860px){.heroe{grid-template-columns:1fr;gap:28px}}
.heroe>*{min-width:0}
.puntos{list-style:none;padding:0;margin:24px 0 0;display:grid;gap:10px}
.puntos li{display:flex;gap:12px;align-items:baseline;color:var(--tinta-2)}
.puntos b{color:var(--tinta);font-weight:700}
.puntos .num{color:var(--celeste);font-size:13px;min-width:3.6em;flex:none}
/* comprobante */
.comp{background:var(--hoja);border:1px solid var(--linea);border-radius:4px;position:relative;overflow:hidden}
.comp::before{content:"";display:block;height:5px;background:repeating-linear-gradient(90deg,var(--celeste) 0 16px,transparent 16px 24px)}
.comp-cab{display:flex;justify-content:space-between;align-items:baseline;gap:8px 16px;flex-wrap:wrap;padding:16px 22px;border-bottom:1px dashed var(--linea);font:600 12px/1.3 var(--f-num);letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-2)}
.comp-cuerpo{padding:20px 22px 24px;display:grid;gap:16px}
.campo label{display:block;font-weight:700;font-size:15px;margin-bottom:6px}
.campo .entrada{display:flex;align-items:center;border:1.5px solid var(--linea);border-radius:4px;background:var(--papel)}
.campo .entrada:focus-within{border-color:var(--celeste)}
.campo .entrada span{padding:0 0 0 14px;font:600 18px var(--f-num);color:var(--tinta-2)}
.campo input,.campo select{width:100%;min-width:0;border:0;background:transparent;color:var(--tinta);padding:12px 14px;font:600 20px var(--f-num);font-variant-numeric:tabular-nums}
.campo select{font:400 17px var(--f-texto)}
.campo input:focus,.campo select:focus{outline:none}
.fila2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media (max-width:480px){.fila2{grid-template-columns:1fr}}
.resultado{display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:center;padding-top:16px;border-top:1px dashed var(--linea)}
.sello{width:96px;height:96px;border-radius:50%;border:3px double var(--celeste);display:grid;place-items:center;transform:rotate(-8deg);color:var(--celeste)}
.sello b{font:700 52px/1 var(--f-display)}
.sello.alerta{border-color:var(--sello);color:var(--sello)}
.sello small{display:block;font:600 9px/1 var(--f-num);letter-spacing:.14em;text-align:center;margin-top:-4px}
.datos{display:grid;gap:4px;font-size:15px;min-width:0}
.datos div{display:flex;justify-content:space-between;gap:12px;border-bottom:1px dotted var(--linea);padding-bottom:4px}
.datos dt{color:var(--tinta-2)}
.datos dd{white-space:nowrap}
.datos dd{margin:0;font:600 15px var(--f-num);font-variant-numeric:tabular-nums;text-align:right}
.estado{font-size:15px;margin:0}
.estado.mal{color:var(--sello)} .estado.bien{color:var(--ok)}
/* escala A-K */
.escala{margin-top:4px}
.escala-barra{position:relative;display:grid;grid-template-columns:repeat(11,1fr);gap:2px;height:30px}
.escala-barra span{background:var(--celeste-suave);display:grid;place-items:center;font:600 11px var(--f-num);color:var(--tinta-2)}
.escala-barra span.on{background:var(--celeste);color:var(--hoja)}
.escala-pie{display:flex;justify-content:space-between;font:500 11px var(--f-num);color:var(--tinta-2);margin-top:6px}
/* tablas */
.tabla-wrap{overflow-x:auto;border:1px solid var(--linea);border-radius:4px;background:var(--hoja)}
table{width:100%;border-collapse:collapse;font-size:15px;min-width:540px}
th{font:600 11px/1.3 var(--f-num);letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-2);text-align:right;padding:12px 14px;border-bottom:1px solid var(--linea);vertical-align:bottom}
td{padding:9px 14px;border-bottom:1px solid var(--linea);text-align:right;font-family:var(--f-num);font-variant-numeric:tabular-nums}
th:first-child,td:first-child{text-align:left}
tbody tr:last-child td{border-bottom:0}
td.cat{font:700 18px var(--f-display);color:var(--celeste)}
/* botón y oferta */
.boton{display:inline-flex;align-items:center;gap:12px;background:var(--tinta);color:var(--papel);border-radius:4px;padding:15px 22px;font:700 16px/1 var(--f-texto);text-decoration:none}
.boton:hover{color:var(--papel);background:color-mix(in srgb,var(--tinta) 84%,var(--celeste))}
.boton .num{font-weight:600;padding-left:12px;border-left:1px solid color-mix(in srgb,var(--papel) 35%,transparent)}
.oferta{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:center;margin-top:64px;padding:28px;border:2px solid var(--tinta);border-radius:4px;background:var(--hoja)}
.oferta>*{min-width:0}
.oferta h2{margin:0 0 10px}
.oferta ul{margin:12px 0 0;padding-left:20px;color:var(--tinta-2)}
.oferta li{margin:4px 0}
.oferta .compra{display:grid;gap:10px;justify-items:start}
@media (max-width:760px){.oferta{grid-template-columns:1fr;padding:22px}}
.pie{border-top:1px solid var(--linea);margin-top:80px;background:var(--hoja)}
.pie .wrap{padding-block:24px;display:flex;flex-wrap:wrap;gap:8px 24px;justify-content:space-between;color:var(--tinta-2);font-size:14px}
.mensaje{max-width:620px;margin:0 auto;padding-block:64px}
.mensaje h1{font-size:clamp(30px,4vw,44px);margin-bottom:16px}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
"""

MENU = [("/", "Calculadora monotributo"), ("/escalas-monotributo-2026", "Escalas 2026"),
        ("/recategorizacion-monotributo-febrero-2027", "Recategorización"),
        ("/cuanto-se-paga-de-monotributo", "Cuánto se paga"), ("/precios-mercado-libre", "Precios Mercado Libre"), ("/aumento-alquiler", "Aumento de alquiler")]

def layout(slug, title, desc, body, og_type="article", extra_head="", script=""):
    url = f"{BASE}/{slug}" if slug else f"{BASE}/"
    href = f"/{slug}" if slug else "/"
    menu = "".join(f'<a href="{h}"{' aria-current="page"' if h == href else ""}>{t}</a>' for h, t in MENU)
    return f"""<!doctype html>
<html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:type" content="{og_type}"><meta property="og:locale" content="es_AR"><meta property="og:site_name" content="Kit Monotributista">
{FONTS}<link rel="stylesheet" href="/estilo.css">{extra_head}</head>
<body><header class="top"><div class="wrap"><a class="marca" href="/"><i>A–K</i>Kit Monotributista</a><nav class="menu" aria-label="Secciones">{menu}</nav></div></header>
<main class="wrap">
{body}
</main>
<footer class="pie"><div class="wrap"><span>Información general actualizada a octubre de 2026. No reemplaza a un contador ni la información oficial de ARCA.</span><span>Pagos procesados por Mercado Pago</span></div></footer>
{script}</body></html>
"""

def oferta_kit():
    return """<section class="oferta" aria-labelledby="of-kit"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-kit">Kit Monotributista 2026</h2>
<p>Cargás cada factura con fecha e importe. La planilla hace el resto, mes a mes.</p>
<ul><li>Facturación de los últimos 12 meses y categoría que te corresponde</li><li>Margen antes de subir de categoría y antes de la exclusión</li><li>Proyección al ritmo de tus últimos 3 meses, con alerta</li><li>Tablero de gastos y ahorro en pesos y en dólares</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=kit">Comprar el Kit <span class="num">$ 6.999</span></a><span class="nota">Pagás con Mercado Pago y lo descargás al instante. Escalas editables para cuando cambien.</span></div></section>"""

def oferta_ml():
    return """<section class="oferta" aria-labelledby="of-ml"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-ml">Calculadora de Precios para Vendedores</h2>
<p>Todo tu catálogo en una hoja: cargás costo, envío y el margen que querés, y te dice a cuánto publicar en cada canal.</p>
<ul><li>Precio para Clásica, Premium y venta directa con Mercado Pago</li><li>Ganancia neta y margen real de lo que ya tenés publicado</li><li>Costo fijo de productos baratos, cuotas, Ingresos Brutos y retenciones</li><li>Hasta 500 productos, con alertas de margen bajo</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=vendedores">Comprar la planilla <span class="num">$ 4.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante.</span></div></section>"""

def tabla_escalas():
    filas = "".join(f'<tr><td class="cat">{c}</td><td>{ars(t)}</td><td>{ars(s)}</td><td>{ars(v)}</td></tr>' for c, t, s, v in CATS)
    return f'<div class="tabla-wrap"><table><thead><tr><th>Cat.</th><th>Tope de ingresos anuales</th><th>Cuota mensual servicios</th><th>Cuota mensual venta de bienes</th></tr></thead><tbody>{filas}</tbody></table></div>'

cats_js = json.dumps([[c, t, s, v] for c, t, s, v in CATS])
HOME_BODY = f"""<section class="heroe">
<div><span class="etiqueta">Escalas vigentes de agosto 2026 a enero 2027</span>
<h1>¿En qué categoría del Monotributo estás?</h1>
<p class="bajada">Poné lo que facturaste en los últimos 12 meses y mirá tu categoría, tu cuota y cuánto margen te queda antes de la recategorización de febrero.</p>
<ul class="puntos"><li><span class="num">05/02</span><span><b>Vence la recategorización.</b> Se mira lo facturado de enero a diciembre de 2026.</span></li>
<li><span class="num">A–K</span><span><b>Once categorías.</b> Arriba de la K quedás fuera del régimen.</span></li>
<li><span class="num">50%</span><span><b>Multa</b> sobre la cuota si correspondía subir y no lo hiciste.</span></li></ul></div>
<form class="comp" id="calc" aria-labelledby="calc-t" onsubmit="return false">
<div class="comp-cab"><span id="calc-t">Cálculo de categoría</span><span>Comprobante no válido como factura</span></div>
<div class="comp-cuerpo">
<div class="campo"><label for="fact">Facturación de los últimos 12 meses</label><div class="entrada"><span>$</span><input id="fact" inputmode="numeric" autocomplete="off" value="20.000.000"></div></div>
<div class="campo"><label for="act">Actividad</label><div class="entrada"><select id="act"><option value="s">Servicios</option><option value="v">Venta de bienes</option></select></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-cat">C</b><small>CATEGORÍA</small></div></div>
<dl class="datos"><div><dt>Cuota mensual</dt><dd id="r-cuota">–</dd></div><div><dt>Tope de la categoría</dt><dd id="r-tope">–</dd></div><div><dt>Margen antes de subir</dt><dd id="r-margen">–</dd></div><div><dt>Tope usado</dt><dd id="r-uso">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
<div class="escala" aria-hidden="true"><div class="escala-barra" id="barra"></div><div class="escala-pie"><span>$ 0</span><span>Tope K {ars(CATS[-1][1], False)}</span></div></div>
</div></form>
</section>
<h2>Escalas del Monotributo vigentes</h2>
<p class="lectura">Valores para los pagos de agosto 2026 a enero 2027. La cuota incluye impuesto integrado, aporte jubilatorio y obra social. <a href="/escalas-monotributo-2026">Ver la explicación completa</a>.</p>
{tabla_escalas()}
{oferta_kit()}
<h2>Preguntas frecuentes</h2>
<div class="lectura"><h3>¿Qué meses se cuentan para la recategorización de febrero 2027?</h3><p>Los 12 meses anteriores: de enero a diciembre de 2026. <a href="/recategorizacion-monotributo-febrero-2027">Guía completa de la recategorización</a>.</p>
<h3>¿Solo importa lo que facturo?</h3><p>No. También cuentan la superficie del local, la energía consumida y los alquileres. Te corresponde la categoría más alta que resulte de cualquiera de esos parámetros.</p>
<h3>¿Cuánto voy a pagar por mes?</h3><p>Entre {ars(CATS[0][2])} en la A y {ars(CATS[-1][2])} en la K para servicios. <a href="/cuanto-se-paga-de-monotributo">Ver cuánto se paga en cada categoría</a>.</p></div>
"""
HOME_JS = f"""<script>
const C={cats_js};
const f=n=>"$ "+n.toLocaleString("es-AR",{{minimumFractionDigits:2,maximumFractionDigits:2}});
const $=id=>document.getElementById(id);
$("barra").innerHTML=C.map(c=>`<span data-c="${{c[0]}}">${{c[0]}}</span>`).join("");
function calc(){{
  const v=parseFloat(($("fact").value||"").replace(/\\./g,"").replace(",","."));
  const sello=$("sello"),est=$("r-estado");
  document.querySelectorAll("#barra span").forEach(s=>s.classList.remove("on"));
  if(!(v>=0)){{$("r-cat").textContent="?";est.className="estado";est.textContent="Ingresá un monto, por ejemplo 15.000.000.";return}}
  const i=C.findIndex(c=>v<=c[1]);
  if(i<0){{$("r-cat").textContent="!";sello.classList.add("alerta");["r-cuota","r-tope","r-margen","r-uso"].forEach(x=>$(x).textContent="–");
    est.className="estado mal";est.textContent="Superás el tope de la categoría K: quedarías fuera del Monotributo. Consultá a un contador.";return}}
  const c=C[i],cuota=$("act").value==="s"?c[2]:c[3],uso=v/c[1];
  $("r-cat").textContent=c[0];$("r-cuota").textContent=f(cuota);$("r-tope").textContent=f(c[1]);$("r-margen").textContent=f(c[1]-v);$("r-uso").textContent=(uso*100).toFixed(1).replace(".",",")+"%";
  document.querySelector(`#barra span[data-c="${{c[0]}}"]`).classList.add("on");
  sello.classList.toggle("alerta",uso>=.9);
  est.className="estado "+(uso>=.9?"mal":"bien");
  est.textContent=uso>=.9?"Estás a menos del 10% del tope: si seguís facturando así, en febrero subís de categoría.":"Tenés margen dentro de tu categoría.";
}}
$("fact").addEventListener("input",e=>{{const d=e.target.value.replace(/\\D/g,"");e.target.value=d?Number(d).toLocaleString("es-AR"):"";calc()}});
$("act").addEventListener("change",calc);calc();
</script>"""

ML_BODY = """<section class="heroe">
<div><span class="etiqueta">Para vendedores de Mercado Libre y tienda propia</span>
<h1>¿A cuánto tenés que publicar para ganar lo que querés?</h1>
<p class="bajada">Poné el costo, el envío a tu cargo y el margen que buscás. Te calculo el precio en Clásica, Premium y venta directa, con comisiones e impuestos incluidos.</p>
<ul class="puntos"><li><span class="num">%</span><span><b>Las comisiones cambian por categoría.</b> Mirá las tuyas al publicar y cargalas abajo.</span></li>
<li><span class="num">$</span><span><b>Los productos baratos pagan un costo fijo</b> además de la comisión.</span></li>
<li><span class="num">IIBB</span><span><b>Ingresos Brutos y retenciones</b> también salen de tu precio.</span></li></ul></div>
<form class="comp" id="ml" aria-labelledby="ml-t" onsubmit="return false">
<div class="comp-cab"><span id="ml-t">Cálculo de precio de venta</span><span>Valores de ejemplo editables</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="costo">Costo del producto</label><div class="entrada"><span>$</span><input id="costo" inputmode="numeric" value="10.000"></div></div>
<div class="campo"><label for="envio">Envío a tu cargo</label><div class="entrada"><span>$</span><input id="envio" inputmode="numeric" value="0"></div></div></div>
<div class="fila2"><div class="campo"><label for="margen">Margen que querés</label><div class="entrada"><input id="margen" inputmode="decimal" value="30"><span style="padding:0 14px 0 0">%</span></div></div>
<div class="campo"><label for="iibb">Ingresos Brutos y retenciones</label><div class="entrada"><input id="iibb" inputmode="decimal" value="3"><span style="padding:0 14px 0 0">%</span></div></div></div>
<div class="fila2"><div class="campo"><label for="cc">Comisión Clásica</label><div class="entrada"><input id="cc" inputmode="decimal" value="13"><span style="padding:0 14px 0 0">%</span></div></div>
<div class="campo"><label for="cp">Comisión Premium</label><div class="entrada"><input id="cp" inputmode="decimal" value="18"><span style="padding:0 14px 0 0">%</span></div></div></div>
<div class="tabla-wrap"><table style="min-width:0"><thead><tr><th>Canal</th><th>Precio a publicar</th><th>Te queda</th></tr></thead>
<tbody><tr><td>Clásica</td><td id="p-c">–</td><td id="n-c">–</td></tr><tr><td>Premium</td><td id="p-p">–</td><td id="n-p">–</td></tr><tr><td>Venta directa</td><td id="p-d">–</td><td id="n-d">–</td></tr></tbody></table></div>
<p class="nota" id="ml-nota">Venta directa con Mercado Pago a 6,29%. Productos de menos de $ 33.000 suman un costo fijo estimado de $ 1.100 en Mercado Libre.</p>
</div></form></section>
<h2>Cómo se calcula el precio</h2>
<div class="lectura"><p>El precio sale de dividir todo lo que te cuesta vender por lo que te queda de cada peso:</p>
<p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">precio = (costo + envío + costo fijo) / (1 − comisión − impuestos − margen)</p>
<p>Si sumás la comisión al costo y después le agregás tu margen, el precio te queda corto, porque la comisión también se cobra sobre tu ganancia. Por eso conviene dividir y no sumar.</p>
<h3>¿Clásica o Premium?</h3><p>Premium cobra más comisión porque incluye cuotas sin interés para el comprador. Si tu producto se vende bien sin cuotas, Clásica te deja más margen al mismo precio.</p></div>
""" + oferta_ml()
ML_JS = """<script>
const $=id=>document.getElementById(id);
const num=id=>parseFloat(($(id).value||"0").replace(/\\./g,"").replace(",","."))||0;
const pct=id=>(parseFloat(($(id).value||"0").replace(",","."))||0)/100;
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
const UMBRAL=33000,FIJO=1100,DIRECTA=0.0629;
function precio(base,com,imp,m,fijo){const k=com+imp+m;if(k>=1)return null;let p=base/(1-k);if(fijo&&p<UMBRAL)p=(base+FIJO)/(1-k);return p}
function neto(p,base,com,imp,fijo){return p*(1-com-imp)-base-(fijo&&p<UMBRAL?FIJO:0)}
function calc(){const base=num("costo")+num("envio"),imp=pct("iibb"),m=pct("margen");
 [["c",pct("cc"),true],["p",pct("cp"),true],["d",DIRECTA,false]].forEach(([k,com,fijo])=>{const p=precio(base,com,imp,m,fijo);
  $("p-"+k).textContent=p?f(p):"Margen imposible";$("n-"+k).textContent=p?f(neto(p,base,com,imp,fijo)):"–"})}
["costo","envio"].forEach(id=>$(id).addEventListener("input",e=>{const d=e.target.value.replace(/\\D/g,"");e.target.value=d?Number(d).toLocaleString("es-AR"):"";calc()}));
["margen","iibb","cc","cp"].forEach(id=>$(id).addEventListener("input",calc));calc();
</script>"""

def oferta_alq():
    return """<section class="oferta" aria-labelledby="of-alq"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-alq">Planilla de Alquileres 2026</h2>
<p>Para propietarios con uno o varios alquileres: cada contrato se actualiza solo con el IPC y ves quién te debe.</p>
<ul><li>Alquiler vigente, aumento acumulado y fecha del próximo ajuste de cada contrato</li><li>IPC del INDEC ya cargado, mes a mes</li><li>Registro de cobros de alquiler, expensas, ABL y servicios, con atrasados marcados</li><li>Resumen anual de lo cobrado y lo pendiente por propiedad</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=alquileres">Comprar la planilla <span class="num">$ 3.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante.</span></div></section>"""

# ---------- Alquileres ----------
ALQ_BODY = """<section class="heroe">
<div><span class="etiqueta">Con el IPC oficial del INDEC</span>
<h1>¿Cuánto te aumenta el alquiler?</h1>
<p class="bajada">Poné el monto con el que arrancó el contrato, cuándo empezó y cada cuántos meses se actualiza. Te calculo el alquiler de hoy y todos los ajustes, con el IPC publicado.</p>
<ul class="puntos"><li><span class="num">IPC</span><span><b>El INDEC lo publica a mediados de mes.</b> Por eso cada ajuste usa el índice de dos meses antes.</span></li>
<li><span class="num">3·4·6</span><span><b>La frecuencia la fija tu contrato.</b> Desde fines de 2023 se pacta libremente.</span></li>
<li><span class="num">ICL</span><span><b>Contratos de 2020 a 2023</b> suelen ajustar por ICL del BCRA, no por IPC.</span></li></ul></div>
<form class="comp" id="alq" aria-labelledby="alq-t" onsubmit="return false">
<div class="comp-cab"><span id="alq-t">Actualización de alquiler</span><span id="alq-fuente">IPC INDEC</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="monto">Alquiler inicial</label><div class="entrada"><span>$</span><input id="monto" inputmode="numeric" autocomplete="off" value="600.000"></div></div>
<div class="campo"><label for="inicio">Inicio del contrato</label><div class="entrada"><input id="inicio" type="month" value="2026-01"></div></div></div>
<div class="fila2"><div class="campo"><label for="frec">Se actualiza cada</label><div class="entrada"><select id="frec"><option value="3" selected>3 meses</option><option value="4">4 meses</option><option value="6">6 meses</option><option value="12">12 meses</option><option value="1">mes</option></select></div></div>
<div class="campo"><label for="rez">IPC que usa el ajuste</label><div class="entrada"><select id="rez"><option value="1" selected>Hasta 2 meses antes</option><option value="0">Hasta el mes anterior</option></select></div></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-pct" style="font-size:30px">–</b><small>AJUSTE</small></div></div>
<dl class="datos"><div><dt>Alquiler de hoy</dt><dd id="r-hoy">–</dd></div><div><dt>Aumento desde el inicio</dt><dd id="r-acum">–</dd></div><div><dt>Próximo ajuste</dt><dd id="r-prox">–</dd></div><div><dt>Último IPC publicado</dt><dd id="r-ult">–</dd></div></dl></div>
<p class="estado" id="r-estado">Cargando el IPC del INDEC…</p>
<div class="tabla-wrap"><table style="min-width:0;white-space:nowrap"><thead><tr><th>Desde</th><th>IPC usado</th><th>Aumento</th><th>Alquiler</th></tr></thead><tbody id="r-tabla"></tbody></table></div>
</div></form></section>
<h2>Cómo se calcula</h2>
<div class="lectura"><p>En cada ajuste el alquiler se multiplica por la inflación acumulada del período. Con el índice de nivel del INDEC alcanza con una división:</p>
<p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">alquiler nuevo = alquiler inicial × IPC del mes base del ajuste / IPC del mes base del inicio</p>
<p>El mes base es el último IPC publicado antes del ajuste. Como el INDEC publica cada índice a mediados del mes siguiente, un ajuste de abril usa el IPC de febrero. Algunos contratos usan el del mes anterior: elegí la opción que diga el tuyo.</p>
<h3>¿Mi contrato ajusta por IPC o por ICL?</h3><p>Los contratos firmados entre julio de 2020 y diciembre de 2023 bajo la Ley de Alquileres suelen ajustar por el Índice de Contratos de Locación (ICL) que publica el BCRA. Los firmados después pactan libremente el índice y la frecuencia, y la mayoría eligió el IPC. Lo que vale siempre es la cláusula de tu contrato.</p>
<h3>¿Y si todavía no salió el IPC?</h3><p>El ajuste queda marcado como pendiente. Volvé cuando el INDEC lo publique: la calculadora se actualiza sola.</p></div>
""" + oferta_alq()
ALQ_JS = """<script>
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
const MESES=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"];
const mi=s=>{const[y,m]=s.split("-").map(Number);return y*12+m-1};
const ms=i=>MESES[i%12]+" "+Math.floor(i/12);
let IPC={},ULT=0;
function calc(){const d=$("monto").value.replace(/\\D/g,""),monto=Number(d),ini=$("inicio").value;
 if(!monto||!ini||!ULT)return;const n=+$("frec").value,rez=+$("rez").value,a0=mi(ini),hoy=new Date(),h=hoy.getFullYear()*12+hoy.getMonth();
 const b0=a0-1-rez,i0=IPC[b0];let filas=[`<tr><td>${ms(a0)}</td><td>–</td><td>–</td><td>${f(monto)}</td></tr>`],prev=monto,vig=monto,pctVig=null,prox=null;
 if(!i0){$("r-estado").textContent="No hay IPC publicado para "+ms(b0)+". Probá con una fecha de inicio más reciente.";return}
 for(let a=a0+n;a<=h+n;a+=n){const b=a-1-rez,ib=IPC[b];
  if(!ib){filas.push(`<tr><td>${ms(a)}</td><td>${ms(b)}</td><td colspan="2">Se conoce a mediados de ${ms(b+1)}</td></tr>`);if(a<=h){vig=null}if(!prox)prox=a;break}
  const v=monto*ib/i0,p=v/prev-1;filas.push(`<tr><td>${ms(a)}</td><td>${ms(b)}</td><td>+${(p*100).toFixed(1).replace(".",",")}%</td><td>${f(v)}</td></tr>`);
  if(a<=h){vig=v;pctVig=p}else if(!prox)prox=a;prev=v}
 $("r-tabla").innerHTML=filas.join("");
 $("r-hoy").textContent=vig?f(vig):"Pendiente";$("r-acum").textContent=vig?"+"+((vig/monto-1)*100).toFixed(1).replace(".",",")+"%":"–";
 $("r-pct").textContent=pctVig!=null?"+"+Math.round(pctVig*100)+"%":"–";$("r-prox").textContent=prox?ms(prox):"–";
 $("r-estado").textContent=vig?"Calculado con el IPC nivel general del INDEC.":"El ajuste de este mes espera el próximo IPC.";}
fetch("/api/ipc").then(r=>r.ok?r.json():Promise.reject()).then(j=>{j.datos.forEach(([d,v])=>{IPC[mi(d.slice(0,7))]=v});ULT=Math.max(...Object.keys(IPC).map(Number));$("r-ult").textContent=ms(ULT);calc()})
 .catch(()=>{$("r-estado").textContent="No pudimos traer el IPC del INDEC. Probá recargar en unos minutos."});
$("monto").addEventListener("input",e=>{const d=e.target.value.replace(/\\D/g,"");e.target.value=d?Number(d).toLocaleString("es-AR"):"";calc()});
["inicio","frec","rez"].forEach(id=>$(id).addEventListener("change",calc));
</script>"""

# ---------- Artículos ----------
ARTS = {
"escalas-monotributo-2026": ("Escalas del Monotributo 2026: topes y cuotas vigentes",
"Tabla completa de categorías del Monotributo A a K vigentes desde agosto 2026: tope de ingresos brutos anuales y cuota mensual para servicios y venta de bienes.",
f"""<span class="etiqueta">Agosto 2026 a enero 2027</span><h1>Escalas del Monotributo 2026</h1>
<p class="bajada">Estas son las categorías que rigen para los pagos de agosto de 2026 a enero de 2027. La cuota incluye el impuesto integrado, el aporte jubilatorio (SIPA) y la obra social.</p>
<h2>Topes y cuotas por categoría</h2>{tabla_escalas()}
<div class="lectura"><h2>Cómo leer la tabla</h2><ul><li>El <b>tope de ingresos</b> es lo máximo que podés facturar en los últimos 12 meses para estar en esa categoría.</li>
<li>Si prestás servicios, mirá la columna de servicios. Si vendés productos, la de venta de bienes.</li>
<li>Si superás el tope de la categoría K, quedás fuera del régimen y pasás al régimen general.</li></ul>
<h2>Además de los ingresos</h2><p>La categoría también depende de la superficie afectada a la actividad, la energía eléctrica consumida y los alquileres devengados. Te corresponde la categoría más alta que resulte de cualquiera de esos parámetros.</p>
<p>¿Querés saber tu categoría ahora? Usá la <a href="/">calculadora de categoría</a>.</p></div>""" + oferta_kit()),
"recategorizacion-monotributo-febrero-2027": ("Recategorización del Monotributo febrero 2027: fecha y cómo se hace",
"La próxima recategorización del Monotributo vence el 5 de febrero de 2027. Qué meses se cuentan, qué parámetros se revisan, cómo se hace en ARCA y qué pasa si no la hacés.",
"""<span class="etiqueta">Vence el 5 de febrero de 2027</span><h1>Recategorización del Monotributo, febrero 2027</h1>
<p class="bajada">Es semestral: se hace en febrero y en agosto. La de febrero 2027 se calcula con lo que facturaste de enero a diciembre de 2026.</p>
<div class="lectura"><h2>Qué se revisa</h2><ul><li>Ingresos brutos de los últimos 12 meses.</li><li>Alquileres devengados en ese período.</li><li>Superficie afectada a la actividad.</li><li>Energía eléctrica consumida en el año.</li></ul>
<p>Si ninguno de esos valores salió de los límites de tu categoría actual, no tenés que cambiar nada. Si alguno los superó, tenés que subir. Si quedaste por debajo, podés bajar y pagar menos.</p>
<h2>Cómo se hace</h2><ol><li>Entrá a arca.gob.ar con tu CUIT y Clave Fiscal.</li><li>Abrí el servicio de Monotributo y elegí recategorización.</li><li>Revisá los datos de los últimos 12 meses.</li><li>Confirmá tu categoría actual o elegí la nueva.</li><li>Guardá el comprobante.</li></ol>
<h2>Qué pasa si no te recategorizás</h2><p>Si correspondía cambiar y no lo hiciste, hay una multa del 50% sobre el impuesto integrado y los aportes que debías pagar. ARCA también puede recategorizarte de oficio si detecta diferencias entre tus compras, gastos o acreditaciones bancarias y lo que declaraste. El aviso llega a tu Domicilio Fiscal Electrónico y tenés 15 días para presentar un descargo.</p>
<h2>Cómo llegar tranquilo a febrero</h2><p>Sumá tu facturación mes a mes y comparala con los <a href="/escalas-monotributo-2026">topes vigentes</a>. Para un cálculo rápido, usá la <a href="/">calculadora de categoría</a>.</p></div>""" + oferta_kit()),
"cuanto-se-paga-de-monotributo": ("¿Cuánto se paga de Monotributo en 2026? Cuota por categoría",
"Cuánto se paga de Monotributo por mes en cada categoría, desde $49.527 en la A hasta $1.614.446 en la K. Qué incluye la cuota y cuánto pesa sobre lo que facturás.",
f"""<span class="etiqueta">Cuotas desde agosto 2026</span><h1>¿Cuánto se paga de Monotributo por mes?</h1>
<p class="bajada">La cuota va de {ars(CATS[0][2])} en la categoría A hasta {ars(CATS[-1][2])} en la K para servicios. En venta de bienes, la K paga {ars(CATS[-1][3])}.</p>
<div class="lectura"><h2>Qué incluye la cuota</h2><ul><li><b>Impuesto integrado</b>, que reemplaza a IVA y Ganancias.</li><li><b>Aporte jubilatorio</b> (SIPA).</li><li><b>Obra social.</b></li></ul>
<p>Los Ingresos Brutos provinciales se pagan aparte, salvo en las provincias con régimen simplificado unificado.</p></div>
<h2>Cuota por categoría</h2>{tabla_escalas()}
<div class="lectura"><h2>Cuánto pesa sobre lo que facturás</h2><p>Depende de dónde estés dentro de la categoría. Alguien en la A que factura {ars(6000000, False)} al año paga {ars(CATS[0][2]*12)} de cuota anual, cerca del 9,9% de lo facturado. Cerca del tope de la A, el peso baja a alrededor del 4,9%.</p>
<p>¿Querés saber tu cuota exacta? Probá la <a href="/">calculadora de categoría</a>.</p></div>""" + oferta_kit()),
}

def main():
    os.makedirs(PUB, exist_ok=True)
    w = lambda name, s: open(os.path.join(PUB, name), "w", encoding="utf-8").write(s)
    w("estilo.css", CSS)
    w("index.html", layout("", "Calculadora de categoría de Monotributo 2026", "Calculá gratis tu categoría de Monotributo con las escalas vigentes de agosto 2026 a enero 2027: cuota, tope y margen antes de la recategorización de febrero.", HOME_BODY, "website", script=HOME_JS))
    w("precios-mercado-libre.html", layout("precios-mercado-libre", "Calculadora de precios para Mercado Libre 2026", "Calculá a cuánto publicar en Mercado Libre Clásica, Premium y venta directa para ganar el margen que querés, con comisiones, costo fijo e Ingresos Brutos.", ML_BODY, "website", script=ML_JS))
    w("aumento-alquiler.html", layout("aumento-alquiler", "Calculadora de aumento de alquiler por IPC 2026", "Calculá cuánto te aumenta el alquiler con el IPC oficial del INDEC: alquiler de hoy, todos los ajustes y la fecha del próximo, para contratos que se actualizan cada 3, 4, 6 o 12 meses.", ALQ_BODY, "website", script=ALQ_JS))
    for slug, (t, d, b) in ARTS.items():
        w(f"{slug}.html", layout(slug, t, d, b))
    urls = ["", "precios-mercado-libre", "aumento-alquiler"] + list(ARTS)
    w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{HOY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    w("robots.txt", f"User-agent: *\nDisallow: /comprar\nDisallow: /gracias\nDisallow: /descargar\nSitemap: {BASE}/sitemap.xml\n")
    print("ok", len(urls), "páginas")

if __name__ == "__main__":
    main()
