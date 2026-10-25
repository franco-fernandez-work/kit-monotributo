"""Ronda 6 (HUECOS.md #25, #28 y #24): personal de temporada (pack Word), stock y ventas de Navidad (xlsx) y depósito del alquiler (guía PDF).
build_site.main() importa PAGES. `python tools/ronda8.py` arma private/pack-temporada.zip (python-docx) y private/guia-deposito.pdf (reportlab);
el xlsx con `python tools/build_stock_xlsx.py`. Solo local: commitear los archivos, NO corre en Cloudflare.
Normativa leída el 25/10/2026 en argentina.gob.ar (texto actualizado): LCT arts. 80, 90-95, 92 bis, 92 ter, 96-100, 153-156 (Ley 27.802, BO 6/3/2026); CCyC arts. 768, 886-887, 1196, 1206-1210, 1218, 1222-1223, 2560.
NO verificado: alta en ARCA (plazos RG 2988/10 y datos mínimos RG 5508/2024 solo por buscador de ARCA), RIFL (RG 5844/2026), convenios colectivos por actividad, SAC proporcional (Ley 23.041), ART, mediación prejudicial por jurisdicción."""
import io, os, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ronda2 import head, lec, field, js, quien, AVH
import legal_pages as LP
from ronda4 import of_guia

def sel(id_, label, opts):
    return (f'<div class="campo"><label for="{id_}">{label}</label><div class="entrada"><select id="{id_}">'
            + "".join(f'<option value="{v}">{t}</option>' for v, t in opts) + "</select></div></div>")

PAGO_W = "Pagás con Mercado Pago y lo descargás al instante. Modelos orientativos: no reemplazan asesoramiento legal."

# ===================================================================== 25. PERSONAL DE TEMPORADA
def of_temp():
    return LP.oferta("temporada", "Pack en Word (.docx)", "Pack Personal de Temporada",
        "Contratos, convocatoria y papeles para tomar personal en verano de manera registrada, con la ley citada en cada modelo.",
        ["Contrato de trabajo de temporada, contrato eventual y contrato a plazo fijo", "Convocatoria de la nueva temporada (30 días antes) y respuesta del trabajador", "Planilla de liquidación de cierre: SAC y vacaciones proporcionales", "Checklist de alta en ARCA y constancia de entrega de certificados"],
        "3.999", "Comprar el pack", PAGO_W, '<a class="nota" href="/calculadora-liquidacion-final">¿Cierre de la relación? Calculá la liquidación final</a>')

