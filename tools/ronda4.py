"""Ronda 4 (HUECOS.md #10-#12): guías PDF. build_site.main() importa PAGES.
`python tools/ronda4.py` arma private/guia-exterior.pdf, guia-cobrar.pdf y guia-alquilar.pdf (necesita reportlab; correr local y commitear; NO corre en Cloudflare)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import legal_pages as LP
from ronda2 import head, lec, field, js

PAGO_G = "Pagás con Mercado Pago y lo descargás al instante en PDF. Información general: no reemplaza asesoramiento profesional."

def of_guia(idp, titulo, bajada, items, precio, nota_extra=""):
    return LP.oferta(idp, "Guía en PDF", titulo, bajada, items, precio, "Comprar la guía", PAGO_G, nota_extra)

# ===================================================================== 10. COMPRAS AL EXTERIOR
def of_ext():
    return of_guia("exterior", "Guía: Comprar afuera sin sorpresas",
        "13 páginas con el método de costo final, los topes vigentes desde julio de 2026 y qué hacer si el paquete se retiene.",
        ["Topes del courier: USD 3.000, 50 kg, 3 unidades y 5 envíos al año", "Franquicia de USD 400, IVA, derechos y tasa con ejemplos en pesos", "Cómo ver tu cupo en ARCA y qué hacer si el envío queda retenido", "Estafas de \"paquete retenido\", productos delicados y plan para el Black Friday"],
        "2.999", '<a class="nota" href="/generador-reclamo-consumidor">¿Algo salió mal con una compra? Generador de reclamo gratis</a>')

BODY_X = (head("Gratis · Compras al exterior", "Calculadora de compras al exterior: ¿cuánto sale de verdad?", "Cargá el precio en dólares, el envío y tu cotización. Estimamos IVA y, si pasás la franquicia de USD 400, derechos y tasa. Los porcentajes los editás vos.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu compra</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("x-p", "Precio sin envío (FOB)", 120, "USD") + field("x-e", "Envío", 20, "USD") + "</div>"
 + '<div class="fila2">' + field("x-d", "Dólar que vas a usar", 1500, "$") + field("x-n", "Envíos que ya usaste este año", 0, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("x-iva", "IVA", 21, "", "%") + field("x-fr", "Franquicia", 400, "USD") + "</div>"
 + '<div class="fila2">' + field("x-der", "Derecho de importación", 20, "", "%") + field("x-te", "Tasa de estadística", 3, "", "%") + "</div>"
 + '<p class="nota">El IVA general es 21%. El derecho de importación depende del producto: reemplazá el valor de ejemplo por el que te informe el courier. La tasa de estadística también es un porcentaje que conviene confirmar.</p>'
 + '</div></div><div><div class="r2res" id="x-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa. El courier te informa el importe exacto antes de entregar.</p></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> No es una liquidación aduanera. Los porcentajes son editables y no son oficiales para tu producto. Confirmalos en arca.gob.ar y con tu courier.</p>'
 + lec("<h2>Las reglas de julio de 2026, en breve</h2><ul><li><b>Por envío</b>: hasta USD 3.000 de valor, 50 kg y 3 unidades iguales (RG ARCA 5883/2026).</li><li><b>Por año</b>: hasta 5 envíos por persona en este régimen.</li><li><b>Franquicia</b>: según ARCA, USD 400 por envío, hasta 5 veces por año; adentro se paga IVA, afuera se suman derechos y tasa.</li><li><b>Sin trámites</b>: no se presenta ningún formulario; el courier gestiona a tu nombre. ARCA no reclama pagos por mail, llamada ni redes.</li></ul>"
      "<p>Cuando salgan nuevas normas actualizamos esta página. Mientras tanto, el cupo y los envíos se ven en ARCA, módulo \"Envíos Postales Internacionales\", con Clave Fiscal nivel 2.</p>")
 + lec("<h2>Cómo usarla</h2><ol><li>Cargá el precio sin envío y el envío por separado: la franquicia mira el valor de la mercadería.</li><li>Si ya hiciste 5 envíos este año, la calculadora te avisa que paga todo.</li><li>Comparalo con el precio local antes de pagar.</li></ol>")
 + of_ext())

JS_X = js("""function a(){const p=n('x-p'),e=n('x-e'),d=n('x-d'),fr=n('x-fr'),iva=n('x-iva')/100,der=n('x-der')/100,te=n('x-te')/100,u=n('x-n');
const cupo=u<5,ex=cupo?Math.max(0,p-fr):p,aduana=p+e,vIva=aduana*iva,vDer=ex*der,vTe=ex*te,tot=vIva+vDer+vTe;
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>',u2=v=>'USD '+v.toLocaleString('es-AR',{minimumFractionDigits:2,maximumFractionDigits:2});
let h=f('Valor + envío (base del IVA)',u2(aduana))+f('IVA',u2(vIva))+f('Derechos (sobre USD '+Math.round(ex)+')',u2(vDer))+f('Tasa de estadística',u2(vTe))
+f('<b>Impuestos a pagar al courier</b>','<b>'+u2(tot)+'</b>')+f('En pesos',ars(tot*d))+f('<b>Costo total en pesos</b>','<b>'+ars((p+e+tot)*d)+'</b>');
if(!cupo)h+='<p class="nota" style="margin:0"><b>Ya usaste los 5 envíos del año:</b> se pagan todos los impuestos, sin franquicia.</p>';
if(p>3000)h+='<p class="nota" style="margin:0"><b>Pasa los USD 3.000 por envío:</b> excede el régimen de pequeños envíos.</p>';
$('x-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

# ===================================================================== 11. COBRAR DEL EXTERIOR
def of_cob():
    return of_guia("cobrar", "Guía: Cobrar del exterior siendo freelancer",
        "12 páginas: Factura E paso a paso, cómo suma al monotributo, cómo comparar vías de cobro y la regla del BCRA para los dólares.",
        ["Factura E y punto de venta de exportación, con el orden de los pasos", "Cuánto te sube de categoría lo que cobrás en dólares", "La regla del BCRA (Com. A 8481) para personas humanas y cómo dejar los dólares en tu cuenta", "Checklist de contrato, errores caros y lista previa a la primera factura"],
        "4.999", '<a class="nota" href="/contratos-freelancers-monotributo">¿Necesitás contrato? Pack de contratos para freelancers</a>')

def _cats_json():
    from build_site import CATS
    return json.dumps([[c[0], c[1], c[2]] for c in CATS])

BODY_C = (head("Gratis · Freelancers", "Cobrás en dólares: ¿a qué categoría de monotributo te lleva?", "Cargá cuánto facturás por mes en dólares, el dólar que usás y la comisión de tu vía de cobro. Te mostramos el ingreso anual en pesos, tu categoría de servicios y cuánto te llega neto.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tus cobros</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("c-u", "Facturás por mes", 1500, "USD") + field("c-d", "Dólar de referencia", 1450, "$") + "</div>"
 + '<div class="fila2">' + field("c-c", "Comisión total de tu vía", 3, "", "%") + field("c-m", "Meses que cobrás al año", 12, "", "", "1") + "</div>"
 + '<p class="nota">Usá el dólar al que vas a convertir las facturas (ARCA usa el tipo de cambio comprador del Banco Nación del día anterior si facturás en pesos). La comisión de ejemplo es un supuesto: reemplazala por la de tu servicio.</p>'
 + '</div></div><div><div class="r2res" id="c-out" aria-live="polite"></div>'
 + '<p class="nota">Cálculo orientativo con las escalas de servicios de agosto 2026 a enero 2027.</p></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> Usa un dólar único para todo el año; en la realidad cada factura va a su fecha. No reemplaza a un contador.</p>'
 + lec("<h2>Lo básico de cobrar del exterior</h2><ul><li><b>Facturás con Factura E</b> (no con la C) usando un punto de venta de exportación distinto al local. Lo explica ARCA en su página de exportación de servicios.</li><li><b>Los ingresos suman a tu monotributo</b>: ARCA permite exportar servicios sin superar el límite de la categoría máxima.</li><li><b>Los dólares</b>: el BCRA pide ingresarlos y liquidarlos en 20 días hábiles, salvo que una persona humana los reciba en una cuenta en moneda extranjera a su nombre en un banco local (Com. A 8481, vigente desde el 15/09/2026).</li></ul><p>La guía en PDF ordena todo en pasos y lo ilustra con ejemplos.</p>")
 + of_cob())

JS_C = js("const C=" + _cats_json() + """;
function a(){const u=n('c-u'),d=n('c-d'),c=n('c-c')/100,m=Math.min(12,Math.max(1,n('c-m')||12));const anual=u*m*d;let cat=null;for(const x of C){if(anual<=x[1]){cat=x;break}}
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
let h=f('Facturación anual (pesos)',ars(anual))+f('Categoría de servicios',cat?cat[0]:'Fuera de la K')+f('Cuota mensual',cat?ars(cat[2]):'—')+f('Cuota sobre lo que facturás',cat?(cat[2]*12/anual*100).toFixed(1).replace('.',',')+' %':'—')+f('Margen hasta el tope',cat?ars(cat[1]-anual):'—')+f('<b>Te llega por mes (USD)</b>','<b>USD '+(u*(1-c)).toLocaleString('es-AR',{maximumFractionDigits:0})+'</b>');
if(!cat)h+='<p class="nota" style="margin:0"><b>Pasás el tope de la K:</b> saldrías del monotributo. Consultá a un contador.</p>';
else if(anual>cat[1]*.9)h+='<p class="nota" style="margin:0"><b>Estás muy cerca del tope:</b> un dólar más alto puede subirte de categoría.</p>';
$('c-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

# ===================================================================== 12. ALQUILAR SIN INMOBILIARIA
def of_alq():
    return of_guia("alquilar", "Guía: Alquilar sin inmobiliaria",
        "11 páginas para propietarios e inquilinos: reglas vigentes tras el DNU 70/2023, cláusulas, garantías, ajuste, salida anticipada y modelos en anexo.",
        ["Qué rige hoy: plazo, moneda y ajuste libres, y la salida con el 10% del saldo", "Tabla de cláusulas que no pueden faltar y errores típicos de cada una", "Garantías, depósito y cómo elegir un índice de ajuste", "Checklists de verificación y de entrega, y modelos de recibo, acta e inventario y aviso de ajuste"],
        "3.999", '<a class="nota" href="/contratos-alquiler-modelo-word">¿Querés el contrato listo? Pack de contratos de alquiler en Word</a>')

CHK_A = ["Pedí el DNI del propietario y un comprobante de que es titular o está autorizado a alquilar.",
         "Verifiqué que no haya deudas de expensas, impuestos o servicios que me lleguen.",
         "Visité la propiedad y saqué fotos fechadas de cada ambiente.",
         "El plazo, el precio, la moneda y el día de pago están escritos.",
         "El ajuste está definido con índice, frecuencia y fecha de aplicación.",
         "El depósito y la garantía figuran por escrito, con la condición de devolución.",
         "Quedó claro quién paga expensas, servicios y arreglos.",
         "Hay un inventario del estado del inmueble firmado por las dos partes.",
         "Sé cómo puedo salir antes y cuánto cuesta (10% del saldo del alquiler).",
         "Firmamos todas las hojas, en dos ejemplares, y guardamos los recibos."]

BODY_A = (head("Gratis · Alquilar directo", "Alquilar sin inmobiliaria: checklist y costo de entrada", "Tildá lo que ya tenés resuelto antes de firmar y calculá cuánto se paga al ingresar y cuánto costaría salir antes del contrato.")
 + '<div class="r2dos"><div><h2 style="margin-top:0">Checklist antes de firmar</h2><ul class="r2chk" id="al-chk">' + "".join(f'<li><label><input type="checkbox"> <span>{c}</span></label></li>' for c in CHK_A)
 + '</ul><div class="r2bar"><i id="al-bar"></i></div><p class="nota" id="al-sc"></p></div>'
 + '<div class="comp"><div class="comp-cab"><span>Costo de entrada y de salida</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("al-a", "Alquiler mensual", 600000, "$") + field("al-d", "Meses de depósito", 1, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("al-s", "Sellado / gastos de ingreso", 0, "$") + field("al-p", "Meses de contrato", 24, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("al-t", "Meses ya cumplidos", 6, "", "", "1") + "</div>"
 + '<div class="r2res" id="al-out" aria-live="polite" style="margin-top:14px"></div>'
 + '<p class="nota">El depósito de un mes es un ejemplo habitual, no una obligación. La salida anticipada se calcula como el 10% del saldo del alquiler hasta el fin del contrato (art. 1221 del Código Civil y Comercial, texto del DNU 70/2023).</p></div></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> Información general: no reemplaza a un abogado o escribano. Cada provincia puede cobrar sellados distintos.</p>'
 + lec("<h2>Lo que cambió para alquilar directo</h2><ul><li><b>El DNU 70/2023 derogó la Ley 27.551</b> (art. 249) para contratos nuevos.</li><li><b>Plazo, moneda y ajuste</b> los pactan las partes. Si no se fija plazo para una vivienda permanente, se aplican 2 años.</li><li><b>El inquilino puede salir antes</b> pagando el 10% del saldo del alquiler por el plazo que falta.</li></ul><p>Lo que no esté escrito lo decide el Código Civil y Comercial: por eso conviene un contrato completo. La guía en PDF te lleva cláusula por cláusula.</p>")
 + of_alq())

JS_A = js("""const ch=[...document.querySelectorAll('#al-chk input')];
function c(){const k=ch.filter(x=>x.checked).length;$('al-bar').style.width=(k/ch.length*100)+'%';$('al-sc').textContent=k+' de '+ch.length+' resueltos'+(k===ch.length?': listo para firmar.':'. Lo que falta, resolvelo antes de entregar dinero.')}
function a(){const al=n('al-a'),dep=al*n('al-d'),ing=al+dep+n('al-s'),pl=Math.max(1,n('al-p')),t=Math.min(pl,n('al-t')),rest=Math.max(0,pl-t),saldo=al*rest,sal=saldo*.1;
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
$('al-out').innerHTML=f('Primer mes',ars(al))+f('Depósito',ars(dep))+f('Sellado y gastos',ars(n('al-s')))+f('<b>Para ingresar</b>','<b>'+ars(ing)+'</b>')+f('Saldo del alquiler hasta el fin ('+rest+' meses)',ars(saldo))+f('<b>Salir hoy cuesta (10%)</b>','<b>'+ars(sal)+'</b>')}
ch.forEach(x=>x.addEventListener('change',c));document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));c();a();""")

PAGES = {
 "cobrar-del-exterior-freelancer": ("Cobrar del exterior como freelancer: categoría de monotributo y Factura E", "Calculadora gratis: cuánto te lleva a facturar en dólares como freelancer, tu categoría de monotributo y el neto. Guía PDF con Factura E y regla del BCRA por $4.999.", BODY_C, JS_C),
 "alquilar-sin-inmobiliaria": ("Alquilar sin inmobiliaria: checklist, costo de entrada y reglas 2026", "Checklist gratis y calculadora de costo de entrada y de salida anticipada para alquilar directo, con las reglas del DNU 70/2023. Guía PDF para propietarios e inquilinos por $3.999.", BODY_A, JS_A),
 "calculadora-compras-exterior": ("Calculadora de compras al exterior: franquicia USD 400, IVA y costo final", "Calculá gratis cuánto sale de verdad comprar en Temu, Shein o Amazon: IVA, derechos y tasa con la franquicia de USD 400 y los topes de julio 2026. Guía PDF por $2.999.", BODY_X, JS_X),
}

# ===================================================================== archivos
def build_pdfs():
    from guias_lib import build
    import importlib
    for modulo, salida in [("g_exterior", "guia-exterior.pdf"), ("g_cobrar", "guia-cobrar.pdf"), ("g_alquilar", "guia-alquilar.pdf")]:
        try:
            g = importlib.import_module(modulo)
        except ModuleNotFoundError:
            continue
        print(salida, build(salida, g.META, g.contenido()))

if __name__ == "__main__":
    build_pdfs()
