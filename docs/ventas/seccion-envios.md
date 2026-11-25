---
title: 'Envíos: armar, despachar y seguir las órdenes con envío'
slug: seccion-envios
order: 57
type: Guía
aliases: envíos, dónde veo los envíos, pedidos para enviar, qué falta armar, marcar
  como despachado, número de seguimiento, código de seguimiento, tracking, el paquete
  ya salió, despachar un pedido, envío por correo, Correo Argentino, MiCorreo, generar
  envío en Correo Argentino, etiqueta de Correo Argentino, no puedo despachar la orden,
  la orden todavía está en revisión, este envío es de una orden de otra tienda, pedidos
  web con envío, envío por moto
---

# Envíos: armar, despachar y seguir las órdenes con envío

En **Vender › Envíos** tenés todas las órdenes que se entregan por envío —las de tu tienda web y las que cargás en el local— ordenadas por etapa. De un vistazo sabés qué falta armar, qué ya salió y qué ya llegó.

!!! tip "Tip"
    La sección la ven los usuarios **Administrador** y **Encargado**, con las órdenes de los locales que tienen asignados. Mirá [Usuarios y roles (Administrador, Encargado, Empleado)](../cuenta/usuarios-roles.md).

### Las etapas de un envío

| Etapa | Cuándo está ahí |
| --- | --- |
| **Por armar** | La orden está en **Revisar web** o **Pendiente de armado**, y el paquete todavía no salió. |
| **Armado** | La orden está **Lista para entregar** y el paquete todavía no salió. |
| **Despachado** | Marcaste que el paquete salió y la orden todavía no se entregó. |
| **Entregado** | La orden está **Finalizada** (o **Pendiente de devolución**, si alquilás). |
| **Cancelado** | La orden se canceló o se rechazó. |

### 1. Encontrar un envío

1. Entrá a **Vender › Envíos**.
1. Elegí la pestaña de la etapa: **Todos**, **Por armar**, **Armados**, **Despachados** o **Entregados**.
1. Para buscar una orden puntual, escribí el número de orden o el nombre del cliente y tocá **Buscar**.
1. Tocá el número de la orden para abrir el detalle del envío.
La lista muestra la orden, la fecha, el cliente, el destino, por qué medio sale (**Envío por**), la etapa y el número de seguimiento. Los envíos cancelados aparecen en **Todos**.

### 2. Armar el paquete

Armar y entregar se marcan como siempre, cambiando el estado de la orden. Desde el detalle del envío, tocá **Ver la orden** (arriba a la derecha) y cambiá el estado a **Armada**. El envío pasa solo a **Armado**. Mirá [Devoluciones y cambiar el estado de una orden](devoluciones-estados-orden.md).

### 3. Marcar el envío como despachado

Cuando el paquete sale:

1. Abrí el envío desde la lista.
1. Si ya tenés el número de seguimiento, escribilo en **Número de seguimiento**. Es opcional: lo podés cargar después.
1. Tocá **Marcar despachado**.
El envío pasa a **Despachado** y queda registrada la fecha. Para cargar o corregir el número más tarde, escribilo en el mismo campo y tocá **Guardar seguimiento**.

### 4. Entregar

Cuando el cliente recibe el paquete, cambiá el estado de la orden a **Entregada**. El envío pasa a **Entregado**.

### Cuando el envío sale por Correo Argentino

Si tu tienda tiene conectada su cuenta de Correo Argentino y el comprador eligió Correo Argentino en la web, el detalle del envío trae la tarjeta **Envío por Correo Argentino**:

1. Tocá **Generar envío en Correo Argentino**.
1. Revisá los datos que vienen cargados: quién recibe, la dirección (o el código de la sucursal, si retira en sucursal), las medidas y el peso del paquete y el valor declarado.
1. Tocá **Enviar a Correo Argentino**.
El envío queda cargado en tu cuenta de MiCorreo, donde imprimís la etiqueta, y pasa a **Despachado**. MiCorreo no devuelve el número de seguimiento: copialo de MiCorreo cuando imprimas la etiqueta y guardalo con **Guardar seguimiento**.

También podés marcarlo despachado a mano, sin cargarlo en MiCorreo, con **Marcar despachado**.

### Desde el detalle de la orden

Una orden con envío muestra su etapa (por ejemplo, **Envío: por armar**) y el enlace **Ver envío**, que te lleva al detalle del envío.

### Mensajes que podés ver

| Dice | Significa | Qué hacer |
| --- | --- | --- |
| **La orden todavía está en revisión: aprobala antes de despacharla.** | Es una compra web que nadie aprobó todavía. | Abrí la orden, aprobala y volvé al envío. |
| **La orden está cancelada: no hay nada para despachar.** | La orden se canceló o se rechazó. | Nada: ese paquete no sale. |
| **Este envío ya fue entregado.** | La orden ya está entregada. | Nada. |
| **Este envío es de una orden de otra tienda: lo despacha la tienda dueña de la orden.** | Tu local ve el envío, pero lo despacha el local donde se hizo la orden. | Avisale a ese local. |
| **Hay más de 500 órdenes con envío sin entregar: esta etapa muestra solo las más antiguas.** | Tenés muchas órdenes con envío sin entregar. | Marcá como entregadas las que ya llegaron, o buscá la orden por número o cliente. |
| **Faltan datos para generar el envío: …** | Al formulario de Correo Argentino le falta lo que dice el mensaje. | Completalo y volvé a tocar **Enviar a Correo Argentino**. |
| **Las medidas del paquete tienen que ser números enteros: …** | El peso tiene que ir entre 1 y 25000 gramos y cada lado entre 1 y 150 cm, sin decimales. | Corregí las medidas que nombra el mensaje y volvé a tocar **Enviar a Correo Argentino**. |

### Tener en cuenta

- **Despachar no cambia el estado de la orden.** El envío queda **Despachado**, pero la orden sigue en el estado que tenía hasta que la marques **Entregada**.
- **Tu tienda no le manda un email al cliente cuando despachás.** Si querés pasarle el número de seguimiento, mandáselo vos.
- **Generá el envío en Correo Argentino una sola vez.** Si MiCorreo ya tiene un envío con el número de esa orden (por ejemplo, porque la primera vez se cortó la conexión), el formulario te avisa *MiCorreo dice que ya tiene un envío con el número de esta orden.* Entrá a MiCorreo, revisá que sea el de esta orden y tocá **Ya está en MiCorreo: registrar el envío**. El envío pasa a **Despachado** sin cargarse de nuevo en MiCorreo.
- **Revisá el código postal antes de generar el envío.** El costo que pagó el comprador se calculó con el código postal que cotizó. Si la dirección o la sucursal son de otra zona, el costo real en Correo Argentino puede ser distinto; el formulario te lo avisa.
- **Envíos aparece en el menú aunque tu tienda no haga envíos.** En ese caso la lista queda vacía.
### Qué pasa después

Con la orden **Entregada**, el envío pasa a **Entregados** y sale de las etapas pendientes. Todo lo demás de la orden —cobros, comisiones, facturación— sigue igual que en cualquier venta.

<p class="doc-aliases" markdown>Términos relacionados: envíos, dónde veo los envíos, pedidos para enviar, qué falta armar, marcar como despachado, número de seguimiento, código de seguimiento, tracking, el paquete ya salió, despachar un pedido, envío por correo, Correo Argentino, MiCorreo, generar envío en Correo Argentino, etiqueta de Correo Argentino, no puedo despachar la orden, la orden todavía está en revisión, este envío es de una orden de otra tienda, pedidos web con envío, envío por moto</p>
