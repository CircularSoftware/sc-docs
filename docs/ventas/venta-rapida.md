---
title: 'Venta rápida: vender en el mostrador en pocos clics'
slug: venta-rapida
order: 11
type: Guía
aliases: nuevo flujo de venta, venta rápida, modo mostrador, vender más rápido, pagar
  todo, consumidor final, no quiero cargar el cliente, la venta se guardó sola, no
  se abrió el ticket, dónde está el recibo, dónde quedaron los descuentos, más opciones,
  pago parcial, pagar con dos medios, cambiar la tienda de la venta, el interruptor
  se apagó, la venta arranca con el formulario completo
---

# Venta rápida: vender en el mostrador en pocos clics

El **Nuevo flujo de venta** es una forma corta de registrar una venta de mostrador: buscás (o escaneás) la prenda, elegís el medio de pago y tocás **Pagar todo**. Con ese clic se registra el pago y se guarda la venta, y la pantalla queda vacía y lista para la persona que sigue.

El cliente, la entrega y la tienda ya vienen resueltos. Todo lo demás —descuentos, extras, vale, comentarios— sigue estando, guardado detrás de **Más opciones**.

!!! danger "Importante"
    **Viene apagado.** Cada nueva venta tiene arriba el interruptor **Nuevo flujo de venta**, así que cualquier usuario puede probarlo en una venta sin cambiar nada de la tienda. Para que arranque encendido para todos, un **Administrador** lo configura en **Configuración › Ventas y dinero › Venta rápida**. Es solo para ventas: los alquileres siempre usan el formulario completo.

### 1. Encender el flujo

1. Entrá a **nueva venta**.
1. Arriba a la derecha, junto a **Cancelar** y **Guardar**, encendé **Nuevo flujo de venta**.
1. La pantalla se achica a una sola tarjeta y aparece un aviso que resume cómo se usa. Cuando lo leíste, tocá **Entendido** y no vuelve a aparecer en esa computadora.
!!! note "Nota"
    Captura pendiente: nueva venta con el interruptor «Nuevo flujo de venta» encendido y el aviso de arriba.

### 2. Hacer la venta

