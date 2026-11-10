---
title: Imprimir etiquetas de productos
slug: imprimir-etiquetas
order: 60
type: Guía
aliases: generar etiquetas, imprimir el código de la prenda, configurar la impresora,
  me sale cortado, descargar etiquetas, etiquetas en excel o csv, imprimir solo las
  prendas nuevas, el archivo me trae todos los productos, las etiquetas salen sin
  precio, no aparece el precio en la etiqueta, el nombre sale cortado en la etiqueta,
  imprimir etiquetas de una proveedora, imprimir desde el sistema, brother ql-800,
  impresora brother, imprimir por usb, conectar impresora, rollo de etiquetas, dk-11201,
  dk-22205, dk-22251, rollo negro y rojo, no es una impresora de etiquetas, editor
  lite, tapa abierta, imprimir en windows, descargar pdf de etiquetas, imprimir etiquetas
  de algunos productos, imprimir etiquetas seleccionadas, barra de selección, luz
  roja parpadeando, la impresora rechaza la etiqueta, el sistema no deja usar la impresora,
  no aparece la impresora, detalle técnico, copiar detalle, imprimir en linux, imprimir
  en mac, se imprimen las primeras 1000, la impresora no confirmó, menú imprimir etiquetas
---

# Imprimir etiquetas de productos

Las etiquetas se imprimen de dos maneras, según la impresora que tengas:

- Con una impresora **Brother QL** (como la QL-800), las imprimís **desde la página**, sin descargar nada ni abrir otro programa. El sistema arma la etiqueta con el nombre, el código de barras y el precio.
- Con cualquier otra impresora, Software Circular genera un **archivo** con los datos de tus productos; ese archivo se carga después en el software de tu impresora de etiquetas, que es donde se arma el diseño y se manda a imprimir.
!!! tip "Tip"
    Imprimir etiquetas lo puede hacer **cualquier usuario** con acceso a **Productos**. Elegir productos de la lista con las casillas (para imprimir solo esos) es para **Encargados y Administradores**; elegir el rollo de la impresora, solo para **Administradores**.

### 1. Elegí qué productos entran

Se imprimen —o entran en el archivo— **exactamente los productos que tengas filtrados en pantalla**, no todo tu catálogo, salvo que elijas algunos con las casillas.

Entrá a **Inventario › Productos** y usá el buscador y los filtros de la lista —**Fecha de creación**, **Estado**, **Propiedad**, **Local**, **Canal de venta**, **Tags**— para quedarte solo con las prendas que vas a etiquetar. Lo más habitual es filtrar por fecha, para imprimir únicamente lo que cargaste ese día.

Si querés etiquetar unas prendas sueltas, marcá sus casillas en la lista: aparece la barra de selección, con **Imprimir etiquetas**. Podés elegir hasta 100 productos por vez, también de distintas páginas de la lista.

!!! tip "Tip"
    También podés hacerlo desde la ficha de una proveedora, en su pestaña **Productos**: ahí la lista ya viene acotada a sus prendas, así que no necesitás filtrar nada más.

### 2. Imprimir directo en una impresora Brother QL

1. Abrí el panel de impresión de una de estas tres maneras:
    - En el menú de la izquierda, abrí **Productos** (la flechita al lado del nombre) y tocá **Imprimir etiquetas**. Se abre la lista de productos con el panel ya desplegado: filtrá ahí mismo.
    - Con la lista ya filtrada, tocá **Etiquetas** (al lado del buscador) y elegí **Imprimir etiquetas…**.
    - Con productos marcados, tocá **Imprimir etiquetas** en la barra de selección.
1. El panel se abre debajo de la barra de la lista y dice cuántas etiquetas van a salir (**N etiquetas: una por producto del listado filtrado**, o **una por producto seleccionado**) y en qué rollo.
1. Elegí cómo imprimir:
| Camino | Cómo se usa | Dónde funciona |
| --- | --- | --- |
| **Imprimir directo por USB** | Tocá **Conectar impresora**, elegí la Brother QL en la ventana del navegador y tocá **Imprimir N etiquetas**. La impresora se elige una sola vez: la próxima vez ya aparece conectada. Mientras imprime, el panel dice **Imprimiendo X de N…**. | Chrome o Edge en Mac, Linux o Android. No funciona en Windows ni en Safari. |
| **Imprimir con el diálogo del sistema** | **Imprimir…** abre la ventana de impresión de tu computadora: elegí la Brother QL y el tamaño de papel del rollo (queda recordado). **Descargar PDF** baja las mismas etiquetas para imprimirlas después. | Cualquier navegador, con el driver de Brother instalado. En Windows es el camino. |

Cada etiqueta lleva el nombre del producto en una o dos líneas, un código de barras con el Id escrito debajo, y los precios: el precio de lista en grande y, más chicos, los perfiles de precio con su nombre. Los precios salen con la misma regla que en el archivo: mirá el aviso del paso 4.

