---
title: Conectar tu catálogo a los anuncios de Meta y Google
slug: feed-catalogo-anuncios
order: 82
type: Guía
aliases: feed de productos, feed de catálogo, catálogo de meta, catálogo de facebook,
  catálogo de instagram, anuncios de catálogo, anuncios dinámicos, google merchant
  center, merchant center, commerce manager, feed programado, url del feed, subir
  mis productos a meta, subir productos a google shopping, google shopping, sincronizar
  catálogo, las prendas vendidas siguen en el anuncio, el feed dejó de funcionar,
  regenerar url, xml de productos
---

# Conectar tu catálogo a los anuncios de Meta y Google

Si hacés publicidad en Instagram, Facebook o Google, podés armar anuncios que muestran tus prendas directamente: con su foto, su nombre y su precio. Para eso Meta y Google necesitan tu catálogo, y tu tienda se los da con una **URL del feed**: una dirección privada con tus productos publicados en la web, que ellos leen solos y que se mantiene al día sin que hagas nada.

!!! danger "Importante"
    El feed viene apagado. Lo activa un usuario con rol **Administrador** en **Configuración › Tienda web › Ajustes de la tienda**, pestaña **SEO**. Solo está en tiendas que venden, no en las de alquiler.

### 1. Activar el feed

1. Entrá a **Configuración › Tienda web › Ajustes de la tienda** y abrí la pestaña **SEO**.
1. Buscá la tarjeta **Feed de catálogo para pauta**.
1. Tocá **Activar feed**. Aparece el mensaje *Feed activado. Copiá la URL y pegala en Meta o Google.*
1. Tocá **Copiar URL**.
Esta tarjeta se guarda con sus propios botones: no hace falta tocar **Guardar** en la página.

### 2. Pegar la URL en Meta o en Google

- **Meta**: en **Commerce Manager**, agregá una fuente de datos de tipo **Feed programado** y pegá la URL.
- **Google**: en **Google Merchant Center**, agregá una fuente de productos y pegá la URL.
Podés pegar la misma URL en los dos. Desde ahí, cada uno vuelve a leerla cada tanto y actualiza tu catálogo solo.

### Qué productos entran

Entran los mismos productos que se ven en tu tienda online, siempre que tengan:

- estado **Disponible** y el canal **web** activado (mirá [Publicar productos en la tienda online](publicar-en-web.md));
- al menos una foto;
- un precio mayor que cero.
Un producto sin foto o sin precio no aparece en el feed aunque esté publicado en la web.

### Qué datos lleva cada producto

| Dato | De dónde sale |
| --- | --- |
| Código | El código del producto (`PR_…`). |
| Nombre, descripción y fotos | Lo que cargaste en el producto. |
| Link | La página del producto en tu tienda. |
| Precio | El precio de la web. Si tiene descuento, también va el precio con descuento. |
| Marca | El atributo **Marca** del producto; si no tiene, el nombre de tu tienda. |
| Categoría, talle y estado de la prenda | Lo que cargaste en el producto. |

No lleva costos, comisiones, datos de la proveedora ni de tus clientes.

!!! tip "Tip"
    El código de cada producto es el mismo `PR_…` que mandan los eventos de tu tienda al píxel de Meta. Así Meta une el anuncio con la visita y la compra. Si todavía no conectaste el píxel, mirá [Conectar el píxel de Meta a tu tienda con Google Tag Manager](google-tag-manager.md).

### Regenerar o desactivar la URL

Con el feed activado, la tarjeta muestra la **URL del feed** y tres botones:

| Botón | Qué hace |
| --- | --- |
| **Copiar URL** | Copia la dirección para pegarla en Meta o Google. |
| **Regenerar URL** | Crea una URL nueva. La anterior deja de funcionar al momento. |
| **Desactivar feed** | Apaga el feed. La URL deja de funcionar y Meta y Google dejan de recibir tu catálogo. |

**Regenerar URL** y **Desactivar feed** piden confirmación antes de hacer nada: tocá **Sí, regenerar** o **Sí, desactivar** para seguir, o **Cancelar** para dejar todo como estaba.

### Tener en cuenta

- **Cuidá la URL como una contraseña.** Quien la tenga puede descargar tu catálogo. Si se la pasaste a alguien que ya no debería tenerla, tocá **Regenerar URL**.
- **Después de regenerar, pegá la URL nueva en Meta y en Google.** La anterior deja de funcionar enseguida, y hasta que la cambies no reciben tu catálogo.
- **Las prendas vendidas salen solas, pero no al instante.** El feed se actualiza cada 15 minutos, y Meta y Google lo leen cada cierto tiempo, según cómo lo hayas programado ahí. Por un rato un anuncio puede seguir mostrando una prenda que ya vendiste.
- **Todas las prendas se informan como usadas.** Es lo que corresponde a una tienda de segunda mano.
- **Si la tarjeta dice que tu tienda todavía no tiene una dirección web configurada**, no se puede activar: escribinos y la configuramos.
### Qué pasa después

Con el catálogo cargado en Meta o en Google, ya podés crear anuncios de catálogo desde sus propias herramientas. Lo que pase dentro de esas cuentas, como armar las campañas o elegir qué productos mostrar, se configura ahí y no en tu panel.

<p class="doc-aliases" markdown>Términos relacionados: feed de productos, feed de catálogo, catálogo de meta, catálogo de facebook, catálogo de instagram, anuncios de catálogo, anuncios dinámicos, google merchant center, merchant center, commerce manager, feed programado, url del feed, subir mis productos a meta, subir productos a google shopping, google shopping, sincronizar catálogo, las prendas vendidas siguen en el anuncio, el feed dejó de funcionar, regenerar url, xml de productos</p>
