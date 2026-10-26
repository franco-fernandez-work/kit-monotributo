"""Genera todas las páginas de public/ con un diseño común. Correr: python3 tools/build_site.py"""
import legal_site as LS
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
        ("/cuanto-se-paga-de-monotributo", "Cuánto se paga"), ("/precios-mercado-libre", "Precios Mercado Libre"), ("/aumento-alquiler", "Aumento de alquiler"),
        ("/aguinaldo", "Aguinaldo"), ("/sueldo-empleada-domestica", "Sueldo empleada doméstica"), ("/calculadora-vacaciones", "Vacaciones"), ("/calculadora-liquidacion-final", "Liquidación final"), ("/calculadora-ganancias-sueldo", "Ganancias en el sueldo"), ("/guia-primer-ano-monotributo", "Guía primer año"), ("/recibos-presupuestos-pdf", "Recibos y presupuestos"), ("/generador-reclamo-consumidor", "Reclamos de consumo"), ("/telegrama-renuncia-modelo", "Telegramas laborales"), ("/boleto-compraventa-auto-usado", "Boleto de auto usado"), ("/alquiler-temporario-verano", "Alquiler de verano"), ("/autorizacion-viaje-menores", "Viaje de menores"), ("/cuota-alimentaria-aguinaldo", "Cuota alimentaria"), ("/contrato-alquiler-estudiante", "Alquiler estudiantes"), ("/presupuesto-vuelta-al-cole", "Vuelta al cole"), ("/siradig-que-puedo-deducir", "SIRADIG")]

def layout(slug, title, desc, body, og_type="article", extra_head="", script=""):
    url = f"{BASE}/{slug}" if slug else f"{BASE}/"
    href = f"/{slug}" if slug else "/"
    menu = "".join(f'<a href="{h}"{' aria-current="page"' if h == href else ""}>{t}</a>' for h, t in MENU)
    return f"""<!doctype html>
<html lang="es-AR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:type" content="{og_type}"><meta property="og:locale" content="es_AR"><meta property="og:site_name" content="Kit Monotributista">
{FONTS}<link rel="stylesheet" href="/estilo.css">{extra_head}</head>
<body><header class="top"><div class="wrap"><a class="marca" href="/"><i>A–K</i>Kit Monotributista</a><nav class="menu" aria-label="Secciones">{menu}<a class="arrep" href="/arrepentimiento">Botón de arrepentimiento</a></nav></div></header>
<main class="wrap">
{body}
</main>
{LS.footer()}
{script}</body></html>
"""

def oferta_kit():
    return """<section class="oferta" aria-labelledby="of-kit"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-kit">Kit Monotributista 2026</h2>
<p>Cargás cada factura con fecha e importe. La planilla hace el resto, mes a mes.</p>
<ul><li>Facturación de los últimos 12 meses y categoría que te corresponde</li><li>Margen antes de subir de categoría y antes de la exclusión</li><li>Proyección al ritmo de tus últimos 3 meses, con alerta</li><li>Tablero de gastos y ahorro en pesos y en dólares</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=kit">Comprar el Kit <span class="num">$ 6.999</span></a><span class="nota">Pagás con Mercado Pago y lo descargás al instante. Escalas editables para cuando cambien.</span><a class="nota" href="/comprar?p=kitguia">Con la guía \"Primer año de monotributo\": $ 8.999</a></div></section>"""

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