El código de barras lleva **solo los números del Id** (de `PR_02_1502_22132` quedan `02150222132`): así las barras salen más anchas y cualquier lector lo lee bien. El lector del celular, el buscador de productos y la búsqueda de una venta encuentran la prenda con esos números; también si un lector de pistola escribe `?` donde el Id tiene `_`.

Al terminar, abajo de la página aparece **Se imprimieron N etiquetas.** Si dice **la impresora no confirmó M**, revisá que hayan salido todas: la impresora recibió las etiquetas pero no avisó que las imprimió.

!!! warning "Atención"
    **Hasta 1.000 etiquetas por tanda.** Si la lista tiene más productos, salen las primeras 1.000, las de los productos más nuevos, y el panel dice cuántos productos tiene la lista. Para el resto, acotá el filtro (por ejemplo, por fecha de creación) o marcá productos en la lista, hasta 100 por vez.

### El rollo

El tamaño de la etiqueta es el del rollo elegido en **Configuración › Productos › Rollo de etiquetas** (solo Administradores). De fábrica es el **Brother DK-11201 · 29 × 90 mm**, el que viene con la impresora. Al imprimir por USB, la impresora informa qué rollo tiene puesto y se imprime en ese aunque la configuración diga otro; el panel te lo avisa con **La impresora tiene puesto …: se imprime en ese rollo.**

| Rollo | Etiqueta |
| --- | --- |
| **Brother DK-11201** | 29 × 90 mm (viene con la impresora) |
| **Brother DK-11209** | 62 × 29 mm |
| **Brother DK-11204** | 17 × 54 mm |
| **Brother DK-11203** | 17 × 87 mm |
| **Brother DK-11208** | 38 × 90 mm |
| **Brother DK-11202** | 62 × 100 mm |
| **Troqueladas** de 29 × 42, 39 × 48 y 52 × 29 mm | la medida de la etiqueta |
| **Brother DK-22205** (o los film DK-22212 / DK-22213) | rollo continuo de 62 mm, etiqueta de 30 mm |
| **Brother DK-22210** (o el film DK-22211) | rollo continuo de 29 mm, etiqueta de 90 mm |
| **Brother DK-22225**, **DK-22223**, **DK-N55224** | rollo continuo de 38, 50 o 54 mm, etiqueta de 30 mm |
| **Brother DK-22251** | rollo continuo de 62 mm **negro y rojo**, etiqueta de 30 mm, impresa en negro |

!!! warning "Atención"
    **Si tu rollo es el negro y rojo (DK-22251), elegilo en la configuración.** La impresora no distingue ese rollo del 62 mm común, y solo acepta imprimir en él de una manera especial. Con el 62 mm común configurado, la impresora rechaza la tanda y queda con la luz roja parpadeando: apagala, prendela y elegí el **DK-22251** en **Configuración › Productos**.

Si la impresora informa un rollo que el sistema no conoce, el panel lo dice (**La impresora informa un rollo de … que no conocemos**) y se imprime con el tamaño del rollo configurado.

### Cuando el navegador no puede usar la impresora por USB

Debajo de **Conectar impresora** hay un **Detalle técnico** con lo que vio el navegador en el intento (navegador, impresora, rollo y cada rechazo). Si algo falla, tocá **Copiar detalle** y pegalo en el chat con Software Circular. Cada rechazo también nos llega solo, así que podemos ayudarte sin que nos mandes nada.

| El panel dice | Qué significa | Qué hacer |
| --- | --- | --- |
| **Este navegador no imprime por USB directo.** | Estás en Safari, Firefox u otro navegador sin USB. | Usá Chrome o Edge, o imprimí con **Imprimir…**. |
| **En Windows el navegador no puede usar la impresora por USB** | En Windows la impresora la toma el driver de Brother. | Imprimí con **Imprimir…**, el diálogo del sistema. |
| **El dispositivo elegido no es una impresora de etiquetas.** | La QL-800 está en modo Editor Lite (el botón con la luz verde) y la computadora la ve como un pendrive. | Mantené apretado el botón **Editor Lite** hasta que la luz verde se apague, desconectá y volvé a conectar la impresora, y elegila de nuevo. Lo mismo si en la ventana del navegador no aparece ninguna impresora. |
| **El sistema no deja usar la impresora desde el navegador.** | Otro programa o el sistema tienen tomada la impresora. En **Linux**, el navegador necesita permiso sobre el puerto USB; en **Mac**, suelen ser los programas de Brother (P-touch Editor, el monitor de estado). | En Mac, cerrá los programas de Brother y volvé a intentar. En Linux, mandanos el **Detalle técnico** y te pasamos la configuración. Si no, imprimí con **Imprimir…**. |
| **No se pudo abrir la impresora.** / **La impresora no responde.** | La impresora está apagada, desconectada o no contesta. | Revisá que esté encendida y conectada, y volvé a intentar. |
| **La impresora dejó de recibir datos.** | Se cortó la conexión a mitad de la tanda. | Revisá el cable y volvé a imprimir. |
| **La impresora informó un error: …** (sin rollo, tapa abierta, se terminó el rollo, cuchilla trabada, hay que cambiar el rollo…) | La impresora frenó la tanda por eso. El aviso dice cuántas etiquetas llegaron a salir. | Resolvelo y volvé a imprimir. |
| **No se eligió ninguna impresora.** | Cerraste la ventana del navegador sin elegir. | Tocá **Conectar impresora** de nuevo. |
| **La impresión por USB falló por algo que no esperábamos.** | Un error que no conocemos. | Tocá **Copiar detalle** y mandánoslo; mientras tanto, imprimí con **Imprimir…**. |

