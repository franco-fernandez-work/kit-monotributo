"""Página /pedidos: formulario "¿No encontrás lo que buscás? Pedilo". Backend en src/pedidos.js. Se importa desde build_site."""

BODY = """
<span class="etiqueta">Pedidos</span><h1>¿No encontrás lo que buscás? Pedilo</h1>
<p>Contanos qué documento, planilla o calculadora necesitás. Los pedidos parecidos suman votos y los más pedidos son los próximos que armamos. Es todo automático: no pedimos tu email ni respondemos de forma personal. Si sale algo parecido, lo vas a encontrar publicado en el sitio.</p>
<form class="arr-form" id="ped" novalidate>
<div><label for="p-tipo">Qué necesitás</label><select id="p-tipo" name="tipo"><option value="documento">Un documento o modelo (Word, PDF)</option><option value="planilla">Una planilla (Excel)</option><option value="calculadora">Una calculadora online</option><option value="otro">Otra cosa</option></select></div>
<div><label for="p-texto">Describilo</label><textarea id="p-texto" name="texto" rows="4" maxlength="400" required placeholder="Ej.: un modelo de contrato de comodato para prestar un departamento a un familiar"></textarea></div>
<div style="display:none"><label>No completar<input name="web" tabindex="-1" autocomplete="off"></label></div>
<button class="boton" type="submit">Enviar pedido</button>
</form>
<div class="arr-res" id="ped-res" role="status" aria-live="polite"></div>
<p class="nota">No pongas datos personales ni enlaces. Mirá también <a href="/privacidad">cómo tratamos los datos</a>.</p>
"""

JS = """<script>
const f=document.getElementById("ped"),r=document.getElementById("ped-res"),t0=Date.now();
f.addEventListener("submit",async e=>{e.preventDefault();const b=f.querySelector("button");b.disabled=true;
const d=Object.fromEntries(new FormData(f));d.t=t0;r.style.display="block";r.className="arr-res";r.textContent="Enviando…";
try{const x=await fetch("/pedidos/enviar",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(d)});
const j=await x.json();r.className="arr-res "+(j.ok?"ok":"mal");r.textContent=j.mensaje||"No se pudo enviar. Probá de nuevo.";if(j.ok)f.reset()
}catch{r.className="arr-res mal";r.textContent="No se pudo enviar. Probá de nuevo."}b.disabled=false});
</script>"""

PAGES = {"pedidos": ("Pedí el documento o la herramienta que necesitás", "Pedí un documento, planilla o calculadora que no encontrás en el sitio. Los pedidos con más votos son los próximos que armamos. Sin registro y sin email.", BODY, JS)}
