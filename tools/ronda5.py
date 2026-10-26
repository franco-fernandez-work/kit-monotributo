"""Ronda 4b (HUECOS.md #13-#16): guías PDF aguinaldo, sucesión, jubilación y salir del monotributo. build_site.main() importa PAGES.
`python tools/ronda5.py` arma private/guia-aguinaldo.pdf, guia-sucesion.pdf, guia-jubilacion.pdf y guia-salir.pdf (necesita reportlab; correr local y commitear; NO corre en Cloudflare)."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ronda2 import head, lec, field, js
from ronda4 import of_guia

# ===================================================================== 13. AGUINALDO
def of_agui():
    return of_guia("aguinaldo", "Guía: Dónde poner el aguinaldo",
        "Un método para comparar plazo fijo, fondos, cauciones, letras y dólar con los números de hoy, sin que nadie te venda nada.",
        ["Qué hacer antes de invertir: deudas, fondo de emergencia y gastos de enero", "TNA, TEA y rendimiento real con fórmulas y ejemplos", "Cómo funciona cada alternativa, su riesgo y su liquidez", "Fuentes oficiales para ver tasas e inflación, y cómo evitar estafas"],
        "2.999", '<a class="nota" href="/aguinaldo">¿Cuánto te toca de aguinaldo? Calculadora gratis</a>')

BODY_G = (head("Gratis · Aguinaldo", "¿Cuánto rinde tu aguinaldo en términos reales?", "Cargá el monto, la tasa que te ofrecen, los días y la inflación que esperás. Calculamos el interés, la tasa efectiva y si le ganás o no a los precios.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu colocación</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("g-m", "Monto", 1000000, "$") + field("g-t", "Tasa nominal anual (TNA)", 30, "", "%") + "</div>"
 + '<div class="fila2">' + field("g-d", "Días", 30, "", "", "1") + field("g-i", "Inflación del período", 2, "", "%") + "</div>"
 + '<p class="nota">La tasa y la inflación son ejemplos: reemplazalas por la tasa que te ofrecen hoy y por la última inflación mensual del INDEC. Escribí la inflación para los mismos días que la colocación.</p>'
 + '</div></div><div><div class="r2res" id="g-out" aria-live="polite"></div>'
 + '<p class="nota">Cálculo orientativo. No incluye comisiones ni impuestos.</p></div></div>'
 + '<p class="avisolegal"><b>Información educativa.</b> No es asesoramiento financiero ni una recomendación de inversión. La inflación futura no se conoce y las tasas cambian: verificá en bcra.gob.ar e indec.gob.ar.</p>'
 + lec("<h2>Cómo leer el resultado</h2><ul><li><b>Interés</b>: capital × TNA × días ÷ 365.</li><li><b>Rendimiento real</b>: lo ganado descontando la inflación. Si es negativo, tu plata crece en pesos pero compra menos.</li><li><b>Tasa efectiva anual (TEA)</b>: lo que rendiría en un año si reinvertís cada vez al mismo valor.</li></ul><p>Antes de elegir dónde ponerlo: cancelá deudas caras, separá un fondo de emergencia y los gastos de enero. Si todavía no sabés cuánto te toca, usá la <a href=\"/aguinaldo\">calculadora de aguinaldo</a>.</p>")
 + of_agui())

JS_G = js("""function a(){const m=n('g-m'),t=n('g-t')/100,d=Math.max(1,n('g-d')),i=n('g-i')/100;
const int=m*t*d/365,r=int/m,tea=Math.pow(1+t*d/365,365/d)-1,real=(1+r)/(1+i)-1;
const f=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>',p=v=>(v*100).toFixed(2).replace('.',',')+' %';
let h=f('Interés bruto',ars(int))+f('Rendimiento del período',p(r))+f('Tasa efectiva anual (TEA)',p(tea))+f('Inflación del período',p(i))+f('<b>Rendimiento real</b>','<b>'+p(real)+'</b>')+f('Tu plata al final',ars(m+int))+f('Poder de compra al final (a precios de hoy)',ars((m+int)/(1+i)));
h+=real<0?'<p class="nota" style="margin:0"><b>Pierde contra la inflación</b> en este escenario.</p>':'<p class="nota" style="margin:0"><b>Le gana a la inflación</b> en este escenario, si la inflación es la que cargaste.</p>';
$('g-out').innerHTML=h}
document.querySelectorAll('.comp input').forEach(e=>e.addEventListener('input',a));a();""")

PAGES = {}
PAGES.update({
 "donde-poner-el-aguinaldo": ("Dónde poner el aguinaldo: calculadora de rendimiento real y guía", "Calculá gratis cuánto rinde tu aguinaldo en un plazo fijo o fondo y si le gana a la inflación. Guía en PDF para comparar alternativas sin que nadie te venda nada, por $2.999.", BODY_G, JS_G),
})

# ===================================================================== 14. SUCESIÓN
def of_suc():
    return of_guia("sucesion", "Guía: Sucesión sin perder tiempo",
        "Quién hereda según el Código Civil y Comercial, qué papeles juntar, el trámite paso a paso y los plazos que importan.",
        ["Orden de herederos, parte del cónyuge y legítima, con artículos citados", "Checklist de papeles sobre las personas, los bienes y las deudas", "El trámite en 8 pasos, del certificado de defunción a la inscripción", "Plazos del Código, costos que hay que averiguar y plan de 30 días"],
        "4.999", '<a class="nota" href="/telegrama-renuncia-modelo">¿Trabajaba en relación de dependencia? Modelos de telegramas laborales</a>')

BODY_S = (head("Gratis · Sucesión", "¿Quién hereda y cuánto? Calculadora de herederos sin testamento", "Indicá quiénes sobreviven y el valor de los bienes propios. Aplicamos el orden del Código Civil y Comercial y te mostramos la parte de cada uno.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Familia</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("s-h", "Hijos vivos", 2, "", "", "1") + field("s-a", "Padres o abuelos vivos (más próximos)", 0, "", "", "1") + "</div>"
 + '<div class="fila2"><div class="campo"><label for="s-c">¿Hay cónyuge con derecho a heredar?</label><div class="entrada"><select id="s-c"><option value="1" selected>Sí</option><option value="0">No</option></select></div></div>' + field("s-v", "Bienes propios del fallecido", 90000000, "$") + "</div>"
 + '<p class="nota">Si un hijo falleció antes y dejó hijos, cuenta como una sola rama (cuentan como un hijo). Los bienes gananciales se dividen primero con el cónyuge (la mitad es suya) y solo la otra mitad integra la herencia.</p>'
 + '</div></div><div><div class="r2res" id="s-out" aria-live="polite"></div>'
 + '<p class="nota">Orientativo. Aplica solo a sucesiones sin testamento (arts. 2424 a 2439 del CCyC).</p></div></div>'
 + '<p class="avisolegal"><b>Información general.</b> No reemplaza a un abogado. La sucesión es un trámite judicial y cada caso tiene particularidades (testamento, donaciones, indignidad, bienes en el exterior).</p>'
 + lec("<h2>El orden, en breve</h2><ul><li><b>Hijos</b> (y descendientes por representación): heredan por partes iguales.</li><li><b>Cónyuge con hijos</b>: cobra lo mismo que un hijo sobre los bienes propios.</li><li><b>Sin hijos</b>: los padres o abuelos; con cónyuge, este se lleva la mitad.</li><li><b>Solo cónyuge</b>: hereda todo.</li><li><b>Sin nada de lo anterior</b>: hermanos, sobrinos y demás parientes hasta el cuarto grado.</li></ul><p>Con testamento, la ley protege una legítima: dos tercios para los hijos y la mitad para los padres y para el cónyuge (art. 2445). La guía explica cómo se aplica, qué papeles juntar y los pasos del trámite.</p>")
 + of_suc())

JS_S = js("""function a(){const h=Math.floor(n('s-h')),as=Math.floor(n('s-a')),c=$('s-c').value==='1',v=n('s-v');
const f=(l,x)=>'<div class="fil"><span>'+l+'</span><span>'+x+'</span></div>',pc=x=>(x*100).toFixed(1).replace('.',',')+' %';
let h2='';
if(h>0){const k=h+(c?1:0);h2+=f('Cada hijo',pc(1/k)+' · '+ars(v/k));if(c)h2+=f('Cónyuge',pc(1/k)+' · '+ars(v/k));h2+=f('Orden','Descendientes'+(c?' con cónyuge':''))}
else if(as>0){if(c){h2+=f('Cónyuge',pc(.5)+' · '+ars(v/2));h2+=f('Ascendientes (entre todos)',pc(.5)+' · '+ars(v/2))}else h2+=f('Ascendientes (entre todos)',pc(1)+' · '+ars(v));h2+=f('Cada uno de '+as,pc((c?.5:1)/as)+' · '+ars((c?v/2:v)/as));h2+=f('Orden','Ascendientes'+(c?' con cónyuge':''))}
else if(c){h2+=f('Cónyuge',pc(1)+' · '+ars(v));h2+=f('Orden','Cónyuge (excluye a los colaterales)')}
else h2+='<p class="nota" style="margin:0">Sin hijos, ascendientes ni cónyuge heredan los <b>parientes colaterales hasta el cuarto grado</b> (hermanos, sobrinos, tíos, primos). Si no hay ninguno, los bienes pasan al Estado.</p>';
$('s-out').innerHTML=h2}
document.querySelectorAll('.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")

PAGES.update({
 "quien-hereda-sucesion-sin-testamento": ("Quién hereda sin testamento: calculadora de herederos y guía de sucesión", "Calculadora gratis del reparto de una herencia sin testamento según el Código Civil y Comercial. Guía en PDF con papeles, pasos y plazos de la sucesión por $4.999.", BODY_S, JS_S),
})

# ===================================================================== 15. JUBILACIÓN
def of_jub():
    return of_guia("jubilacion", "Guía: Jubilación ANSES paso a paso",
        "Los requisitos de la Ley 24.241, cómo revisar tu historia laboral, qué hacer si te faltan aportes, la PUAM y el trámite sin gestores.",
        ["Edad y 30 años de aportes con la regla de compensación y los años por hijos", "Cómo ver tus aportes en Mi ANSES y corregir lo que falta", "Alternativas si te faltan años y qué pasó con la moratoria", "La PUAM, el trámite en 6 pasos, estafas frecuentes y plan de 30 días"],
        "3.999", '<a class="nota" href="/guia-primer-ano-monotributo">¿Sos monotributista? Guía del primer año de monotributo</a>')

BODY_J = (head("Gratis · Jubilación", "¿Cuántos años de aportes necesito para jubilarme?", "Cargá tu edad, tus años con aportes y, si sos mujer, tus hijos. Te decimos si cumplís los requisitos de la Ley 24.241 o cuánto te falta.")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tus datos</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2"><div class="campo"><label for="j-s">Sexo registral</label><div class="entrada"><select id="j-s"><option value="h">Varón</option><option value="m">Mujer</option></select></div></div>' + field("j-e", "Tu edad", 63, "", "años", "1") + "</div>"
 + '<div class="fila2">' + field("j-a", "Años con aportes", 26, "", "años", "any") + field("j-h", "Hijos nacidos con vida (solo mujeres)", 0, "", "", "1") + "</div>"
 + '<div class="fila2">' + field("j-u", "De esos hijos, con AUH de 12 meses o más", 0, "", "", "1") + "</div>"
 + '<p class="nota">Los años por hijos se basan en el art. 22 bis de la Ley 24.241 según el texto de Infoleg (Decreto 475/2021). Confirmá su aplicación en ANSES.</p>'
 + '</div></div><div><div class="r2res" id="j-out" aria-live="polite"></div>'
 + '<p class="nota">Orientativo. Solo cuentan los años con aportes registrados.</p></div></div>'
 + '<p class="avisolegal"><b>Información general.</b> No reemplaza a ANSES. La normativa y las moratorias cambian: confirmá en anses.gob.ar.</p>'
 + lec("<h2>Los requisitos en breve</h2><ul><li><b>65 años</b> los hombres y <b>60</b> las mujeres (las mujeres pueden optar por seguir hasta los 65).</li><li><b>30 años de servicios con aportes</b>: trabajo en blanco, monotributo con aportes, autónomo, casas particulares y otras cajas por reciprocidad.</li><li><b>Compensación</b>: dos años de edad de más cubren uno de aportes que falta.</li><li>Sin los aportes necesarios, la <b>PUAM</b> es una alternativa desde los 65 años.</li></ul><p>La guía en PDF explica cómo revisar tu historia laboral, qué hacer si faltan aportes y cómo pedir la jubilación paso a paso.</p>")
 + of_jub())

JS_J = js("""function a(){const m=$('j-s').value==='m',e=n('j-e'),ap=n('j-a'),hj=m?Math.floor(n('j-h')):0,au=m?Math.min(hj,Math.floor(n('j-u'))):0;
const ed=m?60:65,req=30,ex=hj+au*2,ef=ap+ex,falt=Math.max(0,req-ef),ee=Math.max(0,e-ed),comp=Math.min(falt,Math.floor(ee/2)),fin=falt-comp;
const f=(l,x)=>'<div class="fil"><span>'+l+'</span><span>'+x+'</span></div>',y=v=>(Math.round(v*10)/10).toString().replace('.',',')+' años';
let h=f('Edad mínima',ed+' años')+f('Tu edad',e+' años')+f('Aportes registrados',y(ap));if(m)h+=f('Años por hijos',y(ex));
h+=f('Servicios computables',y(ef))+f('Te faltan',y(falt));
if(falt>0&&ee>0)h+=f('Cubiertos por exceso de edad',y(comp));
h+=f('<b>Falta final</b>','<b>'+y(fin)+'</b>');
let v;
if(e>=ed&&fin<=0)v='<b>Cumplís los requisitos de edad y aportes</b> según estos datos. Pedí la jubilación en ANSES.';
else if(e<ed)v='<b>Todavía no llegás a la edad</b> ('+ed+'). Podés usar el tiempo para completar o reconocer aportes.';
else v='<b>Te faltan '+y(fin)+' de aportes</b>. Mirá reconocimiento de servicios, seguir aportando o la PUAM si tenés 65 años o más.';
h+='<p class="nota" style="margin:0">'+v+'</p>';
$('j-out').innerHTML=h}
document.querySelectorAll('.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")


# ===================================================================== 16. SALIR DEL MONOTRIBUTO
def of_sal():
    return of_guia("salir", "Guía: Salir del monotributo",
        "Por qué te pueden excluir, cómo renunciar antes, qué cambia con IVA, Ganancias y autónomos, y el pasaje ordenado con datos de ARCA.",
        ["Las 11 causales de exclusión y los plazos para apelar (15 y 10 días)", "Exclusión, renuncia y baja: cuándo conviene cada una y cuándo podés volver", "Aportes de autónomos vigentes desde octubre de 2026 y el efecto del IVA", "Pasos del pasaje, beneficios del régimen (50%, 30%, 10%) y plan de 90 días"],
        "3.999", '<a class="nota" href="/recategorizacion-monotributo-febrero-2027">¿Todavía estás en el monotributo? Calculadora de recategorización</a>')

def _cats_json2():
    from build_site import CATS
    return json.dumps([[c[0], c[1], c[2], c[3]] for c in CATS])

BODY_L = (head("Gratis · Monotributo", "¿Cuánto cuesta salir del monotributo?", "Cargá tu facturación anual y tus compras. Te mostramos tu categoría, qué parte del tope usás y una estimación del costo en el régimen general (aportes de autónomo e IVA).")
 + '<div class="r2dos"><div class="comp"><div class="comp-cab"><span>Tu negocio</span><span>Gratis</span></div><div class="comp-cuerpo">'
 + '<div class="fila2">' + field("l-f", "Facturación de los últimos 12 meses", 90000000, "$") + '<div class="campo"><label for="l-t">Actividad</label><div class="entrada"><select id="l-t"><option value="s">Servicios</option><option value="b">Venta de bienes</option></select></div></div></div>'
 + '<div class="fila2">' + field("l-c", "Compras y gastos con IVA al año (con el IVA incluido)", 12000000, "$") + field("l-cf", "Ventas a consumidor final", 100, "", "%") + "</div>"
 + '<p class="nota">Aporte de autónomo: categoría mínima I de ARCA vigente desde el 15/10/2026 ($ 78.271,56 por mes). Tu categoría real puede ser otra. Las cuotas del monotributo son las de agosto 2026 a enero 2027.</p>'
 + '</div></div><div><div class="r2res" id="l-out" aria-live="polite"></div>'
 + '<p class="nota">Estimación orientativa. No incluye Ganancias, Ingresos Brutos ni honorarios del contador.</p></div></div>'
 + '<p class="avisolegal"><b>Cálculo orientativo.</b> El IVA se estima sobre precios que lo incluyen. Si vendés a empresas y podés sumar IVA al precio, el resultado cambia. Consultá a un contador.</p>'
 + lec("<h2>Salir antes o esperar</h2><ul><li><b>Exclusión</b>: ARCA te saca por una causal (tope, gastos, depósitos incompatibles). No podés volver por 3 años calendario.</li><li><b>Renuncia</b>: salís vos antes. Tampoco volvés por 3 años, pero tenés beneficios en IVA y Ganancias si cumplís las condiciones.</li><li><b>Baja por cese</b>: dejás la actividad y podés volver cuando quieras.</li></ul><p>Si recibiste un aviso de exclusión, tenés 15 días desde la recepción para apelar. La guía en PDF resume las causales de ARCA, los pasos del pasaje al régimen general y un plan de 90 días.</p>")
 + of_sal())

JS_L = js("const C=" + _cats_json2() + """;
function a(){const f=n('l-f'),b=$('l-t').value==='b',co=n('l-c'),cf=n('l-cf')/100;
let cat=null;for(const x of C){if(f<=x[1]){cat=x;break}}
const cuota=cat?(b?cat[3]:cat[2]):null,tope=C[C.length-1][1],aut=78271.56*12;
const ivaDeb=f*cf*(0.21/1.21),ivaCred=co*(0.21/1.21),iva=Math.max(0,ivaDeb-ivaCred);
const fl=(l,v)=>'<div class="fil"><span>'+l+'</span><span>'+v+'</span></div>',pc=v=>(v*100).toFixed(1).replace('.',',')+' %';
let h=fl('Tu categoría actual',cat?cat[0]:'Fuera de la K')+fl('Usás del tope de la K',pc(f/tope))+fl('Monotributo por año',cuota?ars(cuota*12):'—')+fl('Aportes de autónomo por año (cat. I)',ars(aut))+fl('IVA estimado por año',ars(iva))+fl('<b>Régimen general (aportes + IVA)</b>','<b>'+ars(aut+iva)+'</b>');
if(cuota)h+=fl('<b>Diferencia contra el monotributo</b>','<b>'+ars(aut+iva-cuota*12)+'</b>');
if(!cat)h+='<p class="nota" style="margin:0"><b>Superás el tope de la K:</b> corresponde el régimen general. Consultá a un contador.</p>';
else if(f>tope*.8)h+='<p class="nota" style="margin:0"><b>Estás por encima del 80% del tope de la K:</b> empezá a preparar el pasaje.</p>';
$('l-out').innerHTML=h}
document.querySelectorAll('.comp input,.comp select').forEach(e=>e.addEventListener('input',a));a();""")

PAGES.update({
 "salir-del-monotributo-cuanto-cuesta": ("Salir del monotributo: cuánto cuesta pasar a autónomo, IVA y Ganancias", "Calculadora gratis del costo de salir del monotributo: aportes de autónomo e IVA estimado contra tu cuota actual. Guía en PDF con causales de exclusión, renuncia y pasaje por $3.999.", BODY_L, JS_L),
})

# ===================================================================== archivos
def build_pdfs():
    from guias_lib import build
    import importlib
    for modulo, salida in [("g_aguinaldo", "guia-aguinaldo.pdf"), ("g_sucesion", "guia-sucesion.pdf"), ("g_jubilacion", "guia-jubilacion.pdf"), ("g_salir", "guia-salir.pdf")]:
        try:
            g = importlib.import_module(modulo)
        except ModuleNotFoundError:
            continue
        print(salida, build(salida, g.META, g.contenido()))

if __name__ == "__main__":
    build_pdfs()
