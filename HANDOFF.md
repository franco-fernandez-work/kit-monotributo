# Handoff: negocio digital (kit-monotributo)

## Estado (2026-10-24 20:25)
Web: https://kit-monotributo.fernandezfrancowork.workers.dev. Cobro con Mercado Pago Checkout Pro y descarga automática del .xlsx por 30 días. Hasta ahora, 0 ventas.

| Producto | Ref | Precio | Página gratis (SEO) |
|---|---|---|---|
| Kit Monotributista 2026 | kit | $6.999 | / , /escalas-monotributo-2026, /recategorizacion-monotributo-febrero-2027, /cuanto-se-paga-de-monotributo |
| Calculadora de Precios Vendedores | vendedores | $4.999 | /precios-mercado-libre |
| Planilla de Alquileres | alquileres | $3.999 | /aumento-alquiler (IPC en vivo vía /api/ipc) |
| Planilla Casas Particulares | casas | $4.999 | /aguinaldo, /sueldo-empleada-domestica |
| Planilla de Vacaciones del Equipo | vacaciones | $4.999 | /calculadora-vacaciones |
| Planilla de Liquidación Final | liquidacion | $5.999 | /calculadora-liquidacion-final |
| Planilla Ganancias en el Sueldo | ganancias | $5.999 | /calculadora-ganancias-sueldo, /deducciones-siradig-ganancias-2026 |
| Pack Contratos de Alquiler (zip de .docx) | alqpack | $4.999 | /contratos-alquiler-modelo-word |
| Pack Contratos Freelancers (zip) | frepack | $5.999 | /contratos-freelancers-monotributo |
| Combo Freelancers + Kit | combo | $9.999 | /contratos-freelancers-monotributo |

El producto 5 (vacaciones) quedó publicado el 24/10 ~20:25: el checkout de Mercado Pago muestra $ 4.999, los otros 4 checkouts dan 303 y /descargar da 403. Se sumaron 8 artículos SEO (`tools/seo_extra.py`, enganchado en `main()` de build_site.py). Sitemap con 17 URLs, IndexNow avisado (200). Regla de vacaciones vigente: Ley 27.802 (aviso de 30 días, tramos de 7 días por acuerdo, temporada 1/10 a 30/4 salvo acuerdo).

