# Integración: ARTS.update(__import__("ronda11_arts").ARTS_R11) al inicio de main() en tools/build_site.py
from anses_arts import _oferta
from ronda10_arts import _calc
NOTA = '<p class="nota">Información general y orientativa, sin carácter de asesoramiento legal, contable ni laboral. Confirmá requisitos y plazos en la fuente oficial antes de actuar.</p>'

HX_CALC = _calc("h", "¿Cuántos francos de compensación son?",
 [("h", "Horas extra acumuladas", "0.5", "12"), ("c", "Coeficiente de compensación (1 = hora por hora, 1,5 = una hora y media por cada hora extra)", "0.1", "1"), ("j", "Horas de una jornada de trabajo", "0.5", "8")],
 "var h=+$('h-h').value||0,c=+$('h-c').value||0,j=+$('h-j').value||0;"
 "if(j<=0){$('h-r').innerHTML='<p>Cargá cuántas horas dura una jornada.</p>';return}"
 "var t=h*c,d=t/j;$('h-r').innerHTML='<p>Saldo a compensar: <b>'+t.toLocaleString('es-AR',{maximumFractionDigits:1})+' horas</b>, equivalen a <b>'+d.toLocaleString('es-AR',{maximumFractionDigits:2})+' jornadas</b> de franco.</p>"
 "<p class=\"nota\">El coeficiente lo definen tu convenio o tu acuerdo con la empresa: la cuenta solo convierte horas en días.</p>'")
HX = ("Cómo llevar el control de horas extra y francos compensatorios de tu equipo",
 "Convertí horas extra en días de franco, mirá qué lleva registrar cada evento y por qué conviene separar los francos de las vacaciones. Con planilla Excel y Google Sheets.",
 '<span class="etiqueta">Equipos · Horas extra</span><h1>Horas extra y francos: cuánto le debés a cada uno</h1>'
 '<p class="bajada">Cuando las horas extra se compensan con francos, el saldo de cada persona se pierde entre mensajes y planillas sueltas. Probá la cuenta básica.</p>' + HX_CALC +
 '<div class="lectura"><h2>Qué conviene anotar de cada evento</h2><ul><li>Quién, qué día y cuántas horas.</li><li>El tipo de evento: hora extra, franco tomado o ajuste.</li><li>Un coeficiente si el acuerdo paga más de una hora por hora (por ejemplo, trabajo en feriado).</li><li>El saldo que queda, en horas y en días de franco.</li></ul>'
 '<h2>¿Por qué separar los francos de las vacaciones?</h2><p>Las vacaciones anuales tienen su propio cálculo y su propio plazo. Si se mezclan con los francos compensatorios, ninguno de los dos saldos cierra. Llevalos en columnas distintas. Para calcular las vacaciones usá la <a href="/calculadora-vacaciones">calculadora de vacaciones</a>.</p>'
 '<h2>¿Qué dice la planilla sobre la ley?</h2><p>Nada: es un registro. No aplica convenios colectivos ni recargos legales. Para saber qué corresponde pagar o compensar, consultá tu convenio o a un profesional.</p>' + NOTA + '</div>'
 + _oferta("horasextra", "Planilla (Excel / Google Sheets)", "Control de Horas Extra y Francos", "Un perfil por persona con el saldo de horas y de días de franco a tomar, y las vacaciones oficiales aparte.",
   ["Registro de 1.500 eventos con listas desplegables de persona y tipo", "Perfil de cada persona: saldo en horas y días, historial con saldo acumulado", "Vacaciones oficiales por separado: corresponden, usadas y días que quedan", "Resumen del equipo con gráfico para hasta 25 personas, coeficiente y saldos iniciales"],
   "4.999", "Comprar la planilla", "Pagás con Mercado Pago y la descargás al instante. Solo registro: no da consejo legal."))