BODY_T = (head("Gratis · Comercios de temporada", "Personal de temporada en verano: ¿qué contrato corresponde y cuánto sale?", "Contestá tres preguntas y te decimos qué modalidad describe la ley. Después calculá el aguinaldo y las vacaciones proporcionales que se pagan al cerrar la temporada.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>¿Qué modalidad es?</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + sel("t-a", "¿La tarea se repite todos los años en la misma época?", [("1", "Sí, es parte del giro normal del negocio"), ("0", "No, es algo extraordinario")])
 + sel("t-b", "¿Es un pico o un servicio extraordinario que no se va a repetir?", [("0", "No"), ("1", "Sí")])
 + sel("t-c", "¿Sabés la fecha de fin y la podés escribir en el contrato?", [("1", "Sí, tengo fecha de inicio y de fin"), ("0", "No")])
 + '<hr style="border:0;border-top:1px dashed var(--linea);width:100%">'
 + '<div class="fila2">' + field("t-s", "Sueldo mensual bruto", 900000, "$") + field("t-d", "Días trabajados en la temporada", 90, "", "", "1") + "</div>"
 + '<p class="nota">El sueldo es un ejemplo: cargá el de tu convenio. El aguinaldo se estima proporcional al tiempo trabajado y las vacaciones según el art. 153 de la Ley de Contrato de Trabajo (un día de descanso por cada 20 trabajados), pagadas a sueldo÷25 (art. 155).</p>'
 + '</div></div><div><div class="r2res" id="t-out" aria-live="polite"></div>'
 + '<p class="nota">Orientativo. Cada convenio colectivo puede tener reglas propias.</p></div></div>'
 + AVH
 + lec("<h2>Las tres modalidades, según la Ley de Contrato de Trabajo</h2><ul><li><b>Temporada (arts. 96 a 98)</b>: la actividad es propia del giro normal de la empresa, se cumple en ciertas épocas del año y se repite en cada ciclo. Antes de cada temporada, con al menos 30 días de anticipación, el empleador notifica que quiere repetir la relación; el trabajador responde en 5 días.</li>"
      "<li><b>Eventual (art. 99)</b>: sirve para resultados concretos, servicios extraordinarios determinados de antemano o exigencias extraordinarias y transitorias. Quien la invoca tiene que probarla.</li>"
      "<li><b>Plazo fijo (arts. 90 a 95)</b>: debe constar por escrito, con la duración, y no puede superar 5 años. Si se usa para tareas permanentes o se encadenan contratos sin justificación, se convierte en indeterminado.</li></ul>"
      "<p>En todos los casos la relación se registra desde el primer día: según el art. 92 bis, si no se registra al trabajador desde el inicio, el empleador pierde el período de prueba. El pack trae los modelos de cada modalidad y la lista de pasos para el alta.</p>")
 + quien([("Si querés repetir cada año", "Lo habitual es el contrato de temporada: el trabajador adquiere derechos de permanente desde su primera temporada si la necesidad es permanente (art. 97).", False),
          ("Despido antes de que termine", "El despido sin causa mientras corre el ciclo da lugar a indemnización como en el plazo fijo (art. 97, remite al art. 95).", False),
          ("Ojo con el negro", "Contratar sin registrar suma multas, contingencia ante un accidente y pérdida de todas las ventajas. Consultá a un contador o abogado laboralista.", True)])
 + of_temp())

JS_T = js("""function a(){const rep=n('t-a'),extra=n('t-b'),f=n('t-c'),s=n('t-s'),d=n('t-d');
const mod=document.getElementById('t-a').value==='1'?'Temporada (arts. 96 a 98)':(document.getElementById('t-b').value==='1'?'Eventual (art. 99)':(document.getElementById('t-c').value==='1'?'Plazo fijo (arts. 90 a 95)':'Indeterminado (art. 90)'));
const sac=s*d/360,vd=d/20,vac=s/25*vd,tot=sac+vac;
const fl=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
let h=fl('<b>Modalidad que describe la ley</b>','<b>'+mod+'</b>')+fl('Aguinaldo proporcional',ars(sac))+fl('Días de vacaciones proporcionales',vd.toFixed(1).replace('.',','))+fl('Vacaciones proporcionales',ars(vac))+fl('<b>A pagar al cierre (sin sueldo ni cargas)</b>','<b>'+ars(tot)+'</b>');
h+='<p class="nota" style="margin:0">'+(document.getElementById('t-a').value==='1'?'Si la tarea es de todos los años, repetí el contrato de temporada y mandá la convocatoria 30 días antes.':(document.getElementById('t-b').value==='1'?'Para un pico extraordinario usá el contrato eventual y dejá escrita la causa concreta.':'Si no es repetitiva ni extraordinaria, un plazo fijo por escrito suele ser lo más claro; evitá encadenarlos.'))+'</p>';
document.getElementById('t-out').innerHTML=h}
document.querySelectorAll('.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")

# ===================================================================== 28. STOCK, COSTOS Y VENTAS (NAVIDAD)
def of_stock():
    return LP.oferta("stock", "Planilla (Excel / Google Sheets)", "Planilla de Stock, Costos y Ventas para Emprendedores",
        "Cargá cada producto y cada venta y mirá cuánto ganás de verdad, qué tenés que reponer y cuánta plata tenés parada en mercadería.",
        ["Margen por producto con comisión y envío, en pesos y en porcentaje", "Stock actual y aviso REPONER cuando llegás al mínimo", "Ganancia neta del período contra tus costos fijos y tu meta", "Producto más rentable y plata parada en stock"],
        "2.999", "Comprar la planilla", "Pagás con Mercado Pago y la descargás al instante. Funciona en Excel y en Google Sheets.",
        '<a class="nota" href="/como-calcular-precio-mercado-libre">¿Vendés en Mercado Libre? Calculá tu precio con comisiones</a>')

BODY_S = (head("Gratis · Emprendedores en Navidad", "Vender en Navidad: calculá tu precio, tu margen y cuánto stock comprar", "Cargá lo que te cuesta un producto, la comisión y el margen que querés. Te damos el precio, la ganancia por unidad y cuántas unidades comprar para la temporada.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu producto</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("s-c", "Costo del producto", 5000, "$") + field("s-env", "Envío o packaging por venta", 800, "$") + "</div>"
 + '<div class="fila2">' + field("s-com", "Comisión de cobro o plataforma", 6, "", "%") + field("s-m", "Margen deseado sobre el precio", 40, "", "%") + "</div>"
 + '<div class="fila2">' + field("s-u", "Unidades que esperás vender", 120, "", "", "1") + field("s-st", "Stock que ya tenés", 20, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("s-col", "Colchón de seguridad", 15, "", "%") + field("s-fij", "Costos fijos del período", 150000, "$") + "</div>"
 + '<p class="nota">Todos los valores son ejemplos que podés editar. El margen se calcula sobre el precio de venta. No incluye impuestos ni el costo financiero de comprar mercadería con anticipación.</p>'
 + '</div></div><div><div class="r2res" id="s-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa.</p></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> No es asesoramiento contable ni impositivo. Consultá con tu contador.</p>'
 + lec("<h2>Por qué se pierde plata en el pico</h2><ul><li><b>El margen no es la diferencia entre costo y precio</b>: hay que restar comisión, envío y packaging de cada venta.</li><li><b>Sin stock mínimo te quedás sin producto</b> justo cuando más se vende; con demasiado, la plata queda parada hasta enero.</li><li><b>Los costos fijos corren con o sin ventas</b>: hay que saber cuántas unidades cubren el puesto, internet y monotributo.</li></ul><p>La planilla lleva estas cuentas por vos, producto por producto, y avisa cuándo reponer.</p>")
 + of_stock())

JS_S = js("""function a(){const c=n('s-c'),e=n('s-env'),com=n('s-com')/100,m=n('s-m')/100,u=n('s-u'),st=n('s-st'),col=n('s-col')/100,fij=n('s-fij');
const den=1-com-m,fl=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
if(den<=0){document.getElementById('s-out').innerHTML='<p class="nota" style="margin:0">La comisión y el margen suman 100% o más: bajá alguno.</p>';return}
const p=Math.ceil((c+e)/den/10)*10,mu=p-c-e-p*com,comprar=Math.max(0,Math.ceil(u*(1+col))-st),inv=comprar*c,gan=mu*u-fij,eq=mu>0?Math.ceil(fij/mu):null;
let h=fl('<b>Precio sugerido</b>','<b>'+ars(p)+'</b>')+fl('Ganancia por unidad',ars(mu))+fl('Unidades a comprar (con colchón)',comprar)+fl('Inversión en mercadería',ars(inv))+fl('Ganancia del período',ars(gan));
h+=eq===null?'':fl('Punto de equilibrio','<b>'+eq+' unidades</b>');
h+='<p class="nota" style="margin:0">'+(gan>=0?'Con esas ventas cubrís los costos fijos.':'Con esas ventas no cubrís los costos fijos: subí el precio, bajá el costo o vendé más.')+'</p>';
document.getElementById('s-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

# ===================================================================== 24. DEPÓSITO DEL ALQUILER
def of_dep():
    return of_guia("deposito", "Guía: Recuperá tu depósito de alquiler",
        "11 páginas con el cronograma de salida, qué pueden descontar, cuánto te corresponde según tu contrato y 4 cartas listas.",
        ["Qué dice el Código hoy sobre el depósito y qué cláusulas leer en tu contrato", "Cronograma de 60 días a la entrega de llaves, con checklist de pruebas", "Qué descuentos son razonables y cómo defenderte de los que no", "Escalera de reclamo y cartas: aviso de entrega, acta, intimación y pedido de liquidación"],
        "2.999", '<a class="nota" href="/renovar-alquiler-o-mudarse">¿Se vence el contrato? Renovar o mudarte: hacé la cuenta</a>')

BODY_D = (head("Gratis · Alquileres", "Depósito del alquiler: ¿cuánto te tienen que devolver?", "Cargá lo que pagaste de depósito, los alquileres y cómo dice tu contrato que se devuelve. Calculamos el monto, los descuentos justificados y el interés por demora.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu depósito</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + sel("d-f", "Cómo dice tu contrato que se devuelve", [("n", "El mismo monto que entregué"), ("u", "Al valor del último alquiler"), ("i", "Ajustado por un índice pactado")])
 + '<div class="fila2">' + field("d-dep", "Depósito que pagaste", 400000, "$") + field("d-ai", "Alquiler cuando entraste", 400000, "$") + "</div>"
 + '<div class="fila2">' + field("d-af", "Último alquiler que pagás", 700000, "$") + field("d-ix", "Índice acumulado (solo si es por índice)", 60, "", "%") + "</div>"
 + '<div class="fila2">' + field("d-desc", "Descuentos justificados con comprobante", 0, "$") + field("d-dias", "Días de demora desde la entrega", 0, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("d-tasa", "Interés por demora (mensual)", 3, "", "%") + "</div>"
 + '<p class="nota">La forma de devolución la fija tu contrato: el Código deja libres las cantidades, la moneda y la forma (art. 1196). El interés es un supuesto editable: la tasa la acuerdan las partes, la fija una ley especial o, si no, el Banco Central (art. 768). El cálculo usa interés simple.</p>'
 + '</div></div><div><div class="r2res" id="d-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa.</p></div></div>'
 + AVH
 + lec("<h2>Lo que conviene saber antes de entregar las llaves</h2><ul><li><b>Manda tu contrato</b>: desde el DNU 70/2023, las partes pactan libremente el monto, la moneda y la forma de devolución del depósito (art. 1196 del Código Civil y Comercial).</li><li><b>Devolvés la propiedad como la recibiste</b>, salvo el desgaste por el paso del tiempo y el uso regular (art. 1210). Por eso el inventario y las fotos del inicio valen oro.</li><li><b>Dejá todo por escrito</b>: acta de entrega con fecha, libre deuda de servicios y una carta si no te devuelven en el plazo.</li></ul><p>La guía en PDF trae el cronograma de salida, la lista de descuentos que sí y no corresponden, y 4 cartas modelo.</p>")
 + of_dep())

JS_D = js("""function a(){const f=document.getElementById('d-f').value,dep=n('d-dep'),ai=Math.max(1,n('d-ai')),af=n('d-af'),ix=n('d-ix')/100,desc=n('d-desc'),dias=n('d-dias'),tasa=n('d-tasa')/100;
let base=dep;if(f==='u')base=dep/ai*af;if(f==='i')base=dep*(1+ix);
const neto=Math.max(0,base-desc),inter=neto*tasa*dias/30,tot=neto+inter,perd=Math.max(0,base-dep);
const fl=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>';
let h=fl('Depósito que pagaste',ars(dep))+fl('<b>Depósito que te corresponde</b>','<b>'+ars(base)+'</b>')+fl('Descuentos justificados','- '+ars(desc))+fl('Neto a devolver',ars(neto))+fl('Interés por la demora ('+dias+' días)',ars(inter))+fl('<b>Total a reclamar</b>','<b>'+ars(tot)+'</b>');
if(f==='n'&&af>ai)h+='<p class="nota" style="margin:0">Si tu contrato devuelve el monto nominal, la inflación se lleva parte del valor: con el último alquiler habría sido '+ars(dep/ai*af)+'. Es lo que pactaron: revisá la cláusula.</p>';
else if(f!=='n')h+='<p class="nota" style="margin:0">La actualización suma '+ars(perd)+' sobre lo que pagaste.</p>';
document.getElementById('d-out').innerHTML=h}
document.querySelectorAll('.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")

PAGES = {
 "contratar-personal-de-temporada-verano": ("Personal de temporada en verano: qué contrato usar y cuánto cuesta cerrar", "Elegí entre contrato de temporada, eventual o plazo fijo según la Ley de Contrato de Trabajo y calculá aguinaldo y vacaciones proporcionales. Pack de modelos en Word por $3.999.", BODY_T, JS_T),
 "vender-en-navidad-margen-precio-stock": ("Vender en Navidad: calculá precio, margen y stock + planilla para emprendedores", "Calculá gratis el precio de venta, la ganancia por unidad y cuánto stock comprar para la temporada. Planilla de stock, costos y ventas en Excel por $2.999.", BODY_S, JS_S),
 "recuperar-deposito-alquiler": ("Recuperar el depósito del alquiler: calculadora, cartas y guía", "Calculá cuánto te tienen que devolver del depósito según tu contrato, con descuentos e interés por demora. Guía en PDF con cronograma y 4 cartas modelo por $2.999.", BODY_D, JS_D),
}

# ===================================================================== archivos
def build_pdfs():
    from guias_lib import build
    import g_deposito
    print("guia-deposito.pdf", build("guia-deposito.pdf", g_deposito.META, g_deposito.contenido()))

def build_pack():
    from packs_lib import Doc
    priv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "private")
    AV = "Modelo orientativo. No reemplaza el asesoramiento de un abogado/a laboralista o contador/a. Verificá tu convenio colectivo y las normas vigentes antes de firmar."
    P = "Pack Personal de Temporada"
    def mk(t, s, box=None):
        d = Doc(P, t, s); d.box("Antes de usarlo", box or [AV, "Completá los campos resaltados en amarillo y borrá lo que no aplique."]); return d
    docs = []
    d = Doc(P, "Guía del pack", "Qué modalidad usar y cómo dar de alta")
    d.box("Importante", [AV, "Registrá al trabajador desde el primer día: sin registro no hay contrato válido ante ARCA ni cobertura ante un accidente."])
    d.h("Qué incluye"); d.bullets(["01. Contrato de trabajo de temporada", "02. Contrato de trabajo eventual", "03. Contrato de trabajo a plazo fijo", "04. Convocatoria de la nueva temporada", "05. Respuesta del trabajador", "06. Liquidación de cierre de temporada", "07. Checklist de alta y documentación", "08. Constancia de entrega de certificados"])
    d.h("Qué modalidad usar (Ley de Contrato de Trabajo, texto actualizado)")
    d.table(["Modalidad", "Cuándo", "Artículos"], [
        ["Temporada", "La actividad es propia del giro normal y se repite en determinadas épocas del año.", "96 a 98"],
        ["Eventual", "Resultados concretos, servicios extraordinarios determinados de antemano o exigencias extraordinarias y transitorias. El empleador prueba la causa.", "99 y 100"],
        ["Plazo fijo", "Duración expresa y por escrito, hasta 5 años. Preaviso de 1 a 2 meses antes del vencimiento.", "90 a 95"],
        ["Indeterminado", "Es la regla si no se cumplen las condiciones anteriores. Período de prueba de 6 meses (art. 92 bis).", "90 y 92 bis"]], [3, 10, 2.5])
    d.h("Reglas que importan")
    d.bullets(["Temporada: al menos 30 días antes del inicio de cada temporada, el empleador notifica que quiere repetir la relación; el trabajador responde en 5 días (art. 98). Si el empleador no notifica, se considera que rescinde el contrato.", "Temporada: el trabajador adquiere los derechos de los permanentes de prestación continua desde la primera temporada si la necesidad de la empresa es permanente (art. 97).", "Plazo fijo: si no se preavisa el fin, el contrato se convierte en indeterminado (art. 94). Los contratos sucesivos sin justificación también.", "Vacaciones: si no se llega al mínimo de días trabajados, corresponde un día de descanso por cada 20 trabajados (art. 153), pagados a sueldo÷25 si es mensual (art. 155).", "Certificados: dentro de los 45 días hábiles de terminada la relación (art. 80)."])
    d.h("Alta en ARCA (a confirmar en arca.gob.ar)")
    d.bullets(["Ingresá con Clave Fiscal al servicio Simplificación Registral y registrá el alta con el CUIL del trabajador antes del primer día de trabajo.", "Contratá la ART antes de que empiece a trabajar.", "Consultá si podés acogerte a algún régimen de promoción del empleo registrado vigente."])
    d.p("Fuentes: Ley 20.744 (texto actualizado en argentina.gob.ar, con las reformas de las leyes 24.013, 27.742 y 27.802). Los plazos del alta y los regímenes de promoción deben confirmarse en ARCA.", size=9, italic=True)
    docs.append(("00-LEEME-Guia-del-pack.docx", d))

    d = mk("Contrato de trabajo de temporada", "Modalidad de los arts. 96 a 98 de la Ley de Contrato de Trabajo")
    d.p("En [[ciudad]], a los [[fecha]], entre [[razón social o nombre del empleador]], CUIT [[número]], con domicilio en [[domicilio]] (EL EMPLEADOR), y [[nombre del trabajador]], DNI [[número]], CUIL [[número]], con domicilio en [[domicilio]] (EL/LA TRABAJADOR/A), se celebra el siguiente contrato:")
    d.clauses([
        ("Modalidad", "El contrato es de temporada: la actividad es propia del giro normal de la explotación, se cumple en determinadas épocas del año y se repite en cada ciclo (art. 96 LCT)."),
        ("Tareas", "EL/LA TRABAJADOR/A se desempeñará como [[cargo o categoría]], realizando [[descripción de tareas]], en [[lugar de trabajo]], conforme al convenio colectivo [[número y actividad]]."),
        ("Ciclo", "La temporada se extiende previsiblemente desde el [[fecha de inicio]] hasta el [[fecha de fin]]. El contrato comienza el [[fecha de inicio]]."),
        ("Jornada", "La jornada será de [[horas]] horas semanales, distribuidas de [[días]], de [[hora]] a [[hora]], con los descansos y francos que fija la ley y el convenio."),
        ("Remuneración", "La remuneración mensual bruta será de $ [[monto]], más los adicionales del convenio que correspondan, pagadera dentro de los plazos legales por [[transferencia / efectivo con recibo]]."),
        ("SAC y vacaciones", "Corresponden el sueldo anual complementario y las vacaciones proporcionales al tiempo trabajado, que se liquidarán al cierre de cada ciclo, de acuerdo con los arts. 153 y 155 de la LCT."),
        ("Registro y cargas", "EL EMPLEADOR registrará la relación laboral ante ARCA desde el primer día de trabajo, ingresará los aportes y contribuciones de la seguridad social y contratará la cobertura de riesgos del trabajo. Se entregará copia de los comprobantes que correspondan."),
        ("Convocatoria", "Con una antelación no menor a 30 días del inicio de cada temporada, EL EMPLEADOR notificará su voluntad de reiterar la relación en los términos del ciclo anterior, y EL/LA TRABAJADOR/A responderá dentro de los 5 días de notificado, por escrito o presentándose (art. 98 LCT)."),
        ("Extinción", "El despido sin causa durante el ciclo dará lugar a los resarcimientos previstos en la ley (art. 97 LCT). La falta de notificación de la nueva temporada será considerada rescisión unilateral por el empleador."),
        ("Certificados", "Al finalizar la relación, EL EMPLEADOR pondrá a disposición los certificados del art. 80 de la LCT dentro de los 45 días hábiles."),
        ("Jurisdicción", "Las partes constituyen domicilio en los indicados y se someten a la jurisdicción laboral que corresponda.")])
    d.firmas(["Empleador", "Trabajador/a"]); docs.append(("01-Contrato-de-temporada.docx", d))

    d = mk("Contrato de trabajo eventual", "Art. 99 de la Ley de Contrato de Trabajo")
    d.p("En [[ciudad]], a los [[fecha]], entre [[empleador]], CUIT [[número]], y [[trabajador/a]], DNI [[número]], CUIL [[número]], se celebra el siguiente contrato:")
    d.clauses([
        ("Causa", "El contrato es eventual porque se celebra para [[describir el servicio extraordinario, resultado concreto o exigencia transitoria: por ejemplo, la atención del evento de ___ / el inventario de ___ / el aumento transitorio de ventas por ___]], conforme al art. 99 de la LCT. EL EMPLEADOR declara que la causa existe y se compromete a acreditarla."),
        ("Duración", "La relación comienza el [[fecha]] y finalizará al concluir [[el servicio o resultado que motiva el contrato]], previsto aproximadamente para el [[fecha]]."),
        ("Tareas y lugar", "EL/LA TRABAJADOR/A realizará [[tareas]] en [[lugar]], como [[categoría]], conforme al convenio [[número]]."),
        ("Jornada y remuneración", "[[horas]] horas semanales; remuneración de $ [[monto]] por [[mes / día / hora]] con los adicionales del convenio."),
        ("Registro", "EL EMPLEADOR registrará la relación ante ARCA desde el primer día y abonará aportes, contribuciones y cobertura de riesgos del trabajo."),
        ("Liquidación final", "Al terminar, se abonarán los proporcionales de SAC y vacaciones que correspondan y se entregarán los certificados del art. 80 de la LCT.")])
    d.p("Aviso: el empleador es quien debe probar que se dan las condiciones del contrato eventual (art. 99 LCT). Si la causa no es real, se presume una relación por tiempo indeterminado.", size=9, italic=True)
    d.firmas(["Empleador", "Trabajador/a"]); docs.append(("02-Contrato-eventual.docx", d))

    d = mk("Contrato de trabajo a plazo fijo", "Arts. 90 a 95 de la Ley de Contrato de Trabajo")
    d.p("En [[ciudad]], a los [[fecha]], entre [[empleador]], CUIT [[número]], y [[trabajador/a]], DNI [[número]], CUIL [[número]], se acuerda:")
    d.clauses([
        ("Plazo", "El contrato se celebra por tiempo determinado, desde el [[fecha]] hasta el [[fecha]], por la siguiente razón: [[causa objetiva: por ejemplo, cobertura de una temporada de ___]] (art. 90, inc. a y b, LCT). No supera los cinco años (art. 93)."),
        ("Preaviso", "Las partes deberán preavisar la finalización con una antelación no menor a 1 mes ni mayor a 2 meses, salvo que el contrato dure menos de 1 mes (art. 94). Si no se preavisa, se entiende que se acepta la conversión a plazo indeterminado."),
        ("Tareas", "[[Cargo, tareas, lugar y convenio]]."),
        ("Jornada y remuneración", "[[horas]] horas semanales; remuneración mensual bruta de $ [[monto]]."),
        ("Despido sin causa", "El despido injustificado antes del vencimiento dará derecho a las indemnizaciones del art. 95 de la LCT, calculadas con la antigüedad que se habría acumulado hasta la fecha de finalización."),
        ("Registro", "EL EMPLEADOR registrará al trabajador ante ARCA desde el primer día y cumplirá con los aportes y la cobertura de riesgos del trabajo.")])
    d.firmas(["Empleador", "Trabajador/a"]); docs.append(("03-Contrato-plazo-fijo.docx", d))

    d = mk("Convocatoria de la nueva temporada", "Notificación del art. 98 de la LCT (al menos 30 días antes)")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Sr./Sra. [[nombre del trabajador/a]]\nDomicilio: [[domicilio]]", False)
    d.p("Por la presente, y en los términos del art. 98 de la Ley de Contrato de Trabajo, le notifico mi voluntad de reiterar la relación laboral en los términos de la temporada anterior: cargo [[cargo]], lugar [[lugar]], inicio el [[fecha de inicio]] y finalización prevista el [[fecha de fin]], con las condiciones del convenio [[número]] y una remuneración de $ [[monto]].")
    d.p("Le solicito que manifieste su decisión de continuar o no dentro de los 5 días de notificado, por escrito o presentándose en [[domicilio del establecimiento]]. Esta notificación se efectúa con una antelación no menor a 30 días del inicio de la temporada.")
    d.firmas(["Empleador"]); docs.append(("04-Convocatoria-nueva-temporada.docx", d))

    d = mk("Respuesta del trabajador", "Aceptación o rechazo de la convocatoria")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Señor/a [[empleador]]\nDomicilio: [[domicilio]]", False)
    d.p("En respuesta a su notificación del [[fecha]] por la temporada [[período]], manifiesto que [[ACEPTO continuar la relación en las condiciones propuestas / NO DESEO continuar la relación]], conforme al art. 98 de la Ley de Contrato de Trabajo.")
    d.p("[[Si acepta: me presentaré a trabajar el __ de ___ a las __ horas.]] [[Si no acepta: solicito la liquidación de los conceptos pendientes y la entrega de los certificados.]]")
    d.firmas(["Trabajador/a"]); docs.append(("05-Respuesta-del-trabajador.docx", d))

    d = mk("Liquidación de cierre de temporada", "Planilla para completar con tu convenio")
    d.table(["Concepto", "Cómo se calcula", "Monto ($)"], [
        ["Sueldo del último período", "Días trabajados × sueldo ÷ 30", "[[ ]]"],
        ["SAC proporcional", "Mejor sueldo mensual del semestre ÷ 2, proporcional al tiempo trabajado", "[[ ]]"],
        ["Vacaciones no gozadas", "Días de descanso proporcionales (1 por cada 20 trabajados) × sueldo ÷ 25", "[[ ]]"],
        ["Adicionales del convenio", "Según tu convenio colectivo", "[[ ]]"],
        ["Descuentos legales", "Aportes jubilatorios, obra social y otros", "[[ ]]"],
        ["TOTAL NETO", "", "[[ ]]"]], [4.5, 8, 3])
    d.p("Contrastá estas cuentas con el convenio de tu actividad y, si hay dudas, con un contador o abogado laboralista.", size=9, italic=True)
    docs.append(("06-Liquidacion-de-cierre.docx", d))

    d = mk("Checklist de alta y documentación", "Antes del primer día de trabajo")
    d.table(["Paso", "Hecho"], [[x, "[[ ]]"] for x in [
        "Pedir DNI, CUIL, domicilio y datos de contacto del trabajador.", "Elegir la modalidad (temporada, eventual o plazo fijo) y firmar el contrato por duplicado.",
        "Registrar el alta en ARCA (Simplificación Registral) con Clave Fiscal, antes del primer día.", "Contratar o actualizar la ART con el nuevo trabajador.",
        "Confirmar el convenio colectivo, la categoría y la escala salarial vigente.", "Entregar copia del contrato y de la constancia de alta.",
        "Anotar la fecha de la próxima convocatoria (30 días antes de la temporada).", "Guardar recibos de sueldo firmados y comprobantes de pago de aportes."]], [12, 3])
    docs.append(("07-Checklist-de-alta.docx", d))

    d = mk("Constancia de entrega de certificados", "Art. 80 de la Ley de Contrato de Trabajo")
    d.p("[[Ciudad]], [[fecha]]", False)
    d.p("Se deja constancia de que [[empleador]], CUIT [[número]], pone a disposición de [[trabajador/a]], DNI [[número]], los certificados que acreditan los datos de la relación laboral, la función desempeñada, las capacitaciones realizadas y la constancia del ingreso de aportes y contribuciones a la seguridad social, correspondientes al período del [[fecha de inicio]] al [[fecha de fin]]. La entrega se realiza en formato [[físico / digital con constancia de entrega]], dentro de los 45 días hábiles de la extinción del contrato.")
    d.firmas(["Empleador", "Trabajador/a (recibí conforme)"]); docs.append(("08-Constancia-de-certificados.docx", d))

    with zipfile.ZipFile(os.path.join(priv, "pack-temporada.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        for fn, dd in docs:
            buf = io.BytesIO(); dd.d.save(buf); z.writestr(fn, buf.getvalue())
    print("ok pack-temporada.zip", len(docs))

if __name__ == "__main__":
    build_pdfs(); build_pack()
