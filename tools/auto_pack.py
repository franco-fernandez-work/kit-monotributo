"""Compraventa de auto usado: generador gratis de boleto, página, artículo y pack Word (/comprar?p=boletoauto).
build_site.main() importa PAGES, ARTS_AUTO y CSS; `python tools/auto_pack.py` arma private/pack-boletoauto.zip (necesita python-docx; correr local y commitear)."""
import io, os, re, zipfile
import legal_pages as LP

AVISO = "Modelo orientativo. No reemplaza el asesoramiento de un escribano/a o abogado/a ni los requisitos vigentes de la DNRPA. Verificalos antes de firmar."
CAMPOS = [("vendedor", "Vendedor/a (nombre y apellido)"), ("vendedor_dni", "DNI del vendedor"), ("vendedor_dom", "Domicilio del vendedor"),
          ("comprador", "Comprador/a (nombre y apellido)"), ("comprador_dni", "DNI del comprador"), ("comprador_dom", "Domicilio del comprador"),
          ("marca_modelo", "Marca, modelo y versión"), ("anio", "Año"), ("dominio", "Dominio (patente)"), ("motor", "N.º de motor"),
          ("chasis", "N.º de chasis"), ("km", "Kilometraje"), ("precio", "Precio total ($)"), ("sena", "Seña entregada ($)"),
          ("fecha_saldo", "Fecha de pago del saldo y entrega"), ("ciudad", "Ciudad")]

PRE = "En {ciudad}, a los {hoy}, entre {vendedor}, DNI {vendedor_dni}, con domicilio en {vendedor_dom} (en adelante, EL VENDEDOR), y {comprador}, DNI {comprador_dni}, con domicilio en {comprador_dom} (en adelante, EL COMPRADOR), se celebra el presente BOLETO DE COMPRAVENTA de automotor, sujeto a las cláusulas siguientes:"
CLAUS = [
 ("Objeto", "EL VENDEDOR vende y EL COMPRADOR compra el automotor marca y modelo {marca_modelo}, año {anio}, dominio {dominio}, motor N.º {motor}, chasis N.º {chasis}, con {km} km al día de la fecha, en el estado que EL COMPRADOR declara conocer por haberlo revisado."),
 ("Precio y forma de pago", "El precio total es de $ {precio}. EL COMPRADOR entrega en este acto $ {sena} en concepto de seña y a cuenta de precio, sirviendo este boleto de recibo. El saldo se pagará el {fecha_saldo}, contra la entrega del vehículo y de la documentación. Cada pago se documentará con recibo firmado."),
 ("Titularidad y libre de gravámenes", "EL VENDEDOR declara ser titular registral del automotor y que se encuentra libre de embargos, prendas, inhibiciones y otras medidas, así como de deudas de patentes e infracciones al día de la fecha. EL COMPRADOR podrá verificarlo con un informe de dominio. Si resultara lo contrario, EL VENDEDOR responde por el saneamiento (arts. 1033 y siguientes del Código Civil y Comercial)."),
 ("Entrega y documentación", "Contra el pago del saldo, EL VENDEDOR entregará el vehículo con sus llaves, la cédula verde (o azul), el título del automotor y el Formulario 08 firmado, con las firmas certificadas en la forma que exija el Registro, y toda otra documentación necesaria para la transferencia. Los juegos de llaves y el manual de uso, si existen, forman parte de la entrega."),
 ("Transferencia", "Las partes concurrirán al Registro de la Propiedad del Automotor que corresponda, o harán el trámite por los medios que la DNRPA habilite, dentro de los 10 días corridos de la entrega, para inscribir la transferencia a nombre de EL COMPRADOR. Los gastos, sellados y aranceles de la transferencia están a cargo de {gastos_a_cargo}."),
 ("Deudas y responsabilidad", "Las deudas de patentes, multas e infracciones anteriores a la entrega son a cargo de EL VENDEDOR; las posteriores, de EL COMPRADOR. Desde la entrega, EL COMPRADOR asume el uso y la guarda del vehículo y los daños que cause. EL VENDEDOR podrá presentar la denuncia de venta ante el Registro para dejar constancia de la entrega."),
 ("Incumplimiento", "Si EL COMPRADOR no paga el saldo en la fecha pactada y tras ser intimado por medio fehaciente a hacerlo en 3 días hábiles, EL VENDEDOR podrá resolver el contrato y retener la seña. Si EL VENDEDOR no entrega el vehículo o la documentación en tiempo, EL COMPRADOR podrá resolver y exigir la devolución de la seña duplicada."),
 ("Jurisdicción", "Para toda controversia las partes se someten a los tribunales ordinarios de {ciudad}, y constituyen domicilio en los indicados al comienzo."),
]
CIERRE = "En prueba de conformidad se firman dos ejemplares de un mismo tenor y a un solo efecto, en el lugar y fecha indicados."

