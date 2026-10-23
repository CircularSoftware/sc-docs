---
title: Usar el celular como lector de códigos
slug: celular-lector-de-codigos
order: 12
type: Guía
aliases: escanear etiquetas, lector de código de barras, scanner, escáner, vincular
  celular, QR para vincular, celular conectado, el celular no lee el código, no se
  agregó el producto, no hay una orden abierta, este QR venció, este celular se desvinculó,
  código de barras de la etiqueta, la cámara no funciona, agregar productos escaneando,
  pistola lectora
---

# Usar el celular como lector de códigos

Con **Vincular celular** convertís tu teléfono en un lector de códigos de barras para el panel: apuntás la cámara a la etiqueta de la prenda y la prenda se agrega sola a la venta que tenés abierta en la computadora. No hay que instalar nada ni comprar un lector: alcanza con el celular y un QR o código de barras.

!!! tip "Tip"
    Funciona en la pantalla de **nueva venta** (también de **nuevo alquiler**) y al **editar una orden**. Lo puede usar **cualquier usuario** del panel: Administrador, Encargado o Empleado. En el celular no hace falta iniciar sesión.

### Antes de empezar: las etiquetas

El celular lee **códigos de barras (Code 128)** y **códigos QR**. Para que la prenda se encuentre, el código de la etiqueta tiene que ser uno de estos:

