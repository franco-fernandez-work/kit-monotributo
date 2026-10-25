"""Páginas de apoyo que arma seo_boost.py (glosario, fechas clave, metodología y 404) y ajustes de títulos.
Todo dato de acá ya está publicado y verificado en otra página del sitio (se indica cuál): si cambia allá, cambiarlo acá."""

# slug -> (title, meta description). Pisa lo que generó build_site.py, para acercarlo a cómo se busca.
TITULOS = {
    "sueldo-empleada-domestica": ("Sueldo de empleada doméstica 2026: valor hora y mensual (noviembre y diciembre)",
        "Cuánto pagarle a tu empleada doméstica en noviembre y diciembre 2026: valor hora y mensual de cada categoría, con antigüedad y zona desfavorable. Escala oficial Resolución 6/2026."),
    "aguinaldo": ("Calculadora de aguinaldo diciembre 2026: bruto, neto y proporcional",
        "Calculá tu aguinaldo de diciembre 2026: bruto, descuentos y neto, y el proporcional si entraste en el semestre. Vence el 18 de diciembre."),
    "aumento-alquiler": ("Calculadora de aumento de alquiler por IPC 2026 (INDEC)",
        "Calculá cuánto te aumenta el alquiler con el IPC oficial del INDEC: alquiler de hoy, todos los ajustes y la fecha del próximo, para contratos que se actualizan cada 3, 4, 6 o 12 meses."),
}

# Glosario: (término, definición en HTML, página del sitio donde se amplía)
GLOSARIO = [
    ("ARCA", "Agencia de Recaudación y Control Aduanero, el organismo que reemplazó a la AFIP. Ahí se hacen el alta y la recategorización del Monotributo, la factura electrónica y el SIRADIG.", "/guia-primer-ano-monotributo"),
    ("Monotributo", "Régimen simplificado para pequeños contribuyentes. Una cuota mensual incluye el impuesto integrado, el aporte jubilatorio (SIPA) y la obra social. Tiene 11 categorías, de la A a la K.", "/escalas-monotributo-2026"),
    ("Impuesto integrado", "La parte de la cuota del Monotributo que reemplaza a IVA y Ganancias.", "/cuanto-se-paga-de-monotributo"),
    ("Recategorización", "Revisión semestral de la categoría del Monotributo, en febrero y agosto. La de febrero de 2027 vence el 5 de febrero y se calcula con lo facturado de enero a diciembre de 2026.", "/recategorizacion-monotributo-febrero-2027"),
    ("Régimen general (responsable inscripto)", "Régimen al que pasa quien supera el tope de la categoría K del Monotributo: paga IVA y Ganancias por separado.", "/que-pasa-si-me-paso-del-tope-monotributo"),
    ("Factura E", "Comprobante para exportar servicios. Se emite desde un punto de venta de exportación distinto al local.", "/cobrar-del-exterior-freelancer"),
    ("Ingresos Brutos", "Impuesto provincial que no está incluido en la cuota del Monotributo, salvo en las provincias con régimen simplificado unificado.", "/cuanto-se-paga-de-monotributo"),
    ("Aguinaldo (SAC)", "Sueldo Anual Complementario. Se paga en dos cuotas, en junio y en diciembre, y cada una es el 50% de la mejor remuneración mensual del semestre.", "/aguinaldo"),
    ("Liquidación final", "Lo que se cobra al terminar una relación laboral: según el caso, indemnización, preaviso, aguinaldo y vacaciones proporcionales.", "/calculadora-liquidacion-final"),
    ("Ganancia no imponible", "Monto anual que no paga Ganancias. Para 2026, acumulado a diciembre, es de $ 5.585.720,79 según ARCA.", "/deducciones-siradig-ganancias-2026"),
    ("SIRADIG (F.572)", "Formulario web de ARCA donde quien cobra sueldo informa sus deducciones de Ganancias a su empleador. El del año vence el 31 de marzo del año siguiente, salvo prórroga.", "/siradig-que-puedo-deducir"),
    ("IPC", "Índice de Precios al Consumidor del INDEC. Se publica a mediados de cada mes y se usa para actualizar alquileres y presupuestos.", "/aumento-alquiler"),
    ("ICL", "Índice de Contratos de Locación del BCRA. Lo usan en general los contratos de alquiler firmados entre julio de 2020 y diciembre de 2023.", "/aumento-alquiler"),
    ("DNU 70/2023", "Decreto que derogó la Ley de Alquileres 27.551 para los contratos nuevos: plazo, moneda y ajuste los pactan las partes.", "/contratos-alquiler-modelo-word"),
    ("Botón de arrepentimiento", "Enlace que deben mostrar los sitios que venden online para revocar una compra dentro de los 10 días corridos (Disposición 954/2025).", "/boton-de-arrepentimiento-compra-online"),
    ("Franquicia de compras al exterior", "Según ARCA, USD 400 por envío, hasta 5 veces por año. Dentro de la franquicia se paga IVA; por el excedente, derechos y tasa.", "/calculadora-compras-exterior"),
    ("Formulario 08", "Solicitud de transferencia de un automotor que firman vendedor y comprador. El boleto de compraventa no transfiere el auto: lo hace la inscripción con el 08.", "/boleto-compraventa-auto-usado"),
    ("Homologación", "Aprobación de un convenio por el juzgado. Un convenio de alimentos tiene fuerza ejecutiva recién cuando el juzgado de familia lo homologa.", "/cuota-alimentaria-aguinaldo"),
    ("PUAM", "Pensión Universal para el Adulto Mayor: una alternativa desde los 65 años para quien no tiene los aportes necesarios para jubilarse.", "/cuantos-aportes-necesito-para-jubilarme"),
]

