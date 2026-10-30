---
title: Editar los emails que reciben tus clientes
slug: editar-emails-clientes
order: 50
type: Guía
aliases: emails, personalizar los emails, cambiar el texto de los emails, plantillas
  de email, configuración emails, emails a clientes, aviso de comisiones, email de
  prueba, cambiar el asunto del email, poner mi texto en los correos, apagar un email,
  no quiero que se envíe ese email, mis clientes no reciben el email, el email de
  la web es distinto, volver al texto original, probar un email antes de mandarlo,
  siempre se envía, no puedo apagar el email, email de la fila, aviso de orden nueva
  a la tienda, email de invitación al panel
---

# Editar los emails que reciben tus clientes

Todos los avisos que tu tienda le manda por correo a un cliente —la confirmación de una compra, el aviso de un vale nuevo, el recordatorio de una comisión— salen con un texto que escribimos nosotros. Desde **Configuración → Emails** puedes reemplazarlo por el tuyo: el asunto, el título, el mensaje y hasta el orden de las partes que arman el correo.

Cada email se edita y se guarda por separado, y puedes probarlo antes de que lo reciba nadie.

!!! danger "Importante"
    La sección **Emails** solo aparece en el menú de un usuario con rol **Administrador**. Mira [Usuarios y roles](../cuenta/usuarios-roles.md).

### Qué vas a ver

Ingresa a **Configuración → Emails**. La pantalla tiene tres columnas: a la izquierda la lista de los emails de tu tienda, al lado la columna **Datos y bloques**, y a la derecha el editor del email que elegiste.

La lista tiene todos los emails que salen a nombre de tu tienda: los que reciben tus clientes y quienes te venden, los avisos que llegan al email de la tienda y los que reciben los usuarios de tu panel. Viene agrupada en **Pedidos** (o **Reservas**, o **Pedidos y reservas**, según lo que haga tu tienda), **Cuenta**, **Vales y proveedores**, **Fila de venta** (solo en tiendas que venden), **Avisos a la tienda** y **Equipo**.

Cada email muestra en qué situación está:

| Estado | Qué significa |
| --- | --- |
| **Original** | Todavía tiene nuestro texto. |
| **Editado** | Ya lo reemplazaste por el tuyo. |
| **Apagado** | No se envía. |
| **Con errores** | Tiene algo que corregir antes de poder guardarlo. |
| **Sin guardar** | Lo estuviste editando y dejaste cambios a medio camino. |

### Los emails de tu tienda

![La lista agrupada en Pedidos, Cuenta y Vales y proveedores, con el estado de cada email a la derecha de su nombre](/assets/editar-emails-clientes/55fc8f70f93c.webp)

Los nombres cambian según tu operación: donde una tienda de venta lee **Compra creada**, una de alquiler lee **Reserva creada**, y una que hace las dos cosas lee **Reserva o compra creada**.

**Cuenta**

| Email | Cuándo se envía |
| --- | --- |
| **Bienvenida** | Al crear una cuenta de cliente. |
| **Confirmación de cuenta** | Cuando alguien se registra en la web y hay que confirmar su correo. |
| **Recuperar contraseña** | Cuando alguien pide recuperar su contraseña desde la web. |
| **Contraseña cambiada** | Cuando el cliente elige una contraseña nueva. |

**Pedidos y reservas**

| Email | Cuándo se envía |
| --- | --- |
| **Compra creada** | Cuando la compra se carga en el local, desde el panel. |
| **Compra web creada** | Cuando el cliente termina la compra en tu tienda online. |
| **Compra cancelada** | Cuando se cancela desde el panel o se rechaza una compra web. |
| **Compra finalizada** | Cuando pasa al estado Finalizada, si tiene facturación electrónica. Las que nacen ya finalizadas no lo mandan. |
| **Compra actualizada** | Cuando se modifican sus productos o su entrega. |
| **Encuesta** | Al finalizar, si tu tienda tiene una encuesta cargada. |
| **Enlace a los pedidos** | Cuando alguien que compró sin cuenta pide ver sus pedidos en la web con su email, y cuando queda registrado el pedido de una compra hecha sin cuenta. Se envía siempre. |