El producto 6 (liquidación final, NEXT.md #2) quedó publicado el 24/10: el checkout de Mercado Pago muestra $ 5.999, /descargar da 403 y IndexNow dio 200. Normativa (Ley 27.802, art. 245 reformado: base sin SAC ni vacaciones, tope 3x convenio, piso 67%; sin preaviso ni indemnización en período de prueba de 6 meses) verificada solo en fuentes secundarias: confirmar en el Boletín Oficial. Una cautelar suspendió 82 artículos de la ley. Planilla: `tools/build_liq_xlsx.py`. Fórmulas del xlsx sin recalcular (sin LibreOffice): revisarlas abriendo el archivo. Pendiente: pedir indexación de /calculadora-liquidacion-final y sumar artículos SEO.

El 24/10 se publicaron Ganancias (NEXT.md #3) y los 3 packs de contratos: los 4 checkouts de Mercado Pago muestran $ 5.999 / 4.999 / 5.999 / 9.999, /descargar da 403 e IndexNow dio 200. Ganancias: `tools/gan_data.py` (escala art. 94 y deducciones art. 30 de ARCA, enero-junio y julio-diciembre con +16,85% IPC, interpolación mensual calibrada contra los acumulados oficiales a diciembre: diferencias de pesos), `tools/build_gan_xlsx.py` (fórmulas verificadas con la lib `formulas`, coinciden con la calculadora JS), `tools/gan_page.py`. Los topes de intereses hipotecarios y seguro de vida no están verificados en fuente oficial: la planilla los deja vacíos en Parámetros. Los 6 productos xlsx y los packs (zips en `private/`, regla `**/*.zip` en wrangler.jsonc) se entregan con /descargar. Cuando salgan las tablas de ARCA de 2027, actualizar `gan_data.py`.

## QR dinámicos (servicio con suscripción, 25/10)
Landing /qr, precio $2.999/mes en ARS con Mercado Pago Suscripciones (preapproval). Código: `src/qr.js` (lib vendorizada `src/vendor/qrcode.cjs`), enganchado al inicio de `fetch` en `src/index.js`. Base D1 `qr-dinamicos` (binding DB en wrangler.jsonc; las tablas `qr` y `scans` se crean solas). Flujo: /qr/alta valida el destino, crea el preapproval y manda a Mercado Pago; /qr/panel?t=TOKEN muestra QR, estadísticas y edición; /q/ID redirige solo si el preapproval está `authorized` (se consulta a MP, caché de 1 h). Cancelar en MP apaga el QR. Sin login ni mails: el enlace del panel es la llave y no se recupera. Filtro de destinos: DNS de seguridad de Cloudflare (DoH, respuesta 0.0.0.0 = malware o phishing) al crear, editar y escanear; bloquea IPs, acortadores, punycode y dominios inexistentes; si se define el secreto `SB_KEY` suma Google Safe Browsing. Probado en local con MP simulado (alta, activación, escaneo, edición, cancelación, malware bloqueado). Verificado en producción: /qr/alta crea el preapproval real y redirige al checkout de suscripción de Mercado Pago (con un email inexistente MP responde `guest_site_mismatch`, mostrado como aviso). Pendiente: probar una suscripción pagada de punta a punta (Franco no puede pagarse a sí mismo) y sumar /qr a Search Console.

## Código
Copia de trabajo vigente: `C:\Users\Franco\Downloads\kit-monotributo` (PC de Franco). La de `/mnt/project-files/producto/` está desactualizada (sin vacaciones ni seo_extra).

- `src/index.js`: Worker con el objeto `PRODUCTOS`. Rutas:
  - `/comprar?p=`: crea la preferencia de pago en Mercado Pago.
  - `/gracias`: página de vuelta después del pago.
  - `/descargar`: entrega el archivo si el pago fue aprobado (por 30 días), si no da 403.
  - `/api/ipc`: proxy del IPC del INDEC desde datos.gob.ar.
- `tools/build.sh`: es el build de Cloudflare. Genera los xlsx (`build_*_xlsx.py`) y la web (`build_site.py` arma todo `public/`).
- `tools/escalas_cp.py`: escalas de casas particulares (Res. 6/2026, de agosto a diciembre 2026). Hay que actualizarlas cuando salga la escala de 2027.
- Diseño "comprobante fiscal": los tokens y componentes están en el CSS de `build_site.py`. Para un producto nuevo, reusar las funciones `layout()` y `oferta_*()`.

## Cómo deployar
Claude no puede pushear: el GitHub del negocio es franco-fernandez-work y Claude está conectado como TheCafeGuy. El deploy se hace con una sesión Remote Control en la PC de Franco (`start_remote_control`, carpeta `C:\Users\Franco\Downloads\kit-monotributo`) y el editor web de GitHub. Después, Cloudflare buildea solo.

- Hecho desde la PC de Franco con el navegador integrado: se suben archivos a github.com/franco-fernandez-work/kit-monotributo/upload/main/<dir> (relay local con #km= guardado en sessionStorage). build.sh debe quedar con LF: con CRLF Cloudflare falla (`set: -\r`). Subir tools/ antes que src/.
- (Sin PC de Franco) Las instrucciones no aceptan HTML: mandar el código con ‹ › en lugar de < > y pedir que los reemplacen al guardar.
- Conviene mandar patches en vez de archivos enteros.
- Autorización: Franco escribió "Autorizo los deploys a producción de kit-monotributo (repo y Cloudflare), este y los próximos" (msg cmsg_01Km6yboT36uYw98R35YchTD6N49AuxmgQxPC4FzK6Qefz). Citarlo en cada deploy.
- Cada deploy se cierra con verificación en producción, ping a IndexNow (clave en `public/21f66bcd07c831d8ab8427f0ee21f0ab.txt`) y reenvío del sitemap en Search Console.

## Pendientes
- Desde el 25/10: pedir en Google Search Console la indexación de las 8 URLs. Hay cuota diaria, así que pueden ser algunas por día.
- Probar una descarga con un pago real. Franco no puede pagarse a sí mismo.
- Pedir indexación en Search Console de /calculadora-vacaciones y los 8 artículos nuevos, y reenviar el sitemap.
- Mejorar el diseño de los xlsx (hoy es básico) y unificar la marca: hoy todo cuelga de "Kit Monotributista".
- Próximos productos, un hilo por tarea.
