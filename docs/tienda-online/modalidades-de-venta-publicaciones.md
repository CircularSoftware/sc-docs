---
title: Ofrecer modalidades de venta en las publicaciones de clientas
slug: modalidades-de-venta-publicaciones
order: 75
type: Guía
aliases: modalidad de venta, tipo de venta, venta básica, venta estándar, cuánto recibe
  la clienta, cuánto voy a recibir, recibirías aprox, comisión de la tienda más IVA,
  producto en casa de la clienta, producto en el local, parte de la tienda, las condiciones
  de esa modalidad cambiaron, comisión del producto, términos y condiciones al publicar,
  aceptar los términos, no puede enviar la publicación
---

# Ofrecer modalidades de venta en las publicaciones de clientas

Si consignás de más de una manera —por ejemplo, prendas que quedan en el local y prendas que se quedan en casa de la clienta hasta que se venden, cada una con su comisión—, podés cargar esas maneras como **modalidades de venta**. La clienta elige una al proponerte un producto y ve, antes de mandarlo, cuánto recibiría según el precio que sugiere. Esta guía explica cómo cargarlas y qué ve cada lado.

!!! danger "Importante"
    Es opcional. Si no cargás ninguna modalidad, el formulario de **Proponer un producto** queda como siempre. Necesitás tener activadas las publicaciones de clientes: mirá [Activar que tus clientas propongan productos](activar-publicaciones-clientes.md).

### Cargar las modalidades

1. Entrá a **Configuración › Tienda web › Ajustes de la tienda**.
1. Abrí la pestaña **Checkout**.
1. En **Publicaciones de clientes**, debajo del interruptor, buscá **Modalidades de venta** y tocá **Agregar modalidad**.
1. Completá cada modalidad:
    - **Nombre**: cómo la ve la clienta, por ejemplo *Estándar*.
    - **Dónde queda el producto**: **En el local** o **En casa de la clienta**.
    - **Parte de la tienda, sin impuesto (%)**: lo que te quedás vos del precio de venta, antes del impuesto. Por ejemplo, 25.
    - **Impuesto sobre la parte de la tienda (%)**: el impuesto que se suma a tu parte, por ejemplo 22 de IVA. Si no corresponde, dejalo vacío.
    - **Explicación para la clienta**: las condiciones de la modalidad, con tus palabras. Podés copiar el texto de tu página de términos y condiciones.
1. Tocá **Guardar**.
Debajo de cada modalidad ves la cuenta hecha, por ejemplo *La tienda se queda con el 30,5% del precio de venta y la clienta recibe el 69,5%.* Podés cargar hasta 5 modalidades.

!!! note "Nota"
    Captura pendiente: pestaña Checkout con dos modalidades cargadas y la cuenta debajo de cada una.

!!! warning "Atención"
    Acá no va la comisión de la clienta. En el resto del sistema, «comisión» es lo que recibe la clienta (por ejemplo, 69,5). En este campo va **tu** parte (por ejemplo, 25). Si la cuenta de abajo dice que la clienta recibe muy poco, revisá ese número.

#### Un ejemplo

| Modalidad | Dónde queda | Parte de la tienda + impuesto | La tienda se queda con | La clienta recibe |
| --- | --- | --- | --- | --- |
| **Estándar** | En el local | 25% + 22% | 30,5% | 69,5% |
| **Básica** | En casa de la clienta | 15% + 22% | 18,3% | 81,7% |

El impuesto se calcula sobre tu parte, no sobre el precio: 25% más el 22% de ese 25% da 30,5%.

#### Si algo está mal

Cada modalidad te dice qué le falta: el nombre, una parte de la tienda entre 0 y 100 con hasta dos decimales, o que con el impuesto te quedarías con el 100% del precio o más (a la clienta siempre le tiene que quedar algo). Mientras alguna tenga un error, no se guarda nada de la pestaña. Para sacar una modalidad, tocá **Quitar modalidad**.

### Qué ve la clienta en la tienda

Cuando entra a **Mi cuenta › Mis publicaciones › Proponer un producto**, el formulario suma la sección **Modalidad de venta**, antes del precio sugerido:

