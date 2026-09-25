---
title: Conectar el píxel de Meta a tu tienda con Google Tag Manager
slug: google-tag-manager
order: 80
type: Guía
aliases: google tag manager, gtm, contenedor gtm, pixel de meta, píxel de meta, meta
  pixel, facebook pixel, pixel de facebook, eventos, eventos de ecommerce, conversiones,
  purchase, add to cart, view content, remarketing, retargeting, catálogo de meta,
  anuncios, publicidad, instagram ads, facebook ads, medir ventas, atribución
---

# Conectar el píxel de Meta a tu tienda con Google Tag Manager

Esta guía te acompaña, paso a paso, para que los anuncios de Instagram y Facebook sepan qué productos mira la gente en tu tienda y qué compras terminan cerrando. No necesitas saber de tecnología ni pegar una línea de código en el sitio: tu tienda ya publica todo lo que hace falta, y aquí vas a aprender a engancharlo con el píxel de Meta.

**Tiempo estimado:** 45 a 60 minutos la primera vez.
**Qué vas a necesitar:** una cuenta de Google, una cuenta de Meta Business (la que administra tu página de Instagram o de Facebook) y acceso a tu backoffice.

!!! tip "Tip"
    Si todavía no mides nada, haz primero la guía *Cómo medir las visitas de tu tienda con Google Analytics*. Los Pasos 1 y 2 de esta guía son exactamente los mismos: si ya los hiciste, sáltalos y empieza en el Paso 3.

---

### Qué hace Circular por ti y qué te toca a ti

Esto es lo más importante para entender el resto de la guía, porque casi todo el trabajo pasa en una herramienta que no es Circular.

**Lo que hacemos nosotros:**

- **Instalamos Google Tag Manager en tu tienda.** Tú pegas un código en el backoffice y listo. Nunca tienes que pegar un bloque de código en el sitio ni pedirle nada a un programador.
- **Publicamos cuatro eventos de venta** — mirar un producto, agregarlo al carrito, empezar el checkout y comprar — con el importe, la moneda y el código de cada producto. Salen solos, sin configurar nada.
**Lo que te toca a ti (o a tu agencia):**

- Crear la cuenta de Google Tag Manager y el píxel en Meta.
- Armar, dentro de Tag Manager, las etiquetas que toman esos cuatro eventos y se los mandan a Meta. Eso es de los Pasos 4 al 8.
!!! tip "Tip"
    Nosotros publicamos los datos; **tu contenedor de Tag Manager decide a dónde van**. Lo que pasa adentro de ese contenedor es tuyo: no tenemos acceso y no podemos configurarlo por ti. Lo que sí podemos es revisar contigo que la tienda esté publicando bien los eventos.

**¿Lo puede hacer tu agencia?** Sí, y es lo habitual. Dale acceso a tu contenedor de Tag Manager y a tu cuenta de Meta Business, y de Circular va a necesitar una sola cosa: que el código del contenedor esté pegado en el backoffice (Paso 2). Eso lo haces tú en dos minutos; todo lo demás lo hace la agencia desde sus propias cuentas.

---

### Los cuatro eventos que tu tienda publica sola

Apenas pegas el código del contenedor en el backoffice, tu tienda empieza a publicar estos cuatro eventos. No hay nada que activar.

| Evento | Cuándo se dispara | Qué lleva |
| --- | --- | --- |
| `view_item` | Cuando alguien abre la ficha de un producto | `currency`, `value` e `items[]` |
| `add_to_cart` | Cuando el producto **ya quedó** agregado al carrito. Si el agregado falla, no se dispara nada | `currency`, `value` e `items[]` |
| `begin_checkout` | Cuando alguien entra al checkout con el carrito cargado | `currency`, `value` con el total a pagar, e `items[]` con todas las líneas |
| `purchase` | Cuando la compra queda confirmada | Lo mismo, más `transaction_id` |

Y esto es lo que significa cada dato:

