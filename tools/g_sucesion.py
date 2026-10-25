"""Guía 'Sucesión sin perder tiempo' (HUECOS.md #14). Normativa verificada en Infoleg, texto del Código Civil y Comercial (Ley 26.994), Libro Quinto:
arts. 2277, 2280, 2288, 2289, 2301, 2317, 2321, 2335-2342, 2383, 2424-2439, 2445, 2310-2311. NO verificado: tasa de justicia, honorarios, impuesto provincial y trámites por jurisdicción."""
from guias_lib import *

META = dict(nombre="Sucesión sin perder tiempo", etiqueta="GUÍA PRÁCTICA · ACTUALIZADA A OCTUBRE DE 2026",
            titulo=["Sucesión sin", "perder tiempo"], sub=["Quién hereda, qué papeles juntar, qué pasos seguir", "y qué plazos del Código Civil conviene conocer."],
            sello="HERENCIA", sello2="PASO A PASO", cabecera="SUCESIÓN SIN PERDER TIEMPO",
            pie="Información general. No reemplaza a un abogado: la sucesión es un trámite judicial.", tam=44)

def contenido():
    f = []
    f += cap("0", "ANTES DE EMPEZAR", "Cómo usar esta guía", "Para quien perdió a un familiar y tiene que ordenar papeles, plazos y decisiones sin conocer el proceso.")
    f.append(P("Una sucesión es el trámite por el que los bienes, derechos y deudas de una persona fallecida pasan a sus herederos. En general es <b>un juicio</b>, y casi siempre conviene contar con un abogado. Esta guía no lo reemplaza: te explica <b>quién hereda según el Código Civil y Comercial</b>, <b>qué papeles ir juntando</b> y <b>en qué orden pasan las cosas</b>, para que llegues a la primera reunión sabiendo qué preguntar y para que ahorres tiempo y plata."))
    f.append(alerta("LO QUE ESTA GUÍA NO HACE", "No calcula honorarios ni tasas y no sustituye a un profesional. Los trámites, los costos y algunos impuestos dependen de la provincia y del juzgado: los marcamos para que los consultes. Los artículos citados son del Código Civil y Comercial (Libro Quinto), texto de Infoleg."))
    f.append(tabla(["Capítulo", "Qué resuelve"], [
        ("1. Qué pasa cuando alguien fallece", "Qué se transmite y desde cuándo."),
        ("2. Quién hereda", "Órdenes, cónyuge y porciones sin testamento."),
        ("3. Con testamento", "La legítima y qué se puede dejar libremente."),
        ("4. Los papeles", "Checklist para empezar y para los bienes."),
        ("5. El trámite paso a paso", "Del certificado de defunción a la inscripción."),
        ("6. Costos e impuestos", "Qué gastos hay y cómo averiguarlos."),
        ("7. Plazos que importan", "Aceptación, renuncia, inventario."),
        ("8. Casos frecuentes", "La casa, las deudas, los hermanos, el conviviente."),
        ("9. Errores y plan de 30 días", "Qué evitar y por dónde empezar."),
        ("Anexo", "Glosario y fuentes.")], [52 * mm, W - 2 * M - 52 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("SI ESTÁS ATRAVESANDO ESTO AHORA", "No tenés que resolver todo esta semana. Empezá por el capítulo 4 (papeles) y el 9 (plan de 30 días). Lo urgente suele ser el certificado de defunción y la lista de bienes."))
    f.append(PageBreak())

    f += cap("1", "LO BÁSICO", "Qué pasa cuando alguien fallece", "La ley transmite la herencia desde el día de la muerte, aunque el trámite lleve meses.")
    f.append(P("Según el art. 2277 del Código Civil y Comercial, <b>la muerte real o presunta de una persona causa la apertura de su sucesión y la transmisión de su herencia</b> a las personas llamadas por el testamento o por la ley. La herencia comprende <b>todos los derechos y obligaciones del causante</b> que no se extinguen por su fallecimiento: tanto los bienes como las deudas."))
    f.append(Tiles([("Día del|fallecimiento", "se abre la sucesión"), ("Juez del|último domicilio", "es el competente|(art. 2336)"), ("10 años", "para aceptar la herencia|(art. 2288)"), ("Hasta el|valor recibido", "responde el heredero|(art. 2317)")]))
    f.append(Spacer(1, 10))
    f += L(["<b>Desde el fallecimiento</b>, los herederos tienen todos los derechos y acciones del causante, de manera indivisa (art. 2280): hasta que se haga la partición, los bienes son de todos en conjunto.", "<b>Entre ascendientes, descendientes y cónyuge</b>, el heredero queda investido de su calidad desde la muerte, sin intervención de los jueces (art. 2337). El juicio sirve para <b>acreditarlo y poder disponer de los bienes</b> ante bancos y registros.", "<b>Competencia</b>: entiende el juez del último domicilio del causante (art. 2336), no el del lugar de los bienes.", "<b>Deudas</b>: el heredero responde por las deudas y legados solo hasta el valor de los bienes que recibe (art. 2317). Eso no es automático: si no hace el inventario cuando se lo intiman o oculta bienes, puede responder con su propio patrimonio (art. 2321)."])
    f.append(P("La sucesión también se abre por <b>ausencia con presunción de fallecimiento</b>. Esta guía se concentra en el caso común: fallecimiento con certificado de defunción.", "nota"))
    f.append(PageBreak())

    f += cap("2", "SIN TESTAMENTO", "Quién hereda", "Si no hay testamento (o no alcanza a todos los bienes), la ley fija el orden. Es lo más común.")
    f.append(P("Las sucesiones sin testamento van, en este orden, a los <b>descendientes</b>, los <b>ascendientes</b>, el <b>cónyuge</b> y los <b>colaterales</b> hasta el cuarto grado (art. 2424). Un orden excluye al siguiente, con una excepción: el cónyuge concurre con descendientes o con ascendientes."))
    f.append(tabla(["Quién queda", "Quién hereda y cuánto", "Artículo"], [
        ("Hijos (y nietos si algún hijo murió antes)", "Los hijos heredan por partes iguales. Los nietos heredan por representación lo que le tocaba a su padre o madre, sin límite de grados.", "2426-2429"),
        ("Hijos y cónyuge", "El cónyuge recibe la misma parte que un hijo, sobre los bienes propios del causante. No participa en los bienes gananciales que corresponden al fallecido.", "2433"),
        ("Sin hijos: padres o abuelos", "Heredan los ascendientes más próximos, por partes iguales.", "2431"),
        ("Padres o abuelos y cónyuge", "Al cónyuge le corresponde la mitad de la herencia.", "2434"),
        ("Solo cónyuge", "Hereda todo, con exclusión de los colaterales.", "2435"),
        ("Hermanos, sobrinos, tíos, primos", "Heredan los parientes hasta el cuarto grado. Los de grado más cercano excluyen a los lejanos; hermanos y sobrinos desplazan al resto.", "2438-2439"),
        ("Nadie", "Los bienes vacantes pasan al Estado nacional, provincial o a la Ciudad de Buenos Aires, según donde estén.", "2424")],
        [44 * mm, W - 2 * M - 68 * mm, 24 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("Ejemplo: cónyuge y dos hijos"))
    f.append(P("Una persona fallece dejando a su cónyuge y a dos hijos, y bienes propios por $ 90.000.000. El cónyuge tiene la misma parte que un hijo: <b>cada uno recibe un tercio, $ 30.000.000</b>. Si además hubiera una casa ganancial, primero se divide la sociedad conyugal: el cónyuge se queda con su mitad de lo ganancial por derecho propio, y solo la mitad del fallecido integra la herencia."))
    f.append(Barra("Reparto del ejemplo (bienes propios, en millones de $)", [("Cónyuge", 30, CEL), ("Hijo 1", 30, TINTA), ("Hijo 2", 30, OK_C)], "$ M"))
    f.append(Spacer(1, 6))
    f.append(consejo("EL CÓNYUGE Y LA CASA", "El cónyuge tiene derecho real de habitación vitalicio y gratuito sobre la vivienda que fue el último hogar conyugal, si era propiedad del causante y no estaba en condominio con terceros (art. 2383). No se pierde por falta de trámite, pero conviene inscribirlo."))
    f.append(P("El divorcio, la separación de hecho sin voluntad de unirse y la decisión judicial de cese de la convivencia <b>excluyen el derecho hereditario entre cónyuges</b> (art. 2437). Si el matrimonio fue en los 30 días previos a la muerte por una enfermedad preexistente conocida de desenlace previsible, el cónyuge tampoco hereda, salvo que haya una unión convivencial previa (art. 2436).", "nota"))
    f.append(PageBreak())

    f += cap("3", "CON TESTAMENTO", "La legítima y lo que se puede dejar libremente", "Un testamento no puede dejar sin nada a los herederos forzosos.")
    f.append(P("El art. 2445 fija las porciones legítimas: <b>dos tercios para los descendientes, un medio para los ascendientes y un medio para el cónyuge</b>. La parte restante se llama <b>porción disponible</b> y se puede dejar a quien se quiera. Las porciones se calculan sobre el valor neto de la herencia al momento de la muerte, más el valor de los bienes donados que sean computables."))
    f.append(Tiles([("2/3", "legítima de|los hijos"), ("1/2", "legítima de|los padres"), ("1/2", "legítima del|cónyuge"), ("1/3", "disponible con|hijos")]))
    f.append(Spacer(1, 10))
    f.append(Barra("Con hijos: legítima y porción disponible (sobre 100)", [("Legítima de los hijos", 66.7, CEL), ("Disponible", 33.3, OK_C)], "100"))
    f.append(Spacer(1, 6))
    f += L(["<b>Si hay hijos y cónyuge</b>, la legítima de los descendientes sigue siendo dos tercios y la libre disposición un tercio: los herederos forzosos concurren dentro de esa legítima.", "<b>Si el testamento afecta la legítima</b>, el heredero forzoso puede pedir su reducción (acción de reducción). Las donaciones también pueden reducirse si invadieron la legítima.", "<b>Formas del testamento</b>: por acto público (escritura ante escribano y dos testigos, art. 2479) u ológrafo (escrito entero, fechado y firmado de puño y letra del testador, art. 2477). Faltar a esas formas lo invalida.", "<b>Dónde buscarlo</b>: en la escribanía, entre los papeles del causante o en el registro de actos de última voluntad de la jurisdicción. Si es ológrafo, hay que presentarlo al juez, que verifica su autenticidad (art. 2339)."])
    f.append(alerta("TESTAMENTO ENCONTRADO", "No lo abras ni lo tires. Si es ológrafo y está cerrado, el juez ordena su apertura. Entregalo a tu abogado o presentalo en el juzgado."))
    f.append(PageBreak())

    f += cap("4", "LOS PAPELES", "Qué juntar y por dónde empezar", "Imprimí esta lista y tildala. Todo lo que juntes antes acorta la consulta con el abogado.")
    f.append(Checklist(["<b>Acta o certificado de defunción</b> (varias copias certificadas): es el primer documento de cualquier trámite.", "<b>DNI</b> del fallecido y de cada heredero.", "<b>Actas de nacimiento y de matrimonio</b> que prueben el vínculo (hijos, cónyuge, padres), con la partida del Registro Civil.", "<b>Último domicilio</b> del fallecido (define el juzgado): una factura o el DNI.", "<b>Testamento</b>, si existe, o certificado de que no hay inscripto.", "<b>Sentencia de divorcio</b> o acta de convivencia, si corresponde."], "SOBRE LAS PERSONAS"))
    f.append(Spacer(1, 6))
    f.append(Checklist(["<b>Inmuebles</b>: escritura, datos de la partida y deuda de impuestos y servicios.", "<b>Automotores</b>: título del automotor y cédula.", "<b>Cuentas y plazos fijos</b>: banco y número, saldo a la fecha de fallecimiento.", "<b>Acciones, fondos, inversiones</b>: resúmenes de la sociedad de bolsa o la billetera.", "<b>Sociedades</b>: contrato social, acciones o cuotas.", "<b>Seguros de vida</b>: póliza y beneficiarios (en general no integran la herencia).", "<b>Deudas</b>: tarjetas, préstamos, impuestos, alquileres, juicios en trámite."], "SOBRE LOS BIENES Y LAS DEUDAS"))
    f.append(Spacer(1, 6))
    f.append(P("Un bien registrable (inmueble, auto, acciones) <b>no se puede vender ni transferir</b> hasta que la declaratoria o la sentencia de adjudicación se inscriba en el registro correspondiente. Pedir <b>informes de dominio</b> a nombre del fallecido en el registro de la propiedad y del automotor te dice qué bienes figuran a su nombre."))
    f.append(PageBreak())

    f += cap("5", "EL TRÁMITE", "De la defunción a la inscripción", "El orden es parecido en todo el país; los detalles varían según el juzgado.")
    f.append(Flujo([("Certificado|de defunción", "Registro Civil"), ("Papeles y|abogado", "Checklist del|capítulo 4"), ("Inicio del|juicio", "Juzgado del último|domicilio"), ("Edicto y|publicación", "30 días para|presentarse"), ("Declaratoria", "Resolución|que nombra herederos")], CEL))
    f.append(Spacer(1, 10))
    f.append(Flujo([("Inventario|y avalúo", "Bienes y deudas|con su valor"), ("Pago de|impuestos y tasa", "Según la|jurisdicción"), ("Partición", "Entre todos los|herederos"), ("Adjudicación", "Cada bien a su|heredero"), ("Inscripción", "Registros de la|propiedad y automotor")], OK_C))
    f.append(Spacer(1, 10))
    f += E(["<b>Obtené el certificado de defunción</b> en el Registro Civil. Pedí varias copias.", "<b>Elegí abogado</b> y entregale los papeles. Pedí por escrito el presupuesto y la forma de pago de los honorarios.", "<b>Iniciá el juicio</b> ante el juez del último domicilio (art. 2336). Se pide la apertura, se acompaña el certificado y se denuncian los herederos conocidos.", "<b>Edicto</b>: se cita por un día en el diario de publicaciones oficiales a herederos, acreedores y a quienes se consideren con derecho, que tienen <b>treinta días</b> para acreditarlo (art. 2340).", "<b>Declaratoria de herederos</b> (o declaración de validez del testamento): reconoce a los herederos y permite pedir las inscripciones.", "<b>Inventario y avalúo</b> de los bienes (arts. 2341-2343). Los herederos pueden de común acuerdo reemplazarlo por una denuncia de bienes, salvo que lo pidan acreedores (art. 2342).", "<b>Partición y adjudicación</b>: si hay acuerdo entre todos, es rápida. Si no, la decide el juez.", "<b>Inscripción</b> de lo adjudicado en cada registro. Recién ahí se puede vender o transferir."])
    f.append(P("La duración depende del juzgado, de la cantidad de herederos y bienes, y de si hay conflictos o deudas. Un acuerdo entre herederos y los papeles al día son lo que más acelera.", "nota"))
    f.append(PageBreak())

    f += cap("6", "COSTOS E IMPUESTOS", "Qué se paga y cómo averiguarlo", "Acá la guía no inventa números: dependen de la jurisdicción y del valor de los bienes.")
    f.append(tabla(["Concepto", "Qué es", "Cómo averiguar"], [
        ("Tasa de justicia", "Un porcentaje sobre el valor de los bienes, que fija cada jurisdicción (en la justicia nacional, la Ley 23.898).", "Consultá el valor vigente con el juzgado o tu abogado."),
        ("Honorarios", "De abogados, peritos y otros profesionales. Los regulan las leyes arancelarias locales.", "Pedí presupuesto por escrito antes de empezar."),
        ("Aportes profesionales", "Cajas de abogados y escribanos.", "Se calculan sobre los honorarios y el valor."),
        ("Publicación del edicto", "Costo de publicar en el diario de publicaciones oficiales.", "Lo informa el juzgado."),
        ("Inscripciones", "Tasas de los registros de la propiedad y del automotor.", "Consultá en cada registro."),
        ("Impuesto a la transmisión gratuita", "Algunas provincias (por ejemplo, Buenos Aires) lo cobran sobre herencias. No hay un impuesto nacional a la herencia.", "Consultá en el organismo de rentas de la provincia (por ejemplo ARBA).")],
        [38 * mm, 70 * mm, W - 2 * M - 108 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("AHORRAR DE VERDAD", "Una sucesión sin conflictos, con papeles completos y un acuerdo entre herederos suele costar menos tiempo y menos honorarios. Lo más caro es el desacuerdo entre herederos."))
    f.append(alerta("DEUDAS DE IMPUESTOS", "Antes de aceptar bienes, pedí un estado de deuda de impuestos y servicios (inmuebles, automotor, ARCA). Las deudas del fallecido integran la herencia."))
    f.append(PageBreak())

    f += cap("7", "PLAZOS", "Los plazos que importan", "Los que figuran en el Código; los del juzgado los fija el juez.")
    f.append(tabla(["Plazo", "Qué significa", "Art."], [
        ("10 años desde la muerte", "Es el límite para aceptar la herencia. Si pasa sin aceptar, se considera que renunció.", "2288"),
        ("1 a 3 meses (renovable una vez)", "Si un interesado pide la intimación judicial a aceptar o renunciar, el heredero debe responder en ese plazo; si no responde, se lo considera aceptante. No puede pedirse antes de 9 días del fallecimiento.", "2289"),
        ("30 días", "Plazo del edicto para que se presenten herederos y acreedores.", "2340"),
        ("3 meses", "Para hacer el inventario desde que acreedores o legatarios lo intiman. Si no se hace, el heredero puede responder con sus bienes.", "2341, 2321"),
        ("Imprescriptible", "La petición de herencia: el heredero que fue desplazado puede reclamar su parte sin plazo (con límites para cosas individuales).", "2311")],
        [40 * mm, W - 2 * M - 52 * mm, 12 * mm]))
    f.append(Spacer(1, 8))
    f.append(H2("Aceptar o renunciar"))
    f.append(P("Aceptar significa asumir los derechos <b>y las obligaciones</b> de la herencia, siempre limitados al valor de los bienes recibidos (art. 2317). Renunciar es como si nunca hubieras sido llamado (art. 2301): se hace con una forma especial y conviene hacerlo con asesoramiento. Si hay deudas grandes, hablalo con tu abogado <b>antes</b> de aceptar de hecho (por ejemplo, vendiendo o usando bienes del fallecido)."))
    f.append(PageBreak())

    f += cap("8", "CASOS FRECUENTES", "Lo que más se pregunta")
    f.append(tabla(["Situación", "Qué conviene saber"], [
        ("La casa está a nombre del fallecido", "Es un bien registrable: se transfiere con la declaratoria o adjudicación inscripta. El cónyuge tiene derecho de habitación (art. 2383)."),
        ("Hay una cuenta bancaria", "El banco suele pedir la declaratoria o una autorización judicial. Los saldos se denuncian en el expediente."),
        ("Hay un auto", "Se transfiere por el registro del automotor luego de la inscripción de la declaratoria o adjudicación."),
        ("Convivía con su pareja sin casarse", "El conviviente no hereda por la ley, aunque puede tener derechos propios de la unión convivencial y ser instituido por testamento. Consultalo con un abogado."),
        ("Un hijo no quiere o no puede ocuparse", "Los herederos pueden dar un poder a uno de ellos o a un abogado; también existe la cesión de herencia (arts. 2302 y siguientes)."),
        ("Hay herederos menores", "La partición y la venta de bienes suelen requerir intervención del juez y del Ministerio Público."),
        ("Hay un hijo no reconocido o dudas de filiación", "Hablá con un abogado: puede afectar la declaratoria."),
        ("Fallecido con bienes en el exterior", "Cada país tiene sus reglas. Se necesita asesoramiento específico.")],
        [58 * mm, W - 2 * M - 58 * mm]))
    f.append(Spacer(1, 8))
    f.append(consejo("EL MEJOR AHORRO", "Hablar de estos temas en vida: un testamento claro, la lista de bienes y las claves de acceso guardadas evitan muchos conflictos."))
    f.append(PageBreak())

    f += cap("9", "ERRORES Y PLAN", "Qué evitar y plan de 30 días")
    f += L(["<b>Vender o retirar bienes</b> del fallecido antes de la declaratoria: puede generar problemas con otros herederos y con acreedores.", "<b>Firmar un papel de un \"gestor\"</b> sin entender qué es. Un poder o una cesión tiene consecuencias.", "<b>Pagar adelantado</b> honorarios sin acuerdo escrito.", "<b>Perder el testamento</b> o abrirlo.", "<b>Ignorar las deudas</b>: pueden crecer con intereses.", "<b>Dejar pasar los plazos</b> de intimación del art. 2289."])
    f.append(Spacer(1, 6))
    f.append(Checklist(["<b>Días 1 a 5</b>: certificado de defunción (varias copias). Avisar a la ANSES y al empleador o caja de jubilación si corresponde.", "<b>Días 5 a 10</b>: juntar DNI y actas de los herederos. Buscar testamento.", "<b>Días 10 a 15</b>: lista de bienes y deudas, con informes de dominio.", "<b>Días 15 a 20</b>: consultar abogados y pedir presupuestos por escrito.", "<b>Días 20 a 30</b>: acuerdo entre herederos sobre quién lleva el trámite; firmar el poder y presentar el inicio."], "PLAN DE 30 DÍAS"))
    f.append(PageBreak())

    f += cap("A", "ANEXO", "Glosario y fuentes")
    f.append(tabla(["Término", "Significado"], [
        ("Causante", "La persona fallecida."),
        ("Heredero forzoso", "Descendientes, ascendientes y cónyuge: la ley les reserva una porción (legítima)."),
        ("Legítima", "Porción de la herencia que el testador no puede quitarle a los herederos forzosos."),
        ("Declaratoria de herederos", "Resolución del juez que reconoce quiénes son los herederos."),
        ("Ganancial", "Bien adquirido durante el matrimonio con el trabajo de alguno de los cónyuges."),
        ("Bien propio", "El que tenía antes del matrimonio o recibió por herencia o donación."),
        ("Partición", "División de los bienes entre los herederos."),
        ("Edicto", "Aviso publicado para que se presenten quienes tengan derecho.")], [44 * mm, W - 2 * M - 44 * mm]))
    f.append(H2("Fuentes"))
    f += L(["Código Civil y Comercial de la Nación (Ley 26.994), Libro Quinto, Transmisión de derechos por causa de muerte: arts. 2277, 2280, 2288, 2289, 2301-2302, 2310-2311, 2317, 2321, 2335-2343, 2383, 2424-2439, 2445, 2477 y 2479. Texto en Infoleg.", "Ley 23.898 (tasas judiciales en la justicia nacional)."])
    f.append(P("Aviso importante", "h2"))
    f.append(P("Esta guía es información general y educativa, actualizada a octubre de 2026. No constituye asesoramiento legal ni reemplaza a un abogado: la sucesión es un trámite judicial y cada caso tiene particularidades. Los costos, tasas e impuestos dependen de cada jurisdicción y no están incluidos. La normativa puede cambiar. Está prohibida su reventa o redistribución.", "nota"))
    return f
