"""Guía 'Mudanza sin estafas' (HUECOS.md #18). Verificado: ARCA (domicilio fiscal: Sistema Registral > Registro Único Tributario > Domicilios, F. 420/D, clave fiscal nivel 3, 10 días hábiles, RG 5809/2026 según notas).
NO verificado: trámite nacional del DNI (varía por jurisdicción), costos y turnos, precios de fletes (la calculadora usa valores editables)."""
from guias_lib import *

META = dict(nombre="Mudanza sin estafas", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Mudanza", "sin estafas"], sub=["Presupuestos, inventario, cambio de domicilio y bajas de servicios:", "todo en orden antes, durante y después del camión."],
            sello="M³", sello2="MUDANZA", cabecera="MUDANZA SIN ESTAFAS",
            pie="Información general. Los precios y trámites cambian: verificá en cada organismo.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien se muda (o ayuda a alguien) y no quiere perder plata, muebles ni trámites en el camino.")
    f.append(P("Una mudanza sale mal por tres motivos: <b>presupuesto vago</b>, <b>nada anotado</b> y <b>trámites olvidados</b>. Esta guía los cubre con checklists, un inventario por caja y la lista de cambios de domicilio (DNI, ARCA, ANSES, bancos y servicios). Hay una planilla de inventario y de bajas/altas en el último capítulo."))
    f.append(alerta("DESCONFIÁ DE LO MUY BARATO", "No hay tarifa oficial de fletes y mudanzas: el mercado es informal y los precios varían mucho por zona y día. Un precio muy por debajo del resto, sin nombre de empresa ni presupuesto escrito, es la señal más común de problemas."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Flete o mudanza completa", "Qué contratás y qué incluye cada opción."),
        ("2. Presupuestos que se pueden comparar", "Qué pedir por escrito y cómo comparar."),
        ("3. Señales de estafa", "Antes de pagar y el día de la carga."),
        ("4. Inventario y embalaje", "Cuánto embalaje necesitás y cómo etiquetar."),
        ("5. El día de la mudanza", "Carga, descarga y conformidad."),
        ("6. Si algo se rompe o se pierde", "Reclamo ordenado y a quién acudir."),
        ("7. Cambio de domicilio", "DNI, ARCA, ANSES, bancos, servicios y vehículo."),
        ("8. Cronograma de 30 días", "Semana por semana."),
        ("Anexo", "Planillas y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA CALCULADORA DE VOLUMEN", f"Estimá los m³ y el costo con tus muebles: {BASE_URL}/mudanza-calculadora-metros-cubicos"))
    f.append(PageBreak())

    f += cap("1", "QUÉ CONTRATÁS", "Flete o mudanza completa", "Comparar precios sin distinguir esto es la primera trampa.")
    f.append(tabla(["", "Flete", "Mudanza completa"], [
        ("Incluye", "Camioneta o camión y chofer. A veces uno o dos ayudantes.", "Camión, cuadrilla, embalaje, desarmado y armado de muebles."),
        ("Conviene si", "Poco volumen, pocos pisos, vos embalás.", "Casa entera, muebles grandes, tiempo escaso."),
        ("Riesgo", "Sin cuadrilla, los golpes y los tiempos son tuyos.", "Más caro; el daño es responsabilidad de la empresa."),
        ("Se cobra", "Por hora, por viaje o por distancia.", "Por volumen, distancia, pisos y servicios.")],
        [26 * mm, 70 * mm, W - 2 * M - 96 * mm]))
    f.append(Spacer(1, 8))
    f.append(Tiles([("m³", "volumen de lo|que movés"), ("pisos", "escaleras y|ascensor"), ("km", "distancia|entre domicilios"), ("horas", "carga, viaje|y descarga")]))
    f.append(Spacer(1, 10))
    f.append(P("Estos cuatro datos explican casi todo el precio. Antes de pedir presupuestos, anotá los tuyos: sin ellos cada empresa estima distinto y no podés comparar."))
    f.append(PageBreak())

    f += cap("2", "PRESUPUESTOS", "Qué pedir por escrito", "Comparar solo se puede si todos cotizan lo mismo.")
    f.append(Checklist(["Pedí <b>al menos tres presupuestos</b> con la misma lista de muebles y cajas.", "Que figure <b>nombre de la empresa o del dueño, teléfono, dirección y CUIT</b> si es una empresa.", "Qué <b>incluye</b>: camión, ayudantes, cantidad de horas, embalaje, desarmado y armado.", "Qué <b>no incluye</b>: pisos sin ascensor, estacionamiento, espera, materiales.", "<b>Precio total</b> o tarifa por hora con tope de horas, y forma de pago.", "Hora de <b>llegada</b> y qué pasa si llegan tarde o si el trabajo se alarga.", "Si tienen <b>seguro</b> y hasta qué valor cubre lo que se rompa o se pierda.", "Cómo se factura (<b>factura o recibo</b>) y qué pasa si cancelás."], "PEDIR POR ESCRITO"))
    f.append(Spacer(1, 8))
    f.append(P("Guardá los mensajes (WhatsApp, mail) donde figura el precio y lo acordado: son tu comprobante si después cambian las condiciones. Un acuerdo \"de palabra\" es difícil de probar."))
    f.append(consejo("CONFIRMÁ EL EDIFICIO", "Pedí por escrito al consorcio o al administrador el horario permitido, el uso del ascensor de servicio y dónde puede estacionar el camión. Evita multas y esperas que se cobran por hora."))
    f.append(PageBreak())

    f += cap("3", "SEÑALES DE ESTAFA", "Qué mirar antes de pagar y durante la carga", "Casi todas se ven antes de que suba la primera caja.")
    f.append(alerta("NO PAGUES TODO POR ADELANTADO", "Una seña chica para reservar fecha es normal. Pagar el total antes de la carga te deja sin margen si no se presentan o si pasa algo con tus cosas. Pagá el saldo cuando termina la descarga y revisaste todo."))
    f += L(["<b>Sin nombre ni dirección</b>: solo un número de WhatsApp y una foto de un camión.", "<b>Precio muy bajo</b> respecto de otros presupuestos comparables, o que cambia el día de la carga.", "<b>Piden el 100% antes</b> o un pago a una cuenta de un tercero sin relación con la empresa.", "<b>No dejan presupuesto escrito</b> ni quieren firmar el inventario.", "<b>Llegan con menos gente o con otro camión</b> que el acordado.", "<b>Aumentan el precio ya cargado</b> el camión (te retienen las cosas hasta que pagues más).", "<b>Subcontratan sin avisar</b>: no sabés a quién le entregaste tus cosas."])
    f.append(consejo("SI TE RETIENEN LAS COSAS", "No discutas a solas en la calle. Si sentís presión, pedí que quede asentado lo reclamado y llamá a la policía si hay amenazas o si no te entregan tus bienes. Documentá todo con fotos y mensajes."))
    f.append(PageBreak())

    f += cap("4", "INVENTARIO Y EMBALAJE", "Anotá lo que se mueve", "Sin lista no hay reclamo posible.")
    f.append(P("Hacé un inventario <b>por ambiente</b> antes de embalar. Para cada ítem: descripción, estado (con fotos de los muebles de valor y de los golpes que ya existen), caja o bulto, y si es frágil. Es la base de cualquier reclamo y también te sirve para decidir qué no llevar."))
    f.append(tabla(["Tipo de caja", "Para qué sirve", "Peso máx. recomendado"], [
        ("Chica", "Libros, vajilla, objetos pesados", "Hasta unos 15 kg"),
        ("Mediana", "Ropa de cama, cocina, juguetes", "Hasta unos 10 kg"),
        ("Grande", "Almohadones, ropa de abrigo, livianos", "Hasta unos 8 kg"),
        ("Armario/colgador", "Ropa colgada", "Según el modelo")], [32 * mm, 80 * mm, W - 2 * M - 112 * mm]))
    f.append(P("Los pesos son una referencia práctica de uso, no una norma: lo importante es que la caja se pueda levantar sin romperse.", "nota"))
    f += L(["<b>Etiquetá cada caja</b> con el ambiente de destino y un número del inventario; no solo el contenido.", "<b>Frágil</b>: envolvé cada pieza, relleno en los huecos, cinta en el fondo y en la tapa.", "<b>Llevá vos</b> documentos, dinero, joyas, medicamentos, cargadores y llaves.", "<b>Desarmá</b> muebles con tiempo y guardá tornillos en una bolsa pegada al mueble.", "<b>Vaciá y descongelá</b> la heladera un día antes; los electrodomésticos grandes viajan secos.", "<b>Sacá fotos</b> de las conexiones antes de desenchufar la tele, el router, el equipo de música."])
    f.append(PageBreak())

    f += cap("5", "EL DÍA DE LA MUDANZA", "Carga, viaje y descarga", "Estar presente es la mejor protección.")
    f.append(Flujo([("Antes|de cargar", "Fotos y|inventario firmado"), ("Carga", "Verificar que|todo sube"), ("Viaje", "Datos del|chofer y patente"), ("Descarga", "Cada caja|contra la lista"), ("Conformidad", "Firmar solo|si está todo")], CEL))
    f.append(Spacer(1, 10))
    f += E(["<b>Recibí a la cuadrilla</b> con el presupuesto en mano y confirmá que son los acordados y el camión previsto.", "<b>Anotá la patente y los datos del chofer</b> y sacá una foto del camión.", "<b>Revisá los muebles</b> antes de cargar y marcá cualquier daño previo con fotos.", "<b>Controlá que sube cada bulto</b> contra el inventario; que alguien de tu confianza haga lo mismo en destino.", "<b>No dejes sola la casa vieja</b> hasta que el camión salga y la revisaste vacía.", "<b>En la descarga</b>, abrí y revisá lo frágil; sacá fotos de lo que llega dañado antes de que se vayan.", "<b>Firmá la conformidad solo si está todo</b>; si falta o se rompió algo, anotalo en el comprobante antes de firmar y pedí una copia.", "<b>Pagá el saldo</b> recién cuando terminaste de revisar y tenés el recibo."])
    f.append(consejo("LA REGLA DE ORO", "Lo que no se anota en el momento es casi imposible de reclamar después. Una frase escrita en el comprobante (\"falta caja 12, mesa de luz con golpe\") vale más que una discusión."))
    f.append(PageBreak())

    f += cap("6", "SI ALGO SE ROMPE", "Reclamo ordenado", "Primero a la empresa, por escrito; después a los organismos.")
    f += E(["<b>Reunís las pruebas</b>: presupuesto, inventario, fotos de antes y después, comprobante de conformidad con la observación, mensajes y pagos.", "<b>Mandás un reclamo por escrito</b> a la empresa (mail o carta) con el detalle de lo dañado o faltante, el valor y lo que pedís (reposición, reparación o pago).", "<b>Esperás una respuesta razonable</b> (por ejemplo 5 a 10 días hábiles) y guardás la constancia del envío.", "<b>Si no responden</b>, hacés el reclamo ante la Dirección de Defensa del Consumidor de tu provincia o municipio, o ante el sistema nacional de conciliación de consumo (COPREC), según corresponda.", "<b>Si hubo estafa o retención de bienes</b>, hacé la denuncia en la comisaría o en el Ministerio Público Fiscal con las pruebas."])
    f.append(P("Las relaciones de consumo con empresas de mudanzas se rigen por la Ley 24.240 de Defensa del Consumidor; con un particular que hace fletes sin estructura formal la situación es más débil, por eso importa tener todo por escrito. Para un modelo de carta, mirá el generador de reclamo de la web.", "nota"))
    f.append(consejo("GENERADOR DE RECLAMO", f"Armá la carta en minutos: {BASE_URL}/generador-reclamo-consumidor"))
    f.append(PageBreak())

    f += cap("7", "CAMBIO DE DOMICILIO", "Qué avisar y dónde", "Hacelo en las primeras semanas: es lo que más se olvida.")
    f.append(tabla(["Dónde", "Qué hacer", "Nota"], [
        ("DNI (RENAPER)", "Actualizar el domicilio en el documento.", "El trámite varía según la jurisdicción; consultá en argentina.gob.ar o en el Registro Civil de tu provincia. En algunos casos hay costo y turno."),
        ("Padrón electoral", "Se actualiza con el cambio de domicilio del DNI.", "Confirmá en la web de la Cámara Nacional Electoral."),
        ("ARCA", "Domicilio fiscal: Sistema Registral, Registro Único Tributario, Domicilios, Modificar.", "Clave Fiscal nivel 3. Formulario 420/D. Plazo informado: 10 días hábiles desde el cambio."),
        ("Monotributo", "Domicilio de la actividad si cambia el local.", "Se actualiza en el mismo sistema."),
        ("ANSES", "Mi ANSES: datos personales.", "Si cobrás AUH, jubilación u otro beneficio, actualizá el domicilio."),
        ("Bancos y tarjetas", "Cambiar domicilio en la home banking o sucursal.", "Evita que el resumen llegue al domicilio viejo."),
        ("Obra social / prepaga", "Cambio de domicilio en la web o app.", "A veces cambia la cartilla o la cuota por zona."),
        ("Registro automotor", "Cambiar el domicilio en el título y la cédula.", "El trámite depende del registro; averiguá en el seccional."),
        ("Trabajo", "Avisar a RR. HH.", "Necesario para recibos y libreta."),
        ("Colegio / servicios", "Actualizar datos y transporte.", "Chequeá cobertura y ruta.")],
        [32 * mm, 60 * mm, W - 2 * M - 92 * mm]))
    f.append(P("Los nombres de los menús pueden cambiar. Verificá los pasos vigentes en cada organismo antes de empezar.", "nota"))
    f.append(H2("Bajas y altas de servicios"))
    f += L(["<b>Luz, gas, agua</b>: anotá la lectura final del medidor y sacale una foto; pedí la baja o el traspaso con fecha.", "<b>Internet y cable</b>: averiguá si podés trasladar el servicio; a veces cambia el plan por zona.", "<b>Expensas y ABL/ municipales</b>: pedí un libre deuda si corresponde.", "<b>Seguro del hogar</b>: actualizá la dirección y el valor asegurado.", "<b>Correo / Mercado Libre / Apps</b>: cambiá la dirección de entrega."])
    f.append(PageBreak())

    f += cap("8", "CRONOGRAMA", "30 días antes, semana por semana", "Una lista corta que no te deja olvidar lo importante.")
    f.append(Checklist(["<b>Semana -4</b>: definir fecha, decidir flete o mudanza completa, pedir tres presupuestos por escrito.", "<b>Semana -4</b>: confirmar con el edificio, y avisar al propietario o inquilino que entrega.", "<b>Semana -3</b>: elegir qué vender, donar o tirar; empezar a embalar lo que no usás.", "<b>Semana -3</b>: avisar a bancos, trabajo y obra social del cambio de domicilio.", "<b>Semana -2</b>: contratar y pagar la seña; conseguir cajas y materiales.", "<b>Semana -2</b>: pedir la baja o traspaso de servicios con fecha.", "<b>Semana -1</b>: terminar de embalar, hacer el inventario y fotos de los muebles de valor.", "<b>Día -1</b>: vaciar la heladera, preparar la caja de lo esencial y confirmar hora con la empresa.", "<b>Día 0</b>: seguir el capítulo 5 y anotar lecturas de medidores en ambas casas.", "<b>Semana +1</b>: ARCA, DNI y ANSES; desembalar por prioridad.", "<b>Semana +2</b>: revisar que nada falte y reclamar por escrito si corresponde."], "CRONOGRAMA"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Planillas y fuentes")
    f.append(H2("Planilla de inventario por ambiente"))
    f.append(tabla(["N°", "Ambiente", "Descripción", "Estado / daños previos", "Caja o bulto"], [
        ("1", "Living", "", "", ""), ("2", "Cocina", "", "", ""), ("3", "Dormitorio", "", "", ""), ("4", "Baño", "", "", ""), ("5", "Otro", "", "", "")],
        [12 * mm, 28 * mm, 54 * mm, 50 * mm, W - 2 * M - 144 * mm]))
    f.append(H2("Planilla de bajas y altas"))
    f.append(tabla(["Servicio", "Titular / N° de cliente", "Lectura final", "Fecha de baja", "Hecho"], [
        ("Luz", "", "", "", "[  ]"), ("Gas", "", "", "", "[  ]"), ("Agua", "", "", "", "[  ]"), ("Internet", "", "", "", "[  ]"), ("Seguro", "", "", "", "[  ]")],
        [30 * mm, 50 * mm, 30 * mm, 30 * mm, W - 2 * M - 140 * mm]))
    f.append(H2("Fuentes"))
    f += L(["ARCA: modificación del domicilio fiscal (arca.gob.ar/regimenGeneral/modificacion/domicilio-fiscal.asp), RG 5809/2026 según notas de prensa.", "Ley 24.240 de Defensa del Consumidor (Infoleg).", "Guías públicas de mudanzas (roomix.ai, Expats Argentina) para el cronograma general; los precios varían y no se incluyen."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal. Los trámites, los costos y los plazos cambian según la jurisdicción: verificá en cada organismo. Está prohibida su reventa o redistribución.", "nota"))
    return f