# Fechas: (fecha visible, ISO o "" si es un período, qué pasa, página)
FECHAS = [
    ("Todos los meses, a mediados", "", "El INDEC publica el IPC del mes anterior. Con ese dato se actualizan los alquileres por IPC.", "/aumento-alquiler"),
    ("1 de octubre al 30 de abril", "", "Temporada de vacaciones de la Ley de Contrato de Trabajo, salvo que se acuerden otras fechas. El aviso es con 30 días de anticipación como mínimo.", "/calculadora-vacaciones"),
    ("27 de noviembre de 2026", "2026-11-27", "Cierra la inscripción a Progresar Formación Profesional (convocatoria 2026).", "/becas-progresar-requisitos-fechas"),
    ("18 de diciembre de 2026", "2026-12-18", "Vence la segunda cuota del aguinaldo. El empleador tiene 4 días hábiles más para pagarla.", "/aguinaldo"),
    ("Enero de 2027", "2027-01", "Último mes de pago con las escalas del Monotributo vigentes desde agosto de 2026.", "/escalas-monotributo-2026"),
    ("5 de febrero de 2027", "2027-02-05", "Vence la recategorización del Monotributo, con lo facturado de enero a diciembre de 2026.", "/recategorizacion-monotributo-febrero-2027"),
    ("31 de marzo de 2027", "2027-03-31", "Vence el SIRADIG (F.572) del período 2026 para informar deducciones de Ganancias, salvo prórroga.", "/siradig-que-puedo-deducir"),
]

