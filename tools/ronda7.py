"""Ronda 5b (HUECOS.md #21 y #23): guía costa/ferias y página gratis Progresar. build_site.main() importa PAGES.
`python tools/ronda7.py` arma private/guia-costa.pdf (necesita reportlab; correr local y commitear el PDF; NO corre en Cloudflare)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ronda2 import head, lec, field, js
import legal_pages as LP
from ronda4 import of_guia

# ===================================================================== 21. COSTA / FERIAS
def of_costa():
    return of_guia("costa", "Guía: Vender en la costa o en ferias",
        "Papeles, precio, cobros y la cuenta del punto de equilibrio para salir a vender en la temporada de verano.",
        ["Qué pedir y en qué orden: monotributo, habilitación municipal y permisos del rubro", "Cuenta de costos fijos y variables con ejemplo en pesos", "Cobros con efectivo, transferencia y QR, y cómo anotar las ventas", "Calendario de octubre a marzo, errores frecuentes y preguntas para la municipalidad"],
        "2.999", '<a class="nota" href="/escalas-monotributo-2026">Antes de arrancar: mirá las cuotas y topes del monotributo</a> · <a class="nota" href="/qr">QR dinámico para tu puesto</a>')

BODY_C = (head("Gratis · Emprender en verano", "Calculadora de punto de equilibrio para vender en la costa o en ferias", "Cargá tu precio, tus costos y los gastos fijos de la temporada. Te decimos cuántas unidades tenés que vender para no perder y cuánto ganás si vendés lo que esperás.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu temporada</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("c-p", "Precio de venta", 12000, "$") + field("c-c", "Costo de cada producto", 5000, "$") + "</div>"
 + '<div class="fila2">' + field("c-com", "Comisión de cobro promedio", 3, "", "%") + field("c-v", "Unidades que esperás vender", 250, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("c-canon", "Permiso o canon de temporada", 200000, "$") + field("c-alo", "Alojamiento y traslado", 600000, "$") + "</div>"
 + '<div class="fila2">' + field("c-mono", "Cuota de monotributo por mes", 60000, "$") + field("c-meses", "Meses que la vas a pagar", 3, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("c-otros", "Otros gastos fijos (puesto, cartelería)", 50000, "$") + "</div>"
 + '<p class="nota">Todos los valores son ejemplos que podés editar. La cuota de monotributo la ves en la tabla de escalas del sitio; el canon y los requisitos los fija cada municipio; la comisión depende de cómo cobres.</p>'
 + '</div></div><div><div class="r2res" id="c-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa.</p></div></div>'
 + '<p class="avisolegal"><b>Información general.</b> No es asesoramiento contable ni legal. Los permisos, cupos y cánones los define cada municipalidad.</p>'
 + lec("<h2>Qué mirar antes de salir a vender</h2><ul><li><b>El permiso primero</b>: los cupos de playa y feria se asignan antes de la temporada y a veces piden residencia, constancia de ARCA y certificado de reincidencia.</li><li><b>El monotributo se paga todos los meses</b> que estés inscripto, también los sin ventas.</li><li><b>Cobrá con QR y transferencia</b>: en la playa mucha gente no lleva efectivo.</li></ul><p>La guía en PDF trae los papeles en orden, la cuenta de costos con ejemplo, los cobros, el stock, el calendario y las preguntas para llevar a la municipalidad.</p>")
 + of_costa())

JS_C = js("""function a(){const p=n('c-p'),c=n('c-c'),com=n('c-com')/100,v=n('c-v'),fijos=n('c-canon')+n('c-alo')+n('c-mono')*n('c-meses')+n('c-otros');
const mu=p-c-p*com,eq=mu>0?Math.ceil(fijos/mu):null,gan=mu*v-fijos,ing=p*v;
const f=(l,x)=>'<div class="fil"><span>'+l+'</span><span>'+x+'</span></div>';
let h=f('Margen por unidad',ars(mu))+f('Gastos fijos de la temporada',ars(fijos));
h+=eq===null?'<p class="nota" style="margin:0">Con este precio y costo no hay margen: subí el precio o bajá el costo.</p>':f('<b>Punto de equilibrio</b>','<b>'+eq+' unidades</b>')+f('Ventas necesarias en pesos',ars(eq*p));
h+=f('Ventas esperadas ('+v+' un.)',ars(ing))+f('<b>'+(gan>=0?'Ganancia':'Pérdida')+' estimada</b>','<b>'+ars(Math.abs(gan))+'</b>');
if(eq!==null)h+='<p class="nota" style="margin:0">'+(v>=eq?'Superás el equilibrio por '+(v-eq)+' unidades.':'Te faltan '+(eq-v)+' unidades para no perder.')+' Probá también con un escenario pesimista.</p>';
$('c-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

# ===================================================================== 23. PROGRESAR (solo tráfico, no se vende)
BODY_G = (head("Gratis · Becas Progresar", "Becas Progresar: requisitos, fechas y si podés anotarte", "Revisá las tres líneas de Progresar, sus requisitos según argentina.gob.ar y chequeá en un minuto si el ingreso de tu familia entra en el tope de 3 Salarios Mínimos.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>¿Entrás en el tope?</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("g-smvm", "Salario Mínimo, Vital y Móvil vigente", 350000, "$") + field("g-n", "Integrantes con ingresos", 2, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("g-i1", "Ingreso mensual del estudiante", 0, "$") + field("g-i2", "Ingresos del resto del grupo familiar", 600000, "$") + "</div>"
 + '<p class="nota">Cargá el valor del SMVM que publica el Consejo del Salario (el de ejemplo es solo orientativo). Sumá los ingresos de todos los que viven en tu hogar. Progresar calcula el ingreso de su propia manera: esto es solo un chequeo previo.</p>'
 + '</div></div><div><div class="r2res" id="g-out" aria-live="polite"></div>'
 + '<p class="nota">Chequeo orientativo. La decisión la toma el programa.</p></div></div>'
 + '<p class="avisolegal"><b>Información general, no oficial.</b> Esta página no pertenece al Ministerio de Capital Humano ni a ANSES. Inscribite solo en el sitio oficial, y desconfiá de mensajes que te pidan plata o claves.</p>'
 + lec("<h2>Las tres líneas y sus requisitos</h2><ul><li><b>Progresar Obligatorio</b> (primaria y secundaria): entre 16 y 24 años cumplidos al cierre de la convocatoria, alumno regular.</li><li><b>Progresar Superior</b> (terciario, universitario y enfermería): ingresantes de 17 a 24 años, estudiantes avanzados hasta 30 y enfermería sin límite de edad; egresado del nivel medio y sin materias adeudadas.</li><li><b>Formación Profesional</b>: de 18 a 24 años, hasta 35 si no tenés trabajo formal registrado; curso validado por el INET.</li></ul>"
      "<p><b>En todas</b>: DNI, ingresos del estudiante y su grupo familiar de hasta 3 SMVM, y esquema de vacunación completo o en curso. Los extranjeros necesitan residencia legal (2 años en Obligatorio y Formación Profesional, 5 en Superior).</p>")
 + lec("<h2>Fechas de la convocatoria 2026</h2><ul><li>Obligatorio: cerró el 4 de septiembre.</li><li>Superior y enfermería: cerró el 11 de septiembre.</li><li>Formación Profesional: abierta hasta el <b>27 de noviembre</b>.</li></ul><p>La inscripción es en el sitio oficial becasprogresar26.educacion.gob.ar. Las fechas de la próxima convocatoria (en general, en el primer semestre) las anuncia el Ministerio: revisá argentina.gob.ar/educacion/progresar. Montos, retenciones e incompatibilidades están en el Reglamento Progresar: no los verificamos acá.</p>")
 + lec("<h2>Si ya sos estudiante, ordená los gastos del año</h2><ul><li><a href=\"/presupuesto-vuelta-al-cole\">Presupuesto de vuelta al cole</a>: cuánto cuesta arrancar el año.</li><li><a href=\"/contrato-alquiler-estudiante\">Contrato de alquiler para estudiantes</a>, si te mudás a estudiar.</li><li><a href=\"/presupuesto-familiar-2027-inflacion\">Presupuesto familiar 2027 con inflación</a>.</li></ul>"))

JS_G = js("""function a(){const s=n('g-smvm'),tope=3*s,tot=n('g-i1')+n('g-i2'),f=(l,x)=>'<div class="fil"><span>'+l+'</span><span>'+x+'</span></div>';
let h=f('Tope (3 SMVM)',ars(tope))+f('Ingresos del grupo',ars(tot))+f('<b>'+(tot<=tope?'Margen disponible':'Excedente')+'</b>','<b>'+ars(Math.abs(tope-tot))+'</b>');
h+='<p class="nota" style="margin:0">'+(tot<=tope?'Por ingresos entrás en el tope. Revisá edad, regularidad y el resto de los requisitos.':'Superás el tope con estos datos. Verificá qué ingresos cuenta el programa.')+'</p>';
$('g-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

PAGES = {
 "vender-en-la-costa-feria-punto-de-equilibrio": ("Vender en la costa o en ferias: calculadora de punto de equilibrio y guía", "Calculá gratis cuántas unidades tenés que vender en temporada para no perder. Guía en PDF con papeles, precio, cobros y calendario por $2.999.", BODY_C, JS_C),
 "becas-progresar-requisitos-fechas": ("Becas Progresar 2026: requisitos, fechas y chequeo de ingresos", "Requisitos de las tres líneas de Progresar según argentina.gob.ar, fechas de la convocatoria 2026 y un chequeo del tope de 3 Salarios Mínimos.", BODY_G, JS_G),
}

def build_pdfs():
    from guias_lib import build
    import g_costa
    print("guia-costa.pdf", build("guia-costa.pdf", g_costa.META, g_costa.contenido()))

if __name__ == "__main__":
    build_pdfs()