!!! warning "Atención"
    **Las compras del local y las de la web son dos emails distintos.** Si editas **Compra creada** pensando en tus ventas online, tus clientes de la web van a seguir recibiendo el texto original: ese es **Compra web creada**.

**Vales y proveedores**

| Email | Cuándo se envía |
| --- | --- |
| **Producto en revisión** | Cuando el producto de quien vende queda pendiente de aprobación. |
| **Producto devuelto o donado** | Cuando su producto pasa a Pendiente de devolución a cliente o a Donado. |
| **Confirmar uso de vale** | Cuando alguien que compra en la web sin cuenta ingresa un vale activo y su titular tiene un email cargado. Se envía siempre. |
| **Vale nuevo** | Cuando se emite un vale: a mano, por una devolución, por una compra sobrepagada o al pagar comisiones. Mira [Crear y usar vales](../ventas/vales.md). |
| **Comisiones pagadas** | Cuando le registras a quien vende el pago de sus comisiones. |
| **Comisión a cobrar** | Cuando la comisión se habilita para cobrar, el mes siguiente a la venta. Mira [Pagar comisiones a proveedoras](../pagos/pagar-comisiones.md). |
| **Prerremito** | Cuando registras un prerremito con las prendas que entrega quien vende. |
| **Publicación: precio propuesto** | Cuando le proponés otro precio a una publicación desde **Publicaciones de clientes**. |
| **Publicación aprobada** | Cuando aprobás una publicación. No sale si quedó aprobada porque quien vende aceptó tu propuesta de precio. |
| **Publicación rechazada** | Cuando rechazás una publicación, con el motivo. |

Los tres de publicaciones salen solo si quien vende tiene un email cargado. Mirá [Revisar, aprobar o rechazar publicaciones de clientas](../catalogo/revisar-publicaciones-clientes.md).

**Fila de venta**

Solo aparecen en tiendas que venden. Le llegan a quien se anotó en la fila con su email. Mirá [Vender un producto por fila con un link](../tienda-online/vender-por-fila.md).

| Email | Cuándo se envía |
| --- | --- |
| **Lugar en la fila** | Cuando alguien se anota en la fila de un producto, con el enlace para volver a su lugar desde cualquier dispositivo. |
| **Turno en la fila** | Cuando le toca comprar, con la hora límite. |
| **Fila: producto vendido** | Cuando se acepta el pedido de quien tenía el turno: le llega a cada persona que seguía esperando. |
| **Fila cerrada** | Cuando la fila se cierra sin vender a nadie de la fila: la cerrás vos, vence su plazo, o el producto se vende por otro lado o cambia de estado. |

**Avisos a la tienda**

Llegan al email de tu tienda, no a un cliente, y salen solo si la tienda tiene un email cargado.

| Email | Cuándo se envía |
| --- | --- |
| **Orden nueva (aviso a la tienda)** | Cuando se crea una orden desde el panel o se termina una compra en la web, con el comprobante en PDF adjunto. |
| **Comprobante de transferencia recibido** | Cuando quien compró en la web con transferencia bancaria sube el comprobante a su orden. |
| **Publicación: respuesta a tu propuesta** | Cuando quien vende responde tu propuesta de precio con otro precio, un comentario o los dos. |
| **Publicación: precio aceptado** | Cuando quien vende acepta tu propuesta de precio y la publicación queda aprobada. |
| **Producto transferido a la tienda** | Cuando un producto de quien vende pasa a ser de la tienda al alcanzar la meta de comisiones. |
| **Error de CAE en la facturación** | Cuando Biller rechaza un comprobante porque no hay un CAE habilitado para ese tipo. Ese comprobante no se reintenta solo: hay que habilitar el CAE en Biller y reintentarlo desde la orden. |

**Equipo**

| Email | Cuándo se envía |
| --- | --- |
| **Invitación al back office** | Con el enlace para elegir la contraseña: cuando se crea la tienda con su primer administrador, y cuando Software Circular reenvía la invitación o restablece la contraseña. Se envía siempre. |
| **Usuario nuevo del back office** | Cuando un administrador crea un usuario desde **Usuarios**: le dice dónde entrar y con qué usuario, sin la contraseña. Mirá [Untitled](usuarios-roles.md). |

### Cómo se edita un email

