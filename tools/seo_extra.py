"""Páginas SEO extra. Se importa desde build_site.py (ver DEPLOY.md). Usa CATS, ars y las ofertas de build_site."""
import build_site as B
ars, CATS = B.ars, B.CATS

def head(et, h1, baj):
    return f'<span class="etiqueta">{et}</span><h1>{h1}</h1>\n<p class="bajada">{baj}</p>\n'

def tabla(cols, filas):
    t = "".join(f"<th>{c}</th>" for c in cols)
    r = "".join("<tr>" + "".join(f'<td class="cat">{c}</td>' if i == 0 else f"<td>{c}</td>" for i, c in enumerate(f)) + "</tr>" for f in filas)
    return f'<div class="tabla-wrap"><table><thead><tr>{t}</tr></thead><tbody>{r}</tbody></table></div>'

def lec(s): return f'<div class="lectura">{s}</div>'
ES = '<p>Escalas vigentes de agosto 2026 a enero 2027: <a href="/escalas-monotributo-2026">ver tabla completa</a>. Para saber tu categoría, usá la <a href="/">calculadora gratis</a>.</p>'

# 1 servicios vs bienes
serv = tabla(["Cat.", "Servicios", "Venta de bienes", "Diferencia"], [(c, ars(s), ars(b), ars(s - b)) for c, _, s, b in CATS])
p1 = head("Monotributo 2026", "Monotributo: servicios o venta de bienes, ¿cuál pagás?", "Hasta la categoría C pagás lo mismo. Desde la D, quien presta servicios paga una cuota más alta que quien vende productos.") + \
 "<h2>Cuota mensual según tu actividad</h2>" + serv + lec("<h2>Cómo se decide</h2><ul><li>Si <b>prestás servicios</b> (diseño, clases, programación, oficios), pagás la columna de servicios.</li><li>Si <b>vendés cosas muebles</b> que comprás o fabricás, pagás la de venta de bienes.</li><li>Quien hace las dos cosas paga según la actividad de mayor facturación.</li></ul>" + ES) + B.oferta_kit()

# 2 cuánto puedo facturar por mes
mes = tabla(["Cat.", "Tope anual", "Promedio mensual"], [(c, ars(t), ars(t / 12)) for c, t, _, _ in CATS])
p2 = head("Monotributo 2026", "¿Cuánto puedo facturar por mes en el Monotributo?", "El tope es anual y se mide en los últimos 12 meses. Dividido en 12 te da una referencia mensual, pero no es un límite mes a mes.") + \
 "<h2>Tope anual y promedio mensual</h2>" + mes + lec("<h2>Lo importante</h2><ul><li>Lo que cuenta es la suma de <b>los últimos 12 meses</b>, no cada mes por separado: un mes fuerte se compensa con uno flojo.</li><li>Conviene llevar la cuenta mes a mes para no pasarte sin darte cuenta.</li></ul>" + ES) + B.oferta_kit()

# 3 qué pasa si me paso
ult = CATS[-1]
p3 = head("Monotributo 2026", "¿Qué pasa si me paso del tope del Monotributo?", "Depende de cuánto te pasaste: si superás tu categoría, subís a una mayor; si superás la K, salís del régimen.") + \
 lec(f"<h2>Dos situaciones distintas</h2><ul><li><b>Te pasás de tu categoría pero no de la K:</b> en la próxima recategorización te corresponde una categoría más alta y una cuota mayor.</li><li><b>Superás el tope de la K ({ars(ult[1])} anuales):</b> quedás excluido del Monotributo y pasás al régimen general (responsable inscripto).</li></ul><h2>Cómo evitarlo</h2><p>Controlá tu facturación acumulada de 12 meses y proyectá el ritmo de los últimos meses. Mirá la <a href=\"/recategorizacion-monotributo-febrero-2027\">fecha de recategorización</a> y los <a href=\"/escalas-monotributo-2026\">topes por categoría</a>.</p>" + ES) + B.oferta_kit()

# 4 fórmula de precio ML
p4 = head("Mercado Libre", "Cómo calcular el precio de venta en Mercado Libre", "Si sumás la comisión al costo y después tu margen, el precio te queda corto. La cuenta correcta es dividir.") + \
 lec('<h2>La fórmula</h2><p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">precio = (costo + envío + costo fijo) / (1 − comisión − impuestos − margen)</p><h2>Ejemplo</h2><p>Costo $ 10.000, envío a tu cargo $ 0, sin costo fijo, comisión 13%, impuestos 3% y margen deseado 20%: precio = 10.000 / (1 − 0,13 − 0,03 − 0,20) = 10.000 / 0,64 = <b>$ 15.625</b>.</p><p>Si hubieras sumado 36% al costo, habrías puesto $ 13.600 y tu margen real sería menor al 20%. Las comisiones cambian por categoría y por tipo de publicación: usá las tuyas.</p><p>Hacelo para un producto con la <a href="/precios-mercado-libre">calculadora gratis</a>.</p>') + B.oferta_ml()

# 5 clásica vs premium
p5 = head("Mercado Libre", "Publicación Clásica o Premium: cuál te conviene", "Premium cobra más comisión porque incluye cuotas sin interés para el comprador. Si vendés bien sin cuotas, Clásica te deja más ganancia.") + \
 lec('<h2>Cuándo conviene cada una</h2><ul><li><b>Clásica:</b> productos con demanda propia, donde el comprador no necesita cuotas para decidir.</li><li><b>Premium:</b> productos caros o con mucha competencia, donde las cuotas sin interés aumentan las ventas lo suficiente para pagar la diferencia de comisión.</li></ul><p>La forma de decidir es comparar la <b>ganancia neta</b> de cada una al precio que necesitás, no solo la comisión. La <a href="/precios-mercado-libre">calculadora gratis</a> te muestra las dos.</p>') + B.oferta_ml()

