---
title: Pagar comisiones a proveedoras
slug: pagar-comisiones
order: 10
type: Guía
aliases: cómo pago las comisiones, comisiones a abonar, dónde veo lo que tengo que
  pagar, registrar el pago a la proveedora, comisiones pendientes
---

# Pagar comisiones a proveedoras

Cuando una proveedora viene a cobrar, el pago se registra desde su ficha de cliente. El sistema marca las comisiones como abonadas, genera el movimiento de caja y le avisa por mail.

### Estados de una comisión

| Estado | Qué significa |
| --- | --- |
| **Pendiente** | La venta ya ocurrió, pero todavía no llegó la fecha de pago. |
| **Para abonar** | Lista para pagar. Es lo que le tenés que dar hoy. |
| **Vencida** | No se cobró dentro del plazo. |
| **Cancelada** | La venta se devolvió o se canceló. |
| **Abonada** | Ya se pagó. |

!!! tip "Tip"
    El día de habilitación del pago de comisiones es configurable. El cambio aplica al mes siguiente.

### Encontrar sus comisiones

Entrá a **clientes**, buscá a la persona por nombre y abrí su ficha. Ahí tenés todo lo suyo repartido en pestañas: **Productos** (la mercadería que dejó), **Ordenes** (lo que compró) y **Comisiones** (lo que se le vendió y le generó comisión).

Entrá a **Comisiones**. Por defecto viene filtrado por estado **Para Abonar**, que es justo lo que necesitás.

![Comisiones pendientes de pago](/assets/pagar-comisiones/f3e11dae9fa1.webp)

Arriba de la lista tenés el resumen — **Total pendiente**, **Total pagada** y **Total a pagar** — y cada línea muestra el producto, la tienda y el importe. El número de orden es un link: si querés ver de qué venta salió esa comisión, hacé clic y vas directo a la orden.

### Registrar el pago

Hacé clic en **pagar**. Se abre la ventana **Pagar Comisiones Pendientes** con el detalle de cada comisión y el **TOTAL** a abonar.

Elegí la forma de **Pago**:

| Opción | Cuándo se usa |
| --- | --- |
| **Efectivo** | Le pagás en el momento. |
| **Débito** / **Crédito** / **Transferencia** / **MercadoPago** | Según el medio por el que le mandes la plata. |
| **Vale** | La persona prefiere dejar el importe como crédito para comprar en la tienda. |

![Ventana de pago con las formas disponibles](/assets/pagar-comisiones/8b13e0d8d483.webp)

Hacé clic en **confirmar**.

### Qué pasa después

#### Las comisiones pasan a Abonada

Si volvés a la pestaña Comisiones con el filtro **Para Abonar**, ya no aparece nada. Sacá ese filtro y elegí el estado **Abonada** para verlas: cada línea ahora muestra la fecha en que se pagó, quién la pagó y desde qué tienda.

![Comisiones ya abonadas](/assets/pagar-comisiones/35dc205171ad.webp)

El histórico queda completo, así que podés revisar pagos de meses anteriores cambiando el filtro de fechas.

#### Si pagaste con vale, se crea el vale

En **vales** aparece uno nuevo a nombre de la persona, por el importe pagado y en estado **Activo** — o sea, todavía sin usar. En su ficha, el campo **Origen Vale** dice *Pago comisiones*.

![Vale generado por el pago de comisiones](/assets/pagar-comisiones/6c0344dd9de2.webp)

El título del vale es su identificador, y es lo que se usa para aplicarlo cuando esa persona compre algo.

#### Se registra la salida de caja

En **pagos → movimiento de caja** queda el egreso, **en rojo** porque es plata que sale. La descripción indica de quién era la comisión y de qué mes.

El importe cae en la columna del medio con el que pagaste: si fue un vale va a **VALE**, y si fue efectivo, crédito, débito, transferencia o MercadoPago aparece en **CONTADO**, **C.D.T.** o **MP** según corresponda.

![Movimiento de caja del pago](/assets/pagar-comisiones/8cb01f5718dc.webp)

#### Se le avisa por mail

La persona recibe automáticamente un correo avisándole que se le pagaron comisiones y por qué monto.

![Mail de comisiones pagadas](/assets/pagar-comisiones/2f3d2ea751c6.webp)

Si el pago fue con vale, además recibe un segundo mail con el número del vale generado.

!!! video "Video"
    Ver el video tutorial: [https://youtu.be/F0PAr31s0I0](https://youtu.be/F0PAr31s0I0)

<p class="doc-aliases" markdown>Términos relacionados: cómo pago las comisiones, comisiones a abonar, dónde veo lo que tengo que pagar, registrar el pago a la proveedora, comisiones pendientes</p>