Elige el email en la lista y trabaja en el centro de la pantalla. Los campos son cuatro:

| Campo | Qué es |
| --- | --- |
| **Asunto** | Lo que el cliente ve en su bandeja de entrada. Si lo dejas vacío, se usa el asunto original. |
| **Título** | El encabezado grande arriba del mensaje. Si lo dejas vacío, no se muestra. |
| **Vista previa en la bandeja** | La línea que muchos programas de correo muestran al lado del asunto. Si la dejas vacía, no se muestra. |
| **Mensaje** | El cuerpo del correo. |

![El editor de un email: arriba el interruptor Se envía y los botones Descartar y Guardar; abajo los campos Asunto, Título, Vista previa en la bandeja y Mensaje](/assets/editar-emails-clientes/6dae9084d413.webp)

En el **Mensaje** escribes texto normal: **Enter** empieza un párrafo nuevo y **Shift+Enter** hace un salto de línea dentro del mismo párrafo. Puedes poner **negrita** y usar **Enlace** para convertir el texto seleccionado en un vínculo.

Cuando termines, haz clic en **Guardar**. Cada email se guarda por su cuenta.

!!! tip "Tip"
    Si cambias a otro email con cambios sin guardar, el sistema te ofrece **Guardar y cambiar** o **Cambiar sin guardar**. Aunque elijas no guardar, el borrador queda esperándote para cuando vuelvas.

### Los datos se insertan solos

No escribas a mano el número de pedido ni el nombre del cliente: esos valores cambian en cada correo. En la columna **Datos y bloques** están todos los datos que ese email puede mostrar, agrupados por tema —Cliente, Pedido, Entrega, Producto, Vale, Comisión, Tienda— y con un buscador arriba. Cada dato viene con un ejemplo al lado, para que sepas qué va a ver el cliente.

![La columna Datos y bloques abierta, con el buscador arriba y los datos agrupados por Cliente y Tienda](/assets/editar-emails-clientes/7101513de6fb.webp)

Haz clic en el dato que necesites y se inserta donde tengas el cursor. Una vez puesto:

- Se comporta como una sola palabra: se mueve y se borra entero.
- Cuando el email sale, el cliente ve el valor real: su nombre, el número, el total.
- Si un dato no tiene sentido en ese email, no aparece en su lista.
### Las partes del mensaje

Además de párrafos, el mensaje puede llevar **bloques**: partes que arma el sistema y que no se editan, pero que sí puedes reordenar, quitar y volver a poner. Se agregan con **+ Agregar párrafo o bloque**.

En los emails de pedido los bloques son **Productos y resumen de pago**, **Entrega**, **Comentarios del pedido** y **Botón «Ver mi pedido»**. Los que estén disponibles para ese email aparecen al final de la columna **Datos y bloques**, bajo el título **Bloques · solo en el mensaje**.

Cada fila tiene sus acciones: **Subir**, **Bajar** y **Quitar**. También puedes arrastrarla para moverla.

![Las acciones de una fila del mensaje: Subir, Bajar y Quitar](/assets/editar-emails-clientes/6b9967028917.webp)

!!! danger "Importante"
    Algunos bloques aparecen marcados como **Obligatorio**: son los que llevan el enlace del que depende el email, como el de confirmar la cuenta o el de recuperar la contraseña. Se pueden mover, pero no quitar — sin ese enlace el correo no sirve para nada.

### El texto de entrega

En los emails de pedido puedes escribir un texto distinto según cómo recibe el cliente su compra. Las pestañas son **Retiro en tienda**, cada forma de envío que tengas creada, y **Otras formas de envío** para las que no tengan un texto propio. Si alquilas, además tienes **Devolución en la tienda** y **Retiro para devolución**.

Las formas de envío salen de las que cargaste en **Configuración › Ajustes de la tienda › Checkout**. Mira [Configurar envíos y medios de pago en la web](../tienda-online/envios-y-pagos-web.md).

![El email Compra creada con sus bloques en el mensaje y, abajo, las pestañas de Entrega con la opción Se retira en](/assets/editar-emails-clientes/7e06e9ec9e59.webp)

En **Se retira en** eliges qué dirección ve el cliente:

