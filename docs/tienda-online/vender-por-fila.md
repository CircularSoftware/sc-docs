---
title: Vender un producto por fila con un link
slug: vender-por-fila
order: 45
type: Guía
aliases: fila de venta, vender por fila, filas de venta, link para Instagram, varias
  personas quieren la misma prenda, quién llegó primero, turno para comprar, el primero
  que llega compra, verificar comprobante, esperando comprobante, sin comprobante
  a tiempo, se le pasó el turno, la fila está llena, aceptar pago y aprobar, rechazar
  y pasar al siguiente, pasar al siguiente, no puedo vender el producto en el local,
  minutos para hacer el pedido, el pedido se canceló solo, volver a hacer fila
---

# Vender un producto por fila con un link

Cuando una prenda única la quieren varias personas a la vez —por ejemplo, la mostrás en Instagram—, podés venderla por fila: compartís un link, cada interesada hace fila con un toque y compra de a una por vez, en orden de llegada. Vos no tenés que decidir por chat quién llegó primero: la fila lo decide, le da a cada una unos minutos para comprar y pasa a la siguiente si no lo hace.

La compra es una venta web de siempre, pagada por transferencia. Vos ves el comprobante y aceptás o rechazás el pago desde el panel.

!!! danger "Importante"
    La función viene apagada. La prende un usuario con rol **Administrador** en **Configuración › Tienda web › Ajustes de la tienda**, pestaña **Checkout**. Solo está en tiendas que venden, no en las de alquiler.

!!! tip "Tip"
    Abrir filas y atender los pagos lo hacen los usuarios con rol **Administrador**, desde **Inventario › Productos › Filas de venta**.

### 1. Prender la venta por fila

1. Entrá a **Configuración › Tienda web › Ajustes de la tienda** y abrí la pestaña **Checkout**.
1. Revisá que la tienda esté lista para cobrar por transferencia:
    - **Tienda online abierta**, prendido.
    - En **Métodos de pago web**, **Transferencia bancaria**.
    - **Datos para transferencias bancarias**, con tu cuenta: es lo que ve la compradora para transferirte.
    - **Permitir comprar sin iniciar sesión**, prendido.
1. En **Fila de venta**, prendé **Vender productos por fila**.
1. Revisá los cuatro valores que aparecen debajo (tabla de abajo) y tocá **Guardar**.
!!! note "Nota"
    Captura pendiente: pestaña Checkout con «Vender productos por fila» prendido y sus cuatro valores.

| Opción | De fábrica | Qué hace |
| --- | --- | --- |
| **Minutos para tomar el turno** | 5 | Cuando le toca, la persona tiene estos minutos para tocar **Comprar ahora**. Si no, pasa la siguiente. |
| **Minutos para hacer el pedido y mandar el comprobante** | 15 | Desde que toca **Comprar ahora**, el tiempo para confirmar el pedido, transferir y adjuntar el comprobante. Es un solo plazo para las tres cosas. |
| **Máximo de personas esperando** | 100 | Con la fila llena, quien llega ve que está llena y no puede entrar. |
| **Días que dura una fila** | 14 | Pasado ese tiempo la fila vence y el producto vuelve a venderse normalmente. |

Los valores se copian en cada fila cuando la abrís. Si los cambiás, valen para las filas que abras después. Las que ya están abiertas siguen con los suyos: los ves en **Configuración de esta fila**, en el detalle de la fila.

### 2. Abrir la fila de un producto

El producto tiene que estar disponible y publicado en la web. Tampoco puede estar en tránsito entre tiendas, reservado por otra compra ni compartido con un evento.

1. Abrí la ficha del producto.
1. En la tarjeta **Fila de venta**, tocá **Vender por fila**.
1. Tocá **Copiar link** y compartilo donde muestres la prenda.
!!! note "Nota"
    Captura pendiente: ficha del producto con la tarjeta Fila de venta abierta, con Copiar link y Ver la fila.

#### Varios productos a la vez

En **Inventario › Productos**, seleccioná los productos y tocá **Vender por fila** en la barra de selección. Cada uno abre su propia fila.

Los que no se pueden poner en fila quedan como estaban, y el aviso dice por qué, con una frase por motivo. Si alguno falló solo por no estar publicado en la web, queda seleccionado y aparece el botón **Publicar en la web y vender por fila**, que hace las dos cosas en un paso.

### 3. Qué hace la compradora

