# Se integra igual que packs_arts: ARTS.update(__import__("anses_arts").ARTS_ANSES) al inicio de main() en tools/build_site.py
def _oferta(idp, etiqueta, titulo, bajada, items, precio, texto_boton, nota):
    li = "".join(f"<li>{i}</li>" for i in items)
    return (f'<section class="oferta" aria-labelledby="of-{idp}"><div><span class="etiqueta">{etiqueta}</span><h2 id="of-{idp}">{titulo}</h2><p>{bajada}</p><ul>{li}</ul></div>'
            f'<div class="compra"><a class="boton" href="/comprar?p={idp}">{texto_boton} <span class="num">$ {precio}</span></a><span class="nota">{nota}</span></div></section>')
FUENTE = '<p class="nota">Información general y orientativa, sin carácter de asesoramiento. Fuente oficial: <a href="https://www.argentina.gob.ar/anses" rel="noopener">argentina.gob.ar/anses</a>. Confirmá plazos y requisitos antes de actuar.</p>'

LIB = ("Libreta AUH 2026: cómo presentarla paso a paso y cobrar el 20%",
 "Los 5 pasos para presentar la Libreta AUH en Mi ANSES, qué firmas y sellos necesitás y por qué rechazan formularios.",
 '<span class="etiqueta">AUH · Libreta</span><h1>Libreta AUH: cómo presentarla y cobrar el 20%</h1>'
 '<p class="bajada">ANSES paga el 80% de la AUH cada mes y retiene el 20%. Ese 20% se cobra una vez al año, solo si presentás la libreta con controles de salud, vacunas y escolaridad.</p>'
 '<div class="lectura"><h2>Los 5 pasos en Mi ANSES</h2><ol><li>Entrá a Mi ANSES con tu CUIL y Clave de la Seguridad Social.</li><li>Elegí “Hijos” y “Libreta AUH” y verificá los datos de cada hijo.</li><li>Descargá e imprimí el formulario.</li><li>Pedí que la escuela y el centro de salud lo completen, firmen y sellen.</li><li>Sacale una foto (JPG, hasta 3 MB), subila y confirmá el trámite.</li></ol>'
 '<h2>Por qué la rechazan</h2><ul><li>Sello o firma ilegible o faltante.</li><li>Foto con sombras, cortada o muy pesada.</li><li>Formulario de otro año o con campos en blanco.</li></ul>'
 '<h2>Plazos</h2><p>La Resolución ANSES 203/2019 fija la presentación desde el primer día hábil de enero hasta el último día hábil de diciembre de cada año, con posibles prórrogas (el 31 de marzo de 2026 fue una prórroga para el período 2025 y ya venció). Desde marzo de 2026 el 20% de los chicos de 0 a 4 años se paga solo cada mes, y desde septiembre de 2026 se suman los de 5 a 17 años por cruce de datos: la libreta se presenta solo si ese cruce no verifica los controles. El pago suele llegar unos 60 días después. Confirmá la fecha vigente en Mi ANSES.</p>' + FUENTE + '</div>'
 + _oferta("libreta", "Guía PDF + planilla", "Guía y carpeta Libreta AUH", "Todo lo que juntar y un control por hijo, para no perder el 20%.",
   ["Guía PDF de 5 páginas: papeles, pasos, plazos y qué hacer si te rechazan", "Planilla Excel con una fila por hijo, estado del trámite y cobro estimado calculado solo", "Registro de controles y vacunas", "Checklist anual para imprimir"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

CALC = """<div class="lectura" id="calc" style="background:var(--hoja);border:1px solid var(--linea);padding:16px;border-radius:4px">
<h2 style="margin-top:0">Calculá cuándo podrías jubilarte</h2>
<p><label>Sexo (según DNI)<br><select id="j-s"><option value="M">Mujer</option><option value="V">Varón</option></select></label></p>
<p><label>Fecha de nacimiento<br><input id="j-n" type="date"></label></p>
<p><label>Años de aportes que tenés<br><input id="j-a" type="number" min="0" max="60" step="0.5" value="0"></label></p>
<p><label><input id="j-c" type="checkbox" checked> Sigo aportando todos los meses</label></p>
<p><button class="boton" id="j-b" type="button">Calcular</button></p><div id="j-r" aria-live="polite"></div></div>
<script>
(function(){var $=function(i){return document.getElementById(i)};
function f(d){return d.toLocaleDateString('es-AR',{year:'numeric',month:'long',day:'numeric'})}
$('j-b').onclick=function(){var n=$('j-n').value;if(!n){$('j-r').textContent='Ingresá tu fecha de nacimiento.';return}
var s=$('j-s').value,e=s==='M'?60:65,b=new Date(n+'T12:00:00'),hoy=new Date(),ed=new Date(b);ed.setFullYear(b.getFullYear()+e);
var a=parseFloat($('j-a').value)||0,falta=Math.max(0,30-a),h=[];
h.push('<p>Cumplís la edad requerida ('+e+' años) el <b>'+f(ed)+'</b>'+(ed<=hoy?' (ya la cumpliste)':'')+'.</p>');
var d30=null;if(falta===0){h.push('<p>Ya tenés los 30 años de aportes.</p>');d30=hoy}
else if($('j-c').checked){d30=new Date(hoy);d30.setMonth(d30.getMonth()+Math.ceil(falta*12));h.push('<p>Si seguís aportando, llegás a los 30 años el <b>'+f(d30)+'</b> (te faltan '+falta.toFixed(1).replace('.',',')+' años).</p>')}
else h.push('<p>Te faltan <b>'+falta.toFixed(1).replace('.',',')+' años</b> de aportes y no estás sumando.</p>');
if(d30){var j=new Date(Math.max(ed,d30));h.push('<p><b>Fecha estimada de jubilación ordinaria: '+f(j)+'</b>.</p>')}
if(falta>0)h.push('<p>Alternativas a revisar en ANSES: plan de pago de deuda previsional (si calificás por edad: mujeres 50 a 59 años, varones 55 a 64) o PUAM desde los 65.</p>');
h.push('<p class="nota">Estimación orientativa; no incluye períodos sin registrar ni superposiciones.</p>');$('j-r').innerHTML=h.join('')}})();
</script>"""
JUB = ("¿Me puedo jubilar? Calculadora de edad y años de aportes",
 "Calculadora gratuita: con tu fecha de nacimiento y años de aportes estimá cuándo cumplís los requisitos de la jubilación ordinaria.",
 '<span class="etiqueta">Jubilación · ANSES</span><h1>¿Me puedo jubilar? Calculadora de edad y aportes</h1>'
 '<p class="bajada">La jubilación ordinaria pide dos cosas a la vez: 60 años (mujeres) o 65 (varones) y 30 años de aportes. Calculá cuándo cumplís las dos.</p>' + CALC +
 '<div class="lectura"><h2>Si te faltan años</h2><ul><li>Seguir aportando como empleado, autónomo o monotributista.</li><li>Plan de Pago de Deuda Previsional (Ley 27.705, modalidad para trabajadores en actividad): mujeres de 50 a 59 años y varones de 55 a 64, para períodos faltantes hasta marzo de 2012. La modalidad para quienes ya tienen la edad venció el 23/03/2025. Confirmá la vigencia en ANSES.</li><li>PUAM: sin exigencia de aportes, desde los 65 años.</li></ul>' + FUENTE + '</div>'
 + _oferta("jubila", "Guía PDF + planilla", "Guía y planilla “Mi camino a la jubilación”", "Revisá tu historia laboral, detectá períodos faltantes y llegá al turno con la carpeta lista.",
   ["Guía PDF: requisitos, cómo revisar aportes, qué hacer si faltan años y cómo es el trámite", "Planilla Excel que calcula edad, años faltantes y fecha estimada", "Registro de períodos y pruebas de cada empleo", "Checklist de documentación para el turno"],
   "3.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

CUD = ("CUD: documentación necesaria y pasos para tramitarlo",
 "Lista de documentación del Certificado Único de Discapacidad, qué vence a los 6 meses y cómo pedir turno en la junta evaluadora.",
 '<span class="etiqueta">Discapacidad · CUD</span><h1>CUD: qué documentación necesitás y cómo tramitarlo</h1>'
 '<p class="bajada">El trámite es gratuito. La mayoría de las demoras vienen de papeles vencidos o incompletos. Esta es la lista.</p>'
 '<div class="lectura"><h2>Documentación</h2><ul><li>Certificado médico con diagnóstico completo (no más de 6 meses de antigüedad, según argentina.gob.ar).</li><li>Estudios complementarios originales (no más de 6 meses).</li><li>Informes de profesionales tratantes.</li><li>DNI original, legible.</li><li>Carnet de obra social o prepaga, si tenés.</li><li>Recibo de sueldo propio, del familiar a cargo o de jubilación.</li></ul>'
 '<h2>Los 3 pasos</h2><ol><li>Reuní la documentación y revisá las fechas.</li><li>Pedí turno en la Junta Evaluadora que corresponde a tu domicilio.</li><li>Asistí en persona: la junta revisa, entrevista y decide.</li></ol>'
 '<p>Qué beneficios abre: transporte gratuito, cobertura de tratamientos, asignaciones y exenciones, según el caso y la jurisdicción.</p>' + FUENTE + '</div>'
 + _oferta("cud", "Guía PDF + planilla", "Guía y carpeta CUD", "Ordená papeles, turnos y beneficios sin que se te venza nada.",
   ["Guía PDF: documentación, paso a paso, si te rechazan, cómo usar los beneficios", "Planilla Excel con vencimiento de cada papel, alerta antes del turno y renovación", "Seguimiento de turnos, expedientes y beneficios pedidos", "Checklist para imprimir"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

ARTS_ANSES = {"libreta-auh-como-presentar": LIB, "me-puedo-jubilar-calculadora": JUB, "cud-documentacion-y-pasos": CUD}