| Opción | Qué muestra |
| --- | --- |
| **La tienda elegida en el pedido** | La dirección de tu local. |
| **La dirección de quien vende cada prenda** | La dirección de cada proveedora. La lista de productos del email se agrupa por dirección de retiro. |

!!! warning "Atención"
    La segunda opción le manda a cada comprador la dirección particular de tus proveedoras. Por eso la primera vez tienes que marcar una confirmación expresa antes de poder guardar. Asegúrate de que tus proveedoras estén de acuerdo.

### Prender y apagar un email

El interruptor **Se envía** decide si ese correo sale o no. Al lado, el signo de pregunta abre **¿Cuándo se envía este email?**, que te dice la condición exacta —por ejemplo, que la tienda tenga activado el aviso de comisiones, o que haya una encuesta cargada—.

!!! warning "Atención"
    Piensa dos veces antes de apagar **Recuperar contraseña**: si lo haces, tus clientes se quedan sin forma de recuperar su cuenta.

**Enlace a los pedidos**, **Confirmar uso de vale** e **Invitación al back office** no se pueden apagar: sin ellos quien los espera no puede seguir. En lugar del interruptor muestran **Siempre se envía**, y sus textos se editan como los de cualquier otro email.

### Probarlo antes de que lo reciba un cliente

Hay dos formas, y ninguna necesita que guardes primero.

**Vista previa.** Muestra el email armado con un pedido, un cliente y unas prendas inventados. Puedes elegir con qué forma de entrega verlo, alternar entre **Computadora** y **Celular**, y usar **Otros datos** para sortear otro pedido de ejemplo. Con el selector **Editar / Ambos / Vista previa** decides cuánto espacio le das a cada cosa en la pantalla.

**Enviarme una prueba.** Te manda el correo de verdad a tu dirección o a una de la tienda. Llega con **[Prueba]** en el asunto y una franja amarilla, para que nadie lo confunda con uno real. Se envía lo que estás viendo, aunque no lo hayas guardado.

!!! tip "Tip"
    Puedes mandar hasta **10 pruebas por hora**.

### Si algo no se puede guardar

Cuando hay algo mal, aparece un aviso arriba con la cuenta de errores y un enlace **Ir a…** que te lleva al campo exacto. Los casos típicos son un dato mal escrito, unas llaves sin cerrar, un enlace que no es seguro o un asunto que, con los datos de un pedido real, se pasa del largo máximo.

Casi todos traen un arreglo de un clic: **Cerrar las llaves**, **Borrarlo**, **Quitar el enlace**, **Volver a ponerlo**.

![El aviso de error arriba del editor, el campo marcado en rojo y el botón que lo arregla de un clic](/assets/editar-emails-clientes/c0065bde5b72.webp)

!!! tip "Tip"
    Nada se guarda hasta que esté todo bien, y tu borrador no se pierde mientras tanto.

### Volver a nuestro texto

**Volver al texto original** descarta lo que escribiste y repone el nuestro. Te pedimos confirmación antes, y después queda disponible **Deshacer** para recuperar exactamente lo que tenías.

!!! warning "Atención"
    El cambio se aplica recién cuando guardas, y **al guardar se pierde el Deshacer**. Si no estás seguro, prueba antes con la vista previa.

### Qué pasa después

Lo que guardas se usa en los correos que salgan de ahí en adelante; los que ya se enviaron no cambian. El resto del email — el encabezado con tu logo o el nombre de tu tienda, el pie y la línea que indica que se envió con Software Circular— lo seguimos armando nosotros, para que todos tus correos se vean iguales y lleguen bien a cualquier casilla.

Si quieres confirmar que quedó como esperabas, la forma más rápida es mandarte una prueba a ti mismo y leerla en el teléfono, que es donde la va a abrir la mayoría de tus clientes.

<p class="doc-aliases" markdown>Términos relacionados: emails, personalizar los emails, cambiar el texto de los emails, plantillas de email, configuración emails, emails a clientes, aviso de comisiones, email de prueba, cambiar el asunto del email, poner mi texto en los correos, apagar un email, no quiero que se envíe ese email, mis clientes no reciben el email, el email de la web es distinto, volver al texto original, probar un email antes de mandarlo, siempre se envía, no puedo apagar el email, email de la fila, aviso de orden nueva a la tienda, email de invitación al panel</p>
