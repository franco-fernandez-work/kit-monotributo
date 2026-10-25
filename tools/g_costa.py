"""Guía 'Vender en la costa o en ferias' (HUECOS.md #21). Fuentes: argentina.gob.ar/elmercadoentubarrio/feriantes (requisitos del programa nacional: constancia de inscripción en AFIP sin deuda, habilitación municipal, permisos de puestos móviles, certificado de reincidencia, controles de Bromatología, SENASA y AFIP);
notas de prensa sobre cupos y cánones municipales de temporada (Las Grutas, Mar del Plata: ordenanzas locales). NO verificado: requisitos y montos de cada municipio (cambian por localidad y temporada), tasas, cuota de monotributo vigente (ver la calculadora del sitio), reglas de monotributo social."""
from guias_lib import *

META = dict(nombre="Vender en la costa o en ferias", etiqueta="GUÍA PRÁCTICA · TEMPORADA 2026/2027",
            titulo=["Vender en la costa", "o en ferias"], sub=["Papeles, precio, cobros y números", "para salir a vender en la temporada."],
            sello="11", sello2="PÁGINAS", cabecera="VENDER EN LA COSTA O EN FERIAS",
            pie="Información general. Verificá la ordenanza de tu municipio.")

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien quiere vender en la costa, en una feria o en un puesto temporal durante el verano.")
    f.append(P("Vender en temporada es una oportunidad corta: hay meses de ventas fuertes y muchos gastos fijos antes de vender el primer producto. Esta guía te ordena los <b>papeles</b>, el <b>precio</b>, los <b>cobros</b> y la <b>cuenta</b> para saber, antes de gastar, cuántas unidades tenés que vender para no perder plata."))
    f.append(alerta("LAS REGLAS LAS FIJA CADA MUNICIPIO", "Los cupos, cánones, rubros permitidos y fechas cambian por localidad y por temporada. Esta guía explica qué preguntar y en qué orden; los datos de tu lugar los confirmás en la municipalidad. No es asesoramiento legal ni contable."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Dónde y qué vender", "Playa, feria, puesto fijo temporal o venta online."),
        ("2. Papeles", "Monotributo, habilitación, permisos y controles."),
        ("3. Precio y costos", "Margen, punto de equilibrio y ejemplo con números."),
        ("4. Cobrar", "Efectivo, transferencia, QR y factura."),
        ("5. Stock y logística", "Cuánto llevar y cómo no quedarte sin nada."),
        ("6. Calendario", "Qué hacer de octubre a marzo."),
        ("7. Errores frecuentes", "Los que más cuestan."),
        ("Anexo", "Checklist, preguntas para la municipalidad y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("LA CALCULADORA GRATIS", f"Calculá tu punto de equilibrio: {BASE_URL}/vender-en-la-costa-feria-punto-de-equilibrio"))
    f.append(PageBreak())

    f += cap("1", "DÓNDE Y QUÉ VENDER", "Cuatro formas de vender en temporada", "Cada una tiene costos, permisos y riesgos distintos.")
    f.append(tabla(["Forma", "Ventaja", "Riesgo"], [
        ("Venta ambulante en playa", "Sin alquiler de local; ventas por impulso.", "Cupos limitados, canon de temporada y control municipal. Puede estar restringida a ciertos productos."),
        ("Feria o paseo de artesanos", "Público que ya va a comprar; infraestructura armada.", "Hay que ser aceptado por reglamento; algunos exigen residencia o inscripciones específicas."),
        ("Puesto o local temporal", "Más control: luz, techo, vidriera.", "Alquiler y habilitación; gasto fijo alto antes de vender."),
        ("Online con retiro o envío", "No dependés del clima.", "Competencia y logística de envío.")], [40 * mm, 60 * mm, W - 2 * M - 100 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Elegí un producto que ya sepas hacer o comprar bien</b>: en temporada no hay tiempo para aprender.", "<b>Buscá margen, no solo ventas</b>: un producto barato de comprar y fácil de transportar rinde más que uno que se rompe o ocupa mucho.", "<b>Mirá quién vende lo mismo</b> en el lugar elegido y a qué precio: es tu techo.", "<b>Evitá los rubros más regulados</b> al empezar (comida, alcohol, cosmética): exigen controles sanitarios y permisos adicionales."])
    f.append(consejo("PROBÁ CON POCO", "Si es tu primera temporada, empezá con un solo producto y una sola forma de venta. Con lo que aprendas, ampliás."))
    f.append(PageBreak())

    f += cap("2", "PAPELES", "Qué necesitás para vender legalmente", "El orden importa: primero quién sos para ARCA, después dónde podés vender.")
    f.append(Flujo([("1", "Alta en|monotributo"), ("2", "Actividad y|categoría"), ("3", "Habilitación|municipal"), ("4", "Permisos|del rubro"), ("5", "Factura y|cobro")], CEL))
    f.append(Spacer(1, 10))
    f.append(H2("Monotributo"))
    f.append(P("Para vender de manera habitual necesitás estar inscripto en ARCA. El programa nacional de ferias (El Mercado en tu Barrio) pide a los feriantes la <b>constancia de inscripción en AFIP (hoy ARCA) y no tener deuda con el organismo</b>. Ante la duda sobre si tu venta ocasional requiere inscripción, consultá a un contador."))
    f += L(["<b>El alta</b> se hace en ARCA con Clave Fiscal. Elegís la actividad (venta de cosas muebles, servicios, o ambas) y la categoría según tus ingresos de los últimos 12 meses y otros parámetros.", "<b>La cuota se paga todos los meses</b> mientras estés inscripto, también los meses sin ventas. Calculá cuántos meses la vas a pagar antes de decidir.", "<b>Factura</b>: emitís comprobantes electrónicos desde la web de ARCA.", f"<b>Categoría</b>: para ver los topes y cuotas vigentes usá la tabla del sitio ({BASE_URL}/escalas-monotributo-2026). Si tus ventas de temporada te acercan al tope, mirá la guía Salir del monotributo."])
    f.append(P("El monotributo social es otra vía, pensada para personas en situación de vulnerabilidad y emprendimientos de la economía popular. Sus requisitos no fueron verificados en esta guía: consultalos en argentina.gob.ar.", "nota"))
    f.append(PageBreak())

    f.append(H2("Habilitación municipal y permisos"))
    f.append(P("Vender en la vía pública o en un espacio municipal requiere permiso. Lo que dicen las fuentes consultadas: el programa nacional de ferias pide <b>habilitación municipal, permisos para puestos móviles y seguridad e higiene</b>. En la costa, las notas de prensa muestran que algunos municipios otorgan un <b>número limitado de permisos</b> para la venta en playa, con <b>canon</b> por temporada y lista de productos autorizados."))
    f += L(["<b>Preguntá en la municipalidad</b> (oficina de habilitaciones, comercio o inspección general) antes de comprar mercadería.", "<b>Fechas de inscripción</b>: los cupos se asignan antes de la temporada. Llegar tarde puede dejarte afuera.", "<b>Documentación habitual</b>: DNI, constancia de ARCA, certificado de reincidencia, domicilio y, en comida, libreta sanitaria o curso de manipulación de alimentos.", "<b>Residencia</b>: algunas ordenanzas piden años de residencia en el partido (por ejemplo, una ordenanza de feriantes de Mar del Plata, según prensa)."])
    f.append(H2("Rubros con controles extra"))
    f += L(["<b>Comida</b>: Bromatología, manipulación de alimentos y a veces vehículo habilitado. En playa, el alcohol suele estar prohibido.", "<b>Productos importados o con marca</b>: no vendas falsificaciones. Hay controles y sanciones.", "<b>Artesanías</b>: algunas ferias exigen que sean de producción propia."])
    f.append(alerta("VENTA SIN PERMISO", "La venta sin permiso puede terminar en decomiso de la mercadería y multa, y te deja sin respaldo ante cualquier conflicto. Gestioná el permiso antes de comprar el stock."))
    f.append(PageBreak())

    f += cap("3", "PRECIO Y COSTOS", "Cuánto tenés que vender para no perder", "El punto de equilibrio es el número más importante de tu temporada.")
    f.append(P("Dos tipos de gasto: los <b>costos variables</b> (lo que te cuesta cada producto y la comisión de cobro) y los <b>costos fijos</b> (canon o permiso, alojamiento, transporte, monotributo de los meses, puesto). Cada unidad deja un <b>margen</b> = precio − costo variable. El punto de equilibrio es <b>costos fijos ÷ margen por unidad</b>."))
    f.append(tabla(["Concepto", "Ejemplo", "Tipo"], [
        ("Precio de venta", "$ 12.000", "—"),
        ("Costo de cada producto", "$ 5.000", "Variable"),
        ("Comisión de cobro (3%)", "$ 360", "Variable"),
        ("Margen por unidad", "$ 6.640", "Resultado"),
        ("Permiso o canon", "$ 200.000", "Fijo"),
        ("Alojamiento y traslado", "$ 600.000", "Fijo"),
        ("Monotributo (3 meses) y otros", "$ 150.000", "Fijo"),
        ("Total fijos", "$ 950.000", "Fijo"),
        ("Punto de equilibrio", "$ 950.000 ÷ $ 6.640 = 144 unidades", "Resultado")], [58 * mm, 60 * mm, W - 2 * M - 118 * mm]))
    f.append(P("Los valores son ejemplos para mostrar la cuenta. Reemplazalos por los tuyos en la calculadora de la web.", "nota"))
    f.append(Barra("Ejemplo: unidades vendidas contra punto de equilibrio (144)", [("Pérdida: 100 un.", 100, SELLO), ("Equilibrio", 144, CEL), ("Ganancia: 250 un.", 250, CEL)], "unidades"))
    f += L(["<b>Poné un precio que cubra el margen</b>, no solo el del vecino: si tu costo es mayor, tu diferencial tiene que ser otro (calidad, diseño, combo).", "<b>Hacé combos</b> de 2 o 3 unidades: suben el ticket promedio.", "<b>Estimá los días reales de venta</b>: lluvia, viento y semanas flojas. Calculá con un escenario pesimista."])
    f.append(PageBreak())

    f += cap("4", "COBRAR", "Que no se te escape una venta por no tener cómo cobrar", "En la playa mucha gente no lleva efectivo.")
    f.append(tabla(["Medio", "Para qué sirve", "Cuidado con"], [
        ("Efectivo", "Rápido, sin comisión.", "Vueltos, billetes falsos, seguridad del dinero."),
        ("Transferencia con alias", "Gratis y simple.", "Verificar que la acreditación llegó antes de entregar el producto."),
        ("QR de billetera virtual", "Cobro inmediato con la app del cliente.", "Comisión según el proveedor; confirmala antes de fijar precios."),
        ("Posnet o lector", "Tarjeta de débito y crédito.", "Comisiones y plazos de acreditación; conviene comparar antes de la temporada.")], [40 * mm, 58 * mm, W - 2 * M - 98 * mm]))
    f.append(Spacer(1, 8))
    f += L(["<b>Poné un cartel con el alias y el QR</b> bien visibles, y tené un respaldo en el celular.", "<b>Anotá las ventas todos los días</b> (cuánto, qué medio de cobro): te sirve para la categoría del monotributo y para saber cómo vas.", "<b>Verificá siempre la acreditación</b> en tu app, no el comprobante que muestra el cliente.", "<b>Comisiones</b>: confirmalas en cada proveedor antes de calcular precios; cambian. Ponelas en la calculadora."])
    f.append(consejo("QR PARA TU PUESTO", f"Si querés que tu QR lleve al catálogo o a tu Instagram y poder cambiar el destino sin reimprimir: {BASE_URL}/qr"))
    f.append(PageBreak())

    f += cap("5", "STOCK Y LOGÍSTICA", "Cuánto llevar y cómo moverte", "Sobrestockearte te inmoviliza plata; quedarte corto te saca ventas.")
    f += E(["<b>Armá un stock inicial</b> equivalente a 3 a 4 semanas de ventas pesimistas, no optimistas.", "<b>Reponé por semana</b> con las ventas reales; anotá qué se vendió más.", "<b>Dejá un colchón</b> para imprevistos: clima, devolución, un día de feriado largo.", "<b>Transporte</b>: calculá el costo de cada viaje y de guardar la mercadería. Un producto liviano reduce ambos.", "<b>Seguridad</b>: no dejes mercadería ni plata sin cuidado; un candado y una lista de stock ayudan.", "<b>Plan para el sobrante</b>: liquidar en la última semana, vender online o guardar para el año próximo."])
    f.append(P("Tip: llevá un cuaderno o una planilla con tres columnas: cuánto llevaste, cuánto vendiste y cuánto queda. Al cierre de cada día, en 5 minutos sabés cómo viniste.", "nota"))
    f.append(PageBreak())

    f += cap("6", "CALENDARIO", "De octubre a marzo", "Los permisos llegan antes de la temporada; las ventas, después.")
    f.append(Flujo([("Oct-nov", "Elegir lugar|y producto"), ("Nov-dic", "Permisos|y compras"), ("Dic", "Armar puesto|y probar"), ("Ene-feb", "Pico de|ventas"), ("Mar", "Cierre y|balance")], CEL))
    f.append(Spacer(1, 10))
    f.append(Checklist(["<b>Octubre-noviembre</b>: definí el lugar y consultá en la municipalidad por cupos, canon y fechas de inscripción.", "<b>Octubre-noviembre</b>: hacé la cuenta del punto de equilibrio con tres escenarios.", "<b>Noviembre-diciembre</b>: alta en monotributo (si no estás) y gestión del permiso.", "<b>Diciembre</b>: comprá el stock inicial, armá el puesto y probá cobros.", "<b>Enero-febrero</b>: vendé, anotá las ventas diarias y reponé por semana.", "<b>Fin de febrero-marzo</b>: cerrá la temporada, calculá la ganancia real y decidí si seguís, si te pasás de categoría o si te das de baja."], "CALENDARIO"))
    f.append(PageBreak())

    f += cap("7", "ERRORES FRECUENTES", "Los que más cuestan")
    f += L(["<b>Comprar stock antes de tener el permiso</b>.", "<b>Calcular solo con el escenario optimista</b> de ventas.", "<b>No sumar el monotributo de los meses sin ventas</b>.", "<b>No tener cómo cobrar</b> con QR o transferencia.", "<b>No anotar las ventas</b> y llegar a marzo sin saber si ganaste.", "<b>Poner el precio mirando solo al vecino</b>, sin calcular el margen propio.", "<b>Ignorar el clima</b>: tené un plan para los días de lluvia.", "<b>Vender rubros regulados sin papeles</b> (comida, alcohol)."])
    f.append(P("Si recibís una multa o un decomiso, pedí el acta y consultá a un abogado o a la oficina de defensa del consumidor de tu municipio antes de contestar.", "nota"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Checklist y preguntas para la municipalidad")
    f.append(H2("Preguntas para hacer en la municipalidad"))
    f += L(["¿Hay permisos para mi rubro y ubicación? ¿Cuántos cupos hay y cómo se asignan?", "¿Cuál es el canon o tasa de la temporada y cómo se paga?", "¿Qué documentación piden y hasta qué fecha se presenta?", "¿Hay requisitos de residencia o inscripciones especiales?", "¿Qué productos están permitidos y cuáles prohibidos?", "¿Qué controles hay (Bromatología, Inspección General) y qué piden?", "¿Cuáles son los horarios y las zonas permitidas?"])
    f.append(H2("Checklist final"))
    f.append(Checklist(["Monotributo al día y actividad correcta.", "Permiso o habilitación en mano (copia en papel y en el celular).", "Cuenta del punto de equilibrio hecha con tres escenarios.", "Cobro por QR y transferencia probado.", "Stock inicial calculado y plan de reposición.", "Cuaderno o planilla de ventas diaria."], "ANTES DE SALIR"))
    f.append(H2("Fuentes"))
    f += L(["Programa El Mercado en tu Barrio, requisitos para feriantes: argentina.gob.ar/elmercadoentubarrio/feriantes (constancia de inscripción en AFIP sin deuda, habilitación municipal, permisos de puestos móviles, certificado de reincidencia, controles de Bromatología, SENASA y AFIP).", "Prensa local sobre permisos de playa y ordenanzas de feriantes (Las Grutas, Mar del Plata): ejemplos de cupos, canon y requisitos de residencia que varían por municipio y temporada. No verificados en las ordenanzas originales.", "Valores de comisiones, tasas y cuotas: no incluidos porque cambian; confirmalos con cada proveedor y en arca.gob.ar."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal, contable ni impositivo. Las normas municipales cambian por localidad y por temporada. Está prohibida su reventa o redistribución.", "nota"))
    return f
