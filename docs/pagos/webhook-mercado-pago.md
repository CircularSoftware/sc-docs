---
title: La clave secreta del webhook de Mercado Pago
slug: webhook-mercado-pago
order: 35
type: Guía
aliases: clave secreta de mercado pago, secreto del webhook, webhook de mercado pago,
  secret del webhook, notificaciones de mercado pago, firma secreta, el pago está
  acreditado pero la orden sigue pendiente, los pagos no se reflejan en la orden,
  validar notificaciones de mercado pago, clave secreta webhooks, secret key de mp,
  dónde pego la clave secreta, client secret, tus integraciones, no encuentro webhooks
  en mercado pago, simular webhook, error 401 mercado pago, error 500 mercado pago,
  token de aplicación, configuración de webhooks, pagos legacy, pagos (legacy), order
  mercado pago, ambiente de prueba, ambiente de producción, simular notificación,
  simulación de webhook enviada con éxito, me cobró pero no aparece la orden, el pago
  entró pero no se creó la orden, la orden no aparece en ventas, número de la aplicación,
  compra de prueba
---

# La clave secreta del webhook de Mercado Pago

Cuando alguien paga en tu tienda online, Mercado Pago le avisa automáticamente a tu tienda para que la orden quede como pagada. Ese aviso se llama webhook, y viene firmado con una clave secreta que permite comprobar que el aviso es realmente de Mercado Pago y no de un tercero. Si la clave está mal configurada, el cobro entra igual a tu cuenta de Mercado Pago, pero la orden no aparece en **Ventas**.

### Qué es (y qué no es)

- La clave secreta es un código largo de letras y números que Mercado Pago genera para tu aplicación. En Mercado Pago se llama **Firma secreta**; en tu backoffice, **Secreto del webhook**.
- Sirve solo para validar los avisos de pago: no permite cobrar ni mover dinero.
- No es el **Access Token** (el que empieza con `APP_USR-`, que en tu backoffice va en el campo **Token de aplicación**): son dos códigos distintos y necesitas los dos.
- Tampoco es el **Client Secret** que aparece en **Credenciales**.
### Dónde encontrarla en Mercado Pago

La firma está en el portal de desarrolladores de Mercado Pago, dentro de la aplicación que conectaste a la tienda.

