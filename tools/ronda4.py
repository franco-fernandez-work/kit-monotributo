"""Ronda 4 (HUECOS.md #10-#12): guías PDF. build_site.main() importa PAGES.
`python tools/ronda4.py` arma private/guia-exterior.pdf, guia-cobrar.pdf y guia-alquilar.pdf (necesita reportlab; correr local y commitear; NO corre en Cloudflare)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import legal_pages as LP
from ronda2 import head, lec, field, js

PAGO_G = "Pagás con Mercado Pago y lo descargás al instante en PDF. Información general: no reemplaza asesoramiento profesional."

def of_guia(idp, titulo, bajada, items, precio, nota_extra=""):
    return LP.oferta(idp, "Guía en PDF", titulo, bajada, items, precio, "Comprar la guía", PAGO_G, nota_extra)

# ===================================================================== 10. COMPRAS AL EXTERIOR
def of_ext():
    return of_guia("exterior", "Guía: Comprar afuera sin sorpresas",
        "12 páginas con el método de costo final, los topes vigentes desde julio de 2026 y qué hacer si el paquete se retiene.",
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

PAGES = {
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