def boleto_txt():
    return "\n\n".join(["BOLETO DE COMPRAVENTA DE AUTOMOTOR", PRE] + [f"{i}. {t}. {x}" for i, (t, x) in enumerate(CLAUS, 1)] +
                        [CIERRE, "Firma del vendedor: ____________________\n{vendedor}, DNI {vendedor_dni}\n\nFirma del comprador: ____________________\n{comprador}, DNI {comprador_dni}"])

PASOS = [
 ("Antes de pagar", ["Pedí al vendedor el título, la cédula y el DNI, y comprobá que el titular sea quien vende (si no, que muestre poder o autorización).", "Sacá el informe de dominio en la DNRPA: muestra titular, medidas cautelares y prendas.", "Revisá que motor y chasis estampados coincidan con los del título.", "Consultá las deudas de patentes e infracciones y definí quién las paga."]),
 ("Al firmar", ["Firmá el boleto en dos ejemplares y entregá la seña con recibo.", "Si el vendedor está casado, pedí el asentimiento del cónyuge cuando el auto es ganancial (art. 470 del CCyC).", "Para pagos importantes, usá transferencia bancaria: queda el comprobante."]),
 ("Al entregar el auto", ["Pagá el saldo contra la entrega del auto, las llaves y el Formulario 08 firmado.", "Firmen el acta de entrega con el estado y el kilometraje.", "Asegurá el auto a tu nombre desde ese momento."]),
 ("Después", ["Transferí cuanto antes: pedí turno en el Registro o iniciá el trámite online en el sitio de la DNRPA y llevá el 08 y la documentación.", "El vendedor puede presentar la denuncia de venta para dejar constancia de la entrega.", "Cuando el título llegue a nombre del comprador, la operación está cerrada."]),
]

CSS = r"""
/* compraventa de auto */
.pasosauto{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;margin:18px 0}
.pasosauto div{background:var(--hoja);border:1px solid var(--linea);border-radius:4px;padding:14px 16px}
.pasosauto h3{font:600 13px var(--f-num);color:var(--celeste);margin:0 0 6px;text-transform:uppercase;letter-spacing:.04em}
.pasosauto ul{margin:0;padding-left:18px;font-size:14px}.pasosauto li{margin:5px 0}
"""

def oferta_auto():
    return LP.oferta("boletoauto", "Pack en Word (.docx)", "Pack de compraventa de auto usado: boleto, recibos y checklists",
        "Todo para cerrar la operación con papeles ordenados, en Word editable.",
        ["Boleto de compraventa completo, con cláusulas de gravámenes y deudas", "Recibo de seña, recibo de saldo y acta de entrega con el estado del auto", "Checklist de inspección del vehículo y de documentación (Formulario 08, informe de dominio)", "Modelo de intimación por falta de transferencia o de pago, y guía de pasos"],
        "3.999", "Comprar el pack", "Pagás con Mercado Pago y lo descargás al instante. Modelos orientativos: no reemplazan asesoramiento legal.")

AV = f'<p class="avisolegal"><b>Modelo orientativo.</b> {AVISO}</p>'
pasos_html = '<div class="pasosauto">' + "".join("<div><h3>%s</h3><ul>%s</ul></div>" % (t, "".join("<li>%s</li>" % i for i in l)) for t, l in PASOS) + "</div>"
MODELOS = [dict(titulo="Recibo de seña", cuando="Constancia de cada pago a cuenta."), dict(titulo="Recibo de saldo y acta de entrega", cuando="Estado del auto, kilometraje, llaves y documentos entregados."),
           dict(titulo="Checklist de inspección", cuando="Qué revisar en el auto antes de comprar."), dict(titulo="Checklist de documentación", cuando="Vendedor y comprador, paso por paso."),
           dict(titulo="Intimación", cuando="Si la otra parte no cumple con el 08 o con el pago."), dict(titulo="Guía de pasos ante el Registro", cuando="Informe de dominio, 08 y denuncia de venta.")]

