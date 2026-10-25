"""Ronda 5 (HUECOS.md #18 en adelante): guías PDF de mudanza y siguientes. build_site.main() importa PAGES.
`python tools/ronda6.py` arma private/guia-mudanza.pdf, etc. (necesita reportlab; correr local y commitear los PDF; NO corre en Cloudflare)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ronda2 import head, lec, field, js
from ronda4 import of_guia

# ===================================================================== 18. MUDANZA
def of_mud():
    return of_guia("mudanza", "Guía: Mudanza sin estafas",
        "Presupuestos comparables, inventario por caja, señales de estafa, qué hacer si algo se rompe y la lista completa de cambios de domicilio.",
        ["Flete o mudanza completa, y qué pedir por escrito en cada presupuesto", "Las señales de estafa antes de pagar y el día de la carga", "Inventario, embalaje y cronograma de 30 días", "Cambio de domicilio: DNI, ARCA, ANSES, bancos y servicios, con planillas"],
        "2.999", '<a class="nota" href="/generador-reclamo-consumidor">¿Algo salió mal con el flete? Generador de reclamo gratis</a>')

# (id, ambiente, m3 por unidad de ejemplo)
ITEMS = [("m-cama", "Cama / colchón", 1.2), ("m-placard", "Placard o ropero", 1.5), ("m-sofa", "Sillón o sofá", 1.4), ("m-mesa", "Mesa con sillas", 1.0),
         ("m-heladera", "Heladera", 0.8), ("m-lav", "Lavarropas o cocina", 0.6), ("m-tv", "TV / escritorio", 0.5)]

def _items():
    return "".join('<div class="fila2">' + field(i, n + " (cantidad)", 1 if i in ("m-cama", "m-heladera") else 0, "", "", "1") + "</div>" for i, n, _ in ITEMS)

BODY_M = (head("Gratis · Mudanza", "Calculadora de mudanza: metros cúbicos, cajas y costo estimado", "Contá tus muebles y cajas. Estimamos el volumen, cuántas cajas usar y un costo según la tarifa que te pasen. Los valores son ejemplos que podés editar.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu mudanza</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + _items()
 + '<div class="fila2">' + field("m-cajas", "Cajas medianas", 20, "", "", "1") + field("m-cap", "Capacidad del camión", 12, "", "m³") + "</div>"
 + '<div class="fila2">' + field("m-tar", "Tarifa por hora del flete", 40000, "$") + field("m-hs", "Horas estimadas", 4, "", "h") + "</div>"
 + '<div class="fila2">' + field("m-pisos", "Pisos sin ascensor (suma de los dos domicilios)", 0, "", "", "1") + field("m-xp", "Adicional por piso", 5000, "$") + "</div>"
 + '<p class="nota">Los m³ por mueble son valores promedio de ejemplo. La tarifa y el adicional son supuestos: reemplazalos por lo que te cotice cada empresa. Una caja mediana ocupa unos 0,06 m³.</p>'
 + '</div></div><div><div class="r2res" id="m-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa. Pedí siempre presupuestos por escrito.</p></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> No hay una tarifa oficial de fletes y mudanzas. Los precios varían por zona, día y empresa.</p>'
 + lec("<h2>Cómo contratar sin sorpresas</h2><ul><li><b>Pedí tres presupuestos por escrito</b> con la misma lista de muebles y cajas.</li><li><b>Distinguí flete de mudanza completa</b>: el primero es solo transporte; la segunda incluye cuadrilla, embalaje y armado.</li><li><b>Firmá un inventario</b> y sacá fotos antes de cargar.</li><li><b>No pagues todo por adelantado</b>: seña para reservar y saldo al terminar la descarga.</li></ul><p>La guía en PDF trae las señales de estafa, el inventario por ambiente, el reclamo ordenado y la lista de cambios de domicilio (DNI, ARCA, ANSES, bancos y servicios).</p>")
 + of_mud())

JS_M = js("const IT=" + json.dumps([[i, v] for i, _, v in ITEMS]) + """;
function a(){let m3=0;IT.forEach(x=>m3+=n(x[0])*x[1]);const cajas=n('m-cajas'),mc=cajas*0.06,tot=m3+mc,cap=Math.max(1,n('m-cap')),viajes=Math.max(1,Math.ceil(tot/cap));
const costo=n('m-tar')*n('m-hs')*viajes+n('m-pisos')*n('m-xp');
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>',d=v=>v.toFixed(1).replace('.',',');
let h=f('Muebles y electro',d(m3)+' m³')+f('Cajas ('+cajas+')',d(mc)+' m³')+f('<b>Volumen total</b>','<b>'+d(tot)+' m³</b>')+f('Viajes con un camión de '+cap+' m³',viajes)+f('<b>Costo estimado</b>','<b>'+ars(costo)+'</b>');
h+='<p class="nota" style="margin:0">Dejá un margen del 20% en el volumen: casi siempre hay más cosas de las que se anotaron.</p>';
$('m-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

PAGES = {}
PAGES.update({
 "mudanza-calculadora-metros-cubicos": ("Calculadora de mudanza: metros cúbicos, cajas y costo del flete", "Calculá gratis el volumen de tu mudanza, cuántas cajas necesitás y el costo estimado. Guía en PDF con señales de estafa, inventario y cambio de domicilio por $2.999.", BODY_M, JS_M),
})

# ===================================================================== archivos
def build_pdfs():
    from guias_lib import build
    import importlib
    for modulo, salida in [("g_mudanza", "guia-mudanza.pdf")]:
        try:
            g = importlib.import_module(modulo)
        except ModuleNotFoundError:
            continue
        print(salida, build(salida, g.META, g.contenido()))

if __name__ == "__main__":
    build_pdfs()