| Dato | Qué es |
| --- | --- |
| `currency` | El código de tu moneda: `UYU`, `ARS`, `PYG`, `USD`… |
| `value` | El importe, como número limpio. Nunca el texto que se ve en pantalla. |
| `items[]` | La lista de productos de ese evento. |
| `item_id` | El código del producto (`PR_…`). |
| `item_name` | El nombre del producto, tal cual lo cargaste. |
| `price` | El precio de ese producto, como número limpio. |
| `transaction_id` | Solo en `purchase`: el número de orden. |

Los detalles que conviene saber antes de empezar a configurar:

- **El importe va en la escala de tu moneda.** Una tienda en guaraníes manda `150000`, entero y sin decimales, porque el guaraní no tiene centavos. Una tienda en pesos o en dólares manda `139` o `139.5`. Lo que nunca va es el texto formateado `"USD 139,00"`: Meta no lo sabe leer.
- **El ****`item_id`**** es el código del producto**, el `PR_…` que aparece debajo del nombre en el listado de **Productos** (es el mismo por el que puedes buscar ahí). Ese código es lo que le permite a Meta decir *"esta venta fue de este producto"*.
- **Un producto sin precio ("consultar precio") también reporta.** El evento sale igual, pero sin importe: queda registrada la visita a la ficha aunque no haya un número que mandar.
- **En alquileres**, mirar la ficha y agregar al carrito reportan el precio de lista que muestra la tarjeta, porque en ese momento todavía no hay fechas elegidas. El checkout y la compra reportan el importe real del período elegido. Es normal que no coincidan.
- **Las compras con transferencia o pago en el local también reportan la venta.** No hace falta tener Mercado Pago: si tu tienda cobra por transferencia o a coordinar, el evento de compra sale igual cuando la orden queda confirmada.
- **Cada orden se reporta una sola vez.** Si quien compró recarga la pantalla de compra confirmada, no se cuenta dos veces.
- **Si borras el código del backoffice, se apaga todo.** No queda nada dando vueltas ni aparece ningún error en la tienda.
!!! tip "Tip"
    **Ningún dato personal viaja en estos eventos.** No mandamos el nombre, el correo, el teléfono ni el documento de quien compra: solo códigos de producto, nombres de producto, importes y el número de orden. Es la primera pregunta que hace toda agencia, y la respuesta es no, a propósito.

---

### Paso 1 — Crear el contenedor en Google Tag Manager

Si ya hiciste la guía de Google Analytics, este paso ya está: usa el mismo contenedor y pasa al Paso 3.

