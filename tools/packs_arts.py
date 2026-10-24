# Se integra igual que seo_extra: ARTS.update(__import__("packs_arts").ARTS_PACKS) al inicio de main() en tools/build_site.py
def _oferta(idp, etiqueta, titulo, bajada, items, precio, texto_boton, nota):
    li = "".join(f"<li>{i}</li>" for i in items)
    return (f'<section class="oferta" aria-labelledby="of-{idp}"><div><span class="etiqueta">{etiqueta}</span><h2 id="of-{idp}">{titulo}</h2><p>{bajada}</p><ul>{li}</ul></div>'
            f'<div class="compra"><a class="boton" href="/comprar?p={idp}">{texto_boton} <span class="num">$ {precio}</span></a><span class="nota">{nota}</span></div></section>')

ALQ = ("Modelos de contrato de alquiler 2026 (Word): vivienda, comercial y temporario",
 "Pack de 10 documentos Word editables para alquilar con el marco vigente tras el DNU 70/2023: contratos, inventario, cláusula de ajuste, fianza, recibo y cartas de notificación.",
 '<span class="etiqueta">Marco vigente: Código Civil y Comercial + DNU 70/2023</span><h1>Modelos de contrato de alquiler 2026</h1>'
 '<p class="bajada">Contratos de vivienda, comercial y temporario, más inventario, ajuste por IPC o ICL, fianza, recibo y cartas, en Word editable. Completás los campos resaltados y firmás.</p>'
 '<div class="lectura"><h2>Qué cambió con el DNU 70/2023</h2><ul><li>Ya no hay plazo mínimo obligatorio de 3 años: lo pactan las partes.</li><li>El ajuste y la moneda son libres: cualquier índice público o privado, en pesos o en moneda extranjera.</li><li>El depósito y su devolución se pactan libremente.</li><li>El inquilino puede rescindir en cualquier momento pagando el 10% del saldo de los cánones futuros.</li></ul>'
 '<p>Muchos modelos que circulan en internet siguen citando la Ley 27.551, derogada. Este pack está redactado con las reglas actuales.</p></div>'
 + _oferta("alqpack", "Pack en Word (.docx)", "Pack Contratos de Alquiler 2026", "10 documentos listos para completar, con instrucciones de uso.",
   ["Contrato de vivienda, comercial y temporario", "Anexo de inventario y estado del inmueble", "Cláusula de ajuste: IPC, ICL o escalones fijos", "Fianza, recibo de alquiler y acta de restitución", "Cartas de intimación, rescisión y aviso de ajuste"], "4.999", "Comprar el pack", "Pagás con Mercado Pago y lo descargás al instante. Modelo orientativo: no reemplaza asesoramiento legal.")
 + '<p class="nota">¿Querés calcular el aumento? Usá la <a href="/aumento-alquiler">calculadora de aumento de alquiler por IPC</a>.</p>')

FRE = ("Contratos para freelancers en Argentina 2026 (Word): servicios, NDA y presupuesto",
 "Pack de 9 documentos Word editables para freelancers y monotributistas: contrato de servicios, NDA, propuesta, presupuesto, recibo X, cesión de derechos, acta de entrega y cartas de reclamo.",
 '<span class="etiqueta">Para monotributistas y freelancers</span><h1>Contratos para freelancers en Argentina</h1>'
 '<p class="bajada">Cobrar sin contrato es el error más caro del freelance. Este pack te da el circuito completo: propuesta, contrato, NDA, entrega, cobro y reclamo, en Word editable.</p>'
 '<div class="lectura"><h2>Lo que evita un buen contrato</h2><ul><li>Cambios de alcance sin cobrar de más.</li><li>Clientes que no pagan: mora, intereses y suspensión pactados.</li><li>Dudas sobre quién es dueño del trabajo: cesión recién al cobro total.</li><li>Que la relación se confunda con una relación laboral.</li></ul>'
 '<p>Recordá que el recibo X no reemplaza la factura electrónica: el pack incluye la aclaración y el circuito correcto.</p></div>'
 + _oferta("frepack", "Pack en Word (.docx)", "Pack Contratos para Freelancers 2026", "9 documentos listos para completar, con instrucciones de uso.",
   ["Contrato de locación de servicios con anexo de alcance", "Acuerdo de confidencialidad (NDA)", "Propuesta comercial y presupuesto", "Recibo X y acta de entrega y conformidad", "Cesión de derechos y cartas de reclamo de pago"], "5.999", "Comprar el pack", "Pagás con Mercado Pago y lo descargás al instante. Modelo orientativo: no reemplaza asesoramiento legal.")
 + '<section class="oferta" aria-labelledby="of-combo"><div><span class="etiqueta">Combo</span><h2 id="of-combo">Pack Freelancers + Kit Monotributista</h2><p>Los contratos y la planilla que controla tu categoría de monotributo. Ahorrás $ 3.000 juntos.</p></div>'
   '<div class="compra"><a class="boton" href="/comprar?p=combo">Comprar el combo <span class="num">$ 9.999</span></a><span class="nota">Un solo pago, un solo ZIP.</span></div></section>')

ARTS_PACKS = {"contratos-alquiler-modelo-word": ALQ, "contratos-freelancers-monotributo": FRE}
