"""Guía 'Jubilación ANSES paso a paso' (HUECOS.md #15). Verificado en Infoleg (texto actualizado de la Ley 24.241): arts. 19, 22, 22 bis, 24.
Montos de octubre 2026 (Res. ANSES 284/2026, BO 23/09/2026) tomados de medios, coherentes entre sí (PUAM = 80% del haber mínimo). NO verificado en ANSES (el sitio bloquea consultas automáticas): nombres de pantallas y turnos, vigencia de la moratoria Ley 27.705 más allá del 23/03/2025, compatibilidad de la PUAM con trabajo."""
from guias_lib import *

META = dict(nombre="Jubilación ANSES paso a paso", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Jubilación", "ANSES", "paso a paso"], sub=["Requisitos, aportes que faltan, PUAM y el trámite", "para pedir tu jubilación sin gestores."],
            sello="30 AÑOS", sello2="DE APORTES", cabecera="JUBILACIÓN ANSES PASO A PASO",
            pie="Información general. No reemplaza a ANSES ni a un profesional. Confirmá en anses.gob.ar.", tam=46)

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien se acerca a la edad de jubilarse o la cumplió y no sabe si le alcanzan los aportes.")
    f.append(P("Jubilarse es un trámite <b>gratuito</b> que se hace ante la ANSES. Lo difícil no es el trámite: es <b>saber de antemano si tenés los requisitos</b> y qué hacer si te faltan aportes. Esta guía te da el método: qué dice la ley, cómo revisar tu historia laboral, qué alternativas existen si te faltan años y cómo hacer el trámite sin pagar a un gestor."))
    f.append(alerta("LA NORMATIVA CAMBIA", "Las condiciones para jubilarse, las moratorias y los montos se modificaron varias veces en los últimos años. Los requisitos de edad y aportes que citamos son los de la Ley 24.241 (texto actualizado en Infoleg). Todo lo operativo (pantallas, turnos, formularios) y los montos conviene confirmarlos en anses.gob.ar el día que hagas el trámite."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Los requisitos", "Edad y años de aportes, con la regla de compensación."),
        ("2. Qué cuenta como aporte", "Empleo, monotributo, autónomo, hijos y reciprocidad."),
        ("3. Revisá tu historia laboral", "Cómo ver tus aportes y corregir faltantes."),
        ("4. Si te faltan aportes", "Las alternativas reales, sin promesas."),
        ("5. La PUAM", "La pensión para quien no llega a la jubilación."),
        ("6. El trámite paso a paso", "Documentos, solicitud, seguimiento."),
        ("7. Cuánto vas a cobrar", "Cómo se compone y los montos de referencia."),
        ("8. Estafas y errores", "Gestores, falsas moratorias y mensajes truchos."),
        ("9. Plan de 30 días", "Checklist para empezar."),
        ("Anexo", "Glosario y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("SI TE FALTAN POCOS AÑOS", "Revisá primero el capítulo 3 y el 4. A veces faltan aportes que sí existieron (empleos sin cargar) y se pueden reconocer."))
    f.append(PageBreak())

    f += cap("1", "LOS REQUISITOS", "Edad y años de aportes", "Para la jubilación ordinaria, la Ley 24.241 pide tres cosas a la vez.")
    f.append(Tiles([("65 años", "hombres|(art. 19 a)"), ("60 años", "mujeres|(art. 19 b)"), ("30 años", "de servicios con|aportes (art. 19 c)"), ("Hasta 65", "las mujeres pueden|optar por seguir")]))
    f.append(Spacer(1, 10))
    f += L(["<b>Edad</b>: 65 años para los hombres y 60 para las mujeres. Las mujeres pueden optar por seguir trabajando hasta los 65 (art. 19).", "<b>Servicios con aportes</b>: 30 años de servicios <b>con aportes computables</b> en uno o más regímenes del sistema de reciprocidad. Trabajar sin aportes (en negro) <b>no suma</b> si no se reconoce.", "<b>Cómputo</b>: se cuentan los servicios del sistema actual y los anteriores, hasta el momento de pedir la prestación (art. 22)."])
    f.append(H2("La regla de compensación"))
    f.append(P("El art. 19 permite <b>compensar el exceso de edad con la falta de servicios</b>, a razón de <b>dos años de edad excedentes por uno de servicios faltantes</b>, y solo para llegar al mínimo de servicios de la prestación básica universal. Ejemplo: un hombre de 69 años (4 años más que los 65) con 28 años de aportes (faltan 2) cumple, porque 4 años de exceso de edad cubren 2 de servicios."))
    f.append(Barra("Ejemplo: hombre de 69 años con 28 años de aportes (en años)", [("Aportes", 28, CEL), ("Cubiertos por la edad", 2, OK_C)], "años"))
    f.append(Spacer(1, 8))
    f.append(consejo("LA CALCULADORA DE LA WEB", "Cargá tu edad, tus años de aportes y tus hijos y mirá si cumplís o cuánto te falta: kit-monotributo.fernandezfrancowork.workers.dev/cuantos-aportes-necesito-para-jubilarme"))
    f.append(PageBreak())

    f += cap("2", "QUÉ CUENTA COMO APORTE", "Las distintas formas de sumar años", "No todos los años trabajados cuentan igual. Revisá cuáles tenés.")
    f.append(tabla(["Situación", "¿Suma?", "Qué mirar"], [
        ("Relación de dependencia en blanco", "Sí", "Que el empleador haya ingresado los aportes."),
        ("Monotributo", "Sí, con el componente previsional", "Los meses pagos del componente jubilatorio."),
        ("Autónomo", "Sí", "Meses con aportes pagados; las deudas no suman."),
        ("Casas particulares", "Sí", "Que el empleador haya pagado los aportes."),
        ("Trabajo en negro", "No, salvo reconocimiento", "Se necesita probarlo (capítulo 4)."),
        ("Cajas de otras provincias o de profesionales", "Sí, por reciprocidad", "Pedí los certificados de servicios de cada caja."),
        ("Años por hijos (mujeres)", "Sí, según la ley", "Ver recuadro abajo.")],
        [56 * mm, 44 * mm, W - 2 * M - 100 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("Años de servicio por hijos"))
    f.append(P("El texto de la Ley 24.241 publicado en Infoleg incluye el art. 22 bis (incorporado por el Decreto 475/2021): las mujeres y personas gestantes pueden computar <b>un año de servicio por cada hijo nacido con vida</b>; <b>dos años por cada hijo adoptado</b> (si son menores); <b>un año adicional por hijo con discapacidad</b>; y <b>otros dos años</b> por hijo para quienes percibieron la Asignación Universal por Hijo al menos 12 meses. Solo sirve para llegar al mínimo de servicios. <b>Confirmá en ANSES</b> cómo se aplica hoy y qué comprobantes piden."))
    f.append(P("Un mes con aportes es un mes con aportes: no hace falta que sean consecutivos. Lo que importa es el total.", "nota"))
    f.append(PageBreak())

    f += cap("3", "REVISÁ TU HISTORIA LABORAL", "Antes de pedir nada, mirá qué figura", "La ANSES te jubila con lo que tiene registrado. Si falta algo, hay que corregirlo.")
    f += E(["Ingresá a <b>Mi ANSES</b> (anses.gob.ar) con tu CUIL y tu Clave de la Seguridad Social, o con Clave Fiscal de ARCA si te permiten el acceso.", "Buscá la sección de <b>historia laboral</b> o consulta de aportes (el nombre puede variar) y bajá el detalle.", "Anotá <b>períodos y empleadores</b>. Marcá los años que faltan o que no reconocés.", "Pedí a tus ex empleadores los <b>recibos de sueldo y certificados de servicios</b> de esos períodos, si aún los tenés.", "Si trabajaste en cajas provinciales o profesionales, <b>pedí a cada caja el certificado de servicios</b>.", "Presentá la <b>corrección o el reconocimiento de servicios</b> ante ANSES con la prueba que reuniste."])
    f.append(Spacer(1, 6))
    f.append(Checklist(["Tengo mi <b>CUIL</b> y mi clave de la Seguridad Social.", "Bajé el <b>detalle de aportes</b> y lo comparé con mis recuerdos.", "Reuní <b>recibos de sueldo</b> y comprobantes de pago de monotributo o autónomo.", "Pedí los <b>certificados de otras cajas</b>, si corresponde.", "Anoté los <b>períodos sin aportes</b> que quiero reconocer.", "Tengo copias de <b>DNI y partidas</b> de nacimiento de mis hijos (mujeres)."], "CHECKLIST DE HISTORIA LABORAL"))
    f.append(P("Los aportes que se pagaron pero no figuran suelen poder corregirse. Los que nunca se pagaron son otra cosa: pasan al capítulo siguiente.", "nota"))
    f.append(PageBreak())

    f += cap("4", "SI TE FALTAN APORTES", "Las alternativas reales", "Hay que distinguir lo que está vigente de lo que fue o puede ser.")
    f.append(tabla(["Alternativa", "Qué es", "Estado"], [
        ("Reconocer servicios no registrados", "Probar que trabajaste en relación de dependencia con testigos, recibos o documentos para que se sumen los años.", "Vigente; requiere prueba y puede demorar."),
        ("Seguir trabajando y aportando", "Completar los años faltantes con monotributo, autónomo o empleo registrado.", "Siempre disponible."),
        ("Plan de pago de deuda previsional (Ley 27.705)", "Compra de meses faltantes con cuotas descontadas del haber. Su artículo 4 le dio vigencia de dos años, prorrogable por igual período.", "El plazo original venció el 23/03/2025; según lo que pudimos verificar, no hay prórroga sancionada. Confirmá en ANSES."),
        ("PUAM", "Pensión universal para mayores de 65 sin jubilación (capítulo 5).", "Vigente."),
        ("Pagar deudas del autónomo o monotributo", "Regularizar períodos adeudados con planes de ARCA.", "Depende del plan vigente en ARCA.")],
        [48 * mm, 70 * mm, W - 2 * M - 118 * mm]))
    f.append(Spacer(1, 8))
    f.append(alerta("DESCONFIÁ DE LA \"MORATORIA\" QUE TE OFRECEN", "Si alguien te dice que \"todavía hay moratoria\" y te cobra por anotarte, desconfiá. Verificá en anses.gob.ar qué planes están abiertos hoy. Ningún trámite de ANSES necesita gestor ni pago previo."))
    f.append(H2("Qué decisión tomar"))
    f += L(["<b>Te faltan pocos años</b> y podés seguir aportando: sumarlos suele ser lo más claro. Hacé la cuenta de cuántos años y cuánto cuesta cada mes de aporte.", "<b>Te faltan muchos años</b>: evaluá reconocimiento de servicios y la PUAM al cumplir 65.", "<b>No sabés qué te falta</b>: empezá por el capítulo 3."])
    f.append(PageBreak())

    f += cap("5", "LA PUAM", "Pensión Universal para el Adulto Mayor", "Para quienes cumplieron 65 años y no tienen jubilación ni pensión.")
    f.append(P("La PUAM (art. 13 de la Ley 27.260, reglamentada por el Decreto 894/2016) es una prestación <b>vitalicia y no contributiva</b>: no exige 30 años de aportes. Equivale al <b>80% del haber mínimo garantizado</b>. Requisitos generales: tener 65 años o más, residir en el país y no tener jubilación, pensión o retiro (contributivo o no) ni otra prestación incompatible."))
    f.append(Tiles([("65 años", "edad mínima|de la PUAM"), ("80%", "del haber mínimo|garantizado"), ("$ 348.599", "PUAM octubre 2026|(referencia)"), ("+ $ 70.000", "bono extraordinario|de octubre")]))
    f.append(Spacer(1, 10))
    f += L(["<b>Incompatibilidades</b>: no se cobra junto con una jubilación o pensión. Si podés o no trabajar, y cuánto, se definió por normas posteriores: <b>consultá la regla vigente en ANSES</b> antes de decidir.", "<b>Diferencias con la jubilación</b>: la PUAM no genera pensión para derechohabientes y suele tener menor monto. Elegirla tiene consecuencias: evaluá con tiempo.", "<b>Trámite</b>: se pide en ANSES con tu DNI y CUIL, por la web o con turno."])
    f.append(P("Los montos de octubre de 2026 (haber mínimo $ 435.748,51 y PUAM $ 348.598,81, Res. ANSES 284/2026) son de referencia y cambian con la movilidad. Verificalos en anses.gob.ar.", "nota"))
    f.append(PageBreak())

    f += cap("6", "EL TRÁMITE", "Paso a paso para pedir tu jubilación", "Es gratuito. El orden es el mismo; los nombres de pantallas pueden cambiar.")
    f.append(Flujo([("Revisar|aportes", "Historia laboral|en Mi ANSES"), ("Juntar|papeles", "DNI, CUIL y|pruebas"), ("Pedir|turno", "Por web o|canales oficiales"), ("Presentar|solicitud", "Con tus datos|y el CBU"), ("Seguir|el trámite", "Notificación y|resolución")], CEL))
    f.append(Spacer(1, 10))
    f += E(["<b>Ordená la documentación</b>: DNI, CUIL, constancia de CBU de tu cuenta, y las pruebas de períodos que corrigieron (recibos, certificados de otras cajas, partidas de nacimiento de los hijos si corresponde).", "<b>Sacá turno</b> o iniciá la solicitud por Mi ANSES o por los canales que informe la ANSES. Confirmá siempre que la página sea anses.gob.ar.", "<b>Presentá la solicitud</b> con todo lo que acredite los servicios y la edad.", "<b>Pedí el número de expediente</b> y anotá la fecha. Con ese número seguís el trámite.", "<b>Esperá la resolución</b>: te notifican si te acuerdan el beneficio o si piden algo más. Si te falta documentación, respondé en el plazo que indique la notificación.", "<b>Cobrás desde el alta</b> que fije la resolución. Si no estás de acuerdo con el monto o el rechazo, hay una vía de reclamo y de recurso: consultá los plazos en la resolución."])
    f.append(Spacer(1, 6))
    f.append(consejo("EL TRÁMITE ES GRATIS", "ANSES no cobra por tramitar la jubilación. Si necesitás ayuda, podés ir a una UDAI o pedir orientación en los canales oficiales."))
    f.append(P("Los plazos de resolución varían. Si hay demora, podés reclamar por los canales de ANSES; si no hay respuesta, un abogado previsionalista puede iniciar un amparo por mora (consultá antes los costos).", "nota"))
    f.append(PageBreak())

    f += cap("7", "CUÁNTO VAS A COBRAR", "Cómo se compone el haber", "No hay una fórmula simple: depende de tus aportes y de cuándo trabajaste.")
    f += L(["<b>Prestación básica universal (PBU)</b>: un monto fijo para todos los jubilados (art. 20).", "<b>Prestación compensatoria</b>: 1,5% por cada año de servicio con aportes (o fracción mayor de seis meses), hasta 35 años, sobre el promedio de remuneraciones actualizadas del período que fija la ley (art. 24). Se calcula con tus aportes anteriores a 1994.", "<b>Prestación adicional por permanencia</b>: para los servicios posteriores a 1994, también con 1,5% por año.", "<b>Haber mínimo garantizado</b>: si el cálculo da menos, se completa hasta el mínimo, que se actualiza por movilidad. Referencia de octubre de 2026: $ 435.748,51 más un bono extraordinario de $ 70.000 (Res. ANSES 284/2026 y Decreto 1108/2026, según los medios)."])
    f.append(Spacer(1, 6))
    f.append(Barra("Ejemplo de referencia: PUAM y haber mínimo, octubre 2026 (en miles de $)", [("PUAM", 349, TINTA), ("Dif. hasta el mínimo", 87, CEL), ("Bono", 70, OK_C)], "$ mil"))
    f.append(P("El ejemplo suma la PUAM, la diferencia hasta el haber mínimo y el bono. Son números de referencia y se actualizan todos los meses.", "nota"))
    f.append(P("Con un monto de referencia no se puede calcular tu haber exacto: la ANSES lo determina con tu historia laboral. <b>Pedí el cálculo estimado al iniciar el trámite.</b>"))
    f.append(PageBreak())

    f += cap("8", "ESTAFAS Y ERRORES", "Qué evitar")
    f.append(alerta("LA REGLA DE ORO", "ANSES no pide plata, claves ni códigos por mensaje, llamada o red social. El trámite es gratuito."))
    f += L(["<b>Gestores que cobran un porcentaje</b> del retroactivo o un adelanto: no los necesitás para el trámite normal.", "<b>\"Moratoria abierta\" por WhatsApp</b> con un pago previo.", "<b>Páginas parecidas a anses.gob.ar</b>: escribí la dirección vos, no entres por enlaces.", "<b>Firmar poderes</b> sin entender qué autorizás.", "<b>Dejar pasar el plazo</b> de la notificación de ANSES: puede costar el beneficio.", "<b>Dar de baja o cambiar</b> de régimen sin entender el efecto.", "<b>Cobrar por transferencia</b> a cuentas que no sean tuyas."])
    f.append(H2("Si te estafaron"))
    f += L(["Guardá capturas, comprobantes y datos de la cuenta destino.", "Avisá a tu banco de inmediato.", "Denunciá en la comisaría o la fiscalía y en los canales de ANSES."])
    f.append(PageBreak())

    f += cap("9", "PLAN DE 30 DÍAS", "Checklist para empezar")
    f.append(Checklist(["<b>Semana 1</b>: entrar a Mi ANSES, bajar el detalle de aportes y marcar lo que falta.", "<b>Semana 1</b>: anotar la edad que cumplís y la fecha en que alcanzás los 60 o 65 años.", "<b>Semana 2</b>: reunir recibos, certificados de cajas y partidas de hijos.", "<b>Semana 2</b>: hacer la cuenta con la calculadora de la web.", "<b>Semana 3</b>: decidir: seguir aportando, reconocer servicios o evaluar la PUAM.", "<b>Semana 4</b>: sacar turno o iniciar la solicitud y anotar el número de expediente."], "CHECKLIST"))
    f.append(Spacer(1, 8))
    f.append(tabla(["Si tu caso es…", "Empezá por…"], [
        ("Tengo la edad y los 30 años", "Capítulo 6: pedir la jubilación."),
        ("Tengo la edad y me faltan años", "Capítulo 3 y 4: revisar aportes y alternativas."),
        ("Me faltan años y todavía no cumplí la edad", "Capítulo 4: seguir aportando y reconocer servicios."),
        ("Tengo 65 y no llego", "Capítulo 5: PUAM.")], [66 * mm, W - 2 * M - 66 * mm]))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("PBU", "Prestación básica universal."),
        ("PC / PAP", "Prestación compensatoria y adicional por permanencia."),
        ("Haber mínimo", "Monto mínimo garantizado de una jubilación."),
        ("PUAM", "Pensión universal para el adulto mayor."),
        ("Reciprocidad", "Sistema que permite sumar servicios de distintas cajas."),
        ("UDAI", "Unidad de Atención Integral de ANSES."),
        ("SIPA", "Sistema Integrado Previsional Argentino.")], [34 * mm, W - 2 * M - 34 * mm]))
    f.append(H2("Fuentes"))
    f += L(["Ley 24.241, texto actualizado (Infoleg): arts. 19, 20, 22, 22 bis y 24.", "Ley 27.260, art. 13, y Decreto 894/2016 (PUAM).", "Ley 27.705 (plan de pago de deuda previsional), art. 4.", "ANSES, Res. 284/2026 (BO 23/09/2026), según medios, y Decreto 1108/2026 (bono)."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento previsional ni legal y no reemplaza a ANSES ni a un abogado previsionalista. La normativa, los plazos y los montos pueden cambiar: confirmalos en anses.gob.ar antes de decidir. Está prohibida su reventa o redistribución.", "nota"))
    return f
