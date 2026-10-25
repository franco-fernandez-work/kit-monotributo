"""Ronda 5 (HUECOS.md #18 en adelante): guías PDF de mudanza y siguientes. build_site.main() importa PAGES.
`python tools/ronda6.py` arma private/guia-mudanza.pdf, etc. (necesita reportlab; correr local y commitear los PDF; NO corre en Cloudflare)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ronda2 import head, lec, field, js
import legal_pages as LP
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

# ===================================================================== 22. SE VENCE TU ALQUILER
def of_ren():
    return of_guia("renovar", "Guía: Se vence tu alquiler",
        "Qué pasa cuando vence el contrato, cómo negociar con 90 días de anticipación, la cuenta de renovar o mudarte y tres cartas listas.",
        ["Qué dice el Código sobre la continuación del contrato vencido", "Cronograma de 120 a 30 días con checklist", "Los puntos a negociar: precio, ajuste, plazo, depósito y salida", "Cartas modelo de renovación, no renovación e intimación por el depósito"],
        "2.999", '<a class="nota" href="/alquilar-sin-inmobiliaria">¿Buscás un nuevo alquiler? Guía para alquilar sin inmobiliaria</a>')

BODY_R = (head("Gratis · Alquileres", "¿Renovar el alquiler o mudarte? Hacé la cuenta", "Cargá el alquiler que te piden, el de la alternativa y los costos de mudarte. Calculamos cuánto cuesta cada camino y en cuántos meses se recupera la mudanza.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu decisión</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("r-a", "Alquiler que te piden por renovar", 450000, "$") + field("r-b", "Alquiler de la alternativa", 400000, "$") + "</div>"
 + '<div class="fila2">' + field("r-m", "Mudanza", 150000, "$") + field("r-d", "Depósito en garantía", 400000, "$") + "</div>"
 + '<div class="fila2">' + field("r-ad", "Meses adelantados", 1, "", "", "1") + field("r-c", "Comisión de inmobiliaria (si hay)", 0, "$") + "</div>"
 + '<div class="fila2">' + field("r-o", "Otros costos de entrada (servicios, trámites)", 50000, "$") + field("r-n", "Meses que pensás quedarte", 12, "", "", "1") + "</div>"
 + '<p class="nota">Todos los valores son ejemplos: reemplazalos por lo que te piden. El depósito y el mes adelantado se recuperan al final, así que se cuentan por separado. No incluye el ajuste del alquiler durante el contrato.</p>'
 + '</div></div><div><div class="r2res" id="r-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa.</p></div></div>'
 + '<p class="avisolegal"><b>Información general.</b> No es asesoramiento legal. Las condiciones de cada contrato son las que figuran por escrito.</p>'
 + lec("<h2>Qué mirar además de la cuenta</h2><ul><li><b>El ajuste</b> del nuevo contrato: un alquiler más bajo con mal ajuste puede salir más caro.</li><li><b>La carta</b>: si vence el contrato, la locación sigue en los mismos términos hasta una comunicación fehaciente (art. 1218 CCyC, según fuentes secundarias). Dejá todo por escrito.</li><li><b>El tiempo</b>: empezar a hablar 60 a 90 días antes te da margen.</li></ul><p>La guía en PDF trae el cronograma, qué negociar, cómo salir ordenado y tres cartas modelo.</p>")
 + of_ren())

JS_R = js("""function a(){const A=n('r-a'),B=n('r-b'),m=n('r-m'),d=n('r-d'),ad=n('r-ad'),c=n('r-c'),o=n('r-o'),N=Math.max(1,n('r-n'));
const unicos=m+c+o,dif=A-B,cajaIni=d+ad*B,costoRen=A*N,costoMud=B*N+unicos,eq=dif>0?Math.ceil(unicos/dif):null;
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
let h=f('Renovando, en '+N+' meses',ars(costoRen))+f('Mudándote, en '+N+' meses',ars(costoMud))+f('Costos únicos de mudarte',ars(unicos))+f('Plata que adelantás y se recupera',ars(cajaIni))+f('<b>Diferencia a favor de '+(costoRen>costoMud?'mudarte':'renovar')+'</b>','<b>'+ars(Math.abs(costoRen-costoMud))+'</b>');
if(dif<=0)h+='<p class="nota" style="margin:0">La alternativa no es más barata por mes: mudarte no se recupera.</p>';
else h+='<p class="nota" style="margin:0">Los costos únicos se recuperan en <b>'+eq+' meses</b>. '+(eq<=N?'Dentro de tu plazo, mudarte conviene.':'Más de lo que pensás quedarte: renovar sale mejor.')+'</p>';
$('r-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

PAGES.update({
 "renovar-alquiler-o-mudarse": ("Renovar el alquiler o mudarte: calculadora, cartas y guía", "Calculá gratis si conviene renovar el alquiler o mudarte, con costos de entrada y punto de equilibrio. Guía en PDF con cronograma, qué negociar y 3 cartas modelo por $2.999.", BODY_R, JS_R),
})

# ===================================================================== 20. PRESUPUESTO 2027 CON IPC
def of_pres():
    return LP.oferta("presupuesto", "Planilla (Excel / Google Sheets)", "Presupuesto Familiar 2027 con IPC",
        "Un presupuesto anual en pesos que se ajusta solo por el IPC que cargues, para ver mes a mes si tus ingresos le ganan a los precios.",
        ["10 rubros de gasto con ajuste mensual por IPC (SI/NO en cada uno)", "Gasto real contra presupuesto, mes por mes", "Ingresos con aumento mensual y ahorro acumulado contra tu meta", "Ingreso real a precios de enero: si pierde, lo ves al instante"],
        "3.999", "Comprar la planilla", "Pagás con Mercado Pago y la descargás al instante. Funciona en Excel y en Google Sheets.",
        '<a class="nota" href="/donde-poner-el-aguinaldo">¿Cobraste aguinaldo? Calculá cuánto rinde contra la inflación</a>')

BODY_P = (head("Gratis · Presupuesto 2027", "¿Cuánto te va a costar vivir en 2027? Proyectá tus gastos con la inflación", "Cargá tu gasto mensual de hoy, la inflación mensual que esperás y cuánto esperás que suban tus ingresos. Te mostramos el año completo.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu presupuesto</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("p-g", "Gasto mensual de enero", 1400000, "$") + field("p-i", "Inflación mensual esperada", 2.5, "", "%") + "</div>"
 + '<div class="fila2">' + field("p-y", "Ingreso mensual de enero", 1500000, "$") + field("p-a", "Aumento mensual de ingresos", 2, "", "%") + "</div>"
 + '<p class="nota">La inflación y los aumentos son supuestos tuyos: no son predicciones. Reemplazalos por el último IPC mensual del INDEC y por lo que esperás cobrar.</p>'
 + '</div></div><div><div class="r2res" id="p-out" aria-live="polite"></div>'
 + '<p class="nota">Proyección orientativa. Supone que todos los gastos suben con el IPC.</p></div></div>'
 + '<p class="avisolegal"><b>Información educativa.</b> No es asesoramiento financiero. Verificá el IPC en indec.gob.ar.</p>'
 + lec("<h2>Cómo leerlo</h2><ul><li><b>Gasto de diciembre</b>: cuánto cuesta mantener hoy tu nivel de vida dentro de un año.</li><li><b>Ahorro del año</b>: ingresos menos gastos. Si es negativo, estás gastando más de lo que ganás en el año.</li><li><b>Poder de compra</b>: si tu ingreso sube menos que la inflación, compra menos cada mes.</li></ul><p>La planilla trae 10 rubros, ajuste por IPC en cada uno, gasto real contra presupuesto y resumen mensual.</p>")
 + of_pres())

JS_P = js("""function a(){const g=n('p-g'),i=n('p-i')/100,y=n('p-y'),r=n('p-a')/100;let tg=0,ty=0,ahc=0,mneg=0;
for(let m=0;m<12;m++){const gm=g*Math.pow(1+i,m),ym=y*Math.pow(1+r,m);tg+=gm;ty+=ym;ahc+=ym-gm;if(!mneg&&ym<gm)mneg=m+1}
const gd=g*Math.pow(1+i,11),yd=y*Math.pow(1+r,11),ac=Math.pow(1+i,11),yreal=yd/ac;
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>',p=v=>(v*100).toFixed(1).replace('.',',')+' %';
let h=f('Gasto de diciembre',ars(gd))+f('Ingreso de diciembre',ars(yd))+f('Gasto del año',ars(tg))+f('Ingreso del año',ars(ty))+f('<b>Ahorro del año</b>','<b>'+ars(ahc)+'</b>')+f('Inflación acumulada hasta diciembre',p(ac-1))+f('Ingreso de diciembre a precios de enero',ars(yreal));
const MES=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre'];
h+=mneg?'<p class="nota" style="margin:0"><b>Desde '+MES[mneg-1]+' gastás más de lo que ganás</b> con estos supuestos.</p>':'<p class="nota" style="margin:0">Con estos supuestos, tus ingresos cubren los gastos todo el año.</p>';
$('p-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

PAGES.update({
 "presupuesto-familiar-2027-inflacion": ("Presupuesto familiar 2027 con inflación: calculadora y planilla Excel", "Proyectá gratis cuánto te va a costar vivir en 2027 con la inflación que esperás. Planilla Excel de presupuesto con ajuste por IPC por $3.999.", BODY_P, JS_P),
})

# ===================================================================== archivos
def build_pdfs():
    from guias_lib import build
    import importlib
    for modulo, salida in [("g_mudanza", "guia-mudanza.pdf"), ("g_renovar", "guia-renovar.pdf")]:
        try:
            g = importlib.import_module(modulo)
        except ModuleNotFoundError:
            continue
        print(salida, build(salida, g.META, g.contenido()))

if __name__ == "__main__":
    build_pdfs()
