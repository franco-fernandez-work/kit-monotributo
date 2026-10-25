"""Guía 'Recuperá tu depósito de alquiler' (HUECOS.md #24, ronda 6). Fuente oficial leída el 25/10/2026: Código Civil y Comercial, texto actualizado en
argentina.gob.ar/normativa/nacional/ley-26994-235975/actualizacion: art. 1196 (cantidades, moneda y forma de devolución del depósito se pactan libremente, según DNU 70/2023 art. 255),
1206, 1207, 1210 (restituir en el estado recibido salvo deterioro por tiempo y uso regular; entregar constancias de pago), 1218, 1222-1223, 768 (intereses moratorios), 886-887 (mora), 2560 (prescripción genérica de 5 años, Ley 27.799).
NO verificado: mediación prejudicial obligatoria por jurisdicción (Ley 26.589 en el orden nacional), tasa BCRA aplicable, práctica de los juzgados, costo de la carta documento."""
from guias_lib import *

META = dict(nombre="Recuperá tu depósito de alquiler", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Recuperá tu", "depósito"], sub=["Cómo irte del alquiler sin perder plata:", "pruebas, cuentas y cartas para cobrar lo que te corresponde."],
            sello="4", sello2="CARTAS", cabecera="RECUPERÁ TU DEPÓSITO DE ALQUILER",
            pie="Información general. No reemplaza a un abogado.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para inquilinos que se van de un alquiler y quieren que les devuelvan el depósito en garantía.")
    f.append(P("El depósito suele ser el mayor gasto de entrada de un alquiler y el que más se pierde al salir: se devuelve tarde, sin actualizar o con descuentos que nadie explica. La buena noticia es que casi todo se gana <b>antes</b> de entregar las llaves, con fotos, papeles y fechas. Esta guía te da el orden, las cuentas y las cartas."))
    f.append(alerta("NO ES ASESORAMIENTO LEGAL", "Es información general. Cada contrato dice cosas distintas y el Código deja gran libertad a las partes. Si hay un conflicto serio, consultá a un abogado o a un colegio profesional."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Qué dicen la ley y tu contrato", "Quién decide cuánto y cómo se devuelve."),
        ("2. Antes de irte", "Cronograma de 60 días a la entrega de llaves."),
        ("3. Qué pueden descontar", "Desgaste, daños, deudas: lo que sí y lo que no."),
        ("4. Cuánto te corresponde", "Cuenta con tres formas de devolución."),
        ("5. La entrega", "Inspección, acta y llaves."),
        ("6. Si no te lo devuelven", "Escalera de reclamo: mensaje, carta, mediación, juicio."),
        ("7. Errores frecuentes", "Los que más cuestan."),
        ("Anexo", "4 cartas modelo y fuentes.")], [60 * mm, W - 2 * M - 60 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA CALCULADORA GRATIS", f"Calculá cuánto te deberían devolver: {BASE_URL}/recuperar-deposito-alquiler"))
    f.append(PageBreak())

    f += cap("1", "LA LEY Y TU CONTRATO", "Quién decide cuánto se devuelve", "Hoy el Código deja casi todo librado a lo que firmaron las partes.")
    f.append(P("Según el artículo 1196 del Código Civil y Comercial (texto vigente, sustituido por el DNU 70/2023), las partes pueden determinar <b>libremente las cantidades y la moneda</b> del depósito en garantía y <b>la forma en que se devuelve</b> al terminar el contrato. Ya no hay un tope legal de un mes ni una fórmula legal de actualización: <b>manda tu contrato</b>."))
    f.append(Tiles([("Libre", "monto, moneda|y devolución"), ("Art. 1196", "Código Civil|y Comercial"), ("Art. 1210", "devolver en el|estado recibido"), ("Tu contrato", "es la regla|principal")]))
    f.append(Spacer(1, 10))
    f.append(P("Lo que el Código sí exige al inquilino (art. 1210): devolver la propiedad <b>en el estado en que la recibió, salvo los deterioros provenientes del mero transcurso del tiempo y el uso regular</b>, y entregar las constancias de los pagos de servicios que le correspondían. Y mientras vivís ahí, el art. 1207 te pone a cargo el mantenimiento menor."))
    f.append(H2("Leé estas cinco cláusulas hoy"))
    f += E(["<b>Monto y moneda</b> del depósito: si se pagó en pesos o dólares y cuánto.", "<b>Forma de devolución</b>: el mismo monto, el valor del último alquiler, o ajustado por un índice. Es la cláusula que más plata mueve.", "<b>Plazo de devolución</b>: cuántos días después de entregar las llaves.", "<b>Qué se puede descontar</b> y cómo se justifica (presupuestos, facturas).", "<b>Estado inicial</b>: si hay inventario o acta de entrega con fotos."])
    f.append(alerta("SI EL CONTRATO NO DICE NADA", "Si no hay cláusula de devolución, el reclamo se apoya en que el depósito es tuyo hasta que se verifique el estado y los pagos. Dejá todo por escrito y fijá un plazo razonable en tu intimación. Conviene consultar a un profesional."))
    f.append(PageBreak())

    f += cap("2", "ANTES DE IRTE", "Cronograma para cobrar sin pelea", "Lo que se prueba antes vale más que lo que se discute después.")
    f.append(Flujo([("60 días", "Leé el|contrato"), ("30 días", "Aviso de|entrega"), ("15 días", "Fotos y|arreglos"), ("7 días", "Pagos al|día"), ("Entrega", "Acta y|llaves")], CEL))
    f.append(Spacer(1, 10))
    f.append(Checklist(["<b>60 días antes</b>: releé la cláusula de depósito, el plazo de aviso para irte y las penalidades. Anotá las fechas.", "<b>60 días antes</b>: buscá el inventario y las fotos de cuando entraste. Si no hay, es el momento de reconstruirlas con mensajes y fotos viejas.", "<b>30 días antes</b>: avisá por escrito (mail o carta) la fecha de entrega y pedí una inspección conjunta.", "<b>30 días antes</b>: proponé por escrito cómo y cuándo se devuelve el depósito.", "<b>15 días antes</b>: limpiá a fondo y arreglá el mantenimiento menor (lamparitas, canillas, tapones, cerraduras flojas).", "<b>15 días antes</b>: sacá fotos y video de cada ambiente, con fecha, incluidos placares, baño, cocina y paredes.", "<b>7 días antes</b>: juntá los comprobantes de pago de expensas, luz, gas, agua e internet y pedí el libre deuda si corresponde.", "<b>7 días antes</b>: anotá las lecturas de los medidores.", "<b>El día</b>: hacé la inspección con el propietario, firmá el acta de entrega y llevate una copia (anexo, carta 2)."], "CRONOGRAMA"))
    f.append(PageBreak())

    f += cap("3", "QUÉ PUEDEN DESCONTAR", "Desgaste, daños y deudas", "No todo lo que se ve gastado es un daño que te corresponda pagar.")
    f.append(tabla(["Situación", "¿Se puede descontar?", "Cómo defenderte o prepararte"], [
        ("Pintura pasada de color por el paso del tiempo", "En general no: es deterioro por tiempo y uso regular (art. 1210).", "Fotos del estado inicial y fecha de ingreso. Si el contrato pide repintar, leé la cláusula."),
        ("Agujeros grandes, manchas, roturas por mal uso", "Sí, el daño por uso irregular.", "Reparalo antes con presupuesto propio o acordá un monto por escrito."),
        ("Mantenimiento menor (lamparitas, canillas, sifones)", "Sí: a cargo del inquilino (art. 1207).", "Arreglalo antes de entregar."),
        ("Desperfectos que ya estaban", "No: tenés que poder probar el estado inicial.", "Inventario, fotos y mensajes anteriores."),
        ("Expensas, luz, gas o internet impagos", "Sí, si son tuyos y están impagos.", "Pagá todo antes y guardá los comprobantes."),
        ("Cargos sin factura ni presupuesto", "Discutible: pedí que lo justifiquen.", "Exigí presupuesto o factura por escrito.")], [48 * mm, 55 * mm, W - 2 * M - 103 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Pedí la liquidación por escrito</b>: concepto, monto y comprobante de cada descuento.", "<b>Aceptá lo que es justo</b> y discutí solo lo que no lo es: baja el conflicto y acelera el cobro.", "<b>No dejes llaves ni entregues la propiedad sin acta</b>: sin fecha de entrega probada, el propietario puede decir que seguís ocupándola."])
    f.append(consejo("PRUEBA, NO DISCUSIÓN", "Una foto con fecha del mismo ambiente al entrar y al salir es la prueba más simple para resolver una diferencia sobre el estado de la propiedad."))
    f.append(PageBreak())

    f += cap("4", "CUÁNTO TE CORRESPONDE", "Tres formas de devolución, tres resultados", "La cláusula del contrato cambia el número final.")
    f.append(tabla(["Cómo dice el contrato", "Qué te devuelven", "Ejemplo (depósito $ 400.000 con alquiler de $ 400.000 al entrar y $ 700.000 al salir)"], [
        ("Mismo monto entregado", "El nominal.", "$ 400.000"),
        ("Valor del último alquiler", "Tantos meses como depósito, a la cotización del último mes.", "$ 700.000"),
        ("Ajustado por un índice pactado", "El depósito multiplicado por el índice.", "$ 400.000 × índice (por ejemplo 1,60) = $ 640.000")], [48 * mm, 50 * mm, W - 2 * M - 98 * mm]))
    f.append(Spacer(1, 8))
    f.append(Barra("Ejemplo: si el contrato dice 'valor del último alquiler' (miles de $)", [("Nominal pagado", 400, CEL), ("Diferencia por actualización", 300, SELLO)], "$ mil"))
    f.append(P("En el ejemplo, la diferencia entre el nominal y el valor del último alquiler es de <b>$ 300.000</b>: el 75% del depósito. Por eso la cláusula importa más que cualquier otra cosa. Cargá tus números en la calculadora gratis: son solo ejemplos.", "nota"))
    f.append(H2("Intereses por demora"))
    f.append(P("Si el depósito se devuelve tarde, el art. 768 del Código dice que desde la mora se deben intereses, con la tasa que <b>acuerden las partes</b>, la que fijen leyes especiales o, en subsidio, las tasas del Banco Central. La mora corre sola cuando el contrato fija un plazo (art. 886); si no lo fija, tu <b>intimación</b> marca el plazo (art. 887: lo fija el juez a pedido de parte, y la intimación documentada ayuda)."))
    f.append(PageBreak())

    f += cap("5", "LA ENTREGA", "Inspección, acta y llaves", "El día de la entrega define todo lo que viene después.")
    f += E(["<b>Coordiná por escrito</b> la fecha, la hora y quién va a estar presente.", "<b>Recorrelo con el propietario o su representante</b>, ambiente por ambiente, con el inventario inicial en mano.", "<b>Anotá y fotografiá</b> cada observación, con el consenso de ambos si es posible.", "<b>Firmá un acta</b> con fecha y hora, las lecturas de medidores, la cantidad de llaves y las observaciones (anexo, carta 2).", "<b>Llevate una copia firmada</b> o sacá una foto nítida de todas las hojas.", "<b>Si no se presenta nadie</b>: dejá constancia fehaciente (carta documento) de que ofreciste entregar en tal fecha y hora, y resguardá las llaves en un lugar al que puedas acreditar acceso."])
    f.append(alerta("SIN ACTA, SIN PRUEBA", "Entregar las llaves sin dejar constancia de la fecha y del estado es el error que más complica el reclamo. Si el propietario se niega a firmar, dejá constancia con fotos fechadas, mensajes y, de ser posible, un testigo."))
    f.append(Tiles([("Acta", "firmada y|con fecha"), ("Fotos", "de cada|ambiente"), ("Libre deuda", "de servicios|y expensas"), ("Llaves", "contadas y|entregadas")]))
    f.append(PageBreak())

    f += cap("6", "SI NO TE LO DEVUELVEN", "La escalera del reclamo", "De lo más barato a lo más complejo: no te saltees escalones.")
    f.append(Flujo([("1", "Mensaje|escrito"), ("2", "Carta|documento"), ("3", "Mediación|previa"), ("4", "Juicio con|abogado")], CEL))
    f.append(Spacer(1, 10))
    f += E(["<b>Mensaje escrito</b> (mail o chat): recordá la fecha de entrega, el monto y el plazo; pedí fecha cierta de devolución. Guardá capturas.", "<b>Carta documento o medio fehaciente</b>: intimá a devolver en un plazo razonable (10 días corridos suele ser lo habitual) con el monto, la cláusula del contrato y los intereses (anexo, carta 3).", "<b>Mediación</b>: en muchas jurisdicciones es obligatoria antes de demandar. Consultá si corresponde en la tuya y si hay mediación gratuita.", "<b>Juicio</b>: si el monto lo justifica, un abogado evalúa el reclamo. Llevá el contrato, el acta, las fotos y la carta documento."])
    f.append(P("El plazo para reclamar es el general de 5 años del art. 2560 del Código (salvo que corresponda uno distinto): igualmente, <b>no esperes</b>, porque las pruebas y los testigos se pierden.", "nota"))
    f.append(consejo("EL PEOR ESCENARIO", "Si el monto es chico, el costo del juicio puede ser mayor que el depósito. Muchas veces alcanza con la carta documento y la mediación, porque al propietario le sale más barato acordar."))
    f.append(PageBreak())

    f += cap("7", "ERRORES FRECUENTES", "Los que más cuestan")
    f += L(["<b>No guardar el contrato</b> ni el recibo del depósito.", "<b>Entregar las llaves sin acta</b> ni fecha probada.", "<b>No sacar fotos</b> al entrar ni al salir.", "<b>Dejar de pagar el último alquiler</b> diciendo que 'se lo descuente del depósito': es un incumplimiento que te debilita.", "<b>Reclamar de palabra</b> y no por escrito.", "<b>Pagar un arreglo sin comprobante</b> o sin acuerdo previo.", "<b>No pedir el libre deuda</b> de expensas y servicios.", "<b>Aceptar un descuento sin pedir presupuesto</b> ni factura."])
    f.append(P("Para el propietario: devolver el depósito con una liquidación clara y comprobantes evita reclamos, intereses y costos de abogado. Retener sin justificar suele salir más caro.", "nota"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Cartas modelo", "Completá los datos entre corchetes y enviá por un medio que deje constancia.")
    f.append(H2("Carta 1: aviso de entrega y pedido de inspección"))
    f.append(P("[Ciudad], [fecha]. A [nombre del propietario/administrador]. Domicilio: [dirección]. Ref.: contrato de locación de [dirección de la propiedad]. <br/>Le comunico que entregaré el inmueble el [fecha] a las [hora]. Le solicito realizar una inspección conjunta ese día, con el inventario inicial a la vista, y acordar la devolución del depósito en garantía de $ [__] en un plazo de [__] días desde la entrega. Saludo atentamente. [Firma y aclaración]"))
    f.append(H2("Carta 2: acta de entrega"))
    f.append(P("En [ciudad], el [fecha] a las [hora], [inquilino], DNI [__], entrega a [propietario/representante], DNI [__], el inmueble de [dirección]. Se deja constancia de: llaves entregadas: [cantidad]; lecturas de medidores: luz [__], gas [__], agua [__]; estado general: [detalle]; observaciones de [inquilino]: [detalle]; observaciones de [propietario]: [detalle]; fotos adjuntas: [cantidad]. Ambas partes firman en prueba de conformidad con lo escrito. [Firmas y aclaraciones]"))
    f.append(H2("Carta 3: intimación de devolución del depósito"))
    f.append(P("[Ciudad], [fecha]. A [nombre]. Domicilio: [dirección]. <br/>Intimo a restituir en el plazo de [10] días corridos de recibida esta comunicación el depósito en garantía de $ [__], entregado el [fecha] en virtud del contrato de locación de [dirección], inmueble que fue devuelto el [fecha] en el estado en que lo recibí, salvo el deterioro por el uso y el paso del tiempo. La suma deberá actualizarse según la cláusula [__] del contrato e incluir los intereses desde [fecha]. Caso contrario, iniciaré las acciones que correspondan. [Firma y aclaración]"))
    f.append(H2("Carta 4: pedido de liquidación de descuentos"))
    f.append(P("[Ciudad], [fecha]. A [nombre]. Domicilio: [dirección]. <br/>Habiendo informado usted que descontará del depósito de $ [__] la suma de $ [__], le solicito que me remita, dentro de [5] días, el detalle de cada concepto con su comprobante (presupuesto, factura o recibo) y la fecha del arreglo. Dejo constancia de que el inmueble fue devuelto el [fecha], según acta de entrega que se adjunta. [Firma y aclaración]"))
    f.append(P("Son modelos orientativos. Adaptalos a tu contrato y, si hay un conflicto serio, consultá a un abogado.", "nota"))
    f.append(H2("Fuentes"))
    f += L(["Código Civil y Comercial de la Nación, texto actualizado en argentina.gob.ar: arts. 1196 (sustituido por art. 255 del DNU 70/2023), 1206, 1207, 1210, 1218, 1222, 1223, 768, 886, 887 y 2560 (sustituido por art. 34 de la Ley 27.799).", "No verificados: mediación prejudicial por jurisdicción, tasa del Banco Central aplicable y costo de la carta documento."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal. Las normas de locaciones cambiaron y pueden volver a cambiar; verificá su vigencia en argentina.gob.ar/normativa. Está prohibida su reventa o redistribución.", "nota"))
    return f