# 6 aguinaldo cuándo
p6 = head("Aguinaldo 2026", "Aguinaldo: cuándo se paga y cómo se calcula", "El segundo aguinaldo del año vence el 18 de diciembre y equivale al 50% de la mejor remuneración mensual del semestre.") + \
 lec('<h2>Reglas básicas</h2><ul><li>Es el <b>Sueldo Anual Complementario</b>: se paga en dos cuotas, junio y diciembre.</li><li>Se calcula sobre la <b>mayor remuneración mensual</b> devengada en el semestre (julio a diciembre), dividida por dos.</li><li>Si trabajaste menos de seis meses, se paga proporcional a los días trabajados.</li><li>Al cobrarlo, se descuentan los aportes como en un sueldo.</li></ul><p>Calculalo con la <a href="/aguinaldo">calculadora de aguinaldo</a>. Si tenés personal doméstico, mirá también el <a href="/sueldo-empleada-domestica">sueldo de casas particulares</a>.</p>') + B.oferta_cp()

# 7 vacaciones y obligaciones empleada
vac = tabla(["Antigüedad", "Días corridos de vacaciones"], [("6 meses a 5 años", "14"), ("Más de 5 y hasta 10 años", "21"), ("Más de 10 y hasta 20 años", "28"), ("Más de 20 años", "35")])
p7 = head("Casas particulares", "Empleada doméstica: vacaciones, aguinaldo y registro", "La Ley 26.844 le da a quien trabaja en casas particulares vacaciones pagas, aguinaldo y la obligación de estar registrada.") + \
 "<h2>Vacaciones según antigüedad</h2>" + vac + lec('<h2>Otras obligaciones del empleador</h2><ul><li><b>Registrar</b> a la trabajadora ante ARCA y pagar los aportes y contribuciones.</li><li>Pagar el <b>aguinaldo</b> en junio y diciembre.</li><li>Respetar la escala de la Comisión Nacional de Trabajo en Casas Particulares: <a href="/sueldo-empleada-domestica">ver sueldos de noviembre y diciembre</a>.</li></ul>') + B.oferta_cp()

# 8 IPC alquiler
p8 = head("Alquileres", "Cómo se calcula el aumento de alquiler por IPC", "Si tu contrato se actualiza por IPC, el nuevo alquiler es el anterior multiplicado por la inflación acumulada del período de ajuste.") + \
 lec('<h2>La cuenta</h2><p class="num" style="background:var(--hoja);border:1px solid var(--linea);padding:14px 16px;border-radius:4px;overflow-x:auto">alquiler nuevo = alquiler actual × (1 + IPC mes 1) × (1 + IPC mes 2) × …</p><h2>Ejemplo</h2><p>Alquiler de $ 500.000 con tres meses de IPC de 2%, 2,5% y 3%: 500.000 × 1,02 × 1,025 × 1,03 = <b>$ 538.432</b>. Valores de ejemplo, no son datos del INDEC.</p><ul><li>La periodicidad y el índice son los que fije <b>tu contrato</b>.</li><li>Los datos oficiales los publica el INDEC.</li></ul><p>Usá la <a href="/aumento-alquiler">calculadora con el IPC cargado</a>.</p>') + B.oferta_alq()

ARTS_EXTRA = {
 "monotributo-servicios-o-venta-de-bienes": ("Monotributo 2026: cuota de servicios vs venta de bienes", "Cuánto pagás de Monotributo si prestás servicios o vendés bienes, categoría por categoría, con las escalas de agosto 2026 a enero 2027.", p1),
 "cuanto-puedo-facturar-por-mes-monotributo": ("Cuánto puedo facturar por mes en el Monotributo 2026", "Tope anual y promedio mensual de facturación de cada categoría del Monotributo, escalas vigentes de agosto 2026 a enero 2027.", p2),
 "que-pasa-si-me-paso-del-tope-monotributo": ("Qué pasa si me paso del tope del Monotributo", "Qué ocurre si superás tu categoría o el tope de la categoría K: recategorización, exclusión y cómo evitarlo.", p3),
 "como-calcular-precio-mercado-libre": ("Cómo calcular el precio de venta en Mercado Libre", "La fórmula para poner precio en Mercado Libre sin perder margen: comisión, costo fijo e impuestos, con un ejemplo paso a paso.", p4),
 "mercado-libre-clasica-o-premium": ("Mercado Libre: publicación Clásica o Premium", "Diferencias entre Clásica y Premium en Mercado Libre y cómo elegir según tu ganancia neta.", p5),
 "aguinaldo-cuando-se-paga": ("Aguinaldo: cuándo se paga y cómo se calcula", "El aguinaldo de diciembre vence el 18: cómo se calcula (50% de la mejor remuneración del semestre) y cuándo es proporcional.", p6),
 "vacaciones-empleada-domestica": ("Empleada doméstica: vacaciones, aguinaldo y registro", "Días de vacaciones según antigüedad y obligaciones del empleador de casas particulares (Ley 26.844).", p7),
 "como-calcular-aumento-alquiler-ipc": ("Cómo calcular el aumento de alquiler por IPC", "La fórmula para actualizar un alquiler con el IPC del INDEC, con un ejemplo paso a paso.", p8),
}