1. **Agregá las prendas.** El buscador de productos ya tiene el cursor: escribí el código y apretá **Enter**, que agrega la primera prenda disponible que coincide. Repetí con cada prenda. Si tenés el celular vinculado como lector, escaneá la etiqueta y la prenda se agrega sola (mirá [Usar el celular como lector de códigos](https://app.notion.com/p/40244bec059281f0be88c621023b6ce3)).
1. **Elegí el medio de pago.** Viene puesto el que configuró la tienda (Efectivo, si nadie lo cambió).
1. **Tocá Pagar todo.** El botón muestra el importe, por ejemplo **Pagar todo ($680,00)**: es lo que falta pagar con ese medio. Con un clic se registra ese pago y se guarda la venta.
1. Arriba aparece **Venta OR_… guardada**, con los enlaces **Ver orden** y **Ver recibo**. El formulario ya está vacío para la próxima venta.
!!! note "Nota"
    Captura pendiente: la tarjeta con el buscador, el medio de pago y el botón «Pagar todo», y el aviso «Venta OR_… guardada» arriba.

Guardar con este flujo hace lo mismo que con el formulario completo: descuenta el stock, genera la comisión de la proveedora, registra el movimiento de caja y emite el comprobante si la tienda factura electrónicamente. Lo único distinto es que no se abre el ticket ni una ventana de confirmación (ver **Tener en cuenta**).

### Qué viene resuelto

| Qué | Cómo viene | Cómo cambiarlo |
| --- | --- | --- |
| **Cliente** | **Consumidor final**: la venta queda registrada sin datos de la persona. | En **Más opciones**, buscá a la persona en **Cliente** o creala con **Nuevo**. |
| **Entrega** | Retira en la tienda y **se la lleva en el momento**: la venta nace finalizada. | En **Más opciones › Entrega**, y después **Confirmar entrega**. |
| **Tienda** | Si tenés un solo local, ese. Si tenés varios, la del primer producto que agregás. Se ve en el recibo, al lado del cliente. | Apagando el interruptor (ver abajo). |
| **Medio de pago** | El que configuró la tienda. Después de cada pago vuelve a ese. | Elegí otro en la tarjeta antes de tocar **Pagar todo**. |

Cada tienda puede cambiar estos puntos de partida: mirá **Configurar cómo arranca** más abajo.

### Cuando la venta necesita algo más

Nada desapareció: está en **Más opciones**, al pie de la tarjeta. Ahí encontrás el **Cliente**, los **Extras** (la bolsa, por ejemplo), la **Entrega**, los **Descuentos**, el **Vale**, los **Comentarios** y, si tu tienda factura electrónicamente y sos Administrador o Encargado, **Facturación electrónica**.

#### La persona quiere dejar sus datos

Abrí **Más opciones** y, en **Cliente**, buscala por nombre, email o teléfono, o tocá **Nuevo** para darla de alta. La venta queda a su nombre y lo demás sigue igual. Es la forma de que le llegue el mail con su compra: al consumidor final no se le manda nada.

#### Paga con dos medios

1. En la tarjeta de pago, abrí **Pago parcial**.
1. Elegí el primer medio, escribí el importe y tocá **Agregar**.
1. Elegí el segundo medio y tocá **Pagar todo**: registra lo que falta.
1. Tocá **Guardar**.
!!! warning "Atención"
    **Pagar todo** guarda la venta solo cuando es el **único pago**. Si antes cargaste un pago parcial o un vale, registra el resto como un pago más y la venta **no se guarda sola**: tenés que tocar **Guardar**. Si cambiás de pantalla sin guardar, la venta se pierde.

#### Hay que enviarla o la persona no se la lleva ahora

Abrí **Más opciones › Entrega**, cambiá lo que haga falta (envío, otra sucursal, o apagá **Retira en el momento**) y tocá **Confirmar entrega**. Hasta que la confirmes, la venta no se puede guardar.

#### Necesitás el formulario completo

Apagá **Nuevo flujo de venta**. No se pierde nada de lo que cargaste: aparece el formulario completo con todo lo que ya tenía la venta (la tarjeta **Entrega** te va a pedir que la confirmes de nuevo). Es también la forma de elegir otra tienda para la venta.

### Configurar cómo arranca (Administradores)

1. Entrá a **Configuración › Ventas y dinero › Venta rápida**.
1. Ajustá estas cuatro opciones:
| Opción | De fábrica | Qué hace |
| --- | --- | --- |
| **Nuevo flujo de venta encendido por defecto** | Apagado | Si cada nueva venta arranca con el interruptor encendido o apagado. Cada vendedora lo puede cambiar en la venta igual. |
| **Cliente de la venta** | Consumidor final (sin datos) | A nombre de quién queda la venta si nadie elige un cliente. Con **Preguntar cada vez**, la tarjeta Cliente aparece arriba y hay que elegir a alguien (o tocar **Consumidor final**) en cada venta. |
| **Medio de pago inicial** | Efectivo | Con qué medio abre la tarjeta de pago: Efectivo, Transferencia, Débito, Crédito o MercadoPago. |
| **La persona se lleva la compra en el momento** | Encendido | La venta nace finalizada, como con **Retira en el momento**. Apagado, la venta queda pendiente de entregar. |

1. Tocá **Guardar**.
Estas opciones solo cambian cómo arranca el flujo nuevo. Con el interruptor apagado, la nueva venta es la de siempre.

!!! note "Nota"
    Captura pendiente: Configuración › Ventas y dinero › Venta rápida con las cuatro opciones.

### Tener en cuenta

- **Un clic guarda la venta.** Antes de tocar **Pagar todo**, mirá el medio de pago y el importe del botón. Si te equivocaste de medio, el pago se registra igual con el que estaba elegido.
- **El importe depende del medio.** Si tu tienda tiene precios distintos por medio de pago, **Pagar todo** cobra el precio de ese medio. Al cambiar de medio, el botón se apaga un instante mientras recalcula. También está apagado cuando no queda nada por pagar.
- **Enter agrega la primera prenda disponible que coincide** con lo que escribiste. Si escribís solo una parte del nombre o del código, puede agregar otra prenda: escribí el código completo, o elegí la prenda de la lista con el mouse. Si se agregó una que no era, sacala del recibo.
- **No se abre el ticket.** Para imprimirlo o mostrarlo, tocá **Ver recibo** en el aviso de venta guardada. El aviso queda hasta que tocás **Cerrar** o guardás la venta siguiente; después, el recibo está en la orden, desde **ordenes**.
- **El consumidor final es un cliente más.** El sistema lo crea la primera vez que se usa, y aparece en el listado de **Clientes** y en los reportes, juntando todas las ventas sin datos. Si preferís que se llame «Mostrador» o «Sin datos», cambiale el nombre desde su ficha. No recibe mails, y se factura como cualquier venta a un comprador sin documento.
- **Se lleva en el momento = pago completo.** Una venta que se lleva en el momento solo se guarda con el total pagado, igual que siempre.
- **Tu elección del interruptor se recuerda en esa pestaña.** Si lo apagás, la próxima venta en esa misma pestaña del navegador arranca apagada, aunque recargues. Una pestaña nueva, o volver a iniciar sesión, arranca como dice la configuración de la tienda. Mover el interruptor nunca cambia la configuración de la tienda.
- **La tienda no se elige en el flujo.** Con varios locales, la decide la primera prenda que agregás. Para vender desde otra tienda, apagá el interruptor y elegila en el formulario completo.
### Qué pasa después

La venta queda en **ordenes** como cualquier otra, con su recibo, su movimiento de caja y, si la prenda tenía dueña, su comisión. Cómo funciona todo eso, paso por paso, está en [Registrar una nueva venta](https://app.notion.com/p/3bf44bec059281e98515ec8e3933a0d9).

<p class="doc-aliases" markdown>Términos relacionados: nuevo flujo de venta, venta rápida, modo mostrador, vender más rápido, pagar todo, consumidor final, no quiero cargar el cliente, la venta se guardó sola, no se abrió el ticket, dónde está el recibo, dónde quedaron los descuentos, más opciones, pago parcial, pagar con dos medios, cambiar la tienda de la venta, el interruptor se apagó, la venta arranca con el formulario completo</p>
