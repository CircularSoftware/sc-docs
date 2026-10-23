---
title: Registrar una nueva venta
slug: nueva-venta
order: 10
type: Guía
aliases: cómo hago una venta, no me deja hacer la orden, consumidor final, buscar
  el producto por código, siempre tengo que agregar al cliente, pagar todo, pagar
  con dos medios, elegí primero la tienda de la venta, dónde elijo la tienda, cargar
  un vale, escanear la etiqueta
---

# Registrar una nueva venta

Esta es la pantalla que más vas a usar. La lógica es siempre la misma: **a la izquierda completás campos, a la derecha se va armando la orden** con el detalle y los totales. El panel izquierdo se puede achicar con la flecha del menú para trabajar más cómodo.

Entrá a **nueva venta** desde el menú lateral.

!!! note "Nota"
    ¿Una venta de mostrador, con la persona en el local? Encendé **Nuevo flujo de venta**, arriba a la derecha: el cliente, la entrega y la tienda vienen resueltos y la venta se hace en pocos clics. Mirá [Venta rápida: vender en el mostrador en pocos clics](https://app.notion.com/p/40244bec059281838402ecbff3348f37). Esta guía explica el formulario completo, con el interruptor apagado.

La **Tienda** de la venta está en la tarjeta **Pagos de la orden**: es la caja a la que entra la plata. Casi siempre ya viene puesta: si trabajás en un solo local, ese; si tu usuario tiene un local asignado, el tuyo. Si tenés varios locales y no viene puesta, la propone la primera prenda que agregás, y la podés cambiar. Si tu usuario solo puede vender prendas de su tienda, el buscador no te deja agregar productos hasta que la elijas: te avisa con *Elegí primero la tienda de la venta, en «Pagos»*.

### 1. Cliente

Buscá a la persona por nombre, email o teléfono. Tenés tres caminos:

- Ya existe → la seleccionás de la lista.
- Es nueva y tenés sus datos → **nuevo**, completás la ventana y **confirmar**.
- No tenés los datos → tocá **Consumidor final**, al lado de **Nuevo**. La venta queda registrada sin datos de la persona (y no le llega ningún mail).
![Ventana de alta rápida de cliente desde la venta](/assets/nueva-venta/4d07f4b96c17.webp)

### 2. Productos y extras

En **Productos** buscá por nombre o código. Cada producto que agregues aparece a la derecha con su precio base. Si tenés el celular vinculado como lector, escaneá la etiqueta y la prenda se agrega sola: mirá [Usar el celular como lector de códigos](https://app.notion.com/p/40244bec059281f0be88c621023b6ce3).

En **Extras** cargás todo lo que no es una prenda: la bolsa, un recargo, la garantía de un alquiler. Hacé clic en **Agregar extra**, elegí uno de la lista de tu tienda, completá **Precio unitario** y **Cantidad**, y confirmá con **Agregar**. Solo aparecen los extras que estén creados: mirá *Extras: cobrar la bolsa, la garantía y otros conceptos*.

!!! tip "Tip"
    Se puede buscar por el código del producto (`PR_…`), por el código alternativo o solo por los últimos números de cualquiera de los dos. No importan las mayúsculas ni los acentos. Los campos con asterisco rojo son obligatorios.

### 3. Entrega

Elegí el **Tipo de entrega** y la **Sucursal**, y definí el toggle **Retira en el momento**:

| Situación | Toggle | Por qué |
| --- | --- | --- |
| La persona está en el local | **Activado** | Se lleva la prenda en el momento, la entrega queda cerrada. La orden solo se guarda con el total pagado. |
| Venta por WhatsApp o Instagram | **Desactivado** | El producto deja de estar disponible para otros, pero queda marcado como pendiente de preparar y entregar o enviar. |

Después hacé clic en **confirmar entrega**.

![Bloque de entrega y detalle de la orden](/assets/nueva-venta/6635b3c4ef0f.webp)

![Toggle Retira en el momento](/assets/nueva-venta/4d1cbf6e0801.webp)

### 4. Descuentos

Si corresponde, abrí el bloque **Descuentos**. El detalle de cómo funcionan está en la guía *Aplicar descuentos en una venta*.

### 5. Pagos

En **Agregar pago** elegí el **Tipo de pago**. Debajo, la pantalla te dice cuánto cobrar con ese medio: *Para cancelar la orden con este medio, ingresá $…*. Si tu tienda tiene precios distintos por medio de pago, ese importe ya los tiene en cuenta.

- **Paga todo con un medio** → tocá **Pagar todo ($…)**. Registra el saldo entero con ese medio, sin tipear nada.
- **Paga una parte** → escribí en **Valor de pago** el importe que te dieron y tocá **Agregar pago**. Después elegí el otro medio y repetí, o tocá **Pagar todo** para el resto. Así cargás, por ejemplo, una parte en efectivo y el resto con débito.
El importe de cada pago es lo que recibiste con ese medio; no puede superar lo que falta pagar.

Mirá el campo **Por abonar** del panel derecho: mientras quede saldo aparece en rojo, y recién cuando llega a $0 se pone en verde. Ahí la orden está lista para guardarse.

Si la persona tiene un vale a favor, cargálo antes en **Agregar vale** con su ID. El vale se usa entero: si vale más que la compra, la diferencia vuelve en un vale nuevo, que aparece al guardar.

![Pagos cargados y saldo en cero](/assets/nueva-venta/ef143c827a50.webp)

### 6. Guardar

Hacé clic en **guardar**. Con eso se disparan cinco cosas a la vez.

#### Se genera el ticket

Se abre el PDF con el detalle de productos, extras, totales y los comprobantes emitidos en DGI.

![Ticket generado](/assets/nueva-venta/44a6a7c96546.webp)

#### Se le envía un mail a la persona

Con su orden y el mismo ticket adjunto. **No hace falta imprimirlo.** Una venta a **Consumidor final** no manda mail: si la persona lo quiere, elegila como cliente.

#### Se emiten los comprobantes en Biller

Siempre que el local esté conectado a facturación electrónica. Ver la guía *Cómo se factura al vender y al pagar comisiones*.

!!! warning "Atención"
    Si vendés productos de un local que **no** está conectado con facturación electrónica, esos productos no generan comprobante fiscal — solo lo hacen los que sí lo están. Pasa cuando armás una orden con mercadería de otra tienda, algo que depende del permiso **Puede vender productos de otras tiendas** de tu usuario. Un Administrador lo tiene siempre.

#### Queda la orden

En **ordenes** ves todas las del día con su ID, estado, cliente, fecha, tipo de entrega y total.

![Listado de órdenes](/assets/nueva-venta/2d3c019d7df4.webp)

#### Se genera la comisión del proveedor

Si la prenda tenía dueño, la comisión se le carga automáticamente. Se ve en la ficha de esa persona, pestaña **Comisiones**. Nace como **Pendiente** y recién pasa a **Para Abonar** cuando vence el plazo, porque las comisiones se pagan a mes vencido.

![Comisiones del proveedor](/assets/nueva-venta/ce03bb22d8be.webp)

#### Se registra el movimiento de caja

En **pagos → movimiento de caja** queda el ingreso desglosado por forma de pago, con el saldo de caja actualizado.

![Movimientos de caja](/assets/nueva-venta/ff70c18fca2a.webp)

!!! video "Video"
    Ver el video tutorial: [https://youtu.be/PBsSGpr0zOY](https://youtu.be/PBsSGpr0zOY)

<p class="doc-aliases" markdown>Términos relacionados: cómo hago una venta, no me deja hacer la orden, consumidor final, buscar el producto por código, siempre tengo que agregar al cliente, pagar todo, pagar con dos medios, elegí primero la tienda de la venta, dónde elijo la tienda, cargar un vale, escanear la etiqueta</p>