1. Abre el link. Entra a la fila con un solo toque, sin completar nada, y ve su número y cuántas personas tiene adelante.
1. Cuando le toca, la página dice **¡Es tu turno!** y toca **Comprar ahora** antes de que se termine su tiempo.
1. Va al carrito, que solo lleva ese producto y solo acepta transferencia. El carrito le avisa que todavía no transfiera.
1. Toca **Finalizar compra** y vuelve a la página de la fila, que dice **¡Ya casi es tuyo!** y muestra su número de pedido, el monto, tus datos de transferencia y dónde adjuntar el comprobante, con una cuenta regresiva.
1. Transfiere y adjunta el comprobante ahí mismo.
1. Cuando aceptás el pago, su página dice **¡Es tuyo!**.
Si a la compradora se le pasa el turno, la salteás o su pedido se cancela por falta de comprobante, puede tocar **Volver a hacer fila** mientras la fila siga abierta. Queda al final.

!!! note "Nota"
    Captura pendiente: página de la fila en el celular, en «¡Ya casi es tuyo!», con la cuenta regresiva y el lugar para adjuntar el comprobante.

### 4. Revisar el pago y decidir

Entrá a **Inventario › Productos › Filas de venta** y abrí la fila con **Ver la fila**. El listado y el detalle se actualizan solos.

La tarjeta de la compradora en turno muestra en qué paso está:

| Dice | Significa | Qué hacer |
| --- | --- | --- |
| **En turno** | Le tocó y todavía no tocó **Comprar ahora**. | Esperar. Si no responde, **Pasar al siguiente**. |
| **Comprando** | Está en el carrito. | Esperar. Si hace falta, **Pasar al siguiente**. |
| **Esperando comprobante** | Hizo el pedido y todavía no adjuntó el comprobante. | Esperar. Si no llega a tiempo, el pedido se cancela solo. |
| **Verificar comprobante** | Adjuntó el comprobante. | Verificar en tu banco que llegó la plata y aceptar o rechazar. |

- **Aceptar pago y aprobar** registra el pago por transferencia y aprueba el pedido. El producto queda vendido, la fila queda **Vendida** y a las demás les avisamos que se vendió. El botón se habilita cuando hay un comprobante adjunto. Si te pagó sin mandarlo, marcá **Confirmo que recibí la transferencia sin comprobante**.
- **Rechazar y pasar al siguiente** cancela el pedido. Antes escribí el **Motivo del rechazo**. A ella le llega el mail de cancelación, el producto vuelve a la fila y el turno pasa a la siguiente.
También podés aceptar o rechazar desde la orden, como cualquier venta web.

!!! note "Nota"
    Captura pendiente: detalle de una fila con la tarjeta de la compradora en «Verificar comprobante» y los botones Aceptar pago y aprobar / Rechazar y pasar al siguiente.

### Administrar la fila

En el detalle de la fila:

- **Quitar** saca de la lista de espera a alguien que todavía no tiene el turno.
- **Extender vencimiento** le da más días a la fila.
- **Cerrar fila** termina la fila, avisa a todas y el producto vuelve a venderse normalmente. No se puede cerrar mientras hay un pedido esperando tu revisión: aceptalo o rechazalo antes.
- **Historial** muestra cómo terminó cada turno, por ejemplo **Se le pasó el turno**, **Sin comprobante a tiempo** o **Compró**.
### Tener en cuenta

- **Mientras la fila está abierta, el producto solo se vende por ahí.** No lo podés vender en el local ni lo puede comprar otra persona en la web. Para venderlo de otra forma, cerrá la fila.
- **El plazo del turno incluye la transferencia.** Los **Minutos para hacer el pedido y mandar el comprobante** empiezan a contar cuando la compradora toca **Comprar ahora**. Si son pocos, le queda poco tiempo para transferir después de confirmar.
- **Si el comprobante no llega a tiempo, el pedido se cancela solo.** Pasa solo si no adjuntó comprobante y no registraste ningún pago. Le llega el mail de cancelación y el turno pasa a la siguiente. Si dice que transfirió, revisá tu cuenta antes de devolverle la plata.
- **Con el comprobante adjunto, la fila espera tu decisión.** No avanza ni se cancela sola hasta que aceptes o rechaces.
- **Quien entra sin cuenta guarda su lugar en ese navegador.** Si abre el link desde la app de Instagram, la página le propone **Abrir en tu navegador**, y su lugar va con ella.
- **Si apagás la venta por fila, las filas abiertas siguen** hasta que se vendan, las cierres o venzan. No se pueden abrir filas nuevas.
### Qué pasa después

El pedido aceptado es una venta web como cualquier otra: la encontrás en **Ventas** y sigue su camino de preparación y entrega.

<p class="doc-aliases" markdown>Términos relacionados: fila de venta, vender por fila, filas de venta, link para Instagram, varias personas quieren la misma prenda, quién llegó primero, turno para comprar, el primero que llega compra, verificar comprobante, esperando comprobante, sin comprobante a tiempo, se le pasó el turno, la fila está llena, aceptar pago y aprobar, rechazar y pasar al siguiente, pasar al siguiente, no puedo vender el producto en el local, minutos para hacer el pedido, el pedido se canceló solo, volver a hacer fila</p>