- El **código del producto**, el `PR_…` que ves en el listado. Es la columna **Id** del archivo de etiquetas: en el software de tu impresora, armá el código de barras con esa columna. Mirá [Imprimir etiquetas de productos](https://app.notion.com/p/3bf44bec05928164803fc3fddf5f89c9).
- El **código alternativo** del producto, si tu tienda ya imprime sus etiquetas con ese código.
- Un QR con el link a la página de la prenda en tu tienda online.
El código tiene que ser **exacto**. A diferencia del buscador, el lector no busca por parecido ni por los últimos números: si la etiqueta dice `1627` y el código alternativo es `1PI78R1627`, no la encuentra. Las mayúsculas no importan.

### 1. Vincular el celular

1. En la computadora, abrí **nueva venta** (o la orden que vas a editar).
1. Arriba a la derecha, tocá **Usar celular como lector**. Aparece un QR.
1. Con el celular, abrí la cámara y escaneá ese QR. Se abre la página **Lector de códigos** en el navegador del celular.
1. Si el celular lo pide, **permití el acceso a la cámara**.
1. En la computadora, el botón pasa a decir **Celular conectado**.
!!! warning "Atención"
    El QR **vence a los 2 minutos** y sirve para **un solo celular**. Si venció, tocá **Generar otro QR**.

!!! note "Nota"
    Captura pendiente: el botón «Vincular celular» abierto con el QR, y la página «Lector de códigos» en el celular.

### 2. Escanear

Apuntá la cámara del celular a la etiqueta. Cuando lee el código, el celular vibra, lo manda y muestra qué pasó con esa prenda:

| El celular dice | Qué significa | Qué hacer |
| --- | --- | --- |
| **Agregado: (nombre de la prenda)** | La prenda se agregó a la orden. | Seguí con la próxima. |
| **PR_… ya está en la orden** | Esa prenda ya estaba agregada. | Nada: no se agrega dos veces. |
| **PR_… no está disponible** | Está vendida, reservada o en otro estado. En un alquiler, también si está ocupada en esas fechas. | Revisá la prenda en **Productos**. |
| **Ningún producto tiene el código …** | El código no es el de ninguna prenda (por ejemplo, el código de barras de un envase). | Revisá la etiqueta, o buscá la prenda a mano. |
| **N productos tienen el código …: elegilo en el buscador** | Varias prendas disponibles tienen el mismo código alternativo. | Buscala en el buscador de la computadora y elegí la correcta. |
| **PR_… es de la tienda X y esta orden es de Y** | Tu tienda no permite vender prendas de otro local en la misma orden. | Hacé la venta desde la tienda de la prenda. |
| **Elegí la tienda de la orden antes de agregar productos** | La orden todavía no tiene tienda. | Elegila en la computadora y volvé a escanear. |
| **Elegí el período del alquiler antes de agregar productos** | Es un alquiler sin fechas. | Elegí el período y volvé a escanear. |
| **No hay una orden abierta en el backoffice** | La pestaña vinculada no está en una nueva venta ni editando una orden. | Abrí una nueva venta en esa pestaña. |
| **Este código no es de un producto** | Es un QR de otra página, o un texto que no es un código. | Escaneá la etiqueta de la prenda. |
| **No se agregó: el backoffice no respondió** | La computadora no contestó en un minuto (sin internet, apagada, pestaña colgada). | Revisá la computadora y volvé a escanear. Ese escaneo no se va a agregar después. |

En la computadora, al abrir **Celular conectado** ves el último escaneo.

Cada prenda agregada por el celular es igual que una elegida en el buscador: aplican las mismas reglas de stock, precios y tiendas, y la orden se guarda con **Guardar** (o con **Pagar todo** en el Nuevo flujo de venta: mirá [Venta rápida: vender en el mostrador en pocos clics](https://app.notion.com/p/40244bec059281838402ecbff3348f37)), como siempre.

### Cuánto dura la vinculación

El celular queda vinculado a **esa pestaña del navegador**, no a una orden. Por eso:

- **Sigue vinculado** si guardás la venta y abrís la siguiente, si recargás la página o si vas a otra pantalla y volvés, siempre en la misma pestaña. Podés trabajar todo el día sin volver a vincular.
- **Se desvincula** si tocás **Desvincular** (en la computadora o en el celular), si cerrás sesión, si la pestaña queda cerrada más de 10 minutos, si vinculás otro celular a esa pestaña o ese celular a otra pestaña, y siempre a las **12 horas**.
Cuando se desvincula, el celular lo avisa (por ejemplo **Este celular se desvinculó** o **La vinculación venció: duran 12 horas**). Para seguir, tocá **Vincular de nuevo** en la computadora y escaneá el QR nuevo.

### Tener en cuenta

- **Un celular por pestaña, una pestaña por celular.** Si tenés dos pestañas del panel abiertas, los escaneos llegan solo a la que vinculaste. Si dos vendedoras trabajan a la vez, cada una vincula su celular en su computadora.
- **La misma etiqueta no se manda dos veces seguidas.** Si la cámara queda apuntando a la misma etiqueta, se manda una sola vez. Para agregar otra prenda, apuntá a otra etiqueta.
- **La cámara necesita permiso.** Si el celular dice **Permití el acceso a la cámara para escanear**, tocá el candado de la barra de direcciones y habilitá la cámara. Si dice que el navegador no puede usar la cámara, abrí el link en **Chrome** (Android) o **Safari** (iPhone).
- **En iPhone puede tardar un poco más en leer.** Acercá la etiqueta, con buena luz y sin reflejos.
- **El celular solo manda códigos.** Desde el celular no se ven ni se cambian órdenes, productos ni clientes: el que decide y guarda es la computadora. Si perdés el celular, tocá **Desvincular** en la computadora o cerrá sesión.
- **Si ya tenés un lector USB**, no hace falta vincular nada: el lector escribe el código en el buscador de productos como si fuera un teclado.
### Qué pasa después

Nada cambia en la orden: las prendas escaneadas se guardan, se cobran y se facturan igual que las que elegís en el buscador. Cómo completar la venta está en [Registrar una nueva venta](https://app.notion.com/p/3bf44bec059281e98515ec8e3933a0d9).

<p class="doc-aliases" markdown>Términos relacionados: escanear etiquetas, lector de código de barras, scanner, escáner, vincular celular, QR para vincular, celular conectado, el celular no lee el código, no se agregó el producto, no hay una orden abierta, este QR venció, este celular se desvinculó, código de barras de la etiqueta, la cámara no funciona, agregar productos escaneando, pistola lectora</p>
