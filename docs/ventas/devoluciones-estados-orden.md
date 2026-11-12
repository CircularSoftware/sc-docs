---
title: Devoluciones y cambiar el estado de una orden
slug: devoluciones-estados-orden
order: 50
type: Guía
aliases: cómo cancelo una venta, hacer un cambio, no me deja devolver, devuelto al
  cliente, revertir una orden finalizada, devolver un pago de mercado pago, número
  de operación de mercado pago, se registró sin número de operación, reembolso por
  mercado pago
---

# Devoluciones y cambiar el estado de una orden

Cuando alguien devuelve una prenda, la devolución se hace desde la orden original. El sistema libera el producto para volver a venderlo y le devuelve la plata al cliente en la forma que elijas.

### Encontrar la orden

Entrá a **ordenes**, buscá la venta y abrila. Arriba a la derecha vas a ver el botón **devolución de productos**.

![Orden con el botón de devolución](/assets/devoluciones-estados-orden/d0c333e39ba1.webp)

### Elegir qué se devuelve

En la pantalla de devolución tenés dos caminos:

- **Devolver todos los productos de la orden** — activás el toggle de arriba.
- **Devolver algunos** — dejás ese toggle apagado y activás solo las prendas que vuelven, en la lista de **Productos seleccionados**.
![Selección de productos a devolver](/assets/devoluciones-estados-orden/e1b5a94aa27e.webp)

A la derecha tenés el resumen de la orden — totales, pagos realizados y estado de la facturación electrónica — y más abajo la **Distribución de la devolución**, que te muestra cuánto corresponde devolver por cada producto y con qué forma de pago se había cobrado.

### Elegir cómo se devuelve la plata

En **Devolución de Pagos** verificá el **Total de la orden a devolver** y elegí el **Método de pago**:

| Opción | Qué pasa |
| --- | --- |
| **Generar un Vale** | Se crea un vale a favor de la persona y se le envía por mail. El importe queda en la tienda. |
| **Efectivo** | Devolvés la plata en el momento. |
| **Transferencia** | Devolvés por transferencia bancaria. |

![Métodos de devolución disponibles](/assets/devoluciones-estados-orden/6dd3163f9560.webp)

Si elegís vale, revisá el campo **Email para el voucher**: es la dirección a la que se envía.

Podés dejar un **Comentario** y después hacés clic en **guardar**. El sistema confirma con un cartel de *Devolución exitosa*.

#### Si la venta se cobró con Mercado Pago sin número de operación

Cuando la venta se cobró con Mercado Pago en el local y no se cargó el número de operación, al hacer clic en **guardar** la devolución todavía no se guarda. Aparece un aviso: *Este pago de MercadoPago se registró sin número de operación*. En **Cómo se devuelve** elegí una opción:

- **Por MercadoPago, con el número de operación**: escribí el **Número de operación de MercadoPago**, que encontrás en el panel de Mercado Pago. Antes de guardar se verifica con Mercado Pago que ese número corresponda al pago de la orden, y el reembolso sale por Mercado Pago.
- **Por otro medio (efectivo, transferencia o vale)**: la plata se devuelve con el **Método de pago** que elegiste arriba, sin pasar por Mercado Pago.
Después volvé a hacer clic en **guardar**.

| Si ves este mensaje | Qué hacer |
| --- | --- |
| *MercadoPago no encuentra ese número de operación en la cuenta de la tienda.* | Revisá el número en el panel de Mercado Pago y volvé a escribirlo. |
| *Ese número de operación no corresponde a este pago…* | El monto, la moneda o el estado no coinciden, o es el pago de otra orden. Revisalo en el panel de Mercado Pago. |
| *Esta devolución sale de más de un pago de MercadoPago sin número de operación…* | Elegí devolver por otro medio. |
| *No se pudo verificar el número de operación con MercadoPago…* | Intentá de nuevo más tarde, o elegí devolver por otro medio. |

### Qué pasa después

#### El producto vuelve a estar disponible

En **productos**, la prenda devuelta pasa de **Vendido** a **Disponible** y ya se puede volver a vender.

![Producto nuevamente disponible](/assets/devoluciones-estados-orden/f4a4bb73d0f9.webp)

#### Si generaste un vale, queda registrado

En **vales** aparece el nuevo vale a nombre del comprador. Su ficha muestra el cliente, el estado, el monto, las fechas y el **Origen Vale**, que indica de qué orden salió.

![Ficha del vale generado](/assets/devoluciones-estados-orden/176bcdd6c3e3.webp)

!!! danger "Importante"
    El título del vale — por ejemplo `MACARENA-ZAS-46564` — es su **identificador**. Es el dato que se usa para aplicarlo en una venta nueva, desde el campo *Agregar Vale* de la orden.

!!! tip "Tip"
    El estado **Devuelto al cliente** es final: no se puede volver a **Disponible** desde el panel. Si te pasó por error, escribinos y lo corregimos.

<p class="doc-aliases" markdown>Términos relacionados: cómo cancelo una venta, hacer un cambio, no me deja devolver, devuelto al cliente, revertir una orden finalizada, devolver un pago de mercado pago, número de operación de mercado pago, se registró sin número de operación, reembolso por mercado pago</p>