1. Entra al portal de desarrolladores con la misma cuenta que recibe los pagos de la tienda (arriba a la derecha ves su nombre). Usa el enlace de tu país:
    - **Uruguay:** [https://www.mercadopago.com.uy/developers/panel/app](https://www.mercadopago.com.uy/developers/panel/app)
    - **Argentina:** [https://www.mercadopago.com.ar/developers/panel/app](https://www.mercadopago.com.ar/developers/panel/app)
1. En **Gestión de integraciones**, abre la aplicación que conectaste a la tienda (si no ves esa pantalla, haz clic en **Integraciones**, arriba a la derecha). Si tienes más de una, abre la que tenga el mismo **Número de la aplicación** que el primer grupo de números después de `APP_USR-` en tu **Token de aplicación**. Mercado Pago puede pedirte un código que te manda por SMS.
1. Arriba de todo, elige **Producción**: la aplicación abre en **Prueba**, y todo lo que copies tiene que salir de Producción. Si ves una franja amarilla que dice *Estás en el ambiente de prueba*, todavía no cambiaste.
    ![Producción elegido arriba y, en el menú de la izquierda, Configuración de webhooks](/assets/webhook-mercado-pago/70a09f751bb9.webp)

1. En el menú de la izquierda, entra a **Configuración de webhooks**.
1. Revisa la **URL de producción**. Si está vacía, pega esta, cambiando tutienda.com por la dirección de tu tienda online (por ejemplo, `tutienda.softwarecircular.com.uy` si no tienes dominio propio): `https://tutienda.com/api/webhooks/mercadopago?source_news=webhooks`. Si ya hay una, confirma que sea la de tu tienda con ese mismo formato.
1. En **Eventos recomendados para integraciones con Checkout Pro**, marca solo **Pagos (legacy)**. No hace falta marcar nada más, tampoco **Order (Mercado Pago)** en **Otros eventos**. Haz clic en **Guardar**.
1. En **Firma secreta**, haz clic en el ícono del ojo para verla y cópiala completa.
    ![Configuración de webhooks: la URL de tu tienda, solo Pagos (legacy) marcado y, abajo, la Firma secreta](/assets/webhook-mercado-pago/67468dc00f1b.webp)

!!! danger "Importante"
    El **Token de aplicación** y la **Firma secreta** tienen que salir de la misma aplicación, con **Producción** elegido. Si son de aplicaciones distintas, los pagos se acreditan en Mercado Pago pero las órdenes no aparecen en tu backoffice.

### Dónde pegarla en tu backoffice

1. Entra a **Configuración › Mercado Pago**, en el grupo **Ventas y dinero**.
1. Con **Cobrar con Mercado Pago** encendido, borra todo lo que haya en **Secreto del webhook** y pega la firma. El campo muestra puntos aunque tenga una clave vieja guardada: bórralo igual antes de pegar.
1. Haz clic en **Guardar**, arriba a la derecha.
### Probar que funciona

El botón **Simular notificación** de Mercado Pago no sirve para esto: el cartel *Simulación de webhook enviada con éxito* solo confirma que Mercado Pago mandó el aviso, no qué respondió tu tienda. La prueba que sí sirve es una compra real de bajo monto:

1. Crea un producto de prueba con precio 1 y que se venda en la web.
1. Entra a tu tienda online, cómpralo con retiro en el local y paga con Mercado Pago. Es un cobro real.
1. En el backoffice, entra a **Vender › Ventas**. Tiene que aparecer la orden nueva, con estado **Revisar web**.
1. Rechaza esa orden para que el producto vuelva a quedar disponible.
### Si el pago se acredita pero no aparece la orden

Pasa cuando la firma o el token quedaron mal: el cobro figura en la actividad de tu cuenta de Mercado Pago, pero en **Ventas** no hay ninguna orden.

1. Pausa el producto que se vendió, para que nadie más lo compre mientras lo resuelves.
1. Revisa que el **Token de aplicación** y la **Firma secreta** sean de la misma aplicación: el primer grupo de números después de `APP_USR-` tiene que ser igual al **Número de la aplicación** (en **Credenciales** figura como **Client ID**).
1. Copia de nuevo la firma desde **Configuración de webhooks**, con **Producción** elegido, pégala en el backoffice y guarda.
1. Haz una compra de prueba para confirmar que ya funciona.
1. Escríbenos con los pagos que entraron sin orden: reenviamos el aviso desde nuestro lado y la orden se crea.
!!! tip "Tip"
    Trata la clave como una contraseña: no la publiques ni la compartas con nadie. Si en algún momento generas una nueva desde Mercado Pago, pega la nueva en el backoffice.

<p class="doc-aliases" markdown>Términos relacionados: clave secreta de mercado pago, secreto del webhook, webhook de mercado pago, secret del webhook, notificaciones de mercado pago, firma secreta, el pago está acreditado pero la orden sigue pendiente, los pagos no se reflejan en la orden, validar notificaciones de mercado pago, clave secreta webhooks, secret key de mp, dónde pego la clave secreta, client secret, tus integraciones, no encuentro webhooks en mercado pago, simular webhook, error 401 mercado pago, error 500 mercado pago, token de aplicación, configuración de webhooks, pagos legacy, pagos (legacy), order mercado pago, ambiente de prueba, ambiente de producción, simular notificación, simulación de webhook enviada con éxito, me cobró pero no aparece la orden, el pago entró pero no se creó la orden, la orden no aparece en ventas, número de la aplicación, compra de prueba</p>
