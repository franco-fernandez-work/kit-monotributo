"""Guía 'Comprar afuera sin sorpresas' (HUECOS.md #10). Normativa: RG ARCA 5883/2026 (BO 29/07/2026, vigente 30/07/2026) que modifica la RG 5608/2024; Decreto 1065/2024; página 'Régimen de Courier' de ARCA (06/10/2026)."""
from guias_lib import *

META = dict(nombre="Comprar afuera sin sorpresas", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Comprar afuera", "sin sorpresas"], sub=["Courier, franquicia de USD 400, impuestos y qué hacer", "si el paquete queda retenido. Con ejemplos en pesos."],
            sello="USD 400", sello2="FRANQUICIA", cabecera="COMPRAR AFUERA SIN SORPRESAS",
            pie="Información general. No reemplaza a un despachante ni a la información oficial de ARCA.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien compra en Temu, Shein, Amazon, AliExpress o tiendas del exterior y quiere saber el costo final antes de apretar \"comprar\".")
    f.append(P("Comprar afuera sale barato <b>solo si sabés el costo final</b>: precio + envío + impuestos + cómo pagás. Desde el 30 de julio de 2026 cambiaron los topes del courier, y mucha gente sigue guiándose por reglas viejas (los USD 50 y las 12 compras al año). Esta guía junta lo vigente, lo explica con ejemplos y te da un método para no llevarte sorpresas en la puerta."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Las reglas hoy", "Topes de valor, peso, unidades y cantidad de envíos por año."),
        ("2. Qué se paga", "IVA, derechos y tasa: cuándo aplican y ejemplos con cuentas."),
        ("3. Costo final", "El método de 5 pasos para calcularlo antes de comprar."),
        ("4. Seguir tu envío", "Cómo ver tu cupo y tus envíos en ARCA."),
        ("5. Si el paquete se retiene", "Qué significa, qué hacer y qué no hacer."),
        ("6. Pagar y reclamar", "Tarjeta, percepciones, contracargo y devoluciones."),
        ("7. Productos delicados", "Qué conviene averiguar antes."),
        ("8. Estafas", "Mensajes falsos de \"paquete retenido\" y cómo reconocerlos."),
        ("9. Plan Black Friday", "Una lista para el 27 de noviembre."),
        ("Anexo", "Glosario y fuentes.")], [42 * mm, W - 2 * M - 42 * mm]))
    f.append(Spacer(1, 10))
    f.append(consejo("EL ORDEN IMPORTA", "Si solo tenés 10 minutos: leé el capítulo 3 (costo final) y el 8 (estafas). Son los dos que más plata ahorran."))
    f.append(P("Las normas citadas son la Resolución General ARCA 5883/2026 (Boletín Oficial del 29/07/2026), el Decreto 1065/2024 y la información publicada por ARCA en octubre de 2026. Los porcentajes de impuestos de los ejemplos son los generales: cambian según el producto, así que son una estimación, no una liquidación.", "nota"))
    f.append(PageBreak())

    f += cap("1", "LAS REGLAS HOY", "Qué se puede traer por courier", "El régimen de \"pequeños envíos\" es el que usan casi todas las compras personales a tiendas del exterior.")
    f.append(P("Las compras puerta a puerta las gestiona una empresa de courier (o el correo) habilitada por ARCA. <b>No tenés que presentar ningún formulario</b>: la empresa hace la declaración a tu nombre y vos pagás los tributos que correspondan. Desde la RG 5883/2026 (vigente desde el 30/07/2026) los límites son:"))
    f.append(Tiles([("USD 3.000", "valor máximo|por envío (FOB)"), ("50 kg", "por paquete"), ("3 unidades", "iguales por|envío"), ("5 envíos", "por año y|por persona")]))
    f.append(Spacer(1, 10))
    f.append(tabla(["Límite", "Valor", "Detalle"], [
        ("Valor por envío", "hasta USD 3.000 FOB", "FOB es el valor de la mercadería sin flete ni seguro."),
        ("Peso", "hasta 50 kg por paquete", "Se mide por paquete, no por compra."),
        ("Unidades", "hasta 3 de la misma especie", "Tres remeras iguales entran; cuatro, no."),
        ("Cantidad de envíos", "hasta 5 por año y por persona", "Es por persona y por año calendario."),
        ("Uso", "personal, sin fin comercial", "Si lo vas a revender, es otro régimen.")],
        [34 * mm, 42 * mm, W - 2 * M - 76 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("La franquicia de USD 400"))
    f.append(P("Dentro del régimen, ARCA informa una <b>franquicia de USD 400</b>, hasta <b>5 veces por año</b> (es la exención de derechos de importación y tasa de estadística del Decreto 1065/2024). Eso no significa que no pagues nada: en esos primeros USD 400 se pagan igual el <b>IVA</b> y los impuestos internos, si corresponden. Por la parte que supera los USD 400 se suman el <b>derecho de importación</b> y la <b>tasa de estadística</b>."))
    f.append(alerta("LAS REGLAS VIEJAS YA NO RIGEN", "Si leíste que \"hasta USD 50 no se paga\" o que \"se pueden hacer 12 compras por año\", son datos de un esquema anterior. Hoy el criterio publicado por ARCA es el de USD 400 y 5 envíos por año. Confirmalo siempre en la página \"Envíos internacionales\" de arca.gob.ar."))
    f.append(P("Qué pasa con el envío número 6: el courier te avisa y tenés que pagar <b>la totalidad de los impuestos</b>, sin franquicia. Conviene juntar varias compras de la misma tienda en un solo paquete en vez de hacer muchos envíos chicos."))
    f.append(PageBreak())

    f += cap("2", "QUÉ SE PAGA", "IVA, derechos y tasa de estadística", "Tres conceptos distintos, con base de cálculo distinta.")
    f.append(tabla(["Concepto", "Cuándo se paga", "Sobre qué se calcula"], [
        ("IVA", "Siempre, también dentro de la franquicia.", "Valor de la mercadería más flete y seguro (valor en aduana). La alícuota general es 21%."),
        ("Derecho de importación", "Solo por lo que supera los USD 400.", "El porcentaje depende del producto (posición arancelaria)."),
        ("Tasa de estadística", "Solo por lo que supera los USD 400.", "Un porcentaje sobre el valor en aduana."),
        ("Impuestos internos", "Solo en algunos productos.", "Depende del bien.")],
        [34 * mm, 54 * mm, W - 2 * M - 88 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("Ejemplo 1: una compra chica"))
    f.append(P("Comprás zapatillas por USD 120 y el envío cuesta USD 20. Está dentro de la franquicia, así que <b>no hay derechos ni tasa</b>. Pagás IVA sobre USD 140: el 21% son USD 29,40. Con un dólar de referencia de $ 1.500 (es un ejemplo: usá la cotización que corresponda), el IVA son unos <b>$ 44.100</b> a pagar al courier, además de lo que ya pagaste en la tienda."))
    f.append(Barra("Ejemplo 1: costo en dólares", [("Zapatillas", 120, TINTA), ("Envío", 20, CEL), ("IVA 21%", 29.4, SELLO)]))
    f.append(Spacer(1, 6))
    f.append(H2("Ejemplo 2: una compra grande"))
    f.append(P("Comprás una notebook por USD 900 y el envío cuesta USD 60. La parte que supera la franquicia es USD 500 (900 − 400). Sobre esa parte se suman derechos y tasa; sobre el total se suma IVA. Los porcentajes de derechos varían por producto, por eso no hay un número único. <b>Usá la calculadora gratis de la web</b> (kit-monotributo.fernandezfrancowork.workers.dev/calculadora-compras-exterior) y cargá el porcentaje que te informe el courier."))
    f.append(Barra("Ejemplo 2: costo en dólares (sin derechos ni tasa, que dependen del producto)", [("Notebook", 900, TINTA), ("Envío", 60, CEL), ("IVA 21%", 201.6, SELLO)]))
    f.append(Spacer(1, 6))
    f.append(consejo("PARTIR UNA COMPRA NO SIEMPRE CONVIENE", "Dividir una compra en dos envíos gasta uno de tus 5 cupos anuales. Antes de partir, hacé la cuenta: a veces pagar derechos por un solo envío sale menos que gastar un cupo."))
    f.append(P("Los montos del ejemplo son ilustrativos. Los porcentajes de derechos de importación y de tasa de estadística no se fijan en esta guía porque dependen de cada producto; el courier te muestra el cálculo antes de entregar.", "nota"))
    f.append(PageBreak())

    f += cap("3", "COSTO FINAL", "El método de 5 pasos", "Hacelo antes de pagar. Lleva cinco minutos.")
    f += E(["<b>Anotá el precio en dólares sin envío</b> (el FOB) y el costo de envío por separado.",
            "<b>Mirá cuántos envíos usaste este año</b> en ARCA (capítulo 4). Si te quedan cupos, aplica la franquicia.",
            "<b>Calculá el IVA</b>: 21% sobre (precio + envío). Si el producto tiene otra alícuota, el courier te la informa.",
            "<b>Si el valor supera USD 400</b>, sumá derechos y tasa sobre el excedente con el porcentaje que informe el courier.",
            "<b>Sumá cómo pagás</b>: comisiones, cuotas y la percepción de la tarjeta (capítulo 6). Compará con el precio local."])
    f.append(Spacer(1, 6))
    f.append(tabla(["Rubro", "Ejemplo A (USD 120)", "Ejemplo B (USD 900)"], [
        ("Precio + envío", "USD 140", "USD 960"),
        ("IVA 21%", "USD 29,40", "USD 201,60"),
        ("Derechos + tasa", "USD 0 (franquicia)", "Sobre USD 500 de excedente: depende del producto"),
        ("¿Conviene?", "Sí, si el local cuesta más de USD 170", "Hacé la cuenta con tus porcentajes")],
        [38 * mm, 50 * mm, W - 2 * M - 88 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("Un buen hábito: <b>guardá la captura del carrito con el precio y el envío</b> y, cuando llegue el aviso del courier, compará. Si el importe a pagar no coincide con tu cuenta, pedí el detalle por concepto antes de abonar."))
    f.append(PageBreak())

    f += cap("4", "SEGUIR TU ENVÍO", "Ver tus envíos y tu cupo en ARCA", "Con Clave Fiscal podés ver qué usaste, con qué courier y cuánto te queda.")
    f.append(P("ARCA ofrece un módulo llamado <b>\"Envíos Postales Internacionales\"</b>. Se entra con <b>Clave Fiscal nivel 2 como mínimo</b>. Ahí ves el detalle de cada envío, el prestador (el courier) y el cupo utilizado de tus 5 envíos anuales."))
    f += E(["Ingresá a arca.gob.ar con tu CUIL o CUIT y Clave Fiscal.", "Buscá el servicio \"Envíos Postales Internacionales\" (si no aparece, agregalo desde el Administrador de Relaciones).", "Revisá los envíos del año y cuántos te quedan.", "Si un envío no figura o no lo reconocés, pedile el detalle al courier antes de pagar."])
    f.append(Spacer(1, 6))
    f.append(consejo("NO HAY TRÁMITE DE TU LADO", "ARCA aclara que no hay formularios que presentar: los gestiona la empresa de envíos a tu nombre. Si alguien te cobra \"un trámite en ARCA\" por una compra chica, desconfiá."))
    f.append(H2("Qué datos tiene que tener la compra"))
    f += L(["Tu <b>nombre completo y DNI/CUIL</b> como figuran en ARCA: si no coinciden, el envío puede demorarse.", "Una <b>dirección completa</b> y un teléfono o mail que revises todos los días.", "La <b>descripción real</b> de lo que compraste (la tienda la carga; no la cambies)."])
    f.append(PageBreak())

    f += cap("5", "PAQUETE RETENIDO", "Si el envío no llega o queda en aduana", "\"Retenido\" no es lo mismo que \"perdido\": casi siempre falta un dato o un pago.")
    f.append(Flujo([("Despacha|la tienda", "Sale del exterior|con tu DNI"), ("Llega al|país", "El courier declara|a tu nombre"), ("Aviso del|courier", "Importe y|datos a revisar"), ("Pagás|tributos", "Solo en el sitio|oficial"), ("Entrega", "En tu domicilio|o sucursal")]))
    f.append(Spacer(1, 10))
    f.append(tabla(["Qué ves", "Qué suele significar", "Qué hacer"], [
        ("\"Falta información del destinatario\"", "Nombre, documento o dirección incompletos.", "Completalo en el sitio del courier."),
        ("\"Pendiente de pago de tributos\"", "Te toca pagar IVA u otro tributo.", "Pagá solo desde el sitio o la app oficial del courier."),
        ("\"Excede el límite\"", "Valor, peso, unidades o cantidad anual fuera del régimen.", "Pedí al courier las opciones: pagar todo el impuesto, otro régimen o devolución."),
        ("\"En revisión\"", "Control aduanero o producto sujeto a requisitos.", "Esperá y consultá al courier con tu número de seguimiento.")],
        [44 * mm, 52 * mm, W - 2 * M - 96 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Guardá todo</b>: número de seguimiento, comprobantes de pago de la tienda, capturas y mails.", "<b>Reclamá primero a la tienda</b> si el problema es que no despachó; el tema aduanero se resuelve con el courier.", "Si el paquete quedó en destino y nadie te avisa, escribile al courier por sus canales oficiales, no por los enlaces de un mensaje."])
    f.append(alerta("CUIDADO CON LOS PLAZOS", "Los plazos para retirar o decidir los fija cada courier y la aduana; si dejás pasar el tiempo, la mercadería puede considerarse abandonada. Leé el mail del courier completo y anotá la fecha límite."))
    f.append(PageBreak())

    f += cap("6", "PAGAR Y RECLAMAR", "Cómo pagar y qué hacer si algo sale mal")
    f.append(H2("La tarjeta: percepciones y cotización"))
    f.append(P("Cuando pagás una compra del exterior con tarjeta, el resumen puede incluir <b>percepciones a cuenta de Ganancias o Bienes Personales</b> y se convierte al dólar que fija el banco. Esas percepciones cambiaron varias veces desde 2024 y las fuentes periodísticas no coinciden sobre su vigencia en 2026: <b>mirá el resumen de tu tarjeta y confirmá en ARCA</b> antes de dar por hecho un porcentaje. Si tenés una percepción que no podés computar, ARCA tiene un trámite para pedir la devolución."))
    f.append(H2("Antes de pagar"))
    f += L(["Pagá con <b>tarjeta de crédito</b> y no con transferencia o medios sin protección: te permite pedir el contracargo.", "Revisá la <b>moneda del cobro</b> (en dólares o pesos) y las comisiones de tu banco.", "Desconfiá del precio que está muy por debajo del resto del mercado.", "Sacá captura de la política de devoluciones de la tienda."])
    f.append(H2("Si no llegó o llegó mal"))
    f += E(["Reclamá por el chat o mail de la tienda con el número de pedido, dentro del plazo que fije su política.", "Si no responden, iniciá la disputa en la plataforma (Temu, Shein, Amazon y AliExpress tienen protección al comprador).", "Si pagaste con tarjeta y no hay solución, pedí el <b>contracargo</b> al banco con las pruebas.", "Para tiendas con presencia en el país, podés usar la Ventanilla Única Federal de Defensa del Consumidor (hay un generador de reclamo gratis en la web)."])
    f.append(P("El derecho de arrepentimiento (10 días corridos, art. 34 de la Ley 24.240) protege compras a distancia a proveedores que operan en el país; contra una tienda del exterior suele ser más práctico usar la política de la plataforma o el contracargo.", "nota"))
    f.append(PageBreak())

    f += cap("7", "PRODUCTOS DELICADOS", "Qué averiguar antes de comprar", "Algunos productos tienen requisitos aparte. Averigualos antes de pagar.")
    f.append(tabla(["Producto", "Por qué conviene averiguar", "A quién preguntar"], [
        ("Medicamentos y suplementos", "Los productos farmacéuticos requieren autorización previa de ANMAT.", "ANMAT / el courier"),
        ("Baterías, power banks, líquidos", "Muchos couriers no los transportan o lo limitan.", "El courier de la tienda"),
        ("Electrónica con radio (celulares, auriculares)", "Algunos equipos requieren homologación.", "El courier / ENACOM"),
        ("Alimentos, plantas, animales", "Control sanitario.", "SENASA / el courier"),
        ("Marcas y réplicas", "Una copia de marca puede ser retenida.", "El courier"),
        ("Más de 3 unidades iguales", "Excede el régimen de pequeños envíos.", "Courier / otro régimen")],
        [48 * mm, 74 * mm, W - 2 * M - 122 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("La lista no es completa: la RG 5883/2026 prevé que los requisitos operativos y el cronograma se publiquen en el micrositio \"Envíos internacionales\" de ARCA, y los organismos pueden sumar controles."))
    f.append(PageBreak())

    f += cap("8", "ESTAFAS", "Mensajes falsos de \"paquete retenido\"", "En épocas de compras, aparecen por SMS, mail y WhatsApp.")
    f.append(alerta("LA REGLA DE ORO", "ARCA no reclama pagos por correo electrónico, llamada telefónica ni redes sociales. Si un mensaje te pide pagar una \"tasa\" por un enlace, desestimalo."))
    f += L(["<b>Remitente raro o enlace acortado</b>: el courier real tiene un dominio propio. Entrá escribiendo la dirección vos, no por el enlace.", "<b>Urgencia</b>: \"pagá en 24 horas o se devuelve\". Los avisos reales no te presionan por mensaje.", "<b>Pagos a una cuenta personal</b> o por transferencia a un alias.", "<b>No esperabas ningún paquete</b>: antes de cualquier cosa, mirá si tenés una compra pendiente.", "<b>Pedido de datos</b>: tu clave de homebanking o el código de la tarjeta nunca los pide un courier."])
    f.append(P("Qué hacer: no hagas clic, entrá a tu cuenta de la tienda o al sitio del courier desde el navegador, comprobá el número de seguimiento y borrá el mensaje. Si ya pagaste, llamá a tu banco de inmediato."))
    f.append(PageBreak())

    f += cap("9", "PLAN BLACK FRIDAY", "Tu lista para el 27 de noviembre", "Los grandes descuentos tientan: este es el orden para no gastar de más.")
    f.append(Checklist(["<b>Hoy</b>: entrá a ARCA y mirá cuántos envíos usaste del cupo anual.", "<b>Armá una lista de deseos</b> con el precio actual de cada cosa, para ver si el descuento es real.", "<b>Anotá el equivalente local</b> y calculá el costo final con el método del capítulo 3.", "<b>Juntá compras</b> de la misma tienda en un solo paquete, sin pasar de 3 unidades iguales ni de USD 3.000.", "<b>Revisá los datos del envío</b> (nombre, DNI, dirección) antes de pagar.", "<b>Pagá con tarjeta</b> y guardá las capturas.", "<b>Después</b>: seguí el envío y desconfiá de los mensajes que llegan por fuera del sitio del courier."], "TU LISTA PARA IMPRIMIR"))
    f.append(Spacer(1, 6))
    f.append(tabla(["Fecha", "Qué hacer"], [("Ahora", "Revisar cupo y datos personales."), ("Semana previa", "Comparar precios de la lista de deseos."), ("27 de noviembre", "Comprar con el costo final calculado."), ("Dos semanas después", "Seguir los envíos y guardar comprobantes."), ("Diciembre", "Compras de Navidad: revisar plazos de entrega.")], [44 * mm, W - 2 * M - 44 * mm]))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("FOB", "Valor de la mercadería puesta a bordo, sin flete ni seguro."),
        ("CIF / valor en aduana", "Mercadería más flete y seguro: la base del IVA."),
        ("Courier / PSP", "Empresa habilitada por ARCA para despachar envíos pequeños."),
        ("Franquicia", "Parte del valor exenta de derechos y tasa (USD 400)."),
        ("Derecho de importación", "Impuesto aduanero, según el producto."),
        ("Tasa de estadística", "Tasa aduanera sobre el valor importado."),
        ("Contracargo", "Pedido al banco para anular un consumo con tarjeta no resuelto.")], [42 * mm, W - 2 * M - 42 * mm]))
    f.append(H2("Fuentes"))
    f += L(["Resolución General ARCA 5883/2026 (BO 29/07/2026), que modifica la RG 5608/2024.", "Decreto 1065/2024: exención de derechos de importación y tasa de estadística en pequeños envíos.", "ARCA, \"Régimen de Courier\" (publicada el 06/10/2026): franquicia, tributos y consulta de envíos.", "Ley 24.240, art. 34 (arrepentimiento)."])
    f.append(Spacer(1, 8))
    f.append(consejo("CALCULADORA GRATIS", "Cargá el precio, el envío y los porcentajes de tu courier y mirá el costo final: kit-monotributo.fernandezfrancowork.workers.dev/calculadora-compras-exterior"))
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento profesional, aduanero ni legal, y no reemplaza a un despachante de aduana ni a la información oficial de ARCA. Las normas, los montos y los porcentajes pueden cambiar. Confirmá los datos vigentes en arca.gob.ar antes de tomar decisiones. Está prohibida su reventa o redistribución.", "nota"))
    return f
