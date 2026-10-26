# Se integra igual que anses_arts: ARTS.update(__import__("salud_arts").ARTS_SALUD) al inicio de main() en tools/build_site.py
from anses_arts import _oferta, FUENTE
FSS = '<p class="nota">Información general y orientativa, sin carácter de asesoramiento médico ni legal. Fuentes oficiales: <a href="https://www.argentina.gob.ar/sssalud" rel="noopener">Superintendencia de Servicios de Salud</a> y <a href="https://www.argentina.gob.ar/salud/vacunas" rel="noopener">argentina.gob.ar/salud/vacunas</a>. Confirmá plazos y requisitos antes de actuar.</p>'

REC = ("Reclamo a la obra social o prepaga: pasos, formularios y plazos",
 "Cómo reclamar a tu obra social o prepaga: Formulario A, plazos de respuesta, cómo elevar a la Superintendencia de Servicios de Salud y cómo ordenar un pedido de reintegro.",
 '<span class="etiqueta">Salud · Reclamos</span><h1>Reclamo a tu obra social o prepaga: pasos y plazos</h1>'
 '<p class="bajada">Si te negaron una cobertura o pagaste de tu bolsillo, el orden importa: primero la entidad, después la Superintendencia de Servicios de Salud.</p>'
 '<div class="lectura"><h2>Los pasos</h2><ol><li>Pedí en la obra social o prepaga su formulario de reclamo (suele llamarse <b>Formulario A</b>) y presentalo con la documentación.</li><li>Pedí <b>copia sellada</b> como constancia.</li><li>Según la Superintendencia (Res. 75/1998), el informe de solución debe llegar en hasta 10 días corridos (5 si el trámite es especial y 2 si es urgente); un manual de la Superintendencia habla de 15 días corridos en el trámite normal.</li><li>Si no te conforma o no responden, podés insistir ante la Superintendencia con el Formulario de Denuncia (firmado por el titular, por Trámites a Distancia, en persona con turno o por correo) dentro de los 10 días corridos de la respuesta, según su página oficial; algunas notas hablan de 10 días hábiles, así que conviene tomar el más corto.</li></ol>'
 '<h2>Qué se suele pedir</h2><ul><li>DNI y carnet de la obra social o prepaga, original y copia.</li><li>CUIL/CUIT y, si corresponde, último recibo.</li><li>Orden médica o informe del profesional y prueba de la negativa.</li></ul>'
 '<h2>Canales de la Superintendencia</h2><p>0800-222-SALUD (72583), Centro de Atención Virtual y “Trámites y servicios” en argentina.gob.ar/sssalud.</p>'
 '<h2>Reintegros</h2><p>No hay un único procedimiento nacional: depende de tu entidad y plan. Como referencia, el reembolso de gastos médicos de PAMI pide presentar dentro de los 180 días de la prestación, con factura original detallada y documentación clínica.</p>' + FSS + '</div>'
 + _oferta("reclamos", "Guía PDF + planilla", "Guía y carpeta de reclamos y reintegros", "Todo ordenado para reclamar sin perder plazos.",
   ["Guía PDF de 5 páginas: cuándo reclamar, Formulario A y B, canales y checklist", "Planilla Excel con registro de gastos, fecha límite y estado de cada reintegro", "Seguimiento de reclamos con plazos calculados solos", "Checklist de documentación para imprimir"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

SAL = ("Calendario de vacunación y turnos en hospitales públicos: carpeta familiar",
 "Cómo ordenar vacunas, controles y turnos de toda la familia. Calendario nacional como referencia y cómo sacar turno en hospitales públicos.",
 '<span class="etiqueta">Salud · Familia</span><h1>Vacunas, controles y turnos en hospitales públicos</h1>'
 '<p class="bajada">Las vacunas del Calendario Nacional son gratuitas en centros de salud y hospitales públicos, sin orden médica. Lo difícil es acordarse de todo: por eso conviene una carpeta por persona.</p>'
 '<div class="lectura"><h2>Calendario de referencia</h2><ul><li>Recién nacido: hepatitis B (primeras 12 horas) y BCG (antes del alta).</li><li>Primer año: rotavirus (2 y 4 meses), quíntuple, polio IPV, neumococo y meningococo; antigripal desde los 6 meses.</li><li>12 meses: triple viral (1.ª dosis) y hepatitis A.</li><li>15 a 18 meses: 2.ª dosis de triple viral para nacidos desde el 1/7/2024, varicela y refuerzos.</li><li>Embarazo: antigripal, triple bacteriana acelular desde la semana 20 y VSR entre las semanas 32 y 36.</li><li>Adultos: doble bacteriana cada 10 años; antigripal y neumococo en grupos indicados.</li></ul><p>Es un resumen parcial del calendario 2026 (vigente desde el 1/1/2026): las dosis y los meses exactos están en argentina.gob.ar/salud/vacunas y en el 0800-222-1002.</p>'
 '<h2>Turnos en hospitales públicos</h2><p>Cada jurisdicción tiene su sistema. Por ejemplo, la Provincia de Buenos Aires ofrece Mi Salud Digital Bonaerense: validás identidad (ReNaPer, ANSES o ARCA), elegís establecimiento y especialidad y tomás el turno. En otras provincias, consultá el sitio del ministerio de salud local o el servicio de admisión del hospital.</p>' + FSS + '</div>'
 + _oferta("saludfam", "Guía PDF + planilla", "Guía y carpeta de salud familiar", "Vacunas, controles y turnos de toda la familia en una sola planilla.",
   ["Guía PDF de 5 páginas: calendario como referencia, turnos y controles", "Planilla Excel con una hoja por integrante y registro de vacunas", "Turnos y controles con días restantes calculados", "Documentos con vencimiento (aptos, certificados)"],
   "2.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

ESC = ("Ayuda Escolar Anual ANSES: certificado escolar y cómo cobrarla",
 "Cómo cargar el certificado escolar en Mi ANSES para cobrar la Ayuda Escolar Anual: requisitos, paso a paso y plazo.",
 '<span class="etiqueta">ANSES · Escolaridad</span><h1>Ayuda Escolar Anual: cómo cargar el certificado escolar</h1>'
 '<p class="bajada">La Ayuda Escolar Anual la paga ANSES a familias con AUH o asignaciones familiares por hijo, siempre que esté presentado el certificado escolar.</p>'
 '<div class="lectura"><h2>Quién cobra</h2><ul><li>Familias con AUH o Asignación Familiar por Hijo.</li><li>Hijos de 45 días a 17 años en establecimientos oficiales (sin límite de edad si tienen discapacidad).</li></ul>'
 '<h2>Paso a paso en Mi ANSES</h2><ol><li>Entrá con tu CUIL y Clave de la Seguridad Social.</li><li>Andá a “Hijos” y elegí “Presentar certificado escolar”.</li><li>Generá el formulario de cada hijo.</li><li>Pedí que la escuela lo complete, firme y selle.</li><li>Subí la foto del formulario firmado.</li></ol>'
 '<p>Según ANSES, el certificado se presenta todos los años y puede cargarse hasta el 31 de diciembre; el cobro de 2026 comenzó en marzo. En 2026 el pago llegó a $85.000 por hijo (Decreto 115/2026: refuerzo extraordinario y por única vez sobre la asignación base, que varía según la zona), por lo que el monto futuro puede ser distinto. Confirmá fecha y monto vigentes en ANSES.</p>' + FUENTE + '</div>'
 + _oferta("escolar", "Guía PDF + planilla", "Guía y carpeta Ayuda Escolar", "Una fila por hijo y el plazo calculado solo.",
   ["Guía PDF de 4 páginas: quién cobra, paso a paso, calendario y problemas frecuentes", "Planilla Excel con estado por hijo y días hasta el plazo", "Checklist por hijo para imprimir"],
   "1.999", "Comprar la guía", "Pagás con Mercado Pago y la descargás al instante."))

ARTS_SALUD = {"reclamo-obra-social-prepaga-paso-a-paso": REC, "calendario-vacunacion-turnos-hospital-publico": SAL, "ayuda-escolar-anual-certificado-escolar": ESC}