BODY = f"""<span class="etiqueta">Generador gratis · Compraventa de automotor</span>
<h1>Boleto de compraventa de auto usado: armalo gratis</h1>
<p class="bajada">Completá los datos de las partes y del auto y copiá el boleto listo para imprimir y firmar. Sin registro y sin salir de tu navegador.</p>
<div class="gen" style="margin-top:28px">
<div class="comp"><div class="comp-cab"><span>Datos del boleto</span><span>Gratis</span></div><div class="comp-cuerpo">
{LP.campos_html(CAMPOS, "ba")}
<div class="campo"><label for="ba-gastos_a_cargo">Gastos de la transferencia</label><select id="ba-gastos_a_cargo"><option value="EL COMPRADOR">A cargo del comprador</option><option value="ambas partes por mitades">Mitad cada uno</option><option value="EL VENDEDOR">A cargo del vendedor</option></select></div>
</div></div>
<div><div class="hoja-carta" id="ba-out" aria-live="polite"></div>
<div class="copiar"><button type="button" class="boton" id="ba-copiar">Copiar boleto</button><span class="cuenta" id="ba-est"></span></div></div></div>
{AV}
<div class="lectura"><h2>Paso a paso para comprar o vender un auto usado</h2><p>El boleto no transfiere el auto: la titularidad cambia recién cuando se inscribe en el Registro de la Propiedad del Automotor con el Formulario 08. Ordená la operación así:</p></div>
{pasos_html}
<div class="lectura"><h2>Qué es el Formulario 08</h2><p>Es la solicitud de transferencia que firman vendedor y comprador. El trámite se inicia en el sitio de la DNRPA y se completa en el Registro; las firmas deben certificarse en la forma que el Registro exija. Aranceles y requisitos cambian: confirmalos en <a href="https://www.argentina.gob.ar/justicia/registro-automotor" rel="noopener">argentina.gob.ar</a> antes de ir.</p></div>
<h2>Qué suma el pack</h2><p>El boleto de la web alcanza para cerrar la operación. El pack suma los papeles que la rodean, en Word editable:</p>
{LP.modelos_html(MODELOS)}
{oferta_auto()}"""

JS = LP.js_gen("ba", {"b": boleto_txt()}, extra=r"""
const g=$('ba-gastos_a_cargo');
function draw(){let t=T.b.replace('{hoy}',hoy()).replace('{gastos_a_cargo}',g.value);
 t=t.replace(/\{(\w+)\}/g,(m,k)=>val(k)||'['+k.replace(/_/g,' ')+']');$('ba-out').textContent=t}
document.querySelectorAll('.gen input').forEach(e=>e.addEventListener('input',draw));g.addEventListener('change',draw);
$('ba-copiar').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('ba-out').textContent);$('ba-est').textContent='Copiado. Pegalo en Word e imprimilo en dos ejemplares.'}catch(e){const r=document.createRange();r.selectNodeContents($('ba-out'));getSelection().removeAllRanges();getSelection().addRange(r);$('ba-est').textContent='Seleccionado: copialo con Ctrl+C.'}});
draw();""")

PAGES = {"boleto-compraventa-auto-usado": ("Boleto de compraventa de auto usado: modelo gratis y Formulario 08", "Generador gratis de boleto de compraventa de auto usado y guía de pasos con el Formulario 08 y el informe de dominio (DNRPA). Pack con recibos y checklists por $3.999.", BODY, JS)}

