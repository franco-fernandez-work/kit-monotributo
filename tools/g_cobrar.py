"""Guía 'Cobrar del exterior siendo freelancer' (HUECOS.md #11). Normativa verificada en fuente oficial:
ARCA: monotributo/exportacion-servicios (Factura E, punto de venta de exportación, límite categoría máxima, exención MiPyME) y derechos-de-exportacion-de-servicios/comprobantes-y-facturacion/particularidades (tipo de cambio);
BCRA: Comunicación A 8481 (14/09/2026, vigencia 15/09/2026), Exterior y Cambios 2.2.1 y 2.2.2.1 (liquidación en 20 días hábiles y excepción para personas humanas)."""
from guias_lib import *
from build_site import CATS, ars

META = dict(nombre="Cobrar del exterior siendo freelancer", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Cobrar del exterior", "siendo freelancer"], sub=["Factura E, monotributo, dólares y cómo cobrar", "sin sorpresas con ARCA ni con el banco."],
            sello="FACTURA E", sello2="EXPORTACIÓN", tam=40, cabecera="COBRAR DEL EXTERIOR SIENDO FREELANCER",
            pie="Información general. No reemplaza a un contador ni a la información oficial de ARCA y del BCRA.")

def cat_para(anual):
    for l, tope, cs, cb in CATS:
        if anual <= tope: return l, tope, cs
    return None, None, None