from escalas_cp import CATS as CP_CATS, ESCALAS as CP_ESC
CP_MESES = {10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

def oferta_cp():
    return """<section class="oferta" aria-labelledby="of-cp"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-cp">Planilla Casas Particulares 2026</h2>
<p>Todo lo que tenés que calcular como empleador de una trabajadora de casas particulares, con las escalas oficiales cargadas.</p>
<ul><li>Sueldo del mes por hora o mensual, con antigüedad y zona desfavorable</li><li>Recibo de sueldo listo para imprimir y firmar</li><li>Aguinaldo, también proporcional si entró o se fue a mitad de semestre</li><li>Vacaciones y liquidación final por despido o renuncia</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=casas">Comprar la planilla <span class="num">$ 4.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante. Escalas editables para cuando cambien.</span></div></section>"""

def tabla_cp(mes):
    filas = "".join(f'<tr><td>{c}</td><td>{ars(v[0]) if v[0] else "–"}</td><td>{ars(v[1])}</td><td>{ars(v[2]) if v[2] else "–"}</td><td>{ars(v[3])}</td></tr>' for c, v in zip(CP_CATS, CP_ESC[(2026, mes)]))
    return f'<div class="tabla-wrap"><table><thead><tr><th>Categoría</th><th>Hora con retiro</th><th>Hora sin retiro</th><th>Mes con retiro</th><th>Mes sin retiro</th></tr></thead><tbody>{filas}</tbody></table></div>'

# ---------- Aguinaldo ----------
AGU_BODY = """<section class="heroe">
<div><span class="etiqueta">Segunda cuota 2026</span>
<h1>¿Cuánto cobrás de aguinaldo en diciembre?</h1>
<p class="bajada">Poné tu mejor sueldo bruto de julio a diciembre. Si empezaste a trabajar en el semestre, poné la fecha y te calculo el proporcional.</p>
<ul class="puntos"><li><span class="num">18/12</span><span><b>Fecha límite de pago</b> de la segunda cuota, con 4 días hábiles de gracia.</span></li>
<li><span class="num">50%</span><span><b>De la mejor remuneración</b> mensual del semestre.</span></li>
<li><span class="num">184</span><span><b>Días del semestre.</b> Si trabajaste menos, cobrás la parte proporcional.</span></li></ul></div>
<form class="comp" id="agu" aria-labelledby="agu-t" onsubmit="return false">
<div class="comp-cab"><span id="agu-t">Sueldo anual complementario</span><span>Jul a dic 2026</span></div>
<div class="comp-cuerpo">
<div class="campo"><label for="sueldo">Mejor sueldo bruto del semestre</label><div class="entrada"><span>$</span><input id="sueldo" inputmode="numeric" autocomplete="off" value="1.000.000"></div></div>
<div class="fila2"><div class="campo"><label for="ingreso">Fecha de ingreso (si fue después del 1/7)</label><div class="entrada"><input id="ingreso" type="date" min="2026-07-01" max="2026-12-31"></div></div>
<div class="campo"><label for="tipo">Tipo de trabajo</label><div class="entrada"><select id="tipo"><option value="0.17">Empleado/a registrado/a</option><option value="0">Casas particulares</option></select></div></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b style="font-size:30px">SAC</b><small>2ª CUOTA</small></div></div>
<dl class="datos"><div><dt>Aguinaldo bruto</dt><dd id="r-bruto">–</dd></div><div><dt>Descuentos</dt><dd id="r-desc">–</dd></div><div><dt>Te queda en mano</dt><dd id="r-neto">–</dd></div><div><dt>Días computados</dt><dd id="r-dias">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
</div></form></section>
<h2>Cómo se calcula el aguinaldo</h2>
<div class="lectura"><p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">aguinaldo = mejor sueldo bruto del semestre / 2 × días trabajados / 184</p>
<p>Se toma la remuneración bruta más alta de julio a diciembre, con todos los conceptos remunerativos: básico, antigüedad, horas extra, presentismo y comisiones. Las sumas no remunerativas no cuentan.</p>
<h3>¿Qué descuentos tiene?</h3><p>Los mismos aportes que el sueldo: 11% de jubilación, 3% de obra social y 3% de PAMI, en total 17%. En casas particulares los aportes se pagan con montos fijos a ARCA y no se descuenta un porcentaje del aguinaldo.</p>
<h3>¿Cuándo se paga?</h3><p>La segunda cuota vence el 18 de diciembre. Por la ley de contrato de trabajo, el empleador tiene hasta 4 días hábiles más para pagarla.</p>
<h3>¿Y si me voy antes de diciembre?</h3><p>Cobrás el aguinaldo proporcional en la liquidación final, con la misma cuenta y los días trabajados hasta tu salida.</p></div>
""" + oferta_cp()
AGU_JS = """<script>
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
function calc(){const s=Number(($("sueldo").value||"0").replace(/\\D/g,"")),t=+$("tipo").value;
 let dias=184;const ing=$("ingreso").value;if(ing){const d=new Date(ing+"T00:00:00"),fin=new Date("2026-12-31T00:00:00");dias=Math.max(0,Math.min(184,Math.round((fin-d)/864e5)+1))}
 const b=s/2*dias/184,d=b*t;$("r-bruto").textContent=f(b);$("r-desc").textContent=t?"− "+f(d):"Aportes fijos a ARCA";$("r-neto").textContent=f(b-d);$("r-dias").textContent=dias+" de 184";
 $("r-estado").textContent=dias<184?"Proporcional a los días trabajados desde tu ingreso.":"Semestre completo."}
$("sueldo").addEventListener("input",e=>{const d=e.target.value.replace(/\\D/g,"");e.target.value=d?Number(d).toLocaleString("es-AR"):"";calc()});
["ingreso","tipo"].forEach(id=>$(id).addEventListener("change",calc));calc();
</script>"""

# ---------- Sueldo empleada doméstica ----------
CP_JS_DATA = json.dumps({str(m): CP_ESC[(2026, m)] for m in CP_MESES})
SUE_BODY = f"""<section class="heroe">
<div><span class="etiqueta">Escala oficial Resolución 6/2026</span>
<h1>¿Cuánto le tenés que pagar a tu empleada doméstica?</h1>
<p class="bajada">Elegí el mes, la categoría y si trabaja por hora o mensual. Te calculo el sueldo mínimo con antigüedad y zona desfavorable.</p>
<ul class="puntos"><li><span class="num">1%</span><span><b>Por año de antigüedad</b> con el mismo empleador, sobre el básico.</span></li>
<li><span class="num">31%</span><span><b>Zona desfavorable</b> en la Patagonia y en Patagones.</span></li>
<li><span class="num">+1,6%</span><span><b>Aumento de diciembre</b> sobre noviembre.</span></li></ul></div>
<form class="comp" id="sue" aria-labelledby="sue-t" onsubmit="return false">
<div class="comp-cab"><span id="sue-t">Sueldo de casas particulares</span><span>Mínimos oficiales</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="mes">Mes</label><div class="entrada"><select id="mes">{"".join(f'<option value="{m}"{" selected" if m == 11 else ""}>{n} 2026</option>' for m, n in CP_MESES.items())}</select></div></div>
<div class="campo"><label for="cat">Categoría</label><div class="entrada"><select id="cat">{"".join(f'<option value="{i}"{" selected" if i == 4 else ""}>{c}</option>' for i, c in enumerate(CP_CATS))}</select></div></div></div>
<div class="fila2"><div class="campo"><label for="mod">Modalidad</label><div class="entrada"><select id="mod"><option value="0">Con retiro</option><option value="1">Sin retiro (vive en la casa)</option></select></div></div>
<div class="campo"><label for="forma">Forma de pago</label><div class="entrada"><select id="forma"><option value="h">Por hora</option><option value="m">Mensual</option></select></div></div></div>
<div class="fila2"><div class="campo"><label for="horas">Horas por semana</label><div class="entrada"><input id="horas" inputmode="numeric" value="12"></div></div>
<div class="campo"><label for="ant">Años de antigüedad</label><div class="entrada"><input id="ant" inputmode="numeric" value="0"></div></div></div>
<div class="campo"><label for="zona">Zona</label><div class="entrada"><select id="zona"><option value="0">General</option><option value="0.31">Zona desfavorable (+31%)</option></select></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-hora" style="font-size:22px">–</b><small>POR HORA</small></div></div>
<dl class="datos"><div><dt>Básico del mes</dt><dd id="r-bas">–</dd></div><div><dt>Antigüedad</dt><dd id="r-ant">–</dd></div><div><dt>Zona</dt><dd id="r-zona">–</dd></div><div><dt>Total a pagar</dt><dd id="r-tot">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
</div></form></section>
<h2>Escala de noviembre 2026</h2>
<p class="lectura">Salarios mínimos de la Comisión Nacional de Trabajo en Casas Particulares. Con retiro: no vive en la casa. Sin retiro: vive en la casa.</p>
{tabla_cp(11)}
<h2>Escala de diciembre 2026</h2>
{tabla_cp(12)}
<div class="lectura"><h2>Preguntas frecuentes</h2>
<h3>¿Cómo calculo las horas del mes?</h3><p>La calculadora multiplica las horas semanales por 4,33, el promedio de semanas de un mes. Si llevás la cuenta exacta de horas trabajadas, usá esa.</p>
<h3>¿Qué más tengo que pagar?</h3><p>Los aportes y contribuciones a ARCA, que son montos fijos según las horas semanales, y el seguro de riesgos del trabajo. En diciembre, además, la segunda cuota del aguinaldo. <a href="/aguinaldo">Calculá el aguinaldo</a>.</p>
<h3>¿Y si la escala cambia?</h3><p>La Comisión Nacional de Trabajo en Casas Particulares fija nuevos valores varias veces al año. Actualizamos esta página cuando se publican.</p></div>
""" + oferta_cp()
SUE_JS = """<script>
const E=""" + CP_JS_DATA + """;
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
function calc(){const v=E[$("mes").value][+$("cat").value],mod=+$("mod").value,porHora=$("forma").value==="h";
 const vh=v[mod],vm=v[2+mod];$("horas").closest(".campo").style.opacity=porHora?1:.45;
 if(!(porHora?vh:vm)){["r-bas","r-ant","r-zona","r-tot"].forEach(i=>$(i).textContent="–");$("r-hora").textContent="–";$("r-estado").textContent="Los caseros solo tienen modalidad sin retiro.";return}
 const hs=Number(($("horas").value||"0").replace(/\\D/g,"")),a=Number(($("ant").value||"0").replace(/\\D/g,"")),z=+$("zona").value;
 const bas=porHora?vh*hs*4.33:vm,ant=bas*a/100,zo=bas*z;
 $("r-hora").textContent=vh?f(vh):"–";$("r-bas").textContent=f(bas);$("r-ant").textContent=f(ant);$("r-zona").textContent=f(zo);$("r-tot").textContent=f(bas+ant+zo);
 $("r-estado").textContent=porHora?hs+" horas por semana, unas "+Math.round(hs*4.33)+" por mes.":"Sueldo mensual por jornada completa.";}
["mes","cat","mod","forma","zona"].forEach(id=>$(id).addEventListener("change",calc));["horas","ant"].forEach(id=>$(id).addEventListener("input",calc));calc();
</script>"""

def oferta_vac():
    return """<section class="oferta" aria-labelledby="of-vac"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-vac">Planilla de Vacaciones del Equipo</h2>
<p>Para empleadores y PyMEs: cargás a cada persona una vez y la planilla te arma el año de vacaciones.</p>
<ul><li>Días que le corresponden a cada persona, con antigüedad al 31/12 y proporcional si entró en el año</li><li>Monto de cada licencia (sueldo / 25) y fecha límite para pagarla</li><li>Cronograma de octubre a septiembre con cuántas personas están afuera cada mes</li><li>Aviso de vacaciones listo para imprimir y firmar, con la fecha límite de entrega</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=vacaciones">Comprar la planilla <span class="num">$ 4.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante. Hasta 50 personas.</span></div></section>"""

# ---------- Vacaciones ----------
VAC_BODY = """<section class="heroe">
<div><span class="etiqueta">Ley de Contrato de Trabajo, art. 150 a 155</span>
<h1>¿Cuántos días de vacaciones te corresponden y cuánto te pagan?</h1>
<p class="bajada">Poné cuándo entraste y tu sueldo bruto. Te digo los días, el monto y, si ya sabés cuándo te vas, hasta qué fecha te tienen que avisar.</p>
<ul class="puntos"><li><span class="num">14–35</span><span><b>Días corridos según la antigüedad</b> que tenés al 31 de diciembre.</span></li>
<li><span class="num">÷25</span><span><b>Cada día se paga sueldo mensual / 25</b>, y se cobra antes de irte.</span></li>
<li><span class="num">30</span><span><b>Días de aviso por escrito</b> como mínimo antes de que empiecen.</span></li></ul></div>
<form class="comp" id="vac" aria-labelledby="vac-t" onsubmit="return false">
<div class="comp-cab"><span id="vac-t">Licencia anual ordinaria</span><span>Empleado/a mensualizado/a</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="ingreso">Fecha de ingreso</label><div class="entrada"><input id="ingreso" type="date" value="2021-03-01"></div></div>
<div class="campo"><label for="anio">Vacaciones del año</label><div class="entrada"><select id="anio"></select></div></div></div>
<div class="fila2"><div class="campo"><label for="sueldo">Sueldo bruto mensual</label><div class="entrada"><span>$</span><input id="sueldo" inputmode="numeric" autocomplete="off" value="1.200.000"></div></div>
<div class="campo"><label for="inicio">Querés empezar el (opcional)</label><div class="entrada"><input id="inicio" type="date"></div></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-dias">–</b><small>DÍAS</small></div></div>
<dl class="datos"><div><dt>Antigüedad al 31/12</dt><dd id="r-ant">–</dd></div><div><dt>Valor de cada día</dt><dd id="r-dia">–</dd></div><div><dt>Total bruto a cobrar</dt><dd id="r-bruto">–</dd></div><div><dt>Aviso hasta el</dt><dd id="r-aviso">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
<div class="escala" aria-hidden="true"><div class="escala-barra" id="barra" style="grid-template-columns:repeat(4,1fr)"><span data-d="14">14</span><span data-d="21">21</span><span data-d="28">28</span><span data-d="35">35</span></div><div class="escala-pie"><span>hasta 5 años</span><span>hasta 10</span><span>hasta 20</span><span>más de 20</span></div></div>
</div></form></section>
<h2>Cómo se calculan las vacaciones</h2>
<div class="lectura"><p>Los días dependen de la antigüedad que tengas al 31 de diciembre del año de las vacaciones:</p>
<div class="tabla-wrap"><table style="min-width:0"><thead><tr><th>Antigüedad</th><th>Días corridos</th></tr></thead><tbody><tr><td>Hasta 5 años</td><td>14</td></tr><tr><td>Más de 5 y hasta 10</td><td>21</td></tr><tr><td>Más de 10 y hasta 20</td><td>28</td></tr><tr><td>Más de 20</td><td>35</td></tr></tbody></table></div>
<p style="margin-top:18px">El pago de cada día es el sueldo mensual dividido 25:</p>
<p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">vacaciones = sueldo mensual / 25 × días que te corresponden</p>
<p>Con $ 1.200.000 de sueldo y 21 días, el día vale $ 48.000 y cobrás $ 1.008.000. Es más que un mes de sueldo repartido por días porque se divide por 25 y no por 30.</p>
<h3>¿Y si entré hace menos de 6 meses?</h3><p>Para cobrar el período completo tenés que haber trabajado al menos la mitad de los días hábiles del año. Si no llegás, te corresponde un día de descanso por cada 20 días trabajados. La calculadora lo aplica sola.</p>
<h3>¿Cuándo me las tienen que dar?</h3><p>Entre el 1 de octubre y el 30 de abril, salvo que acuerden otras fechas. El empleador tiene que avisarte por escrito con 30 días de anticipación como mínimo. Antes de la reforma de la Ley 27.802 eran 45.</p>
<h3>¿Se pueden dividir?</h3><p>Sí, pero solo si vos y el empleador lo acuerdan, en tramos de al menos 7 días corridos cada uno. El total de días no cambia.</p>
<h3>¿Cuándo se cobran?</h3><p>Antes de que empiecen. El empleador tiene que pagar la licencia por adelantado, antes del primer día.</p>
<h3>¿Los feriados y los fines de semana cuentan?</h3><p>Sí. Son días corridos, así que cuentan todos los días del calendario.</p>
<p class="nota">Cálculo para sueldos mensuales. Si cobrás por jornal, con comisiones, o tu convenio colectivo mejora estos días, valen las reglas de tu convenio.</p></div>
""" + oferta_vac()
VAC_JS = """<script>
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
const hoy=new Date(),an0=hoy.getMonth()<4?hoy.getFullYear()-1:hoy.getFullYear();
$("anio").innerHTML=[an0,an0+1].map(y=>`<option value="${y}">${y}-${y+1}</option>`).join("");
const fl=d=>d.toLocaleDateString("es-AR",{day:"numeric",month:"long",year:"numeric"});
const mas=(d,n)=>new Date(d.getFullYear()+n,d.getMonth(),d.getDate());
function calc(){const iv=$("ingreso").value,Y=+$("anio").value,s=Number(($("sueldo").value||"0").replace(/\\D/g,"")),est=$("r-estado");
 document.querySelectorAll("#barra span").forEach(x=>x.classList.remove("on"));
 ["r-ant","r-dia","r-bruto","r-aviso"].forEach(i=>$(i).textContent="–");$("r-dias").textContent="?";
 if(!iv){est.textContent="Poné la fecha de ingreso.";est.className="estado";return}
 const ing=new Date(iv+"T00:00:00"),corte=new Date(Y,11,31),ini0=new Date(Y,0,1);
 if(ing>corte){est.textContent="Todavía no habías ingresado ese año.";est.className="estado mal";return}
 const trab=Math.round((corte-(ing>ini0?ing:ini0))/864e5)+1;
 let a=corte.getFullYear()-ing.getFullYear();if(mas(ing,a)>corte)a--;
 $("r-ant").textContent=a+(a===1?" año":" años");
 let d,txt;
 if(trab<183){d=Math.floor(trab/20);txt="Trabajaste "+trab+" días del año: te toca 1 día cada 20 trabajados."}
 else{d=corte<=mas(ing,5)?14:corte<=mas(ing,10)?21:corte<=mas(ing,20)?28:35;txt="Tenés el período completo de vacaciones.";
  document.querySelector(`#barra span[data-d="${d}"]`).classList.add("on")}
 $("r-dias").textContent=d;est.className="estado bien";est.textContent=txt;
 if(s){$("r-dia").textContent=f(s/25);$("r-bruto").textContent=f(s/25*d)}
 const iniv=$("inicio").value;
 if(iniv){const i=new Date(iniv+"T00:00:00"),lim=new Date(i-30*864e5);$("r-aviso").textContent=fl(lim);
  if(lim<new Date(hoy.getFullYear(),hoy.getMonth(),hoy.getDate())){est.className="estado mal";est.textContent=txt+" El aviso de 30 días ya venció para esa fecha: hay que acordar otra o postergar el inicio."}}
}
$("sueldo").addEventListener("input",e=>{const x=e.target.value.replace(/\\D/g,"");e.target.value=x?Number(x).toLocaleString("es-AR"):"";calc()});
["ingreso","anio","inicio"].forEach(id=>$(id).addEventListener("change",calc));calc();
</script>"""

# ---------- Liquidación final ----------
def oferta_liq():
    return """<section class="oferta" aria-labelledby="of-liq"><div><span class="etiqueta">Planilla para Excel y Google Sheets</span><h2 id="of-liq">Planilla de Liquidación Final</h2>
<p>Para empleadores y PyMEs: cargás fechas y sueldo y la planilla arma toda la liquidación de cada egreso.</p>
<ul><li>Indemnización del art. 245 con tope del convenio y piso del 67%</li><li>Preaviso, integración del mes, aguinaldo y vacaciones proporcionales</li><li>Despido sin causa o renuncia, y período de prueba configurable</li><li>Recibo de liquidación final listo para imprimir y firmar, hasta 30 personas</li></ul></div>
<div class="compra"><a class="boton" href="/comprar?p=liquidacion">Comprar la planilla <span class="num">$ 5.999</span></a><span class="nota">Pagás con Mercado Pago y la descargás al instante.</span><a class="nota" href="/telegrama-renuncia-modelo">¿Vas a renunciar o intimar? Modelos de telegramas laborales</a></div></section>"""

LIQ_BODY = """<section class="heroe">
<div><span class="etiqueta">Ley de Contrato de Trabajo y Ley 27.802</span>
<h1>Liquidación final: cuánto te corresponde si te despiden o renunciás</h1>
<p class="bajada">Poné las fechas y el sueldo. Te digo la indemnización, el preaviso, el aguinaldo y las vacaciones proporcionales que te deben.</p>
<ul class="puntos"><li><span class="num">1×</span><span><b>Un sueldo por año de antigüedad</b> o fracción mayor de tres meses, si te despiden sin causa.</span></li>
<li><span class="num">1–2</span><span><b>Meses de preaviso</b>: uno hasta 5 años de antigüedad y dos con más.</span></li>
<li><span class="num">0</span><span><b>Indemnización si renunciás</b>, pero cobrás igual aguinaldo y vacaciones proporcionales.</span></li></ul></div>
<form class="comp" id="liq" aria-labelledby="liq-t" onsubmit="return false">
<div class="comp-cab"><span id="liq-t">Liquidación final</span><span>Sueldo mensual</span></div>
<div class="comp-cuerpo">
<div class="fila2"><div class="campo"><label for="tipo">Cómo termina</label><div class="entrada"><select id="tipo"><option value="d">Despido sin causa</option><option value="r">Renuncia</option></select></div></div>
<div class="campo"><label for="sueldo">Mejor sueldo bruto mensual</label><div class="entrada"><span>$</span><input id="sueldo" inputmode="numeric" autocomplete="off" value="1.500.000"></div></div></div>
<div class="fila2"><div class="campo"><label for="ingreso">Fecha de ingreso</label><div class="entrada"><input id="ingreso" type="date" value="2019-03-04"></div></div>
<div class="campo"><label for="egreso">Fecha de egreso</label><div class="entrada"><input id="egreso" type="date"></div></div></div>
<div class="fila2"><div class="campo"><label for="conv">Promedio del convenio (opcional)</label><div class="entrada"><span>$</span><input id="conv" inputmode="numeric" autocomplete="off" placeholder="para el tope"></div></div>
<div class="campo"><label for="gozadas">Vacaciones ya gozadas este año</label><div class="entrada"><input id="gozadas" inputmode="numeric" value="0"><span style="padding:0 14px 0 0">días</span></div></div></div>
<div class="resultado" aria-live="polite"><div class="sello" id="sello"><div><b id="r-tot">–</b><small>BRUTO</small></div></div>
<dl class="datos"><div><dt>Indemnización (art. 245)</dt><dd id="r-ind">–</dd></div><div><dt>Preaviso e integración</dt><dd id="r-pre">–</dd></div><div><dt>Aguinaldo proporcional</dt><dd id="r-sac">–</dd></div><div><dt>Vacaciones proporcionales</dt><dd id="r-vac">–</dd></div></dl></div>
<p class="estado" id="r-estado"></p>
</div></form></section>
<h2>Qué se paga en cada caso</h2>
<div class="lectura"><div class="tabla-wrap"><table style="min-width:0"><thead><tr><th>Rubro</th><th>Despido sin causa</th><th>Renuncia</th></tr></thead><tbody>
<tr><td>Indemnización por antigüedad (art. 245)</td><td>Sí</td><td>No</td></tr>
<tr><td>Preaviso (art. 231 y 232)</td><td>Sí, si no se dio</td><td>No</td></tr>
<tr><td>Integración del mes de despido (art. 233)</td><td>Sí</td><td>No</td></tr>
<tr><td>Aguinaldo proporcional (art. 123)</td><td>Sí</td><td>Sí</td></tr>
<tr><td>Vacaciones no gozadas (art. 156)</td><td>Sí</td><td>Sí</td></tr>
<tr><td>Días trabajados del mes</td><td>Sí</td><td>Sí</td></tr></tbody></table></div>
<h3>¿Cómo se calcula la indemnización?</h3><p>Es un mes de la mejor remuneración mensual normal y habitual por cada año de servicio o fracción mayor de tres meses, con un mínimo de un mes. La Ley 27.802 mantiene la fórmula pero deja fuera de la base el aguinaldo, las vacaciones y los premios que no se pagan todos los meses.</p>
<h3>¿Hay tope?</h3><p>Sí: la base no puede superar tres veces el promedio salarial del convenio aplicable. Aun con tope, la base no baja del 67% de tu mejor remuneración. Si cargás el promedio de tu convenio, la calculadora lo aplica.</p>
<p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">indemnización = base × años de antigüedad (fracción mayor de 3 meses = 1 año)</p>
<h3>¿Y el preaviso y la integración?</h3><p>Si te despiden sin darte preaviso, te pagan 1 mes de sueldo (hasta 5 años de antigüedad) o 2 meses (más de 5). Si el despido no cae el último día del mes, también te pagan los días que faltan hasta fin de mes, y un doceavo de aguinaldo sobre ambos.</p>
<h3>¿Qué pasa en el período de prueba?</h3><p>Con la reforma, durante los primeros 6 meses el despido no genera indemnización ni preaviso. Seguís cobrando los días trabajados, el aguinaldo y las vacaciones proporcionales. Algunos convenios fijan plazos distintos.</p>
<h3>¿Cómo se calculan las vacaciones no gozadas?</h3><p>Se toman los días que te corresponden por antigüedad, en proporción a lo trabajado en el año, menos los que ya tomaste. Cada día vale sueldo mensual / 25.</p>
<p class="nota">Cálculo orientativo para sueldos mensuales. No incluye descuentos, remuneración variable, jornal ni mejoras de tu convenio. La indemnización puede discutirse y los criterios judiciales cambian: consultá a un contador o abogado laboral antes de pagar o firmar.</p></div>
""" + oferta_liq()
LIQ_JS = """<script>
const $=id=>document.getElementById(id);
const f=n=>"$ "+Math.round(n).toLocaleString("es-AR");
const mas=(d,m)=>{const x=new Date(d.getFullYear(),d.getMonth()+m,d.getDate());if(x.getDate()!==d.getDate())x.setDate(0);return x};
const num=v=>Number((v||"0").replace(/[^0-9]/g,""));
const hoy=new Date();$("egreso").value=hoy.toISOString().slice(0,10);
function calc(){const est=$("r-estado"),des=$("tipo").value==="d",s=num($("sueldo").value),cv=num($("conv").value),g=num($("gozadas").value);
 ["r-tot","r-ind","r-pre","r-sac","r-vac"].forEach(i=>$(i).textContent="–");
 if(!$("ingreso").value||!$("egreso").value||!s){est.className="estado";est.textContent="Completá fechas y sueldo.";return}
 const ing=new Date($("ingreso").value+"T00:00:00"),egr=new Date($("egreso").value+"T00:00:00");
 if(egr<ing){est.className="estado mal";est.textContent="La fecha de egreso es anterior al ingreso.";return}
 const prueba=mas(ing,6)>egr,afuera=des&&!prueba;
 let y=egr.getFullYear()-ing.getFullYear();if(mas(ing,12*y)>egr)y--;
 const anios=afuera?Math.max(1,y+(mas(ing,12*y+3)<egr?1:0)):0;
 const base=cv?Math.max(Math.min(s,3*cv),0.67*s):s,ind=anios*base;
 const pre=afuera?(egr>mas(ing,60)?2:1)*s:0;
 const fin=new Date(egr.getFullYear(),egr.getMonth()+1,0),integ=afuera?s/30*(fin.getDate()-egr.getDate()):0;
 const sacPre=(pre+integ)/12;
 const m1=egr.getMonth()<6,i0=new Date(egr.getFullYear(),m1?0:6,1),f0=new Date(egr.getFullYear(),m1?6:12,0);
 const dias=Math.round((egr-(ing>i0?ing:i0))/864e5)+1,sac=s/2*dias/(Math.round((f0-i0)/864e5)+1);
 const corte=new Date(egr.getFullYear(),11,31),da=corte<=mas(ing,60)?14:corte<=mas(ing,120)?21:corte<=mas(ing,240)?28:35;
 const trab=Math.round((egr-(ing>new Date(egr.getFullYear(),0,1)?ing:new Date(egr.getFullYear(),0,1)))/864e5)+1;
 const dv=Math.max(0,da*trab/365-g),vac=dv*s/25,sacVac=vac/12;
 const mes=Math.min(s,s/30*egr.getDate());
 const tot=ind+pre+integ+sacPre+sac+vac+sacVac+mes;
 $("r-tot").textContent=f(tot);$("r-ind").textContent=f(ind);$("r-pre").textContent=f(pre+integ+sacPre);$("r-sac").textContent=f(sac);$("r-vac").textContent=f(vac+sacVac);
 est.className="estado bien";
 est.textContent=!des?"Renuncia: sin indemnización ni preaviso. Incluye "+f(mes)+" por los días trabajados del mes, si no los cobraste."
  :prueba?"Dentro del período de prueba (6 meses): sin indemnización ni preaviso. Incluye "+f(mes)+" por los días del mes."
  :"Antigüedad: "+y+(y===1?" año":" años")+", "+anios+" a indemnizar. Incluye "+f(mes)+" por los días trabajados del mes, si no los cobraste. Importe bruto, sin descuentos."}
$("sueldo").addEventListener("input",e=>{const x=e.target.value.replace(/[^0-9]/g,"");e.target.value=x?Number(x).toLocaleString("es-AR"):"";calc()});
$("conv").addEventListener("input",e=>{const x=e.target.value.replace(/[^0-9]/g,"");e.target.value=x?Number(x).toLocaleString("es-AR"):"";calc()});
["tipo","ingreso","egreso"].forEach(id=>$(id).addEventListener("change",calc));$("gozadas").addEventListener("input",calc);calc();
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
    ARTS.update(__import__("seo_extra").ARTS_EXTRA)
    gan = __import__("gan_page"); ARTS.update(gan.ARTS_GAN)
    ARTS.update(__import__("packs_arts").ARTS_PACKS)
    ARTS.update(__import__("anses_arts").ARTS_ANSES)
    ARTS.update(__import__("salud_arts").ARTS_SALUD)
    ARTS.update(__import__("ronda9_arts").ARTS_R9)
    ARTS.update(__import__("ronda10_arts").ARTS_R10)
    lg = __import__("legal_pages"); ARTS.update(lg.ARTS_LEGAL)
    au = __import__("auto_pack"); ARTS.update(au.ARTS_AUTO)
    r2 = __import__("ronda2"); r3 = __import__("ronda3")
    os.makedirs(PUB, exist_ok=True)
    w = lambda name, s: open(os.path.join(PUB, name), "w", encoding="utf-8").write(s)
    gr = __import__("guia_recibos_page")
    w("estilo.css", CSS + gr.CSS_EXTRA + lg.CSS + au.CSS + LS.CSS + r2.CSS)
    GR = gr.pages()
    GR.update({k: v for k, v in lg.PAGES.items()})
    GR.update(au.PAGES)
    GR.update(LS.PAGES)
    GR.update(r2.PAGES)
    GR.update(r3.PAGES)
    GR.update(__import__("ronda4").PAGES)
    GR.update(__import__("ronda5").PAGES)
    GR.update(__import__("ronda6").PAGES)
    GR.update(__import__("ronda7").PAGES)
    GR.update(__import__("ronda8").PAGES)
    GR.update(__import__("pedidos_page").PAGES)
    for slug, (t, d, b, sc) in GR.items():
        w(f"{slug}.html", layout(slug, t, d, b, "website", script=sc))
    w("index.html", layout("", "Calculadora de categoría de Monotributo 2026", "Calculá gratis tu categoría de Monotributo con las escalas vigentes de agosto 2026 a enero 2027: cuota, tope y margen antes de la recategorización de febrero.", HOME_BODY, "website", script=HOME_JS))
    w("precios-mercado-libre.html", layout("precios-mercado-libre", "Calculadora de precios para Mercado Libre 2026", "Calculá a cuánto publicar en Mercado Libre Clásica, Premium y venta directa para ganar el margen que querés, con comisiones, costo fijo e Ingresos Brutos.", ML_BODY, "website", script=ML_JS))
    w("aumento-alquiler.html", layout("aumento-alquiler", "Calculadora de aumento de alquiler por IPC 2026", "Calculá cuánto te aumenta el alquiler con el IPC oficial del INDEC: alquiler de hoy, todos los ajustes y la fecha del próximo, para contratos que se actualizan cada 3, 4, 6 o 12 meses.", ALQ_BODY, "website", script=ALQ_JS))
    w("aguinaldo.html", layout("aguinaldo", "Calculadora de aguinaldo diciembre 2026", "Calculá tu aguinaldo de diciembre 2026: bruto, descuentos y neto, y el proporcional si entraste en el semestre. Vence el 18 de diciembre.", AGU_BODY, "website", script=AGU_JS))
    w("calculadora-vacaciones.html", layout("calculadora-vacaciones", "Calculadora de vacaciones 2026: días que te corresponden y cuánto cobrás", "Calculá gratis cuántos días de vacaciones te corresponden según tu antigüedad, cuánto te pagan (sueldo / 25) y hasta cuándo te tienen que avisar. Ley de Contrato de Trabajo y Ley 27.802.", VAC_BODY, "website", script=VAC_JS))
    w("calculadora-liquidacion-final.html", layout("calculadora-liquidacion-final", "Calculadora de liquidación final e indemnización por despido 2026", "Calculá gratis la liquidación final: indemnización por antigüedad, preaviso, integración del mes, aguinaldo y vacaciones proporcionales. Despido sin causa o renuncia, con la Ley 27.802.", LIQ_BODY, "website", script=LIQ_JS))
    w("calculadora-ganancias-sueldo.html", layout("calculadora-ganancias-sueldo", "Calculadora de Ganancias en el sueldo 2026: retención y deducciones SIRADIG", "Calculá gratis cuánto Ganancias te retienen del sueldo en 2026 con las escalas oficiales de ARCA, y cuánto ahorrás cargando alquiler, gastos médicos, hijos y otras deducciones en el SIRADIG.", gan.GAN_BODY, "website", script=gan.GAN_JS))
    w("sueldo-empleada-domestica.html", layout("sueldo-empleada-domestica", "Sueldo de empleada doméstica noviembre y diciembre 2026", "Cuánto pagarle a tu empleada doméstica en noviembre y diciembre 2026: valor hora y mensual de cada categoría, con antigüedad y zona desfavorable. Escala oficial Resolución 6/2026.", SUE_BODY, "website", script=SUE_JS))
    for slug, (t, d, b) in ARTS.items():
        w(f"{slug}.html", layout(slug, t, d, b))
    urls = ["", "qr", "precios-mercado-libre", "aumento-alquiler", "aguinaldo", "sueldo-empleada-domestica", "calculadora-vacaciones", "calculadora-liquidacion-final", "calculadora-ganancias-sueldo"] + list(GR) + list(ARTS)
    w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{BASE}/{u}</loc><lastmod>{HOY}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    w("robots.txt", f"User-agent: *\nDisallow: /comprar\nDisallow: /gracias\nDisallow: /descargar\nDisallow: /q/\nDisallow: /qr/\nDisallow: /pedidos/\nSitemap: {BASE}/sitemap.xml\n")
    __import__("seo_boost").post(PUB, BASE, HOY)  # JSON-LD, enlaces relacionados, /guias y fuentes sin bloqueo
    __import__("movil").post(PUB)  # móvil: CSS final, tablas, inputmode y CTA fija
    print("ok", len(urls), "páginas")

if __name__ == "__main__":
    main()
