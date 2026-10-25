"""Guía 'Alquilar sin inmobiliaria' (HUECOS.md #12). Normativa verificada en Infoleg (texto del DNU 70/2023): art. 249 deroga la Ley 27.551; art. 250-251 (moneda, arts. 765-766 CCyC), 255 (art. 1196), 256 (art. 1198: plazo libre; sin plazo, vivienda 2 años), 257 (art. 1199: moneda y ajuste libres), 258-259 y 263 (derogaciones de arts. 1202, 1204, 1204 bis, 1221 bis), 262 (art. 1221: resolución anticipada con 10%)."""
from guias_lib import *

META = dict(nombre="Alquilar sin inmobiliaria", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Alquilar sin", "inmobiliaria"], sub=["Contrato, garantía, ajuste y depósito paso a paso,", "para propietarios e inquilinos. Con modelos en anexo."],
            sello="DNU 70", sello2="REGLAS HOY", cabecera="ALQUILAR SIN INMOBILIARIA",
            pie="Información general. No reemplaza a un abogado ni a un escribano.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien alquila o da en alquiler una vivienda sin intermediarios y quiere hacerlo con papeles claros.")
    f.append(P("Alquilar directo ahorra la comisión, pero te deja solo con las decisiones que una inmobiliaria suele tomar: qué contrato firmar, cómo pedir garantía, cómo ajustar el precio y cómo cerrar. Esta guía las ordena. Está escrita para los dos lados del mostrador: cada capítulo dice qué le conviene mirar al propietario y qué al inquilino."))
    f.append(Tiles([("Plazo libre", "lo pactan|las partes"), ("Moneda libre", "pesos o|dólares"), ("Ajuste libre", "índice o fórmula|que pacten"), ("10%", "resolución anticipada|sobre el saldo")]))
    f.append(Spacer(1, 10))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Las reglas hoy", "Qué cambió con el DNU 70/2023 y qué quedó."),
        ("2. Antes de firmar", "Qué verificar de la propiedad y de las personas."),
        ("3. El contrato", "Las cláusulas que no pueden faltar, una por una."),
        ("4. Garantías y depósito", "Opciones para el propietario y para el inquilino."),
        ("5. Ajuste del alquiler", "Cómo elegir un índice y evitar peleas."),
        ("6. Durante el contrato", "Recibos, arreglos, expensas y salida anticipada."),
        ("7. Al terminar", "Entrega, inventario y devolución del depósito."),
        ("8. Estafas y errores caros", "Lo que más se repite."),
        ("Anexo", "Modelos: recibo, acta de entrega e inventario, aviso de ajuste.")], [48 * mm, W - 2 * M - 48 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("Base normativa: el texto del DNU 70/2023 publicado en Infoleg y el Código Civil y Comercial. Un contrato firmado antes de la derogación sigue su régimen hasta que venza: si es tu caso, revisá qué ley lo rige.", "nota"))
    f.append(PageBreak())

    f += cap("1", "LAS REGLAS HOY", "Qué cambió y qué rige ahora", "Desde el DNU 70/2023, casi todo se pacta entre las partes.")
    f.append(P("El DNU 70/2023 <b>derogó la Ley de Alquileres 27.551</b> (art. 249) y reescribió artículos del Código Civil y Comercial. Para contratos nuevos, estas son las reglas que podés usar:"))
    f.append(tabla(["Tema", "Regla actual", "Artículo"], [
        ("Plazo", "El que fijen las partes, para cualquier destino. Si no se fija plazo en una vivienda permanente, se aplican 2 años.", "CCyC 1198 (DNU art. 256)"),
        ("Moneda", "El alquiler puede pactarse en pesos o en moneda extranjera, y se paga en la moneda pactada.", "CCyC 765, 766 y 1199 (DNU art. 250, 251 y 257)"),
        ("Ajuste", "Lo pactan las partes con un índice público o privado.", "CCyC 1199 (DNU art. 257)"),
        ("Depósito / fianza", "Las partes fijan libremente cantidad y moneda. El pago periódico no puede ser menor a mensual.", "CCyC 1196 (DNU art. 255)"),
        ("Salida anticipada", "El inquilino puede resolver en cualquier momento pagando el 10% del saldo del alquiler por el plazo que falta.", "CCyC 1221 (DNU art. 262)")],
        [26 * mm, 100 * mm, W - 2 * M - 126 * mm]))
    f.append(Spacer(1, 8))
    f.append(Barra("Cuánto se paga al firmar (ejemplo con alquiler de $ 600.000)", [("Primer mes", 600, TINTA), ("Depósito de un mes", 600, CEL)], unidad="$ miles"))
    f.append(P("El depósito de un mes es un ejemplo habitual, no una obligación: la ley actual deja libre la cantidad. Sumá aparte el sellado si tu provincia lo cobra y los gastos de certificaciones.", "nota"))
    f.append(alerta("LA LIBERTAD CUESTA SI NO LO ESCRIBÍS", "Sin la ley anterior que fijaba plazo, ajuste y topes, lo que no esté escrito en el contrato lo decide el Código Civil y Comercial o un juez. Cada cláusula del capítulo 3 existe para evitar eso."))
    f.append(P("Los medios y estudios jurídicos informan que la Ley 27.742 (Ley Bases) consolidó estas reglas; confirmá en Infoleg si hay una modificación posterior antes de firmar.", "nota"))
    f.append(PageBreak())

    f += cap("2", "ANTES DE FIRMAR", "Qué verificar de la propiedad y de las personas")
    f.append(Flujo([("Visita", "Ver la propiedad|y su estado"), ("Verificar", "Titularidad,|deudas, identidad"), ("Acordar", "Precio, plazo,|ajuste y garantía"), ("Firmar", "Contrato e|inventario"), ("Entregar", "Llaves y acta|de entrega")]))
    f.append(Spacer(1, 10))
    f.append(Checklist(["<b>Si alquilás (inquilino)</b>: pedí el DNI del propietario y un comprobante de que es titular o está autorizado (escritura, boleto o poder).", "<b>Si alquilás (inquilino)</b>: pedí los comprobantes al día de impuestos, tasas y expensas y confirmá que no haya deudas que te lleguen a vos.", "<b>Si alquilás (inquilino)</b>: visitá la propiedad, probá canillas, luz y gas, y sacá fotos fechadas.", "<b>Si das en alquiler (propietario)</b>: pedí DNI, recibos de ingresos y referencias del inquilino.", "<b>Si das en alquiler (propietario)</b>: verificá la garantía antes de entregar las llaves.", "<b>Los dos</b>: acordá por escrito qué se incluye (muebles, cochera, servicios).", "<b>Los dos</b>: no pagues ni entregues llaves por transferencia a alguien que no pudiste ver en persona."], "CHECKLIST DE VERIFICACIÓN"))
    f.append(Spacer(1, 8))
    f.append(consejo("SI NO PODÉS VERIFICAR, NO SEÑES", "Una seña es dinero que puede costar mucho recuperar. Si algo de la titularidad o la identidad no cierra, esperá. Un alquiler legítimo aguanta un día más de chequeo."))
    f.append(PageBreak())

    f += cap("3", "EL CONTRATO", "Las cláusulas que no pueden faltar")
    f.append(tabla(["Cláusula", "Qué tiene que decir", "Error típico"], [
        ("Partes y propiedad", "Nombres, DNI, domicilio real y dirección completa del inmueble.", "Falta el DNI o la dirección exacta."),
        ("Destino", "Vivienda permanente, temporaria o con otro uso.", "No aclarar si se puede trabajar desde la casa."),
        ("Plazo", "Fecha de inicio y de fin. Si no se pacta, en vivienda permanente rigen 2 años.", "Dejar el plazo en blanco."),
        ("Precio y moneda", "Monto, moneda, día y forma de pago, y lugar o cuenta.", "No decir la moneda ni el medio."),
        ("Ajuste", "Índice, frecuencia y fecha de aplicación (capítulo 5).", "Escribir \"se ajustará\" sin decir cómo."),
        ("Depósito", "Cantidad, moneda, qué cubre y cuándo se devuelve.", "No fijar el plazo de devolución."),
        ("Garantía", "Quién es el garante o qué seguro se contrata (capítulo 4).", "Aceptar garantía sin verificar."),
        ("Gastos", "Quién paga expensas, servicios, tasas e impuestos.", "No separar ordinarias de extraordinarias."),
        ("Estado y arreglos", "Inventario y quién hace qué tipo de arreglos.", "Sin inventario ni fotos."),
        ("Resolución anticipada", "Cómo puede salir el inquilino y qué paga (10% del saldo).", "No mencionarla."),
        ("Mora y domicilios", "Qué pasa si no se paga y dónde se hacen las notificaciones.", "Sin domicilio para notificar."),
        ("Firma", "Firmas en todas las hojas y dos ejemplares.", "Un solo ejemplar.")],
        [34 * mm, 78 * mm, W - 2 * M - 112 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("El contrato de locación se hace por escrito. No exige escribano ni sellado notarial, pero cada provincia puede cobrar <b>impuesto de sellos</b> sobre el contrato: averiguá cómo funciona en la tuya antes de firmar y quién lo paga según lo que pactes. En la web hay modelos de contrato editables en Word (Pack Contratos de Alquiler).", "nota"))
    f.append(PageBreak())

    f += cap("4", "GARANTÍAS Y DEPÓSITO", "Cómo cubrirte, desde cada lado")
    f.append(tabla(["Opción", "Cómo funciona", "Para quién conviene"], [
        ("Depósito en garantía", "Un monto que queda en poder del propietario y se devuelve al final si no hay daños ni deudas.", "Cualquiera: es lo más simple. Acordá la moneda."),
        ("Garante con propiedad", "Un tercero responde con un inmueble propio.", "Propietario que busca respaldo fuerte; el inquilino necesita a alguien con propiedad."),
        ("Garante con recibos de sueldo", "Un tercero con ingresos demostrables.", "Casos con ingresos estables; verificá antes."),
        ("Seguro de caución", "Una aseguradora emite una póliza que cubre al propietario; el inquilino paga una prima.", "Inquilino sin garante propio; el propietario debe aceptarlo."),
        ("Aval bancario / otras", "Garantía de una entidad financiera.", "Montos altos o inquilinos corporativos.")],
        [38 * mm, 74 * mm, W - 2 * M - 112 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Verificá siempre al garante</b>: DNI, domicilio, titularidad de la propiedad y que el bien no tenga inhibiciones ni embargos (se consulta con un informe de dominio).", "<b>Escribí qué cubre la garantía</b>: alquileres, expensas, servicios, daños y plazo de la fianza.", "<b>Dejá constancia del depósito</b> con un recibo que diga monto, moneda y condiciones de devolución.", "<b>El depósito no es el último mes</b>, salvo que lo pacten: aclaralo para evitar discusiones."])
    f.append(consejo("PARA EL INQUILINO", "Si no tenés garante, preguntá por seguro de caución antes de rechazar un departamento: cada aseguradora tiene sus requisitos y costos, y el propietario tiene que aceptarlo."))
    f.append(PageBreak())

    f += cap("5", "AJUSTE DEL ALQUILER", "Cómo elegir un índice y escribirlo bien", "Es la cláusula que más pelea genera y la que más conviene definir con números.")
    f.append(P("Hoy las partes pactan el ajuste libremente, con un índice público o privado. Lo importante es que <b>se pueda calcular sin discutir</b>."))
    f.append(tabla(["Opción", "Cómo funciona", "Qué mirar"], [
        ("IPC (INDEC)", "El alquiler sube lo que subió el índice de precios del período.", "Fecha de publicación del índice y qué meses se toman."),
        ("Índice propio del contrato (ICL)", "El índice que publica el Banco Central.", "Que siga publicándose y la fecha de referencia."),
        ("Porcentaje fijo", "Un aumento fijo cada tantos meses (por ejemplo, 20% cada 3 meses).", "Que sea realista para ambos."),
        ("Pesos + dólar", "Alquiler en dólares o atado a su cotización.", "Qué cotización y qué día se toma.")],
        [40 * mm, 72 * mm, W - 2 * M - 112 * mm]))
    f.append(Spacer(1, 8))
    f += E(["Elegí <b>un solo índice</b> y escribilo con nombre y fuente.", "Fijá la <b>frecuencia</b>: cada cuántos meses se ajusta.", "Escribí <b>la fecha de aplicación</b> y cómo se calcula: período de meses que se toman.", "Acordá <b>cómo se avisa</b> el nuevo valor: por escrito, con el cálculo.", "Previsto: si el índice deja de publicarse, qué lo reemplaza."])
    f.append(Spacer(1, 6))
    f.append(consejo("CALCULALO GRATIS", "En la web tenés una calculadora de aumento de alquiler por IPC con datos oficiales del INDEC: kit-monotributo.fernandezfrancowork.workers.dev/aumento-alquiler"))
    f.append(PageBreak())

    f += cap("6", "DURANTE EL CONTRATO", "Pagos, arreglos y salida anticipada")
    f += L(["<b>Recibos</b>: el propietario entrega recibo por cada pago. Guardalos todos: son la prueba de que estás al día.", "<b>Arreglos urgentes</b>: si algo se rompe y es urgente, avisá por escrito y por una vía que deje constancia. Acordá antes quién paga cada tipo de arreglo.", "<b>Expensas y servicios</b>: pedí copia de las liquidaciones; cada uno paga lo que pactó.", "<b>Cambios en la propiedad</b>: toda obra o cambio se acuerda por escrito.", "<b>Subalquiler</b>: solo con autorización por escrito del propietario."])
    f.append(H2("Si el inquilino quiere irse antes"))
    f.append(P("Según el texto del DNU 70/2023, el locatario puede resolver el contrato <b>en cualquier momento</b> abonando el equivalente al <b>10% del saldo del alquiler</b> por el plazo que falta. Ejemplo: alquiler de $ 600.000 por mes, quedan 10 meses: saldo $ 6.000.000, indemnización $ 600.000. Avisá por escrito y dejá la fecha de entrega de llaves clara."))
    f.append(H2("Si el inquilino no paga"))
    f += E(["Reclamá por escrito (carta documento o notificación fehaciente) y dale un plazo razonable.", "Dejá constancia de la deuda y de cada pago parcial.", "Si no se resuelve, consultá con un abogado: el desalojo es un trámite judicial."])
    f.append(alerta("NO CAMBIES LA CERRADURA", "Ningún propietario puede sacar al inquilino por la fuerza ni cortar servicios para presionarlo. Eso puede generar responsabilidad civil y penal."))
    f.append(PageBreak())

    f += cap("7", "AL TERMINAR", "Entrega, inventario y devolución del depósito")
    f.append(Checklist(["Fijá un día y hora para la entrega con los dos presentes.", "Recorré la propiedad con el inventario inicial y compará estado, mobiliario y artefactos.", "Sacá fotos fechadas de cada ambiente y de los medidores.", "Anotá las lecturas de luz, gas y agua en el acta.", "Pedí los comprobantes de que los servicios y las expensas están pagos.", "Firmen el acta de devolución de llaves y devuelvan el depósito en el plazo pactado.", "Si hay daños, que se detallen con fotos y un presupuesto, y se descuenten del depósito."], "CHECKLIST DE ENTREGA"))
    f.append(Spacer(1, 8))
    f.append(P("El desgaste normal por el uso no se descuenta del depósito: solo los daños que van más allá. Escribir esa diferencia en el contrato evita la mayor causa de peleas al final."))
    f.append(PageBreak())

    f += cap("8", "ESTAFAS Y ERRORES CAROS", "Lo que más se repite")
    f.append(tabla(["Señal o error", "Qué cuesta", "Cómo evitarlo"], [
        ("Pedirte seña antes de ver la propiedad", "Perder la seña si es falso.", "Visitá y verificá antes de señar."),
        ("Precio demasiado bajo o apuro", "Una estafa clásica.", "Desconfiá: el mercado se compara en minutos."),
        ("Contrato sin ajuste definido", "Peleas al primer aumento.", "Cláusula de ajuste con número."),
        ("No hacer inventario", "Discusión por el depósito.", "Inventario y fotos fechadas el día de entrega."),
        ("Garante sin verificar", "Una garantía que no cubre nada.", "Informe de dominio y DNI."),
        ("Pagos sin recibo", "No podés probar que pagaste.", "Pedir y guardar el recibo siempre."),
        ("Firmar en una hoja sola", "Cambio de hojas.", "Firmar todas las hojas.")],
        [58 * mm, 46 * mm, W - 2 * M - 104 * mm]))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Modelos para adaptar", "Textos de partida: completalos y adaptalos a tu caso. Los modelos completos en Word están en el Pack Contratos de Alquiler de la web.")
    f.append(H2("Modelo 1: recibo de alquiler"))
    f.append(P("En la ciudad de ............., a los .... días del mes de ............. de 20...., recibí de ............. (DNI ..........) la suma de $ ............. (pesos .............) en concepto de alquiler del mes de ............. del inmueble sito en ............., conforme al contrato de locación de fecha ............. . Firma y aclaración del locador: .............", "nota"))
    f.append(H2("Modelo 2: acta de entrega e inventario"))
    f.append(tabla(["Ambiente / elemento", "Estado", "Observaciones", "Foto Nº"], [("Living / comedor", "", "", ""), ("Cocina y artefactos", "", "", ""), ("Dormitorios", "", "", ""), ("Baño", "", "", ""), ("Instalación eléctrica y gas", "", "", ""), ("Lecturas de medidores", "", "", "")], [50 * mm, 28 * mm, W - 2 * M - 108 * mm, 30 * mm]))
    f.append(Spacer(1, 6))
    f.append(H2("Modelo 3: aviso de ajuste"))
    f.append(P("Por la presente comunico que, de acuerdo con la cláusula ... del contrato de locación de fecha ............., a partir del ............. el alquiler pasa a ser de $ ............., según el índice ............. del período ............. (variación: ....%). Se adjunta el cálculo. Firma: .............", "nota"))
    f.append(H2("Fuentes"))
    f += L(["Infoleg: texto del DNU 70/2023, arts. 249 a 263 (derogación de la Ley 27.551 y nuevos arts. 765, 766, 1196, 1198, 1199 y 1221 del CCyC).", "Código Civil y Comercial de la Nación, Libro Tercero, Título IV, Capítulo 4 (locación)."])
    f.append(Spacer(1, 6))
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal ni reemplaza a un abogado o escribano. Las normas pueden cambiar y cada provincia tiene reglas propias (por ejemplo, de sellados). Los modelos son orientativos. Confirmá los datos vigentes antes de firmar. Está prohibida su reventa o redistribución.", "nota"))
    return f