def ejemplo(usd_mes, dolar):
    anual = usd_mes * 12 * dolar
    l, tope, cuota = cat_para(anual)
    return anual, l, tope, cuota

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien trabaja para clientes del exterior desde Argentina como monotributista y quiere cobrar en regla y quedarse con la mayor parte.")
    f.append(P("Cobrar del exterior no es difícil, pero tiene <b>tres decisiones que se toman en orden</b>: cómo facturás (Factura E), cómo cobrás (la vía) y qué hacés con los dólares (la regla del BCRA). Casi todos los problemas aparecen cuando se mezclan: cobrar sin factura, facturar con el punto de venta equivocado o no haber previsto qué pasa con los dólares. Esta guía sigue ese orden."))
    f.append(Tiles([("Factura E", "para clientes|del exterior"), ("20 días", "hábiles para|liquidar o acreditar"), ("Cuenta en USD", "a tu nombre,|en un banco local"), ("Tope K", "límite de|categoría máxima")]))
    f.append(Spacer(1, 10))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. El mapa completo", "Los 3 pasos y qué decisiones tomás en cada uno."),
        ("2. Facturar: la Factura E", "Punto de venta, datos, moneda y tipo de cambio."),
        ("3. Monotributo y dólares", "Cómo cuenta lo que cobrás y a qué categoría te lleva."),
        ("4. Cómo cobrar", "Transferencia, plataformas y billeteras: cómo compararlas."),
        ("5. Qué hacer con los dólares", "La regla del BCRA para personas humanas."),
        ("6. Impuestos", "Cuota, Ingresos Brutos y derechos de exportación."),
        ("7. Clientes y contratos", "Qué pedir, qué firmar y el formulario W-8BEN."),
        ("8. Errores caros", "Los que más se repiten."),
        ("9. Lista y calendario", "Para tener todo en regla antes de la primera factura."),
        ("Anexo", "Glosario y fuentes.")], [46 * mm, W - 2 * M - 46 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("Las normas citadas son las páginas de ARCA sobre exportación de servicios y facturación electrónica de exportación, y la Comunicación \"A\" 8481 del BCRA (14/09/2026, vigente desde el 15/09/2026). Las escalas de monotributo son las de agosto 2026 a enero 2027.", "nota"))
    f.append(PageBreak())

    f += cap("1", "EL MAPA", "Los tres pasos para cobrar bien", "Una venta al exterior es una exportación de servicios: tiene su propia factura y su propia regla cambiaria.")
    f.append(Flujo([("Facturás", "Factura E por|punto de venta de|exportación"), ("Cobrás", "Banco, plataforma|o billetera"), ("Acreditás", "Cuenta en USD o|liquidás en 20 días"), ("Declarás", "Sumás el ingreso|a tu monotributo"), ("Recategoría", "Cada febrero|y agosto")]))
    f.append(Spacer(1, 12))
    f.append(H2("Qué decidís en cada paso"))
    f.append(tabla(["Paso", "Decisión", "Dónde se explica"], [
        ("Facturar", "Moneda de la factura (dólares o pesos) y punto de venta.", "Capítulo 2"),
        ("Cobrar", "La vía de cobro según costo, velocidad y tu cliente.", "Capítulo 4"),
        ("Dólares", "Dejarlos en una cuenta en dólares a tu nombre o venderlos.", "Capítulo 5"),
        ("Monotributo", "Qué categoría te corresponde con ese ingreso.", "Capítulo 3")], [30 * mm, 92 * mm, W - 2 * M - 122 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA REGLA QUE ORDENA TODO", "El medio de cobro no cambia la naturaleza del ingreso: si prestaste un servicio a un cliente del exterior, lo facturás y lo declarás igual, lo hayas cobrado por transferencia, plataforma o billetera."))
    f.append(P("Esta guía es para <b>monotributistas</b> (personas humanas). Si tenés una sociedad, las reglas del BCRA son distintas (capítulo 5)."))
    f.append(PageBreak())

    f += cap("2", "FACTURAR", "La Factura E, paso a paso", "Los monotributistas emiten Factura C para el mercado local; las exportaciones llevan Factura E.")
    f.append(P("Según ARCA, los monotributistas emiten comprobantes tipo \"C\", <b>salvo que se trate de una exportación, en cuyo caso corresponde la factura tipo \"E\"</b>. Se emite con el servicio <b>\"Comprobantes en línea\"</b> de ARCA, después de habilitar un punto de venta propio de exportación."))
    f += E(["Entrá a ARCA con tu CUIT y Clave Fiscal y abrí el servicio <b>Administración de Puntos de Venta y Domicilios</b>.",
            "Creá un <b>punto de venta nuevo</b> del tipo \"Comprobantes de exportación - Comprobante en línea\". Tiene que ser <b>distinto e independiente</b> del que usás para tus facturas C.",
            "Entrá a \"Comprobantes en línea\", elegí ese punto de venta y el tipo de comprobante <b>Factura E</b>.",
            "Completá el tipo de operación <b>\"Exportación de servicios\"</b>, el <b>país de destino</b> y el CUIT correspondiente al país de tu cliente (ARCA tiene la lista de CUIT por país).",
            "Cargá el concepto, el importe y la <b>moneda</b>. Indicá la <b>fecha de pago</b> cuando el comprobante la pide.",
            "Confirmá, descargá el PDF y enviáselo a tu cliente. Guardá una copia."])
    f.append(Spacer(1, 6))
    f.append(H2("Moneda y tipo de cambio"))
    f += L(["La factura puede emitirse <b>en moneda extranjera o en pesos</b>. Si es en pesos, ARCA indica usar el tipo de cambio comprador del Banco Nación del día anterior a la emisión.", "Si facturás en una moneda que no es dólar, ARCA la convierte a dólares con el tipo de cambio vendedor del Banco Nación al cierre del día hábil anterior.", "Una nota de crédito o débito usa el tipo de cambio del comprobante que corrige."])
    f.append(alerta("NO USES LA FACTURA C PARA UN CLIENTE DEL EXTERIOR", "Con el punto de venta de la Factura C el sistema rechaza una Factura E. Y emitir una C por una exportación te deja el ingreso mal clasificado. Habilitá el punto de venta de exportación antes de la primera factura."))
    f.append(PageBreak())

    f += cap("3", "MONOTRIBUTO Y DÓLARES", "Cómo cuenta lo que cobrás en dólares", "Lo que facturás al exterior se mide en pesos y compite por el mismo tope.")
    f.append(P("ARCA dice que los monotributistas <b>pueden exportar servicios sin superar los límites de facturación de la categoría máxima correspondiente a su actividad</b> (hoy, para servicios, la K: " + ars(CATS[-1][1], False) + " al año). Algunas páginas privadas sostienen que las exportaciones no suman al tope: ARCA no lo dice así. <b>La regla prudente es sumar todo</b> y convertir cada factura al tipo de cambio de la fecha."))
    f.append(H2("Cuánto es eso en dólares: tres ejemplos"))
    filas = []
    dolar = 1450
    for usd in (800, 1500, 3000):
        anual, l, tope, cuota = ejemplo(usd, dolar)
        filas.append((f"USD {usd:,}".replace(",", ".") + " por mes", ars(anual, False), l or "Fuera de K", ars(cuota, False) if cuota else "—"))
    f.append(tabla(["Facturás", "Total anual en pesos*", "Categoría", "Cuota mensual"], filas, [38 * mm, 48 * mm, 32 * mm, W - 2 * M - 118 * mm]))
    f.append(P(f"* Cuenta de ejemplo con un dólar de referencia de $ {dolar} para todo el año: en la práctica cada factura va a su tipo de cambio. Escalas de servicios vigentes de agosto 2026 a enero 2027.", "nota"))
    f.append(Spacer(1, 8))
    f += L(["<b>Calculá en pesos</b> cada factura al tipo de cambio de su fecha y sumá los últimos 12 meses.", "<b>La recategorización</b> se hace en febrero y agosto mirando los últimos 12 meses: un cliente que paga grande una vez puede subirte de categoría.", "<b>Si te pasás de la K</b> salís del monotributo y pasás al régimen general: planificalo antes con un contador."])
    f.append(consejo("MARGEN DE SEGURIDAD", "Si estás cerca del tope de tu categoría, un dólar más alto de lo previsto te empuja a la siguiente. Llevá una planilla mensual con tus facturas en dólares y su equivalente en pesos (el Kit Monotributista de la web hace la parte de las categorías)."))
    f.append(PageBreak())

    f += cap("4", "COBRAR", "Cómo cobrar: comparar vías sin enamorarse de ninguna", "Cada vía tiene costos distintos; lo que importa es lo que te llega, no la comisión que anuncian.")
    f.append(tabla(["Vía", "Cuándo conviene", "Qué mirar"], [
        ("Transferencia bancaria internacional (SWIFT)", "Montos grandes, clientes empresa.", "Comisiones del banco emisor, del intermediario y del tuyo."),
        ("Cuenta de cobro de plataforma (tipo Payoneer, Wise)", "Clientes que ya las usan, pagos recurrentes.", "Cotización al convertir, comisión por retiro y cuenta local en USD."),
        ("Billeteras y plataformas de freelancers", "Cuando el cliente llegó por una plataforma.", "Retención de la plataforma, tiempos de liberación."),
        ("Cripto / stablecoins", "Solo si entendés cómo se declara y cómo se convierte.", "El ingreso se factura y declara igual que cualquier otro.")],
        [48 * mm, 46 * mm, W - 2 * M - 94 * mm]))
    f.append(Spacer(1, 6))
    f.append(Barra("Ejemplo: de USD 1.000 facturados, con una comisión total de 3% (supuesto)", [("Te llega", 970, TINTA), ("Comisiones (ejemplo)", 30, SELLO)]))
    f.append(P("El 3% es un supuesto para ilustrar. Las comisiones y cotizaciones de cada servicio cambian: calculalas con tu monto real antes de elegir.", "nota"))
    f.append(H2("Cómo comparar en 4 pasos"))
    f += E(["Simulá un cobro de tu monto típico en cada vía.", "Sumá <b>todo</b>: comisión fija, porcentaje, cotización de conversión y costo de retiro.", "Mirá <b>en qué moneda y en qué cuenta</b> queda el dinero (capítulo 5).", "Elegí la vía que le sirva también a tu cliente: si no puede usarla, no sirve."])
    f.append(consejo("SIEMPRE CON COMPROBANTE", "Guardá el comprobante de cada cobro y conciliá con tus Facturas E: en una consulta de ARCA o del banco, factura, cobro y acreditación tienen que contar la misma historia."))
    f.append(PageBreak())

    f += cap("5", "LOS DÓLARES", "Qué hacer con los dólares: la regla del BCRA", "Hay una regla de liquidación y una excepción para personas humanas.")
    f.append(P("La norma del BCRA \"Exterior y Cambios\" (texto actualizado por la <b>Comunicación \"A\" 8481, del 14/09/2026, vigente desde el 15/09/2026</b>) dice dos cosas sobre los cobros por servicios prestados a no residentes:"))
    f += E(["<b>Regla general</b>: los cobros se ingresan y se liquidan en el mercado de cambios (se venden por pesos) <b>dentro de los 20 días hábiles</b> desde que los percibís o se acreditan.", "<b>Excepción para personas humanas</b>: quedan exceptuados de liquidar los cobros de servicios prestados por personas humanas si <b>los fondos se acreditan en una cuenta en moneda extranjera a tu nombre en un banco local</b> y el mecanismo es <b>neutro en materia fiscal</b>."])
    f.append(Spacer(1, 6))
    f.append(Flujo([("Tu cliente|paga", "Desde el exterior"), ("Llega al|banco local", "A tu cuenta en USD"), ("Registro", "El banco no mueve|pesos (concepto A22)"), ("Los dólares|quedan", "Los usás o los|vendés cuando quieras")], color=OK_C))
    f.append(Spacer(1, 10))
    f += L(["<b>El banco no puede cobrarte comisión</b> por registrar esa acreditación; sí puede trasladarte los cargos documentados de los bancos del exterior que intervinieron.", "Si los fondos los recibís <b>en el exterior</b> (por ejemplo en una plataforma), el ingreso al país se considera cumplido por el monto de los gastos que debitan las entidades del exterior por la transferencia, y el resto sigue la regla general.", "<b>Las sociedades tienen otro régimen</b>: la excepción es mucho más acotada (beneficiarios de la economía del conocimiento)."])
    f.append(alerta("LAS REGLAS CAMBIARIAS CAMBIAN SEGUIDO", "Esta regla se modificó varias veces entre 2025 y 2026 (tope anual y lista de conceptos que hoy ya no figuran). Antes de recibir tu primer pago, preguntale a tu banco cómo registra la operación y pedí que te confirmen por escrito qué condiciones aplican hoy."))
    f.append(PageBreak())

    f += cap("6", "IMPUESTOS", "Qué impuestos entran en juego", "Para un monotributista, casi todo está en la cuota; hay dos cosas para revisar.")
    f.append(tabla(["Concepto", "Qué pasa", "Qué hacer"], [
        ("Cuota del monotributo", "Incluye impuesto integrado, jubilación y obra social. Se paga según tu categoría.", "Recategorizá bien (capítulo 3)."),
        ("IVA", "El monotributista no discrimina IVA; la Factura E de exportación no lo lleva.", "Nada: no agregues impuestos a la factura."),
        ("Derechos de exportación", "ARCA indica que los monotributistas con certificado MiPyME vigente están exentos y no deben inscribirse en el Registro de exportadores.", "Tramitá el certificado MiPyME y guardalo."),
        ("Ingresos Brutos", "Es provincial: algunas jurisdicciones tratan distinto la exportación de servicios.", "Consultá a tu dirección de rentas provincial."),
        ("Retenciones del exterior", "Algunos clientes retienen o piden formularios fiscales propios.", "Pedí el detalle por escrito (capítulo 7).")],
        [38 * mm, 78 * mm, W - 2 * M - 116 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("EL CERTIFICADO MIPYME", "Es un trámite gratuito en ARCA que acredita tu condición de micro, pequeña o mediana empresa. La exención rige desde el primer día del mes en que lo obtenés, para las exportaciones de ese mes y de los siguientes mientras esté vigente. Confirmá en ARCA cómo se tramita hoy."))
    f.append(P("No tomes esto como asesoramiento impositivo: es el mapa de lo que hay que revisar. Con ingresos grandes o clientes en varios países, una consulta con un contador sale barata comparada con un error.", "nota"))
    f.append(PageBreak())

    f += cap("7", "CLIENTES Y CONTRATOS", "Qué pedir y qué firmar", "Un buen acuerdo evita casi todos los conflictos de cobro.")
    f.append(Checklist(["<b>Quién es tu cliente</b>: razón social, país, dirección y número de identificación fiscal (lo necesitás para la Factura E).", "<b>Moneda y monto</b>: en qué moneda se factura, cada cuánto y qué pasa si el tipo de cambio se mueve.", "<b>Plazo de pago</b>: a cuántos días de la factura y por qué vía.", "<b>Quién paga los gastos</b> de transferencia: tuyos, del cliente o repartidos.", "<b>Entregables y aceptación</b>: cuándo se considera entregado el trabajo.", "<b>Propiedad intelectual</b>: qué cedés y qué conservás.", "<b>Confidencialidad</b> y qué pasa si el contrato termina antes.", "<b>Ley y jurisdicción</b>: qué ley rige y dónde se resuelven los conflictos."], "CHECKLIST DEL CONTRATO"))
    f.append(Spacer(1, 8))
    f.append(P("<b>El formulario W-8BEN.</b> Muchos clientes de Estados Unidos piden este formulario del IRS para acreditar que no sos residente estadounidense y no practicarte retenciones. Lo completás vos con tus datos. Si te lo piden, no lo ignores: sin él pueden retenerte."))
    f.append(P("Si trabajás de forma continua con un mismo cliente, vale la pena firmar un contrato. En la web hay un <b>pack de contratos para freelancers</b> con modelos editables en Word."))
    f.append(PageBreak())

    f += cap("8", "ERRORES CAROS", "Los que más se repiten")
    f.append(tabla(["Error", "Qué cuesta", "Cómo evitarlo"], [
        ("Cobrar sin factura", "Ingreso sin declarar y problemas para justificar fondos.", "Facturá cada cobro con Factura E."),
        ("Usar el punto de venta equivocado", "Rechazo de la factura o factura mal clasificada.", "Punto de venta de exportación separado."),
        ("No sumar los ingresos al tope", "Quedarte fuera de categoría sin darte cuenta.", "Planilla mensual en pesos."),
        ("Ignorar la regla de liquidación", "Fondos observados por el banco o la regla cambiaria.", "Cuenta en USD a tu nombre en un banco local."),
        ("Comparar solo la comisión", "Perder en la cotización de conversión.", "Simular el cobro completo."),
        ("Mezclar la plata personal y la del trabajo", "Imposible conciliar.", "Una cuenta o billetera solo para cobros."),
        ("Cobrar por una vía que el cliente no controla", "Pagos demorados o devueltos.", "Acordar la vía antes de empezar."),
        ("No guardar comprobantes", "No podés probar nada.", "Carpeta con factura, contrato y cobro de cada trabajo.")],
        [44 * mm, 60 * mm, W - 2 * M - 104 * mm]))
    f.append(PageBreak())

    f += cap("9", "LISTA Y CALENDARIO", "Todo en regla antes de la primera factura")
    f.append(Checklist(["Estoy inscripto en el monotributo con la actividad correcta.", "Tengo Clave Fiscal nivel 3 y el servicio \"Comprobantes en línea\".", "Habilité un punto de venta de exportación, distinto al de mis facturas C.", "Tengo los datos fiscales completos de mi cliente del exterior.", "Elegí la vía de cobro y simulé el costo real.", "Tengo (o voy a abrir) una cuenta en moneda extranjera a mi nombre en un banco local.", "Pregunté al banco cómo registra la acreditación y lo guardé por escrito.", "Tramité o evalué el certificado MiPyME.", "Armé mi planilla de facturación mensual en pesos.", "Firmé un contrato o acuerdo por escrito con mi cliente."], "ANTES DE LA PRIMERA FACTURA"))
    f.append(Spacer(1, 10))
    f.append(tabla(["Cuándo", "Qué hacer"], [("Cada trabajo", "Emitir la Factura E y guardar el comprobante."), ("Cada cobro", "Registrarlo y conciliarlo con la factura."), ("Todos los meses", "Pagar la cuota y actualizar tu planilla."), ("Febrero y agosto", "Recategorizar con los últimos 12 meses."), ("Cada tanto", "Revisar la regla cambiaria y la de tu banco.")], [44 * mm, W - 2 * M - 44 * mm]))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("Factura E", "Comprobante de exportación que emiten los monotributistas a clientes del exterior."),
        ("Punto de venta de exportación", "Punto de venta separado que habilitás en ARCA para emitir Facturas E."),
        ("Liquidar", "Vender los dólares en el mercado de cambios y recibir pesos."),
        ("Acreditar en cuenta en moneda extranjera", "Dejar los dólares en una cuenta en dólares a tu nombre en un banco local."),
        ("Certificado MiPyME", "Constancia de ARCA que acredita la condición de micro, pequeña o mediana empresa."),
        ("W-8BEN", "Formulario del IRS para acreditar que no sos residente fiscal de EE. UU.")], [50 * mm, W - 2 * M - 50 * mm]))
    f.append(H2("Fuentes"))
    f += L(["ARCA: \"Exportación de servicios - Monotributo\" (Factura E, punto de venta, límites, exención MiPyME).", "ARCA: Derechos de exportación de servicios, comprobantes y facturación (tipo de cambio de la Factura E).", "BCRA: Comunicación \"A\" 8481 (14/09/2026), Exterior y Cambios, puntos 2.2.1 y 2.2.2.1.", "Escalas de monotributo vigentes de agosto 2026 a enero 2027."])
    f.append(Spacer(1, 8))
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento contable, impositivo ni legal, y no reemplaza a un contador ni a la información oficial de ARCA y del BCRA. Las normas, escalas y reglas cambiarias pueden cambiar. Confirmá los datos vigentes antes de tomar decisiones. Está prohibida su reventa o redistribución.", "nota"))
    return f