1. Ve una opción por modalidad, con el nombre, lo que se queda la tienda (por ejemplo, *La tienda se queda con el 25% + IVA (30,5%): vos recibís el 69,5% del precio de venta.*), dónde queda el producto y tu explicación.
1. Elige una. Si cargaste una sola, ya viene elegida. Sin elegir, no puede enviar la publicación.
1. Cuando escribe el **Precio sugerido**, debajo le aparece cuánto recibiría, por ejemplo *Con la modalidad Estándar recibirías aprox. $ 695.* La cuenta se actualiza mientras escribe.
1. Antes de enviar, marca **Acepto los términos y condiciones de la tienda.** El link **Leer los términos** abre tu página de términos y condiciones en otra pestaña, la misma que piden el checkout y el registro. Sin marcarlo, no puede enviar la publicación. Se pide en cada publicación, aunque no cargues modalidades.
!!! warning "Atención"
    El link muestra lo que tengas en tu página **Términos y Condiciones**. Antes de activar las publicaciones, revisá en **Mi sitio web › Páginas** que esa página tenga tu texto y esté publicada: si está vacía, la clienta acepta algo que no puede leer. Es un buen lugar para explicar tus modalidades de venta.

!!! note "Nota"
    Captura pendiente: formulario Proponer un producto con la sección Modalidad de venta y el monto «recibirías aprox.» debajo del precio.

El monto es aproximado: lo que cobra al final depende del precio al que se venda.

### Después de enviarla

La publicación guarda la modalidad con los números que vio la clienta. Si después cambiás esa modalidad o la sacás, las publicaciones que ya llegaron siguen mostrando lo que ella eligió.

- **La clienta** ve en **Mis publicaciones** la modalidad y cuánto recibiría al precio en juego: el acordado; si todavía no hay, la última propuesta; si no, el que ella sugirió. Si le proponés otro precio, el monto se recalcula, así sabe cuánto le quedaría antes de aceptar.
- **Vos** ves en el detalle de la publicación, en la tarjeta **Producto**, la fila **Modalidad de venta**, con las mismas condiciones y el mismo monto que ve ella. En la tarjeta de la clienta, **Aceptó los términos** dice cuándo los aceptó (las publicaciones anteriores dicen *No se pedían cuando la envió*).
Cómo revisar, aprobar y crear el producto está en [Revisar, aprobar o rechazar publicaciones de clientas](../catalogo/revisar-publicaciones-clientes.md).

!!! tip "Tip"
    Si cambiás una modalidad mientras una clienta tiene el formulario abierto, al enviar le aparece *La tienda cambió las condiciones de esa modalidad. Recargá la página para ver las nuevas.* Así nunca queda guardada una modalidad con números distintos a los que ella vio.

### Al crear el producto

Cuando aprobás la publicación y creás el producto desde la tarjeta **Crear el producto**, la modalidad hace dos cosas sola:

- **La comisión del producto es la de la modalidad.** El producto queda con su propia comisión: la parte que le toca a la clienta según lo que eligió (por ejemplo, 81,7% en Básica). Se toma de las condiciones que ella vio al publicar, aunque después hayas cambiado la modalidad. Así cobra lo que le mostró la estimación, calculado sobre el precio al que se venda. La ves en **Se copia de la publicación**, como *Comisión de Ana: 81,7% (modalidad Básica)*.
- **Dónde está el producto** viene elegido según la modalidad, con el aviso *Elegido según la modalidad Básica: confirmá dónde está hoy.* Revisalo: si es Estándar pero la prenda todavía no llegó al local, marcá que sigue en casa de la clienta.
Las dos cosas se pueden cambiar después, desde el producto. La comisión puede tener decimales (por ejemplo, 84,875 con 12,5% + 21% de IVA) y se guarda tal cual.

!!! tip "Tip"
    Si una publicación no tiene modalidad, el producto cobra la comisión de siempre: la de la clienta o la que le cargues al producto.

### Lo que todavía no hace

- **Cambiar la modalidad que eligió la clienta** (por ejemplo, si no tenés lugar en el local) todavía no se puede desde la publicación. Por ahora, acordalo con ella y rechazá o aprobá según corresponda.
- **Si la prenda cambia de lugar después** (de su casa al local), la comisión no cambia sola: si corresponde, cambiala desde el producto.

<p class="doc-aliases" markdown>Términos relacionados: modalidad de venta, tipo de venta, venta básica, venta estándar, cuánto recibe la clienta, cuánto voy a recibir, recibirías aprox, comisión de la tienda más IVA, producto en casa de la clienta, producto en el local, parte de la tienda, las condiciones de esa modalidad cambiaron, comisión del producto, términos y condiciones al publicar, aceptar los términos, no puede enviar la publicación</p>