A1 = ('<span class="etiqueta">Autos usados · DNRPA</span><h1>Comprar un auto usado: qué papeles pedir y qué firmar</h1>'
 '<p class="bajada">Antes de pagar, revisá quién figura como titular y si el auto tiene deudas o medidas. Después, firmá un boleto y transferí el auto lo antes posible.</p>'
 '<div class="lectura"><h2>Antes de pagar</h2><ul><li><b>Informe de dominio:</b> se pide en la DNRPA y muestra titular, prendas, embargos e inhibiciones.</li><li><b>Título y cédula:</b> deben coincidir con el DNI de quien vende. Si no es el titular, exigí poder o autorización.</li><li><b>Motor y chasis:</b> comprobá que los números estampados coincidan con el título.</li><li><b>Deudas:</b> consultá patentes e infracciones y fijá en el boleto quién las paga.</li></ul>'
 '<h2>El boleto y el Formulario 08</h2><p>El boleto fija precio, forma de pago, estado del auto y quién paga qué, pero no cambia la titularidad. Eso lo hace la inscripción en el Registro con el Formulario 08 firmado por ambas partes. Armá un boleto gratis con el <a href="/boleto-compraventa-auto-usado">generador</a>.</p>'
 '<h2>Después de entregar</h2><ul><li>El comprador debe transferir cuanto antes: mientras no lo haga, el titular registral sigue siendo el vendedor.</li><li>El vendedor puede presentar la denuncia de venta para dejar constancia de la entrega.</li><li>Los aranceles y requisitos del trámite cambian: verificalos en el sitio de la DNRPA.</li></ul></div>' + AV + oferta_auto())
ARTS_AUTO = {"comprar-auto-usado-papeles-formulario-08": ("Comprar un auto usado: papeles que pedir, boleto y Formulario 08", "Qué pedir y qué firmar al comprar o vender un auto usado en Argentina: informe de dominio, boleto, Formulario 08 y denuncia de venta.", A1)}

# ------------------------------------------------------------------ pack Word
def _x(s):
    return re.sub(r"\{(\w+)\}", lambda m: "[[" + m.group(1).replace("_", " ") + "]]", s)

