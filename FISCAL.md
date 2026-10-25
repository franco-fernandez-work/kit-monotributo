# FISCAL: cómo facturar las ventas (monotributo)

Estado: 0 ventas hasta ahora. Esto es una guía operativa, no asesoramiento contable. Los puntos marcados (verificar) no los confirmé en fuente oficial: confirmalos con ARCA o un contador antes de actuar.

## 1. Qué tenés que hacer vos (nadie más puede)

Todo esto requiere tu identidad ante ARCA. No lo puedo hacer yo.

1. **Clave fiscal nivel 3** (si no la tenés): se obtiene con DNI y validación facial en la app Mi ARCA, o en una oficina.
2. **Alta en Monotributo**: ARCA, "Monotributo", "Adhesión". Datos que vas a necesitar: domicilio fiscal, actividad (digital: venta de planillas, modelos y PDF; la clasificación exacta es del Nomenclador de Actividades, verificar) y obra social.
3. **Categoría A** para arrancar. Con ventas de $3.000 a $9.000 cada una, llegar a $12.009.410 al año exige más de 150 ventas por mes. Cuota 2026 de la A: $49.527,18 por mes (misma para servicios y bienes). Si te pasás, ARCA te recategoriza en la revisión semestral: no hace falta adivinar de más. Escalas y recategorización de febrero 2027: [/escalas-monotributo-2026](https://kit-monotributo.fernandezfrancowork.workers.dev/escalas-monotributo-2026).
4. **Punto de venta de factura electrónica**: ARCA, "Administración de puntos de venta y domicilios", agregar punto de venta con sistema "Factura en línea" (para empezar a mano). Si después se automatiza, otro con sistema "Web Services".
5. **Ingresos Brutos** (provincial, aparte de ARCA): en varias provincias hay un régimen simplificado que se adhiere al monotributo. Revisar en la página de tu provincia (verificar).
6. **Pagar la cuota** mensual (débito automático o VEP) desde el alta: aunque no vendas, se paga.

## 2. Cómo facturar cada venta

Los monotributistas emiten **Factura C**. Cada venta por Mercado Pago tendría que tener su factura al consumidor final.

**Hoy (manual, gratis, mínimo):** ARCA, "Comprobantes en línea" (o la app Mi ARCA). Cargás fecha, concepto ("Producto digital: <nombre>"), importe y "Consumidor final". Tarda un minuto por venta. El pago en Mercado Pago muestra el nombre del comprador para completarla si querés. Mientras haya pocas ventas, hacelo una vez por semana.

Para no depender de vos al facturar, hay que automatizarlo (sección 3).

## 3. ¿Se puede facturar automático y gratis?

**Sí, técnicamente, sin costo**, con el servicio web de factura electrónica de ARCA (WSAA + WSFEv1). El Worker del negocio lo llamaría al aprobarse cada pago, pediría el CAE y guardaría la factura. Costo: $0. Necesita:

- Un **certificado digital** que generás una sola vez (comando `openssl`, te dejo los pasos exactos cuando lo decidas) y subís a ARCA, "Administración de Certificados Digitales".
- Delegar el servicio `wsfe` a ese certificado en "Administrador de Relaciones de Clave Fiscal" (con tu clave fiscal: único paso solo tuyo).
- Un punto de venta tipo "Web Services" (punto 4 de arriba).
- Cargar el certificado y la clave privada como secretos del Worker (los pegás vos en Cloudflare: yo no manejo claves).

**Lo que falta construir (lo hago yo cuando tengas lo anterior):** firmar el pedido de acceso (CMS) en el Worker, llamar a WSFEv1 (SOAP), guardar el CAE en D1 y mostrar la factura (con el QR obligatorio de ARCA) en la página de agradecimiento. Es trabajo de un hilo entero. Como no hay email, el comprador la ve y la descarga en `/gracias` junto con el producto.

**Alternativas pagas o de terceros** (verificar si tienen plan gratis hoy): servicios de facturación por API de terceros. No las recomiendo: salen del presupuesto cero y son más piezas.

## 4. Recomendación

1. Hacé ahora los pasos 1 a 4. Llevan una tarde y no cuestan nada.
2. Con las primeras ventas, facturá a mano una vez por semana (sección 2).
3. Cuando haya varias ventas por semana, avisame: armo la facturación automática con el certificado.

## 5. Dónde cargar tus datos en la web

Los datos del vendedor que exige la ley (nombre, CUIT, domicilio, email) quedaron como marcadores `[COMPLETAR ...]` en el pie de todas las páginas y en /terminos y /privacidad. Se completan en un solo lugar: `VENDEDOR` al inicio de `tools/legal_site.py`. Después de monotributo, ponés tu nombre y CUIT reales y se redeploya.
