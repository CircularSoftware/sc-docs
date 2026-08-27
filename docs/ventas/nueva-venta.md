---
title: Registrar una nueva venta
slug: nueva-venta
order: 10
type: Guía
aliases: cómo hago una venta, no me deja hacer la orden, consumidor final, buscar
  el producto por código, siempre tengo que agregar al cliente
---

# Registrar una nueva venta

Esta es la pantalla que más vas a usar. La lógica es siempre la misma: **a la izquierda completás campos, a la derecha se va armando la orden** con el detalle y los totales. El panel izquierdo se puede achicar con la flecha del menú para trabajar más cómodo.

Entrá a **nueva venta** desde el menú lateral.

### 1. Cliente

Buscá a la persona por nombre, email o teléfono. Tenés tres caminos:

- Ya existe → la seleccionás de la lista.
- Es nueva y tenés sus datos → **nuevo**, completás la ventana y **confirmar**.
- No tenés los datos → asignás la venta a **consumidor final**.
![Ventana de alta rápida de cliente desde la venta](/assets/nueva-venta/4d07f4b96c17.webp)

### 2. Productos y adicionales

En **Productos** buscá por nombre, descripción o código. Cada producto que agregues aparece a la derecha con su precio base.

En **Adicionales** cargás conceptos que no son prendas — típicamente la bolsa. Poné el importe y las unidades y hacé clic en **agregar adicionales**.

!!! tip "Tip"
    Se puede buscar por código nuevo y por código alternativo, respetando mayúsculas. Los campos con asterisco rojo son obligatorios.

### 3. Entrega

Elegí el **Tipo de entrega** y la **Sucursal**, y definí el toggle **Retira en el momento**:

| Situación | Toggle | Por qué |
| --- | --- | --- |
| La persona está en el local | **Activado** | Se lleva la prenda en el momento, la entrega queda cerrada. |
| Venta por WhatsApp o Instagram | **Desactivado** | El producto deja de estar disponible para otros, pero queda marcado como pendiente de preparar y entregar o enviar. |

Después hacé clic en **confirmar entrega**.

![Bloque de entrega y detalle de la orden](/assets/nueva-venta/6635b3c4ef0f.webp)

![Toggle Retira en el momento](/assets/nueva-venta/4d1cbf6e0801.webp)

### 4. Descuentos

Si corresponde, abrí el bloque **Descuentos**. El detalle de cómo funcionan está en la guía *Aplicar descuentos en una venta*.

### 5. Pagos

En **Agregar Pago** elegí el **Tipo de Pago**, poné el **Valor de Pago** y hacé clic en **agregar pago**. Podés cargar varios pagos para una misma orden — por ejemplo una parte en efectivo y el resto con débito.

Mirá el campo **POR ABONAR** del panel derecho: mientras quede saldo aparece en rojo, y recién cuando llega a $0 se pone en verde. Ahí la orden está lista para guardarse.

Si la persona tiene un vale a favor, cargálo antes en **Agregar Vale**.

![Pagos cargados y saldo en cero](/assets/nueva-venta/ef143c827a50.webp)

### 6. Guardar

Hacé clic en **guardar**. Con eso se disparan cinco cosas a la vez.

#### Se genera el ticket

Se abre el PDF con el detalle de productos, extras, totales y los comprobantes emitidos en DGI.

![Ticket generado](/assets/nueva-venta/44a6a7c96546.webp)

#### Se le envía un mail a la persona

Con su orden y el mismo ticket adjunto. **No hace falta imprimirlo.**

#### Se emiten los comprobantes en Biller

Siempre que el local esté conectado a facturación electrónica. Ver la guía *Cómo se factura al vender y al pagar comisiones*.

!!! warning "Atención"
    Si vendés productos de un local que **no** está conectado con facturación electrónica, esos productos no generan comprobante fiscal — solo lo hacen los que sí lo están. Con un usuario de venta de una sola tienda esto no debería pasar, porque solo ves los productos de tu local; puede aparecer con un usuario administrador que ve todos.

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

<p class="doc-aliases" markdown>Términos relacionados: cómo hago una venta, no me deja hacer la orden, consumidor final, buscar el producto por código, siempre tengo que agregar al cliente</p>
