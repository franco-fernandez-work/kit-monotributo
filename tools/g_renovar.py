"""Guía 'Se vence tu alquiler' (HUECOS.md #22). Fuentes: art. 1218 CCyC (continuación de la locación concluida) según abogados.com.ar y leyfacil (secundarias, NO leído en Infoleg);
DNU 70/2023 (plazo libre, supletorio 2 años en vivienda; deroga Ley 27.551 y arts. 1202, 1204, 1204 bis, 1221 bis según Allende y Colegio de Escribanos). Ver HANDOFF: la salida anticipada con 10% ya figura en la guía 'alquilar'.
NO verificado: texto vigente de arts. 1218 y 1221, si la Ley 27.742 consolidó el DNU, sellado, registración."""
from guias_lib import *

META = dict(nombre="Se vence tu alquiler", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Se vence", "tu alquiler"], sub=["Renovar, negociar o mudarte:", "cartas, números y plazos para decidir con tiempo."],
            sello="10", sello2="CARTAS", cabecera="SE VENCE TU ALQUILER",
            pie="Información general. No reemplaza a un abogado.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para inquilinos y propietarios cuyo contrato de alquiler vence en los próximos meses.")
    f.append(P("Un contrato que vence deja de ser una rutina: desde el DNU 70/2023, el plazo, el ajuste y la moneda se acuerdan libremente, y cada renovación es una <b>negociación nueva</b>. Esta guía te ayuda a llegar con números, con tiempo y con las cartas para dejar todo por escrito."))
    f.append(alerta("NO ES ASESORAMIENTO LEGAL", "Es información general. Las normas de alquileres cambiaron varias veces y los contratos tienen cláusulas propias. Ante un conflicto o un desalojo, consultá a un abogado o a un colegio profesional."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Qué pasa cuando vence", "Si el contrato sigue, qué dice el Código y por qué importa la carta."),
        ("2. Cronograma", "Qué hacer 120, 90, 60 y 30 días antes."),
        ("3. Qué negociar", "Precio, ajuste, plazo, depósito, garantía, salida."),
        ("4. Renovar o mudarte", "La cuenta con costo de entrada y punto de equilibrio."),
        ("5. Si no hay acuerdo", "Cómo dejar la propiedad o qué hacer si el otro no responde."),
        ("6. Errores frecuentes", "Los que salen más caros."),
        ("Anexo", "Cartas modelo y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA CALCULADORA GRATIS", f"Compará renovar contra mudarte: {BASE_URL}/renovar-alquiler-o-mudarse"))
    f.append(PageBreak())

    f += cap("1", "QUÉ PASA CUANDO VENCE", "El contrato no se renueva solo", "La carta marca el comienzo de la negociación.")
    f.append(P("Según las fuentes consultadas sobre el Código Civil y Comercial (art. 1218), si vence el plazo y el inquilino sigue en la propiedad <b>no hay tácita reconducción</b>, es decir, el contrato no se renueva automáticamente por un nuevo plazo. En cambio, la locación continúa en los mismos términos hasta que cualquiera de las partes la da por concluida mediante una <b>comunicación fehaciente</b>. Recibir el alquiler no cambia esa regla."))
    f.append(P("Las fuentes son secundarias (abogados.com.ar, leyfacil, un fallo de la Cámara Civil). Confirmá el texto vigente en Infoleg o con un abogado antes de decidir.", "nota"))
    f.append(Tiles([("Sin renovación", "automática|(art. 1218)"), ("Carta", "fehaciente|(carta documento)"), ("Por escrito", "toda prórroga|y acuerdo"), ("Plazo libre", "desde el|DNU 70/2023")]))
    f.append(Spacer(1, 10))
    f.append(P("Qué cambia por el DNU 70/2023, según el análisis de estudios jurídicos y del Colegio de Escribanos: el <b>plazo</b> se fija libremente, sin mínimo; si el contrato no dice nada, el plazo supletorio es de 2 años en vivienda permanente. Se derogó la Ley 27.551 (de alquileres) y artículos del Código sobre ajuste e indexación, de modo que <b>el ajuste y la moneda se pactan libremente</b> entre las partes."))
    f.append(consejo("DOS RIESGOS DE QUEDARTE SIN CARTA", "Para el inquilino: el propietario puede dar por terminada la locación y pedir la entrega. Para el propietario: seguir cobrando sin dejar nada escrito complica después pedir un nuevo precio. En ambos casos, conviene dejar todo por escrito."))
    f.append(PageBreak())

    f += cap("2", "CRONOGRAMA", "Qué hacer según los días que faltan", "Empezar a hablar con 60 a 90 días de anticipación es una práctica recomendada por profesionales.")
    f.append(Flujo([("120 días", "Revisá el|contrato"), ("90 días", "Primera|conversación"), ("60 días", "Propuesta|escrita"), ("30 días", "Carta de|cierre"), ("Vence", "Firma o|entrega")], CEL))
    f.append(Spacer(1, 10))
    f.append(Checklist(["<b>120 días antes</b>: releé el contrato: plazo, fecha de vencimiento, ajuste pactado, cláusula de renovación y de rescisión, garantía y depósito.", "<b>120 días antes</b>: averiguá los precios de alquileres parecidos en tu zona (portales y avisos), con fecha y captura.", "<b>90 días antes</b>: avisá por mensaje que querés hablar de la renovación y proponé una fecha.", "<b>90 días antes</b>: definí tu piso y tu techo (hasta cuánto aceptás y a partir de cuándo te mudás).", "<b>60 días antes</b>: enviá la propuesta por escrito con precio, ajuste, plazo y condiciones.", "<b>60 días antes</b>: si pensás mudarte, ya empezá a ver opciones (capítulo 4).", "<b>30 días antes</b>: si no hay acuerdo, mandá la carta de no renovación o de intimación (ver anexo).", "<b>Al firmar</b>: nuevo contrato por escrito o adenda firmada por todos, con el estado de la propiedad y los pagos al día."], "CRONOGRAMA"))
    f.append(PageBreak())

    f += cap("3", "QUÉ NEGOCIAR", "Los puntos de una renovación", "El precio es solo uno de ellos.")
    f.append(tabla(["Punto", "Qué conviene acordar", "Para quién importa más"], [
        ("Precio inicial", "Monto en pesos y fecha desde la que rige.", "Ambos"),
        ("Ajuste", "Índice (IPC, UVA, acuerdo fijo), frecuencia y cómo se informa.", "Inquilino: previsibilidad. Propietario: no perder contra la inflación."),
        ("Plazo", "Duración y si hay prórroga automática pactada.", "Inquilino: estabilidad."),
        ("Depósito y garantía", "Si se mantienen, se actualizan o se devuelven.", "Inquilino: no inmovilizar plata de más."),
        ("Reparaciones", "Quién paga qué, con topes y plazos.", "Ambos"),
        ("Rescisión anticipada", "Aviso, penalidad y desde cuándo.", "Inquilino: poder mudarse."),
        ("Mascotas, subalquiler, uso", "Qué se permite.", "Ambos"),
        ("Expensas, impuestos", "Quién paga qué y cómo se comprueba.", "Ambos")],
        [32 * mm, 80 * mm, W - 2 * M - 112 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Armá escenarios</b>: calculá el costo total de 12 meses con tres inflaciones posibles. Un alquiler más bajo con un mal ajuste puede salir más caro que uno más alto con un ajuste razonable.", "<b>Mostrá datos</b>: capturas de avisos parecidos y tu historial de pagos puntuales.", "<b>Ofrecé algo a cambio</b>: más plazo, pago adelantado de un mes o menos pedidos de reparación pueden bajar el precio.", "<b>Propietarios</b>: un buen inquilino evita meses vacíos, gastos de aviso y comisión de un nuevo contrato; es un argumento para mantener el precio razonable."])
    f.append(PageBreak())

    f += cap("4", "RENOVAR O MUDARTE", "La cuenta que decide", "No es solo comparar alquileres: mudarse tiene un costo de entrada.")
    f.append(P("Compará los <b>costos únicos de mudarte</b> contra la <b>diferencia mensual</b> entre quedarte y el nuevo alquiler. El resultado es el <b>punto de equilibrio</b>: cuántos meses necesitás vivir en el nuevo lugar para que la mudanza valga la pena."))
    f.append(tabla(["Costo único de mudarte", "Cómo estimarlo"], [
        ("Mudanza (flete o empresa)", "Tres presupuestos por escrito."),
        ("Depósito en garantía", "Lo que pida el nuevo contrato; recuperable al final si se pactó así."),
        ("Mes adelantado", "Si lo piden; es un costo de caja, no definitivo."),
        ("Comisión de la inmobiliaria", "Si hay intermediario, lo que figure en el contrato; varía y debe estar por escrito."),
        ("Servicios y trámites", "Altas, cambio de domicilio, internet."),
        ("Superposición de alquileres", "Si pagás dos lugares unas semanas.")], [60 * mm, W - 2 * M - 60 * mm]))
    f.append(Spacer(1, 8))
    f.append(Barra("Ejemplo: si el nuevo alquiler es $ 50.000 menor por mes (miles de $)", [("Costos únicos", 400, SELLO), ("Ahorro en 12 meses", 600, CEL)], "$ mil"))
    f.append(P("En el ejemplo, los costos únicos ($ 400.000) se recuperan en 8 meses ($ 400.000 ÷ $ 50.000). Después de eso, cada mes ahorrás $ 50.000. Cargá tus números en la calculadora de la web: son solo ejemplos.", "nota"))
    f.append(consejo("LO QUE LA CUENTA NO MIDE", "La cercanía al trabajo, a la escuela o a la familia, el ruido, la seguridad y el estado del lugar también cuentan. Poné un número a lo que valorás y compará con el ahorro."))
    f.append(PageBreak())

    f += cap("5", "SI NO HAY ACUERDO", "Cómo salir ordenado", "Sin discusiones y con pruebas.")
    f += E(["<b>Comunicá por escrito</b> (carta documento o medio fehaciente) que no vas a renovar, con la fecha de entrega.", "<b>Acordá la fecha de entrega</b> y el estado: fotos del inventario inicial y del final, fechas y firmas.", "<b>Dejá todo pago</b>: alquiler, expensas, servicios; pedí los comprobantes y el libre deuda si corresponde.", "<b>Pedí la devolución del depósito</b> y fijá la fecha; si la propiedad está en buen estado, es lo que corresponde.", "<b>Entregá las llaves</b> y firmá un acta de entrega con fecha y hora.", "<b>Si el propietario no responde o no devuelve el depósito</b>, reclamá por carta documento; el siguiente paso es la mediación y, si hace falta, un abogado."])
    f.append(P("Para el propietario: si el inquilino no deja la propiedad al terminar el contrato, no hagas justicia por mano propia (cambiar cerraduras, cortar servicios). Hay una vía judicial para pedir la entrega; consultá a un abogado.", "nota"))
    f.append(alerta("NO CORTES LOS SERVICIOS NI CAMBIES LA CERRADURA", "Es una situación de riesgo legal para el propietario. Antes de actuar, enviá la intimación por escrito y consultá a un profesional."))
    f.append(PageBreak())

    f += cap("6", "ERRORES FRECUENTES", "Los que más cuestan")
    f += L(["<b>Esperar a que llegue el vencimiento</b> para empezar a hablar.", "<b>Aceptar de palabra</b> y no firmar adenda o contrato nuevo.", "<b>Dejar de pagar</b> cuando hay desacuerdo; empeora tu posición.", "<b>No comparar</b> con avisos reales de la zona.", "<b>Firmar un ajuste sin calcular</b> cuánto sube con distintas inflaciones.", "<b>No sacar fotos</b> al entregar el lugar.", "<b>No pedir libre deuda</b> de expensas y servicios.", "<b>Dar un depósito sin recibo</b>."])
    f.append(P("Si ya firmaste algo que no entendés o recibiste una intimación, consultá a un abogado antes de contestar.", "nota"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Cartas modelo", "Completá los datos entre corchetes y enviá por un medio que deje constancia.")
    f.append(H2("Carta 1: propuesta de renovación"))
    f.append(P("[Ciudad], [fecha]. A [nombre del propietario/inquilino]. Domicilio: [dirección]. Ref.: contrato de locación de [dirección de la propiedad], con vencimiento el [fecha]. <br/>Por la presente le propongo renovar el contrato en las siguientes condiciones: plazo de [__] meses desde el [fecha]; alquiler mensual inicial de $ [__]; ajuste [índice y frecuencia]; depósito [se mantiene / se actualiza / se devuelve]; resto de las cláusulas sin cambios. Le ruego respuesta antes del [fecha]. Saludo atentamente. [Firma y aclaración]"))
    f.append(H2("Carta 2: no renovación"))
    f.append(P("[Ciudad], [fecha]. A [nombre]. Domicilio: [dirección]. <br/>Comunico que no deseo renovar el contrato de locación de [dirección de la propiedad], que vence el [fecha]. Propongo entregar el inmueble el [fecha], previa inspección conjunta del estado, y coordinar la devolución del depósito de $ [__]. Quedo a su disposición para fijar día y hora. [Firma y aclaración]"))
    f.append(H2("Carta 3: intimación por el depósito"))
    f.append(P("[Ciudad], [fecha]. A [nombre]. Domicilio: [dirección]. <br/>Intimo a restituir en el plazo de [__] días el depósito en garantía de $ [__], entregado el [fecha] por el contrato de la propiedad de [dirección], desocupada y entregada el [fecha]. Caso contrario, iniciaré las acciones correspondientes. [Firma y aclaración]"))
    f.append(P("Son modelos orientativos. Adaptalos a tu contrato y, si hay un conflicto serio, consultá a un abogado.", "nota"))
    f.append(H2("Fuentes"))
    f += L(["Art. 1218 del Código Civil y Comercial (continuación de la locación concluida), según abogados.com.ar y leyfacil.com.ar (fuentes secundarias).", "DNU 70/2023, locaciones: análisis de estudios jurídicos y del Colegio de Escribanos (plazo libre, supletorio de 2 años en vivienda, derogación de la Ley 27.551).", "Prácticas profesionales de renegociación: iProfesional y Roomix (60 a 90 días de anticipación)."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal. Las normas de locaciones cambiaron y pueden volver a cambiar; verificá su vigencia en Infoleg. Está prohibida su reventa o redistribución.", "nota"))
    return f