1. Entra a [**https://tagmanager.google.com**](https://tagmanager.google.com/) e inicia sesión con tu cuenta de Google.
1. Haz clic en **Crear cuenta**.
1. Completa **Nombre de la cuenta** (el de tu negocio), **País**, y **Nombre del contenedor** (pon la dirección de tu tienda, por ejemplo `mitienda.com`).
1. En **Plataforma de destino**, elige **Web**.
1. Haz clic en **Crear** y acepta los términos.
1. Se abre una ventana con **dos bloques de código** para instalar en el sitio. **Ciérrala con la X: no los necesitas.** Circular ya pone ese código por ti, y si además los pegaras en algún lado, todo se contaría dos veces.
1. Arriba a la derecha vas a ver el código del contenedor: empieza con `GTM-` (por ejemplo `GTM-AB12CD3`). Cópialo.
✅ **Al terminar este paso tienes:** tu código `GTM-XXXXXXX`.

---

### Paso 2 — Pegar ese código en tu backoffice

1. Ingresa a tu **backoffice**.
1. En el menú de la izquierda, abre **Mi sitio web** y entra a **Configuraciones**.
1. Haz clic en la pestaña **SEO**.
1. Baja hasta el recuadro **Medir las visitas de tu tienda**.
1. En el campo **ID de Google Tag Manager**, pega el código que empieza con `GTM-`.
1. Haz clic en **Guardar**. Tiene que aparecer el mensaje *"Configuración guardada correctamente."*
!!! warning "Atención"
    Si en vez del código pegas el bloque de instalación entero, el campo te avisa: *"Parece que pegaste el código de instalación completo. Pegá sólo el ID: GTM-…"*, y te dice cuál es el que sirve. Copia ese y guarda. Y cuidado con el otro código parecido: el que empieza con `G-` es de Google Analytics y **no va en ese campo**.

✅ **Al terminar este paso:** tu tienda ya está publicando los cuatro eventos. Todavía no le llegan a Meta — para eso son los pasos que siguen.

---

### Paso 3 — Crear el píxel en Meta y copiar su número

1. Entra a [**Meta Events Manager**](https://business.facebook.com/events_manager) con la cuenta que administra tu página de Instagram o Facebook.
1. Haz clic en **Conectar orígenes de datos** y elige **Web**.
1. Haz clic en **Conectar**, ponle un nombre (el de tu tienda) y **Crear**.
1. Cuando te pregunte cómo quieres instalarlo, elige la opción de instalar el código manualmente y **no copies nada**: el código lo va a poner Tag Manager. Cierra el asistente.
1. En la lista de orígenes de datos, al lado del nombre del píxel vas a ver un **número largo**, de 15 o 16 dígitos. Ese es el **ID del píxel**. Cópialo.
✅ **Al terminar este paso tienes:** el número de tu píxel.

---

### Paso 4 — Agregar la plantilla del píxel de Meta a Tag Manager

Tag Manager no trae el píxel de Meta de fábrica: hay que sumar la plantilla, una sola vez.

1. Entra a tu contenedor en [**https://tagmanager.google.com**](https://tagmanager.google.com/).
1. En el menú de la izquierda, haz clic en **Plantillas**.
1. En el recuadro **Plantillas de etiquetas**, haz clic en **Buscar en la galería**.
1. Busca **Meta Pixel** (antes se llamaba *Facebook Pixel*) y elige la de la comunidad, publicada por Meta.
1. Haz clic en **Agregar al espacio de trabajo** (según la variante de español puede decir *Añadir al espacio de trabajo*) y confirma.
!!! tip "Tip"
    **La plantilla está en inglés aunque tu Tag Manager esté en español.** Los nombres de campo que vas a ver de aquí en adelante — **Event Name**, **Object Properties**, **Add Row** — son los de la plantilla y aparecen en inglés. No te equivocaste de pantalla.

---

### Paso 5 — Crear las variables

Una *variable* es la forma que tiene Tag Manager de agarrar un dato del evento que publica tu tienda y pasárselo a Meta. Vas a crear cuatro.

Para las tres primeras: menú de la izquierda → **Variables**; en el recuadro **Variables definidas por el usuario**, **Nueva** → **Configuración de la variable** → **Variable de capa de datos**. El campo que importa es **Nombre de la variable de la capa de datos**, y tiene que escribirse **exactamente** así, con el punto y todo en minúscula:

| Nombre que le pones tú (arriba de la página, donde dice Variable sin título) | Nombre de la variable de la capa de datos |
| --- | --- |
| `DL - ecommerce.value` | `ecommerce.value` |
| `DL - ecommerce.currency` | `ecommerce.currency` |
| `DL - ecommerce.items` | `ecommerce.items` |

La cuarta es distinta. Meta no quiere la lista de productos entera: quiere solamente los códigos. En **Variables** → **Nueva**, elige **JavaScript personalizado**, ponle de nombre `JS - content_ids` y pega esto tal cual:

```javascript
function() {
  var items = {{DL - ecommerce.items}};
  if (!items || !items.length) {
    return [];
  }
  return items.map(function(item) {
    return item.item_id;
  });
}
```

Si a la variable de los productos le pusiste otro nombre, cambia `DL - ecommerce.items` por el nombre que usaste: tiene que coincidir letra por letra.

!!! tip "Tip"
    **Alternativa más simple, solo para la ficha de producto:** si prefieres no pegar código, puedes crear una **Variable de capa de datos** llamada `ecommerce.items.0.item_id` y usarla en las etiquetas de **ViewContent** y **AddToCart**, donde siempre hay un producto solo. **No sirve** para **InitiateCheckout** ni **Purchase**: ahí puede haber varios productos y se reportaría uno solo, dejando el resto de la compra sin atribuir.

---

### Paso 6 — Crear los cuatro activadores

El *activador* es lo que le dice a una etiqueta cuándo dispararse. Vas a crear uno por evento.

Para cada uno: menú de la izquierda → **Activadores** → **Nuevo** → **Configuración del activador** → **Evento personalizado**. En **Nombre del evento** escribe el nombre exacto, deja marcado **Todos los eventos personalizados** y guarda.

| Nombre del activador | Nombre del evento (exacto) |
| --- | --- |
| Evento - view_item | `view_item` |
| Evento - add_to_cart | `add_to_cart` |
| Evento - begin_checkout | `begin_checkout` |
| Evento - purchase | `purchase` |

!!! warning "Atención"
    Si el nombre del evento tiene una letra de más, una mayúscula o un espacio, la etiqueta **nunca se dispara y no aparece ningún mensaje de error**. Copia y pega desde esta tabla.

---

### Paso 7 — Crear las etiquetas

Son cinco: una de base, que se dispara en todas las páginas, y cuatro de venta.

#### La etiqueta de base (PageView)

1. **Etiquetas** → **Nueva** → **Configuración de la etiqueta** → **Meta Pixel**.
1. En **Meta Pixel ID(s)**, pega el número del píxel del Paso 3.
1. En **Event Name**, elige **PageView**.
1. En **Activación**, elige **All Pages** (Todas las páginas).
1. Ponle de nombre `Meta Pixel - PageView` y **Guardar**.
#### Las cuatro etiquetas de venta

Se arman todas igual. Lo único que cambia es el **Event Name** y el activador:

| Nombre de la etiqueta | Event Name | Activación |
| --- | --- | --- |
| Meta Pixel - ViewContent | `ViewContent` | Evento - view_item |
| Meta Pixel - AddToCart | `AddToCart` | Evento - add_to_cart |
| Meta Pixel - InitiateCheckout | `InitiateCheckout` | Evento - begin_checkout |
| Meta Pixel - Purchase | `Purchase` | Evento - purchase |

Y en cada una de esas cuatro, además:

1. Pega el mismo **Meta Pixel ID(s)** del Paso 3.
1. Deja **apagado** el interruptor **Use GA4 dataLayer Integration**. Más abajo explicamos por qué: es el error que más tiempo hace perder.
1. Deja **destildada** la casilla **Opt in to a Meta-enabled Conversions API integration**.
1. Abre **Object Properties** y carga estas cuatro filas, una por una con **Add Row**:
| Property Name | Property Value |
| --- | --- |
| `value` | `{{DL - ecommerce.value}}` |
| `currency` | `{{DL - ecommerce.currency}}` |
| `content_ids` | `{{JS - content_ids}}` |
| `content_type` | `product` |

Las tres primeras no se escriben a mano: haz clic en el ícono de **+** que aparece a la derecha del campo de valor y elige la variable de la lista. `content_type` sí se escribe literal, la palabra `product`, sin llaves.

✅ **Al terminar este paso tienes:** cinco etiquetas guardadas. Cuidado con esa palabra: guardadas, no publicadas.

---

### Paso 8 — Enviar y publicar

1. Arriba a la derecha, haz clic en **Enviar**.
1. Ponle un nombre a la versión, por ejemplo *"Píxel de Meta con eventos de venta"*.
1. Haz clic en **Publicar**.
!!! danger "Importante"
    Mientras no aprietes **Publicar**, todo lo que armaste existe solo en tu pantalla: la tienda en vivo sigue exactamente igual que antes. Y no es una sola vez — **cada** cambio que hagas después necesita otro **Enviar → Publicar**.

---

### Paso 9 — Comprobar que esté midiendo

#### Con Vista previa, en Tag Manager

1. En tu contenedor, a la derecha, haz clic en los tres puntos y después en **Vista previa**.
1. Escribe la dirección de tu tienda y haz clic en **Conectar**. Se abre tu tienda en una ventana nueva y, en la otra, el panel de Tag Assistant.
1. Navega tu tienda en esa ventana nueva: abre un producto, agrégalo al carrito, entra al checkout.
1. En la columna de la izquierda de Tag Assistant (en la ventana original) se va armando la lista de eventos. Al abrir un producto tiene que aparecer `view_item`; al agregarlo, `add_to_cart`. Haciendo clic en cada evento, en **Tags** tienen que figurar las etiquetas de Meta como **Tags Fired**.
#### Con Probar eventos, en Meta

1. En Meta Events Manager, elige tu píxel y entra a la pestaña **Probar eventos**.
1. Pega la dirección de tu tienda donde dice probar eventos del navegador y ábrela. Esto está en la sección **Confirma que los eventos de tu sitio web estén configurados correctamente**.
1. Navega la tienda. Los eventos aparecen en la lista **en el momento**, con todos sus parámetros.
1. Haz clic en un **ViewContent** y revisa que traiga `value`, `currency`, `content_ids` y `content_type`. Si dice que *no se detectaron parámetros*, ve directo al error 4 de la lista de abajo.
!!! tip "Tip"
    Para la prueba final, haz una compra de verdad por el monto más chico que puedas y confírmala: es la única forma de ver el **Purchase** con su importe real. Después la puedes cancelar desde el backoffice — el evento ya quedó reportado y no se borra.

---

### Si algo no anda

Casi todos estos problemas son silenciosos: no hay mensaje de error, simplemente no pasa nada. Búscalos aquí antes de rehacer la configuración.

#### 1. El botón Guardar está apagado, o mi cambio no queda

**Síntoma:** editas un campo de la etiqueta y el botón **Guardar** no se activa; o guardas, vuelves a entrar y está como estaba.

**Qué pasa:** estás dentro del **editor de la plantilla**, no de tu etiqueta. Se reconoce porque arriba dice **Vista previa de plantilla** y hay un botón **Ejecutar código**. Esa pantalla es un simulador para quien programa plantillas: lo que toques ahí no llega nunca a tu tienda.

**Cómo se arregla:** sal de ahí, ve al menú **Etiquetas** de la izquierda y abre tu etiqueta por su nombre (`Meta Pixel - ViewContent`, etc.). Los cambios se hacen siempre desde **Etiquetas**.

#### 2. Guardar no es publicar

**Síntoma:** en Tag Manager está todo bien armado, pero en la tienda en vivo no se dispara nada. Ni siquiera el `PageView`.

**Qué pasa:** guardar una etiqueta la deja en tu borrador de trabajo. La tienda en vivo sigue funcionando con la última versión **publicada**, que todavía no incluye nada de esto.

**Cómo se arregla:** **Enviar → Publicar**, arriba a la derecha. Cada vez que cambies algo.

#### 3. No llega absolutamente nada, y ya publicaste

**Síntoma:** publicaste y sigue sin aparecer ningún evento, ni el `PageView`.

**Qué pasa:** o falta el código en el backoffice, o tu navegador está bloqueando el píxel. Una extensión (uBlock, AdBlock, Ghostery, el escudo de Brave, algunos antivirus) lo bloquea antes de que salga, y desde Meta se ve idéntico a *"no está instalado"*.

**Cómo se arregla:** revisa en **Mi sitio web → Configuraciones → SEO** que el campo tenga tu código `GTM-`. Si está, prueba en una ventana **con las extensiones desactivadas**, en otro navegador, o desde el teléfono con datos móviles.

#### 4. El evento llega a Meta "sin parámetros"

**Síntoma:** en **Probar eventos** ves el evento (por ejemplo `Purchase`), pero Meta dice que **no se detectaron parámetros**: sin importe, sin moneda, sin productos. La venta se registra, pero no sirve para optimizar campañas.

**Qué pasa:** la etiqueta tiene **encendido** el interruptor **Use GA4 dataLayer Integration**. Con ese interruptor prendido, la plantilla arma el evento por su cuenta e **ignora por completo** las **Object Properties** que cargaste a mano. Si algo no le cierra, manda el evento pelado.

**Cómo se arregla:** abre la etiqueta y **apaga** *Use GA4 dataLayer Integration*. Las dos formas no conviven: o la automática, o las cuatro propiedades a mano. Esta guía usa las propiedades a mano justamente porque se pueden revisar campo por campo.

#### 5. Llega el PageView, no llega ninguno de venta

**Síntoma:** el píxel figura como instalado, el `PageView` llega, y ninguno de los cuatro eventos de venta aparece nunca.

**Qué pasa:** hay dos causas posibles. La primera es que en la etiqueta quedó tildada **Opt in to a Meta-enabled Conversions API integration**: esa opción es para tiendas que además mandan los eventos desde su propio servidor, y tildada sin tener ese envío armado, la etiqueta inicializa el píxel y después no manda nada — sin avisar. La segunda es que el activador no coincide con el nombre del evento.

**Cómo se arregla:** destilda esa casilla en las cinco etiquetas. Después confirma que cada activador sea de tipo **Evento personalizado** y que el nombre del evento esté exacto y en minúscula.

#### 6. Te quedó el evento equivocado en el desplegable

**Síntoma:** los `PageView` suben sin parar y el `ViewContent` no aparece nunca.

**Qué pasa:** al crear una etiqueta, el campo **Event Name** viene con **PageView** elegido de entrada. Es facilísimo armar las cuatro etiquetas de venta, ponerles bien el nombre y el activador, y olvidarse de cambiar ese desplegable.

**Cómo se arregla:** abre las cuatro etiquetas de venta y confirma que el **Event Name** diga `ViewContent`, `AddToCart`, `InitiateCheckout` y `Purchase`, cada una la suya. Es el error más común de todos.

#### 7. El importe llega vacío, en cero, o con decimales raros

**Síntoma:** el evento llega pero el valor no tiene sentido.

**Qué pasa:** si llega vacío o en cero, o el producto no tiene precio cargado, o la variable está mal escrita. Si llega multiplicado o con decimales de más, alguien transformó el valor dentro de Tag Manager.

**Cómo se arregla:** revisa que el producto tenga precio, y que la variable diga exactamente `ecommerce.value`. El importe sale ya listo de tu tienda: no hay que dividirlo ni multiplicarlo por nada.

#### 8. En Purchase llega un solo producto de varios

**Síntoma:** la compra se reporta, pero con un producto cuando fueron tres.

**Qué pasa:** se usó la variable `ecommerce.items.0.item_id`, que devuelve siempre el primer producto de la lista.

**Cómo se arregla:** usa la variable de JavaScript `JS - content_ids` del Paso 5, que devuelve todos.

#### 9. Las compras aparecen duplicadas

**Síntoma:** cada venta se cuenta dos veces, o aparecen eventos que no configuraste.

**Qué pasa:** o se pegó a mano el bloque de instalación de Tag Manager en algún lado (el que te dijimos de no copiar en el Paso 1), o se usó además **Configurar eventos** de Meta. Esa herramienta, donde marcas botones de tu sitio con el mouse, está pensada para tiendas que **no** publican datos de venta — que no es tu caso.

**Cómo se arregla:** no pegues el bloque de instalación en ningún lado, y si ya marcaste botones con **Configurar eventos**, borra esas configuraciones desde la misma pantalla de Meta.

#### 10. El resumen de Meta viene muy atrasado

**Síntoma:** la pantalla de resumen del píxel dice algo como *"última recepción hace 51 minutos"* y te convences de que se rompió algo — mientras los eventos están entrando en ese mismo momento.

**Qué pasa:** ese panel se actualiza cada tanto y puede quedar muy atrás. No es un indicador en vivo.

**Cómo se arregla:** no saques ninguna conclusión de esa pantalla mientras estás configurando. Usa **Probar eventos**, que sí es en vivo. El resumen se acomoda solo en las horas siguientes.

#### 11. Los códigos no coinciden con tu catálogo de Meta

**Síntoma:** Meta registra las ventas y el importe, pero en los anuncios de catálogo no le atribuye nada a ningún producto, y el remarketing no muestra las prendas que la gente estuvo mirando.

**Qué pasa:** `content_ids` tiene que traer el mismo identificador con el que cargaste el catálogo de productos en Meta. Si el catálogo está cargado con otro código — un SKU, un número de planilla —, Meta no puede unir las dos puntas.

**Cómo se arregla:** tu tienda manda el código `PR_…` del producto, el que aparece debajo del nombre en el listado de **Productos**. Carga el catálogo de Meta usando ese mismo código como identificador de cada producto.

#### 12. En alquileres el importe no coincide con la ficha

No es un error: es el comportamiento esperado. Mirar la ficha reporta el precio de lista; el checkout y la compra reportan el importe del período elegido.

#### 13. Vista previa no logra conectarse con tu tienda

Esto es un ajuste de nuestro lado. Escríbenos: lo corregimos nosotros, no tú.

---

### Preguntas frecuentes

**¿Tengo que pegar algún código en mi tienda?**
No. Lo único que se pega en Circular es el código que empieza con `GTM-`, en **Mi sitio web → Configuraciones → SEO**. Todo el resto pasa en Tag Manager y en Meta, que son cuentas tuyas.

**¿Esto sirve también para Google Analytics 4?**
Sí, y ahí es más fácil todavía: en la etiqueta de evento de GA4 hay una opción para enviar los datos de comercio electrónico tomándolos de la capa de datos. Activándola, los cuatro eventos llegan con sus productos e importes sin configurar nada más.

**¿Puedo medir con Meta y con Analytics al mismo tiempo?**
Sí. Un mismo contenedor de Tag Manager puede tener todas las etiquetas que quieras: el mismo evento alimenta a Google y a Meta a la vez, sin tocar de nuevo el backoffice.

**¿Le llega algún dato de mis clientes a Meta?**
De estos eventos, no. No viajan nombre, correo, teléfono ni documento: solo códigos de producto, nombres de producto, importes y el número de orden.

**Cobro por transferencia o en el local. ¿Se registra igual la venta?**
Sí. El evento de compra sale igual cuando la orden queda confirmada, aunque el pago no pase por Mercado Pago. Puede tardar unos segundos más en aparecer que en una compra con tarjeta.

**Mi agencia me pide "acceso al píxel". ¿Qué le doy?**
Acceso a tu contenedor de Google Tag Manager y a tu cuenta de Meta Business. De Circular no necesita nada más que el código del contenedor puesto en el backoffice, y eso lo haces tú en dos minutos con el Paso 2.

**¿Cómo apago todo?**
Entra a **Mi sitio web → Configuraciones → SEO**, borra el contenido del campo *ID de Google Tag Manager* y guarda. Se apaga el contenedor entero: Meta, Analytics y cualquier otra etiqueta que tengas.

**¿Tiene costo?**
Google Tag Manager y el píxel de Meta son gratuitos. Lo que se paga son los anuncios.

<p class="doc-aliases" markdown>Términos relacionados: google tag manager, gtm, contenedor gtm, pixel de meta, píxel de meta, meta pixel, facebook pixel, pixel de facebook, eventos, eventos de ecommerce, conversiones, purchase, add to cart, view content, remarketing, retargeting, catálogo de meta, anuncios, publicidad, instagram ads, facebook ads, medir ventas, atribución</p>