HO = ("Tareas del hogar por frecuencia: lista imprimible diaria, semanal y mensual",
 "Qué limpiar y ordenar todos los días, cada semana, cada mes y por temporada. Lista para imprimir y planilla que te avisa qué está atrasado.",
 '<span class="etiqueta">Hogar · Organización</span><h1>Tareas del hogar por frecuencia: la lista para imprimir</h1>'
 '<p class="bajada">Lo difícil no es limpiar: es acordarte de qué toca hoy. Esta lista ordena la casa por frecuencia para que no viva en tu cabeza.</p>'
 '<div class="lectura"><h2>Todos los días</h2><ul><li>Lavar los platos y limpiar la mesada.</li><li>Tender las camas y ventilar los ambientes.</li><li>Sacar la basura y repasar el piso de la cocina.</li><li>Guardar lo que quedó fuera de lugar (diez minutos antes de dormir).</li></ul>'
 '<h2>Cada semana</h2><ul><li>Pasar la aspiradora o barrer y trapear todos los pisos.</li><li>Limpiar el baño completo: inodoro, ducha, bacha y espejo.</li><li>Cambiar sábanas y toallas.</li><li>Lavar la ropa, planchar y reponer la heladera.</li><li>Regar las plantas y limpiar el comedero de las mascotas.</li></ul>'
 '<h2>Cada mes</h2><ul><li>Limpiar el interior de la heladera y descartar lo vencido.</li><li>Limpiar el horno, la campana y los filtros.</li><li>Quitar el polvo de estantes, zócalos y detrás de los muebles.</li><li>Lavar cortinas, almohadones y el cesto de basura.</li></ul>'
 '<h2>Cada estación</h2><ul><li>Cambiar la ropa de cama y de armario según la temporada.</li><li>Limpiar ventanas, persianas y mosquiteros.</li><li>Revisar el botiquín y las fechas de vencimiento.</li><li>Dar vuelta colchones y lavar alfombras.</li></ul>'
 '<h2>¿Cómo repartirlo entre quienes viven en casa?</h2><p>Sumá los minutos de cada tarea por semana y dividí entre las personas. Lo parejo no es que cada uno haga lo mismo, sino que el tiempo total sea parecido. La planilla hace esa cuenta sola.</p>'
 '<p class="nota">Podés imprimir esta página (Ctrl+P) y pegarla en la heladera.</p></div>'
 + _oferta("hogar", "Planilla (Excel / Google Sheets)", "Organizador del Hogar y Tareas", "Anotás cada tarea una vez y la planilla te dice qué está atrasado, qué toca hoy y qué viene esta semana.",
   ["Unas 80 tareas ya cargadas por ambiente, con frecuencia y minutos reales", "Lista Hoy ordenada por urgencia, con filtro por persona", "Checklist semanal de una hoja para imprimir", "Reparto parejo entre quienes viven en la casa y 45 tareas extra (chicos, mascotas, jardín, mudanza, estudiante)"],
   "4.999", "Comprar la planilla", "Pagás con Mercado Pago y la descargás al instante. Sin macros."))

VI = ("Checklist de viaje: qué hacer y para cuándo, de 6 meses a 1 mes antes",
 "Las tareas de un viaje al exterior ordenadas por plazo: pasaporte, requisitos de entrada, pasajes, alojamiento, seguro y la última semana. Con planilla de equipaje.",
 '<span class="etiqueta">Viajes · Organización</span><h1>Checklist de viaje: qué hacer y para cuándo</h1>'
 '<p class="bajada">Las cosas que arruinan un viaje se resuelven con meses de anticipación: un pasaporte por vencer o un trámite que no se hizo. Estas son las diez tareas, en orden.</p>'
 '<div class="lectura"><h2>6 a 4 meses antes</h2><ol><li>Revisá el vencimiento del pasaporte. Varios países piden que tenga meses de validez después del regreso.</li><li>Averiguá los requisitos de entrada del destino (visa, autorización electrónica, vacunas) en fuentes oficiales.</li><li>Definí fechas, presupuesto y quiénes viajan.</li><li>Comprá los pasajes con el nombre tal como figura en el documento.</li></ol>'
 '<h2>3 a 2 meses antes</h2><ol start="5"><li>Reservá alojamiento, preferí tarifas con cancelación gratuita.</li><li>Contratá un seguro de viaje: algunos destinos lo exigen.</li><li>Si viajan menores sin alguno de los padres, preparalo con la <a href="/autorizacion-viaje-menores">autorización de viaje de menores</a>.</li></ol>'
 '<h2>1 mes antes</h2><ol start="8"><li>Revisá el límite de tus tarjetas para consumos en el exterior y cuánto te sale con el <a href="/calculadora-compras-exterior">cálculo de compras en el exterior</a>.</li><li>Si viaja una mascota, averiguá los requisitos en el SENASA.</li><li>Armá la lista de equipaje según clima, transporte y duración, y dejala a la vista.</li></ol>'
 '<p class="nota">Los requisitos de entrada cambian y dependen de cada país: confirmalos siempre en argentina.gob.ar y en la Cancillería.</p>' + NOTA + '</div>'
 + _oferta("viaje", "Planilla (Excel / Google Sheets)", "Checklist de Viaje por Plazos + Equipaje", "Cargás la fecha de salida y el tipo de viaje, y la planilla te dice qué hacer y para cuándo.",
   ["Unas 60 tareas con plazo: estado atrasado, por vencer o en fecha", "Resumen de avance y lista de las próximas tareas", "Lista de equipaje que se adapta (exterior o país, avión, auto o tren, chicos, mascotas, frío o calor)", "Unos 70 ítems editables con espacio para los tuyos, lista para imprimir"],
   "1.999", "Comprar la planilla", "Pagás con Mercado Pago y la descargás al instante. Son recordatorios: confirmá los requisitos en fuentes oficiales.")
 + _oferta("viajebundle", "Pack viaje (2 planillas)", "Pack Viaje: Checklist + Presupuesto de Viaje", "El checklist por plazos y el planificador de presupuesto, con los mismos datos del viaje.",
   ["Checklist de viaje por plazos y lista de equipaje", "Planificador de presupuesto de viaje con conversión de moneda y gasto diario", "Presupuesto planeado vs. real", "Las dos comparten nombre del viaje, viajeros, fecha de inicio y duración"],
   "3.499", "Comprar el pack", "Pagás con Mercado Pago y las descargás al instante."))

ARTS_R11 = {
 "planilla-control-horas-extra-francos": HX,
 "tareas-del-hogar-por-frecuencia-lista-imprimible": HO,
 "checklist-viaje-exterior-que-hacer-y-cuando": VI,
}