def build():
    from packs_lib import Doc
    P = "Pack Compraventa de Auto Usado"
    B = lambda t, s: Doc(P, t, s)
    docs = []
    d = B("Guía y contenido del pack", "Cómo usar los modelos")
    d.box("Importante", [AVISO, "Pensado para una venta entre particulares. Completá los campos resaltados en amarillo y borrá lo que no aplique."])
    d.h("Qué incluye")
    d.bullets(["01. Boleto de compraventa", "02. Recibo de seña", "03. Recibo de saldo y acta de entrega", "04. Checklist de inspección del vehículo", "05. Checklist de documentación", "06. Intimación por falta de transferencia o de pago"])
    for t, l in PASOS:
        d.h(t); d.bullets(l)
    d.h("Ante el Registro")
    d.bullets(["Verificá en el sitio de la DNRPA los requisitos, aranceles y la forma de certificar las firmas del Formulario 08 vigentes al momento del trámite.", "La denuncia de venta y el informe de dominio se piden en el Registro o por los medios que la DNRPA habilite."])
    docs.append(("00-LEEME-Guia-del-pack.docx", d))
    d = B("Boleto de compraventa de automotor", "Entre particulares")
    d.box("Antes de firmar", ["Imprimilo en dos ejemplares.", AVISO])
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p(_x(PRE.replace("{hoy}", "{fecha}")))
    d.clauses([(t, _x(x)) for t, x in CLAUS]); d.p(CIERRE); d.firmas(["Vendedor/a", "Comprador/a"])
    docs.append(("01-Boleto-de-compraventa.docx", d))
    d = B("Recibo de seña", "Pago a cuenta del precio")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Recibí de [[comprador]], DNI [[dni]], la suma de $ [[monto]] ([[monto en letras]]) en concepto de seña y a cuenta del precio de $ [[precio total]] por el automotor [[marca y modelo]], dominio [[dominio]], conforme al boleto de compraventa de fecha [[fecha del boleto]]. Forma de pago: [[efectivo / transferencia, con N.º de operación]]. Saldo pendiente: $ [[saldo]], a pagar el [[fecha]].")
    d.firmas(["Vendedor/a (quien recibe)"])
    docs.append(("02-Recibo-de-sena.docx", d))
    d = B("Recibo de saldo y acta de entrega", "Cierre de la operación")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Recibí de [[comprador]], DNI [[dni]], la suma de $ [[monto]] en concepto de pago del saldo del precio del automotor [[marca y modelo]], dominio [[dominio]]. Con este pago el precio queda totalmente cancelado.")
    d.h("Acta de entrega")
    d.table(["Concepto", "Estado"], [["Kilometraje", "[[km]]"], ["Estado general y carrocería", "[[detalle]]"], ["Neumáticos y rueda de auxilio", "[[detalle]]"], ["Llaves entregadas", "[[cantidad]]"], ["Cédula verde / azul", "[[sí / no]]"], ["Título del automotor", "[[sí / no]]"], ["Formulario 08 firmado", "[[sí / no]]"], ["Otros (manual, GNC, accesorios)", "[[detalle]]"]], [7, 8])
    d.p("EL COMPRADOR recibe el vehículo de conformidad, en el estado indicado. Desde este momento asume su uso y guarda.")
    d.firmas(["Vendedor/a", "Comprador/a"])
    docs.append(("03-Recibo-de-saldo-y-acta-de-entrega.docx", d))
    d = B("Checklist de inspección del vehículo", "Qué revisar antes de comprar")
    d.table(["Revisión", "OK / Observación"], [[x, "[[ ]]"] for x in ["Motor y chasis estampados coinciden con el título", "Sin pérdidas de aceite o refrigerante", "Arranque en frío y humo del escape", "Kilometraje coherente con el desgaste de pedales y volante", "Carrocería: golpes, repintados, diferencias de color", "Neumáticos: desgaste parejo y fecha de fabricación", "Luces, balizas, limpiaparabrisas, aire y levantavidrios", "Frenos y dirección en prueba de manejo", "Ruidos de suspensión en baches", "Interior: tapizados, olor a humedad, testigos del tablero", "Documentación del auto y service al día", "Revisión técnica obligatoria vigente, si corresponde"]], [10, 5])
    d.p("Si podés, llevá a un mecánico de confianza: una revisión previa cuesta mucho menos que una reparación.")
    docs.append(("04-Checklist-de-inspeccion.docx", d))
    d = B("Checklist de documentación", "Vendedor y comprador")
    d.h("Vendedor")
    d.bullets(["[[ ]] Título del automotor y cédula verde", "[[ ]] DNI y, si corresponde, asentimiento del cónyuge", "[[ ]] Formulario 08 firmado, con firmas certificadas", "[[ ]] Comprobantes de patentes e infracciones", "[[ ]] Denuncia de venta (después de entregar)"])
    d.h("Comprador")
    d.bullets(["[[ ]] DNI y CUIL/CUIT", "[[ ]] Informe de dominio pedido y revisado", "[[ ]] Seguro contratado desde la entrega", "[[ ]] Trámite de transferencia iniciado", "[[ ]] Dinero para sellados y aranceles de la transferencia"])
    docs.append(("05-Checklist-de-documentacion.docx", d))
    d = B("Intimación por falta de transferencia o de pago", "Carta documento o medio con constancia")
    d.box("Antes de enviar", ["Enviala por carta documento o medio fehaciente y guardá la constancia.", "Respetá el plazo de tu boleto antes de resolver el contrato.", AVISO])
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Señor/a [[nombre de la otra parte]]\nDomicilio: [[domicilio]]\nRef.: boleto de compraventa del automotor dominio [[dominio]]", False)
    d.p("Por la presente intimo a Ud. a que, dentro de [[3]] días hábiles de recibida esta comunicación, [[entregue el Formulario 08 firmado y la documentación del automotor / abone el saldo de $ monto pendiente / concurra al Registro a inscribir la transferencia]], conforme a lo pactado en el boleto de fecha [[fecha del boleto]].")
    d.p("Caso contrario, quedará resuelto el contrato conforme a la cláusula de incumplimiento, sin perjuicio de reclamar los daños y perjuicios que correspondan. Saludo a Ud. atentamente.")
    d.firmas(["Firma"])
    docs.append(("06-Intimacion.docx", d))
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private", "pack-boletoauto.zip")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for fn, doc in docs:
            buf = io.BytesIO(); doc.d.save(buf); z.writestr(fn, buf.getvalue())
    print("ok", len(docs))

if __name__ == "__main__":
    build()
