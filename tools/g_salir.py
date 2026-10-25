"""Guía 'Salir del monotributo' (HUECOS.md #16). Normativa verificada en ARCA (arca.gob.ar/monotributo/ayuda: baja, exclusión, renuncia, pasaje al régimen general, de oficio;
arca.gob.ar/autonomos; regimenGeneral personas humanas; PDF 'Valores autónomos desde octubre 2026', vigente 15/10/2026). NO verificado: alícuotas y escalas de Ganancias, Ingresos Brutos por provincia, límite de microempresa."""
from guias_lib import *
from build_site import CATS, ars

def _f(v): return f"$ {v:,.0f}".replace(",", ".")

META = dict(nombre="Salir del monotributo", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Salir del", "monotributo"], sub=["Exclusión, renuncia, autónomos, IVA y Ganancias:", "qué pasa, qué cuesta y cómo hacerlo ordenado."],
            sello="K", sello2="TOPE", cabecera="SALIR DEL MONOTRIBUTO",
            pie="Información general. No reemplaza a un contador ni a la información oficial de ARCA.")

def contenido():
    k = CATS[-1]
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien factura cerca del tope, recibió un aviso de exclusión o quiere crecer y se pregunta qué viene después del monotributo.")
    f.append(P("Salir del monotributo no es un castigo: suele ser una señal de que el negocio creció. Lo que hace daño es <b>llegar sin preparación</b>: pasar a IVA y Ganancias, sumar aportes de autónomo, cambiar la facturación y descubrir que la plata no alcanza. Esta guía ordena <b>por qué te pueden sacar, cómo salir vos antes, qué se paga después y cómo hacer el pasaje</b>, con la información publicada por ARCA."))
    f.append(alerta("SIEMPRE CONSULTÁ A UN CONTADOR", "Pasar al régimen general tiene consecuencias impositivas (IVA, Ganancias, Ingresos Brutos y aportes). Esta guía te ayuda a llegar informado a esa consulta, pero no la reemplaza."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Las tres salidas", "Exclusión, renuncia y baja por cese: cuándo y cómo."),
        ("2. Por qué te pueden excluir", "Las causales de ARCA, con el plazo para defenderte."),
        ("3. Qué cambia en el régimen general", "IVA, Ganancias, autónomos, facturas."),
        ("4. Cuánto cuesta", "Aporte de autónomo, comparación y cuenta de ejemplo."),
        ("5. Cómo hacer el pasaje", "Pasos en ARCA y qué avisar a tus clientes."),
        ("6. Beneficios del pasaje", "Crédito fiscal, compras y reducción de IVA."),
        ("7. Cómo no pasarte", "Control mensual del tope y de las causales."),
        ("8. Errores frecuentes", "Los que más cuestan."),
        ("9. Plan para los próximos 90 días", "Checklist."),
        ("Anexo", "Glosario y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("SI RECIBISTE UN AVISO DE EXCLUSIÓN", f"Andá directo al capítulo 2: tenés 15 días corridos desde la notificación para apelar por \"Presentaciones digitales\"."))
    f.append(PageBreak())

    f += cap("1", "LAS TRES SALIDAS", "Exclusión, renuncia y baja", "No es lo mismo irte vos que te saquen.")
    f.append(tabla(["Salida", "Qué es", "Qué implica"], [
        ("Exclusión (de pleno derecho)", "ARCA te saca porque se da alguna causal: superaste un parámetro, hay gastos o depósitos incompatibles, etc.", "No podés volver durante 3 años calendario. Pasás al régimen general."),
        ("Exclusión voluntaria / renuncia", "Pasaste los parámetros o estás por pasarlos y decidís irte antes, sin esperar el control.", "Tampoco podés volver por 3 años calendario, pero accedés a beneficios del pasaje (capítulo 6)."),
        ("Baja por cese de actividades", "Dejás de trabajar como monotributista.", "Podés volver a darte de alta cuando quieras."),
        ("Baja de oficio", "ARCA te da de baja por falta de pago durante 10 meses consecutivos.", "Para reingresar hay que cancelar la deuda o tener un plan de pagos; no es automático.")],
        [40 * mm, 62 * mm, W - 2 * M - 102 * mm]))
    f.append(Spacer(1, 8))
    f.append(Tiles([("3 años", "para volver tras|exclusión o renuncia"), ("15 días", "para apelar una|exclusión sistémica"), ("10 días", "para el descargo tras|una fiscalización"), ("10 meses", "sin pagar:|baja de oficio")]))
    f.append(Spacer(1, 10))
    f.append(P("Los \"3 años calendario\" se cuentan de enero a diciembre desde la fecha de la exclusión o la renuncia. ARCA aclara que quienes quedaron excluidos de pleno derecho desde el 1 de enero de 2024 por los parámetros anteriores a la Ley 27.743 pueden volver a adherirse, <b>por única vez</b>, sin esperar los 3 años, si reúnen los requisitos vigentes."))
    f.append(P("La baja por cese se hace desde el portal de monotributo, opción \"Modificación y baja\". El mes en que la pedís debe quedar pago; la baja rige desde el mes siguiente, y con ella terminan también los aportes de jubilación y obra social del monotributo.", "nota"))
    f.append(PageBreak())

    f += cap("2", "POR QUÉ TE PUEDEN EXCLUIR", "Las causales publicadas por ARCA", "Revisalas una por una: algunas no tienen que ver con facturar mucho.")
    f.append(Checklist(["Los <b>ingresos brutos</b> superan el máximo de la categoría más alta disponible.", "La <b>superficie o el costo de alquiler</b> superan los máximos de la categoría más alta.", "El <b>precio unitario de venta</b> supera el máximo permitido.", "Compraste <b>bienes o hiciste gastos personales</b> incompatibles con los ingresos declarados y sin justificar.", "Tus <b>depósitos bancarios</b> son incompatibles con los ingresos declarados para categorizarte.", "Hiciste <b>importaciones</b> de bienes o servicios para comercializarlos.", "Desarrollás <b>más de 3 actividades</b> simultáneas o tenés más de 3 unidades de explotación.", "Te categorizaste como venta de bienes cuando prestás <b>servicios</b>.", "Hay <b>operaciones sin facturar</b>.", "Tus compras más gastos de la actividad igualan o superan el <b>80%</b> (bienes) o el <b>40%</b> (servicios, locaciones y obras) del máximo de ingresos de la categoría K.", "Figurás en el <b>registro de empleadores con sanciones laborales</b> (REPSAL)."], "CAUSALES DE EXCLUSIÓN (ARCA)"))
    f.append(Spacer(1, 8))
    f.append(H2("Cómo te avisan y cómo defenderte"))
    f.append(tabla(["Cómo se detecta", "Qué hacer", "Plazo"], [
        ("Controles sistémicos (cruce de datos)", "Se notifica en el Domicilio Fiscal Electrónico. Si no estás de acuerdo, apelá en \"Presentaciones digitales\", opción \"Exclusión de oficio del Monotributo – Apelación en término\".", "15 días desde la recepción"),
        ("Fiscalización presencial", "Un funcionario te notifica y pone a disposición las pruebas. Presentás el descargo; un juez administrativo resuelve y se puede apelar.", "10 días para el descargo; 15 para apelar")],
        [46 * mm, 82 * mm, W - 2 * M - 128 * mm]))
    f.append(P("Pasado el plazo existe la opción \"Recurso fuera de término\" en el mismo servicio. Mirá el Domicilio Fiscal Electrónico con frecuencia: las notificaciones corren aunque no las leas.", "nota"))
    f.append(PageBreak())

    f += cap("3", "QUÉ CAMBIA", "El régimen general en una página", "Dejás de pagar una cuota única y empezás a manejar varias obligaciones.")
    f.append(tabla(["", "Monotributo", "Régimen general (autónomo)"], [
        ("Impuestos", "Una cuota mensual que reemplaza IVA y Ganancias.", "IVA y Ganancias por separado, más Ingresos Brutos provincial."),
        ("Jubilación", "Incluida en la cuota.", "Aporte mensual fijo de autónomos, según categoría."),
        ("Obra social", "Incluida en la cuota.", "Hay que elegirla y pagarla aparte."),
        ("Factura", "Factura C, sin discriminar IVA.", "Factura A o B (o E si exportás), con IVA discriminado."),
        ("Declaraciones", "Recategorización semestral.", "Declaración mensual de IVA y anual de Ganancias."),
        ("Contador", "Generalmente opcional.", "Prácticamente necesario.")],
        [30 * mm, 58 * mm, W - 2 * M - 88 * mm]))
    f.append(Spacer(1, 8))
    f.append(P("Según ARCA, el régimen de personas humanas (autónomos) es el que corresponde a quien realiza una actividad económica de forma habitual, personal y directa a título lucrativo, sin contrato de trabajo. <b>Previsionalmente</b> aporta un monto mensual fijo según su categoría; <b>impositivamente</b> queda alcanzado por el régimen general, con alta como mínimo en Ganancias e IVA. Debe facturar todas sus operaciones y, de corresponder, inscribirse en Bienes Personales y como empleador."))
    f.append(consejo("EL EFECTO DEL IVA", "Si vendés a consumidores finales, el precio que cobrás ya tiene el IVA adentro: pasás a quedarte con el precio dividido 1,21. Un producto de $ 121.000 deja $ 100.000 y $ 21.000 son IVA. Si podés subir precios, o si tus clientes son empresas que descuentan IVA, el impacto cambia."))
    f.append(PageBreak())

    f += cap("4", "CUÁNTO CUESTA", "Aportes de autónomo y una cuenta de ejemplo", "Los números oficiales de ARCA, vigentes desde el 15/10/2026.")
    f.append(P("ARCA publicó los aportes de autónomos que rigen desde el <b>15 de octubre de 2026</b>. Las categorías mínimas de revista van de la I a la V:"))
    f.append(tabla(["Categoría", "Aporte mensual", "Renta de referencia"], [
        ("I", "$ 78.271,56", "$ 244.598,64"), ("II", "$ 109.578,51", "$ 342.432,85"), ("III", "$ 156.541,75", "$ 489.192,97"), ("IV", "$ 250.466,70", "$ 782.708,42"), ("V", "$ 344.390,34", "$ 1.076.219,83")],
        [40 * mm, 60 * mm, W - 2 * M - 100 * mm]))
    f.append(P("La categoría se determina por la actividad y los ingresos del año anterior; al inscribirte hay una categorización inicial según la actividad y cada mayo se recategoriza con los ingresos brutos del año anterior (ARCA). La tabla de categorías más altas está en el sitio de ARCA, sección Autónomos.", "nota"))
    f.append(H2(f"Ejemplo: servicios en la categoría K"))
    cuotak = k[2]; tope = k[1]
    f.append(P(f"Un freelancer en la categoría K paga por mes {_f(cuotak)} (escala de agosto 2026 a enero 2027), o {_f(cuotak * 12)} al año, y el tope de facturación anual es {_f(tope)}. En el régimen general, si factura el mismo monto a consumidores finales con el IVA incluido, el IVA que debe ingresar es el débito fiscal (21% sobre el precio neto) menos el crédito de sus compras; sumá los aportes de autónomo, Ganancias, Ingresos Brutos y los honorarios del contador. La calculadora de la web hace la cuenta con tus números."))
    f.append(Barra(f"Ejemplo: facturación de {_f(tope)} con IVA incluido, vendiendo a consumidor final (millones de $)", [("Te queda sin IVA", round(tope / 1.21 / 1e6, 1), CEL), ("IVA", round(tope * 0.21 / 1.21 / 1e6, 1), SELLO)], "$ M"))
    f.append(P("El ejemplo muestra solo el efecto del IVA sobre un precio que ya lo incluye, sin descontar el crédito fiscal de tus compras, Ganancias, Ingresos Brutos ni aportes.", "nota"))
    f.append(consejo("LA CALCULADORA DE LA WEB", "Cargá tu facturación, tus compras y tu tipo de clientes: kit-monotributo.fernandezfrancowork.workers.dev/salir-del-monotributo-cuanto-cuesta"))
    f.append(PageBreak())

    f += cap("5", "CÓMO HACER EL PASAJE", "Pasos ordenados", "El orden evita períodos sin cobertura o facturas mal emitidas.")
    f.append(Flujo([("Decidir|el momento", "Mejor a fin de|mes o cuatrimestre"), ("Baja del|monotributo", "Portal de|monotributo"), ("Alta en|autónomos", "Sistema Registral|Empadronamiento"), ("Alta en|IVA y Ganancias", "Régimen general|(Sistema Registral)"), ("Facturar|con IVA", "Punto de venta|y comprobante")], CEL))
    f.append(Spacer(1, 10))
    f += E(["<b>Hablá con un contador</b> y definí la fecha: conviene coordinar el pasaje con el cierre de un mes.", "<b>Pagá el monotributo del mes</b> en que pedís la baja: ARCA aclara que ese mes debe quedar pago.", "<b>Pedí la baja o renuncia</b> desde el portal de monotributo, opción \"Modificación y baja\", indicando el motivo.", "<b>Inscribite como autónomo</b>: con CUIT y clave fiscal, servicio \"Sistema Registral\", menú \"Registro tributario\", opción \"Empadronamiento autónomos\". El sistema genera la credencial de pago con tu Código de Registro Autónomo (CRA).", "<b>Dá el alta en Ganancias e IVA</b> (ARCA tiene la guía \"¿Cómo registro las altas y bajas de impuestos y/o regímenes?\").", "<b>Revisá tu punto de venta</b> y los comprobantes: pasás a emitir Factura A o B, con IVA discriminado. Un contador te ayuda con el alta de los puntos de venta.", "<b>Registrate en Ingresos Brutos</b> en tu provincia o ciudad (regímenes y plazos propios).", "<b>Avisá a tus clientes</b>: cambia el tipo de factura y, si corresponde, el precio."])
    f.append(P("Los nombres de los servicios pueden cambiar en ARCA. Si alguno no aparece, buscalo en el buscador del sitio o en \"Administrador de relaciones de clave fiscal\".", "nota"))
    f.append(PageBreak())

    f += cap("6", "BENEFICIOS DEL PASAJE", "Lo que ARCA te devuelve si salís ordenado", "Aplica a quienes se excluyen o renuncian desde 2022 y cumplen una condición.")
    f.append(P("Según ARCA, quienes a partir del 1 de enero de 2022 sean excluidos o renuncien al monotributo para inscribirse en el régimen general, <b>siempre que sus ingresos brutos de los 12 meses anteriores a la solicitud no superen el 50% del límite de ventas anuales establecido para las microempresas</b>, tienen estos beneficios:"))
    f += L(["<b>IVA</b>: pueden sumar al crédito fiscal del período el IVA que les facturaron en los 12 meses anteriores, siempre que las compras estén relacionadas con la actividad.", "<b>Ganancias</b>: pueden deducir como gasto las compras de los 12 meses anteriores (netas de IVA) relacionadas con la actividad."])
    f.append(P("Además, quienes <b>comunicaron voluntariamente</b> su exclusión o renuncia (desde el 1 de enero de 2021) tienen una reducción del saldo deudor de IVA (débito menos crédito) durante 3 años: <b>50% el primer año, 30% el segundo y 10% el tercero</b>, desde el primer mes del año siguiente a la exclusión o renuncia."))
    f.append(Tiles([("50%", "reducción del saldo|de IVA, año 1"), ("30%", "año 2"), ("10%", "año 3")]))
    f.append(Spacer(1, 10))
    f.append(alerta("LA RENUNCIA VOLUNTARIA PUEDE SER MEJOR", "Si ya sabés que vas a superar el tope, renunciar antes de que te excluyan te da el beneficio de reducción de IVA, que la exclusión de oficio no incluye. Confirmá con tu contador si cumplís la condición del 50%."))
    f.append(PageBreak())

    f += cap("7", "CÓMO NO PASARTE", "Controlá el tope y las causales cada mes", "Salir cuando vos decidís es muy distinto a que decida ARCA.")
    f += L(["<b>Anotá cada mes</b> cuánto facturaste en los últimos 12 meses y compará con el tope de tu categoría y con el de la K.", "<b>Alerta temprana</b>: si superás el 80% del tope de la K, empezá a hablar con tu contador.", "<b>Mirá el mismo mes del año anterior</b>: las ventas de un solo mes alto pueden empujarte.", "<b>Controlá los depósitos</b> de tus cuentas y billeteras: si no coinciden con tus ingresos, puede disparar una causal.", "<b>Mantené las compras y los gastos</b> de la actividad dentro de los porcentajes del 80% y el 40% de la categoría K.", "<b>Facturá todo</b>: las operaciones sin factura son causal de exclusión."])
    f.append(consejo("LA RECATEGORIZACIÓN DE FEBRERO", "Cada semestre ARCA te pide recategorizar. Hacelo con las escalas vigentes: hay una calculadora gratis en la web (kit-monotributo.fernandezfrancowork.workers.dev/recategorizacion-monotributo-febrero-2027)."))
    f.append(PageBreak())

    f += cap("8", "ERRORES FRECUENTES", "Los que más cuestan")
    f += L(["<b>Esperar a que te excluyan</b> y perder el beneficio de la renuncia voluntaria.", "<b>No leer el Domicilio Fiscal Electrónico</b>: la notificación corre y el plazo de apelación se pierde.", "<b>Seguir facturando con Factura C</b> después del pasaje.", "<b>No ajustar precios</b> y regalar el IVA.", "<b>No separar el IVA</b> de lo que cobrás: es plata del Estado, no tuya.", "<b>Dejar de pagar el monotributo del mes de la baja</b>.", "<b>Pasar sin contador</b> y descubrir meses después una declaración sin presentar.", "<b>Olvidar la obra social</b> al dejar el monotributo.", "<b>No avisar a clientes</b> que necesitan la factura A."])
    f.append(P("Si ya pasó: pedí asesoramiento y regularizá lo antes posible. Los intereses corren desde el vencimiento.", "nota"))
    f.append(PageBreak())

    f += cap("9", "PLAN DE 90 DÍAS", "Checklist de preparación")
    f.append(Checklist(["<b>Mes 1</b>: sumar tus ingresos de los últimos 12 meses y compararlos con el tope.", "<b>Mes 1</b>: revisar las causales del capítulo 2, una por una.", "<b>Mes 1</b>: consultar con un contador y pedir presupuesto de honorarios.", "<b>Mes 2</b>: calcular con la calculadora de la web el costo de salir (IVA, aportes).", "<b>Mes 2</b>: decidir si renunciás voluntariamente (capítulo 6) o seguís hasta el tope.", "<b>Mes 2</b>: definir la obra social y la categoría de autónomos.", "<b>Mes 3</b>: pedir la baja o renuncia, inscribirte en autónomos, IVA, Ganancias e Ingresos Brutos.", "<b>Mes 3</b>: actualizar precios y comunicar a tus clientes el cambio de factura."], "CHECKLIST"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("Exclusión de pleno derecho", "Baja del monotributo por una causal prevista en la ley."),
        ("Renuncia", "Dejar el monotributo por decisión propia para pasar al régimen general."),
        ("Régimen general", "Régimen con IVA y Ganancias, sin cuota unificada."),
        ("CRA", "Código de Registro Autónomo."),
        ("Crédito fiscal", "El IVA que te facturaron en las compras."),
        ("Débito fiscal", "El IVA que vos facturás en las ventas."),
        ("REPSAL", "Registro Público de Empleadores con Sanciones Laborales."),
        ("Domicilio Fiscal Electrónico", "Buzón de notificaciones de ARCA.")], [48 * mm, W - 2 * M - 48 * mm]))
    f.append(H2("Fuentes"))
    f += L(["ARCA, Monotributo, Ayuda: Baja, Exclusión, De oficio, Renuncia y Pasaje al régimen general (arca.gob.ar/monotributo/ayuda).", "ARCA, Autónomos: inscripción y valores vigentes desde el 15/10/2026 (arca.gob.ar/autonomos).", "ARCA, Régimen general, personas humanas.", "Ley 27.743 (parámetros del monotributo), según ARCA."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento contable, impositivo ni legal y no reemplaza a un contador ni a la información oficial de ARCA. Las normas, las escalas y los montos pueden cambiar. No incluye alícuotas de Ganancias ni de Ingresos Brutos, que dependen de cada caso y jurisdicción. Está prohibida su reventa o redistribución.", "nota"))
    return f