METODOLOGIA = """<span class="etiqueta">Cómo trabajamos</span><h1>Cómo hacemos las calculadoras y las guías</h1>
<p class="bajada">Herramientas gratis para hacer cuentas y trámites de Argentina sin depender de nadie. Esto es lo que hay detrás de cada número.</p>
<div class="lectura">
<h2>De dónde salen los datos</h2><ul>
<li><b>Monotributo, Ganancias y SIRADIG:</b> escalas, topes y deducciones publicadas por <a href="https://www.arca.gob.ar">ARCA</a>.</li>
<li><b>Inflación:</b> el IPC del <a href="https://www.indec.gob.ar">INDEC</a>. La calculadora de alquileres lo lee en vivo de datos.gob.ar.</li>
<li><b>Normas:</b> el texto de cada ley, decreto o resolución en <a href="https://www.argentina.gob.ar/normativa">argentina.gob.ar/normativa</a> y el Boletín Oficial.</li>
<li><b>Dólares y cobros del exterior:</b> comunicaciones del <a href="https://www.bcra.gob.ar">BCRA</a>.</li>
<li><b>Jubilación:</b> requisitos de <a href="https://www.anses.gob.ar">ANSES</a> y la Ley 24.241.</li></ul>
<p>Cuando un dato no lo pudimos confirmar en una fuente oficial, la página lo dice y el valor queda editable para que cargues el tuyo.</p>
<h2>Cómo se calcula</h2><p>Cada calculadora muestra su fórmula en la misma página, con un ejemplo. Las cuentas se hacen en tu navegador: los montos que cargás no se guardan.</p>
<h2>Cuándo se actualiza</h2><p>Cada página indica la fecha de su última actualización. Revisamos los valores cuando ARCA, el INDEC o la autoridad que corresponda publica cambios: nuevas escalas, índices o normas.</p>
<h2>Qué no es</h2><p>Es información general. No reemplaza a un contador, un abogado ni la información oficial de cada organismo. Antes de una decisión importante, confirmá los valores en la fuente.</p>
<h2>Si encontrás un error</h2><p>Avisanos desde el formulario de <a href="/pedidos">pedidos</a>: lo revisamos y corregimos la página.</p>
<h2>Las planillas y guías pagas</h2><p>Las calculadoras son gratis. Algunas páginas ofrecen una planilla, una guía o un pack de modelos para profundizar. Se pagan con Mercado Pago y se descargan al instante.</p>
</div>"""

NO_ENCONTRADA = """<span class="etiqueta">Error 404</span><h1>No encontramos esta página</h1>
<p class="bajada">Puede que la dirección haya cambiado. Estas son las herramientas más usadas:</p>
<div class="lectura"><ul>
<li><a href="/">Calculadora de categoría de Monotributo 2026</a></li>
<li><a href="/aguinaldo">Calculadora de aguinaldo</a></li>
<li><a href="/aumento-alquiler">Aumento de alquiler por IPC</a></li>
<li><a href="/sueldo-empleada-domestica">Sueldo de empleada doméstica</a></li>
<li><a href="/calculadora-liquidacion-final">Liquidación final</a></li>
<li><a href="/calculadora-ganancias-sueldo">Ganancias en el sueldo</a></li>
</ul><p><a class="boton" href="/guias">Ver todas las calculadoras y guías</a></p></div>"""

# Fuentes oficiales: (palabras que la activan en el texto de la página, nombre, URL)
FUENTES = [
    (["ARCA", "Monotributo", "SIRADIG", "Ganancias", "Clave Fiscal"], "ARCA", "https://www.arca.gob.ar"),
    (["INDEC", "IPC"], "INDEC", "https://www.indec.gob.ar"),
    (["BCRA", "ICL"], "Banco Central (BCRA)", "https://www.bcra.gob.ar"),
    (["ANSES", "PUAM", "jubilarse", "jubilarme"], "ANSES", "https://www.anses.gob.ar"),
    (["DNRPA", "Formulario 08"], "DNRPA (Registro del Automotor)", "https://www.dnrpa.gov.ar"),
    (["Migraciones"], "Dirección Nacional de Migraciones", "https://www.argentina.gob.ar/interior/migraciones"),
    (["Ley 24.240", "Defensa del Consumidor", "arrepentimiento", "COPREC"], "Defensa del Consumidor", "https://www.argentina.gob.ar/produccion/defensadelconsumidor"),
    (["Ley ", "DNU", "Código Civil", "Resolución", "Disposición", "Decreto"], "Normativa nacional (Infoleg)", "https://www.argentina.gob.ar/normativa"),
]

# Páginas que repiten la búsqueda de otra más completa: se marcan con canonical hacia la principal,
# salen del sitemap, del índice y de "Seguí leyendo" (siguen accesibles por su enlace).
CONSOLIDAR = {
    "como-calcular-aumento-alquiler-ipc": "aumento-alquiler",
    "como-calcular-precio-mercado-libre": "precios-mercado-libre",
}
