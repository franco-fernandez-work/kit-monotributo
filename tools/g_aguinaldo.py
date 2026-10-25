"""Guía 'Dónde poner el aguinaldo' (HUECOS.md #13). Educativa, sin recomendar productos ni dar tasas vigentes (cambian a diario).
Fuentes: BCRA (serie 1212 'Tasas de interés por depósitos a 30 días', Principales variables), CNV (régimen de FCI, Ley 24.083), ARCA, Ley 20.744 art. 122 (SAC)."""
from guias_lib import *

META = dict(nombre="Dónde poner el aguinaldo", etiqueta="GUÍA EDUCATIVA · DICIEMBRE DE 2026",
            titulo=["Dónde poner", "el aguinaldo"], sub=["Plazo fijo, fondos, cauciones, letras y dólar:", "cómo compararlos con números, sin vender nada."],
            sello="SAC", sello2="DICIEMBRE", cabecera="DÓNDE PONER EL AGUINALDO",
            pie="Información educativa. No es asesoramiento financiero ni una recomendación de inversión.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Qué es esta guía y qué no es", "Para quien cobra el aguinaldo y quiere decidir con método, no con el consejo del último influencer.")
    f.append(P("Esta guía <b>no te dice qué comprar</b>. No hay tasas \"actuales\" escritas acá, porque cambian todos los días y una guía impresa siempre llega tarde. Lo que sí tiene: cómo funciona cada alternativa, qué riesgo tiene, cómo se calcula lo que ganás y una forma de comparar usando los números de <b>hoy</b>, que vos mismo consultás en fuentes oficiales."))
    f.append(alerta("NO ES ASESORAMIENTO", "Es información educativa. No conocemos tu situación, tu plazo ni tu tolerancia al riesgo. Nadie puede prometer rendimientos. Ante dudas, consultá a un asesor registrado ante la CNV."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Antes de invertir", "Fondo de emergencia, deudas y el orden de las prioridades."),
        ("2. Cómo se mide un rendimiento", "TNA, TEA, inflación y rendimiento real, con fórmulas."),
        ("3. Las alternativas", "Plazo fijo, cuenta remunerada, FCI, caución, letras, ajustables, dólar."),
        ("4. Tabla comparativa", "Plazo, riesgo, liquidez y qué mirar en cada una."),
        ("5. Dónde mirar los números hoy", "Fuentes oficiales para tasas e inflación."),
        ("6. Impuestos y costos", "Qué verificar antes de elegir."),
        ("7. Errores y estafas", "Promesas de ganancia fija, \"grupos\" y cripto-rendimientos."),
        ("8. Plan de 15 minutos", "Checklist para decidir y dejarlo hecho."),
        ("Anexo", "Glosario y fuentes.")], [46 * mm, W - 2 * M - 46 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("EL SAC EN UNA LÍNEA", "El aguinaldo (Sueldo Anual Complementario) es el 50% de la mejor remuneración mensual devengada en el semestre (Ley 20.744, art. 122). La segunda cuota se paga a mediados de diciembre; la calculadora de la web te muestra el monto."))
    f.append(PageBreak())

    f += cap("1", "PRIMERO LO PRIMERO", "Antes de invertir un peso", "El mejor \"rendimiento\" suele estar en otro lado.")
    f.append(Flujo([("Deudas|caras", "Tarjeta, préstamos|con tasa alta"), ("Fondo de|emergencia", "3 a 6 meses de|gastos"), ("Gastos|de enero", "Cole, vacaciones,|seguros"), ("Ahorro a|plazo", "Lo que no vas a|necesitar pronto"), ("Inversión|con riesgo", "Solo lo que podés|ver bajar")]))
    f.append(Spacer(1, 10))
    f += L(["<b>Deuda cara primero.</b> Si pagás intereses de tarjeta o un préstamo personal con una tasa mayor a lo que rinde cualquier colocación, cancelar la deuda es el \"rendimiento\" más seguro.", "<b>Fondo de emergencia.</b> Dinero que podés usar en 24 horas, sin perder capital. Es para imprevistos, no para ganar.", "<b>Enero pega fuerte.</b> Útiles escolares, alquiler, seguros, patentes y vacaciones. Separá ese dinero antes de elegir dónde ponerlo.", "<b>Plazo.</b> ¿Para cuándo lo necesitás? Un mes, un año y cinco años son tres decisiones distintas."])
    f.append(Spacer(1, 6))
    f.append(Barra("Ejemplo: un aguinaldo de $ 1.000.000 repartido por prioridad (ilustrativo)", [("Deuda", 300000, SELLO), ("Gastos de enero", 250000, CEL), ("Emergencia", 250000, TINTA), ("Inversión", 200000, OK_C)], "$"))
    f.append(P("El reparto es un ejemplo para ordenar ideas, no una recomendación: el tuyo depende de tus deudas y gastos.", "nota"))
    f.append(PageBreak())

    f += cap("2", "CÓMO SE MIDE", "Tasa, inflación y rendimiento real", "Si no comparás con la inflación, no sabés si ganaste.")
    f.append(tabla(["Término", "Qué es", "Cómo se calcula"], [
        ("TNA", "Tasa nominal anual. La que anuncian los bancos.", "Interés = capital × TNA × días ÷ 365"),
        ("TEA", "Tasa efectiva anual: incluye reinvertir los intereses.", "TEA = (1 + TNA × d/365)^(365/d) − 1"),
        ("Inflación", "Cuánto subieron los precios en el período (INDEC).", "Variación del IPC del mes"),
        ("Rendimiento real", "Lo que ganaste descontando la inflación.", "(1 + r) ÷ (1 + inflación) − 1")],
        [30 * mm, 60 * mm, W - 2 * M - 90 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("Ejemplo con números inventados"))
    f.append(P("Supongamos <b>$ 1.000.000</b> a 30 días con una TNA de <b>30%</b> (valor de ejemplo, no actual). Interés = 1.000.000 × 0,30 × 30 ÷ 365 = <b>$ 24.658</b>, o sea 2,47% en el mes. Si la inflación del mes fue 2%, el rendimiento real es (1,0247 ÷ 1,02) − 1 = <b>0,46%</b>. Si hubiera sido 3%, el real sería <b>−0,52%</b>: tu plata crece en pesos pero compra menos."))
    f.append(Tiles([("$ 24.658", "interés a 30 días|(TNA 30%, ejemplo)"), ("2,47%", "en el mes"), ("+0,46%", "real con inflación|de 2%"), ("−0,52%", "real con inflación|de 3%")]))
    f.append(Spacer(1, 10))
    f.append(consejo("LA CALCULADORA DE LA WEB", "Cargá tu monto, la tasa de hoy, los días y la inflación que esperás: kit-monotributo.fernandezfrancowork.workers.dev/donde-poner-el-aguinaldo"))
    f.append(P("La inflación futura no se conoce. Usá la del último mes publicado por el INDEC como referencia y probá también un escenario peor.", "nota"))
    f.append(PageBreak())

    f += cap("3", "LAS ALTERNATIVAS", "Cómo funciona cada una", "Descripción general. Los detalles los fija cada entidad: leé el contrato.")
    f.append(H2("Plazo fijo tradicional"))
    f.append(P("Prestás plata a un banco por un plazo (desde 30 días) a una tasa conocida de antemano. <b>Pros:</b> sabés cuánto cobrás en pesos; es simple. <b>Contras:</b> el dinero queda inmovilizado hasta el vencimiento; la tasa puede quedar por debajo de la inflación. Los depósitos están cubiertos por el seguro de depósitos (SEDESA) hasta un tope que se actualiza: <b>consultá el monto vigente</b> en bcra.gob.ar antes de concentrar mucho en un banco."))
    f.append(H2("Plazo fijo ajustable (UVA / CER)"))
    f.append(P("El capital se actualiza por un índice de inflación (UVA o CER, que publica el BCRA) más una tasa. <b>Pros:</b> protege contra la inflación pasada. <b>Contras:</b> plazos mínimos más largos; si la inflación baja, puede rendir menos que uno tradicional."))
    f.append(H2("Cuenta remunerada de billeteras"))
    f.append(P("Dinero disponible con un rendimiento diario. <b>Pros:</b> liquidez inmediata. <b>Contras:</b> la tasa puede cambiar sin aviso y suele tener topes por cliente. Verificá en qué se invierte el saldo y cómo se paga."))
    f.append(H2("Fondos comunes de inversión (FCI)"))
    f.append(P("Un fondo reúne dinero de muchos y lo invierte en una cartera; vos comprás \"cuotapartes\". Están regulados por la CNV (Ley 24.083) y el patrimonio del fondo está separado del de la sociedad que lo administra. Hay de varios tipos:"))
    f += L(["<b>Money market</b>: instrumentos de muy corto plazo; el rescate suele ser el mismo día hábil o al siguiente.", "<b>Renta fija / ajustable por CER</b>: bonos y letras; el valor de la cuotaparte puede subir o bajar.", "<b>Renta variable</b>: acciones; solo para plazos largos y tolerancia a las caídas."])
    f.append(P("Mirá siempre el <b>reglamento y la ficha del fondo</b> en el sitio de la CNV: plazo de rescate, comisiones y composición."))
    f.append(PageBreak())
    f.append(H2("Caución bursátil"))
    f.append(P("Es un préstamo de muy corto plazo (de 1 a unos pocos días) entre inversores, garantizado por valores, que se hace por medio de un agente registrado ante la CNV. <b>Pros:</b> tasa conocida y plazo corto. <b>Contras:</b> hay que operar con un agente; la tasa cambia todos los días y en fin de mes o de año puede moverse mucho."))
    f.append(H2("Letras y bonos del Tesoro"))
    f.append(P("El Estado emite títulos en pesos (a tasa fija, ajustables por CER o dollar-linked) y en dólares. Se compran por un agente de bolsa (ALyC). <b>Pros:</b> hay opciones de plazos cortos y largos. <b>Contras:</b> el precio puede variar si querés vender antes del vencimiento; hay riesgo de que el emisor no pague. Mirar <b>la fecha de vencimiento y el precio de compra</b>."))
    f.append(H2("Dólar: oficial, MEP y otros"))
    f.append(P("Comprar dólares protege contra una devaluación pero <b>no rinde intereses</b>, y su precio puede subir o bajar. Las formas de acceso, los topes y los impuestos asociados cambiaron varias veces: verificá en el BCRA y ARCA qué rige hoy para vos antes de operar. Comprar de a poco reduce el riesgo de elegir un mal día."))
    f.append(H2("Qué no incluimos"))
    f.append(P("Criptoactivos, acciones individuales y derivados: requieren conocimientos y una tolerancia al riesgo distintos. Si te interesan, hacelo con un asesor y con un monto que puedas perder."))
    f.append(PageBreak())

    f += cap("4", "TABLA COMPARATIVA", "Plazo, riesgo y liquidez", "Resumen general. Cada producto tiene condiciones propias.")
    f.append(tabla(["Alternativa", "Plazo habitual", "Riesgo principal", "Disponibilidad"], [
        ("Plazo fijo", "30 días o más", "Inflación mayor que la tasa", "Al vencimiento"),
        ("Plazo fijo UVA/CER", "Más largo", "Que la inflación baje", "Al vencimiento"),
        ("Cuenta remunerada", "Sin plazo", "Cambio de tasa, topes", "Inmediata"),
        ("FCI money market", "Sin plazo mínimo", "Pequeñas variaciones de valor", "Mismo día o siguiente"),
        ("FCI renta fija", "Mediano plazo", "Baja del valor de la cuotaparte", "1 a 3 días hábiles"),
        ("Caución", "1 a pocos días", "Tasa variable; operar con agente", "Al vencimiento"),
        ("Letras / bonos", "Hasta el vencimiento", "Precio de mercado y emisor", "Venta en el mercado"),
        ("Dólar", "Sin plazo", "Su precio en pesos puede bajar", "Inmediata (con restricciones)")],
        [34 * mm, 34 * mm, 58 * mm, W - 2 * M - 126 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA PREGUNTA QUE ORDENA TODO", "¿Cuándo voy a necesitar este dinero? Si es en menos de 3 meses, priorizá liquidez y bajo riesgo. Cuanto más largo el plazo, más variación podés tolerar."))
    f.append(H2("Diversificar"))
    f.append(P("No existe la \"mejor\" opción para todo el aguinaldo. Repartir entre dos o tres alternativas con distinto plazo y riesgo reduce el impacto de equivocarte con una."))
    f.append(PageBreak())

    f += cap("5", "DÓNDE MIRAR HOY", "Fuentes oficiales para los números", "Todo se consulta gratis.")
    f.append(tabla(["Dato", "Dónde", "Cómo se llama"], [
        ("Tasa de plazo fijo a 30 días", "bcra.gob.ar > Estadísticas > Principales variables", "Tasas de interés por depósitos a 30 días de plazo en entidades financieras (% n.a.)"),
        ("UVA y CER", "bcra.gob.ar > Principales variables", "Unidad de Valor Adquisitivo (UVA); CER"),
        ("Dólar mayorista de referencia", "bcra.gob.ar > Principales variables", "Tipo de cambio mayorista, Com. A 3500"),
        ("Inflación", "indec.gob.ar", "Índice de precios al consumidor (IPC)"),
        ("Fondos comunes de inversión", "cnv.gov.ar", "Fondos comunes de inversión: reglamento y ficha"),
        ("Agentes registrados", "cnv.gov.ar", "Registro de agentes (ALyC) autorizados")],
        [44 * mm, 52 * mm, W - 2 * M - 96 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("Las tasas de los bancos y billeteras se ven en la app de cada uno; el BCRA publica además comparadores de costos y tasas de entidades financieras. <b>Siempre anotá la fecha</b> en la que miraste cada número."))
    f.append(PageBreak())

    f += cap("6", "IMPUESTOS Y COSTOS", "Lo que se suele olvidar", "Antes de elegir, verificá estas cinco cosas.")
    f.append(Checklist(["<b>Comisiones</b>: de custodia, de entrada o salida y de operación del agente.", "<b>Impuestos</b>: si los intereses o las ganancias tributan, cuánto y quién retiene. Confirmalo en ARCA o con tu contador; no lo damos por sentado.", "<b>Restricciones cambiarias</b>: si buscás dólares, qué trabas rigen hoy.", "<b>Plazos de acreditación</b>: cuándo tenés la plata disponible de verdad.", "<b>Quién custodia</b>: banco, agente registrado ante la CNV o una billetera; qué cobertura tiene cada uno."], "ANTES DE ELEGIR"))
    f.append(Spacer(1, 6))
    f.append(P("Un rendimiento \"bruto\" alto puede achicarse si hay comisiones o impuestos. Calculá siempre el <b>neto</b>."))
    f.append(PageBreak())

    f += cap("7", "ERRORES Y ESTAFAS", "Qué evitar en diciembre", "Con el aguinaldo en la cuenta aparecen las ofertas.")
    f.append(alerta("DESCONFIAR SIEMPRE", "Nadie legítimo promete una ganancia fija y alta \"sin riesgo\". Quien lo hace, o miente o no lo puede cumplir."))
    f += L(["<b>Grupos de WhatsApp o Telegram</b> que \"duplican\" tu plata o dan señales infalibles.", "<b>Plataformas sin registro</b>: verificá que el agente figure en la CNV antes de transferir.", "<b>Transferir a una cuenta personal</b> para \"invertir\".", "<b>Rendimientos fijos diarios</b> en cripto o \"arbitraje\".", "<b>Apuro</b>: \"último día\", \"quedan 3 cupos\".", "<b>Falta de claridad</b>: si no podés explicar con tus palabras cómo gana el producto, no lo compres."])
    f.append(H2("Si ya caíste"))
    f += L(["Frená los pagos y guardá capturas, comprobantes y datos de la cuenta destino.", "Avisá a tu banco o billetera de inmediato.", "Denunciá en la fiscalía o comisaría y, si es una plataforma de inversión, en la CNV."])
    f.append(PageBreak())

    f += cap("8", "PLAN DE 15 MINUTOS", "Cómo dejarlo decidido hoy")
    f.append(Checklist(["Anoté el monto neto del aguinaldo.", "Separé lo que tengo que pagar en enero y las deudas caras.", "Definí cuánto va al fondo de emergencia y dónde (liquidez inmediata).", "Para el resto, anoté para cuándo lo voy a necesitar.", "Miré las tasas de hoy en las fuentes oficiales (capítulo 5) y anoté la fecha.", "Corrí la calculadora con la inflación del último mes y con un escenario peor.", "Revisé comisiones, impuestos y plazos de acreditación.", "Elegí una o dos alternativas y verifiqué que la entidad esté autorizada.", "Programé la fecha de vencimiento en el calendario."], "CHECKLIST FINAL"))
    f.append(Spacer(1, 8))
    f.append(tabla(["Si tu situación es…", "Tené en cuenta"], [
        ("Necesito el dinero en pocas semanas", "Liquidez y bajo riesgo; evitá renta variable y bonos largos."),
        ("Lo necesito dentro de un año", "Podés combinar plazo fijo ajustable, letras o fondos de renta fija."),
        ("Es ahorro a largo plazo", "La diversificación y el horizonte importan más que el día de compra."),
        ("Tengo deudas con tasa alta", "Cancelalas primero.")], [66 * mm, W - 2 * M - 66 * mm]))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("Cuotaparte", "Unidad de un fondo común de inversión."),
        ("ALyC", "Agente de liquidación y compensación registrado ante la CNV."),
        ("CER / UVA", "Índices que ajustan por inflación, publicados por el BCRA."),
        ("Caución", "Préstamo bursátil de muy corto plazo con garantía."),
        ("MEP", "Dólar que se obtiene comprando y vendiendo un bono; sujeto a normas vigentes."),
        ("SEDESA", "Sociedad que administra el seguro de garantía de los depósitos.")], [34 * mm, W - 2 * M - 34 * mm]))
    f.append(H2("Fuentes"))
    f += L(["BCRA, Principales variables (tasa de depósitos a 30 días, UVA, CER, tipo de cambio de referencia).", "CNV, régimen de fondos comunes de inversión (Ley 24.083) y registro de agentes.", "Ley 20.744 (Contrato de Trabajo), art. 122: SAC.", "INDEC, índice de precios al consumidor."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento financiero, impositivo ni legal, ni una oferta o recomendación de inversión. Toda inversión tiene riesgos y los rendimientos pasados no garantizan resultados futuros. No incluye tasas ni precios vigentes. Verificá las condiciones y los impuestos en fuentes oficiales antes de decidir. Está prohibida su reventa o redistribución.", "nota"))
    return f