### 3. Descargá el archivo

Si tu impresora no es una Brother QL, tocá **Etiquetas**, al lado del buscador y del botón **Descargar**. No es un botón simple: se despliega con **Imprimir etiquetas…** y los dos formatos de archivo.

| Formato | Qué descarga |
| --- | --- |
| **Etiquetas (Excel)** | Una planilla `.xlsx`. Es la opción más común. |
| **Etiquetas (CSV)** | Un archivo de texto separado por comas, para los programas de impresión que no aceptan Excel. |

Si no sabés cuál pide tu impresora, probá primero con Excel.

### 4. Qué trae el archivo

Una fila por producto, con estas columnas:

- **Id** — el código del producto, el `PR_…` que ves en el listado.
- **Nombre** — el nombre de la prenda, **recortado a los primeros 25 caracteres**.
- **Precio_venta** y **Precio_alquiler**, y una columna por cada perfil de precio que tengas activo.
!!! warning "Atención"
    Si el archivo te sale **sin ninguna columna de precio**, no está fallando: los precios aparecen solo si pediste que se muestren en las etiquetas. Eso se activa en **Configuración › Precios y medios de pago**, en la opción **Etiquetas de productos** de cada perfil de precio. Si no tenés perfiles configurados, el archivo sale sin esas columnas.

### 5. Cargá el archivo en tu impresora

Abrí el software de tu impresora de etiquetas e importá el archivo que descargaste. Desde ahí elegís qué columnas se imprimen y cómo se ven.

!!! tip "Tip"
    El diseño, el tamaño y la distribución de la etiqueta se configuran en el software de la impresora, no en el sistema. Si la etiqueta sale cortada o descuadrada, el ajuste va por ahí. La única excepción es el **nombre**: ese ya viene recortado a 25 caracteres desde el archivo, y no se puede alargar.

Si todavía no tenés impresora o estás por comprar una, mirá [Qué impresora de etiquetas comprar para el local](../preguntas-frecuentes.md#que-impresora-comprar).

### Tener en cuenta

- **Si cambiás un filtro o la búsqueda, el panel se cierra**, para que nunca imprimas otra cosa que lo que ves. Volvé a abrirlo con la lista nueva. El panel de una selección no se cierra con los filtros: imprime los productos que marcaste.
- **Mientras imprime, el panel no se puede cerrar** ni abrir otro, para no cortar la tanda. Esperá a que termine.
- **Una selección es de hasta 100 productos**, los que marcaste en la lista. Si uno se borró entre que lo marcaste e imprimiste, se saltea; si no queda ninguno, el panel dice **Ninguno de los productos seleccionados sigue en el catálogo.**
- **La impresora manda.** Por USB, el rollo que la impresora informa le gana al configurado, salvo el negro y rojo, que se elige en la configuración.
- **Si la impresora queda con la luz roja parpadeando**, rechazó la tanda: apagala y prendela con el botón de encendido hasta que vuelva a verde fijo, y mirá el aviso del panel para saber por qué.
- **Con el diálogo del sistema, el tamaño de papel lo elegís vos** en la ventana de impresión, y tiene que ser el del rollo puesto. Si la impresora rechaza la impresión, revisá ahí el tamaño elegido.
### Qué pasa después

Imprimir las etiquetas o generar el archivo no modifica nada: tus productos quedan igual y podés volver a imprimir o descargar las veces que quieras. El archivo tampoco queda guardado en el sistema — es una descarga, así que si lo necesitás de nuevo, repetí los pasos con el mismo filtro.

<p class="doc-aliases" markdown>Términos relacionados: generar etiquetas, imprimir el código de la prenda, configurar la impresora, me sale cortado, descargar etiquetas, etiquetas en excel o csv, imprimir solo las prendas nuevas, el archivo me trae todos los productos, las etiquetas salen sin precio, no aparece el precio en la etiqueta, el nombre sale cortado en la etiqueta, imprimir etiquetas de una proveedora, imprimir desde el sistema, brother ql-800, impresora brother, imprimir por usb, conectar impresora, rollo de etiquetas, dk-11201, dk-22205, dk-22251, rollo negro y rojo, no es una impresora de etiquetas, editor lite, tapa abierta, imprimir en windows, descargar pdf de etiquetas, imprimir etiquetas de algunos productos, imprimir etiquetas seleccionadas, barra de selección, luz roja parpadeando, la impresora rechaza la etiqueta, el sistema no deja usar la impresora, no aparece la impresora, detalle técnico, copiar detalle, imprimir en linux, imprimir en mac, se imprimen las primeras 1000, la impresora no confirmó, menú imprimir etiquetas</p>
