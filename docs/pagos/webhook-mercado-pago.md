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
  en mercado pago
---

# La clave secreta del webhook de Mercado Pago

Cuando alguien paga en tu tienda online, Mercado Pago le avisa automáticamente a tu tienda para que la orden quede como pagada. Ese aviso se llama webhook, y viene firmado con una clave secreta que permite comprobar que el aviso es realmente de Mercado Pago y no de un tercero.

### Qué es (y qué no es)

- La clave secreta (el "secreto del webhook") es un código largo de letras y números que Mercado Pago genera para tu aplicación.
- Sirve solo para validar los avisos de pago: no permite cobrar ni mover dinero.
- No es el Access Token (el que empieza con APP_USR-...): son dos códigos distintos y necesitás los dos.
- Tampoco es el **Client Secret** que aparece en Configuración → Credenciales de tu cuenta de Mercado Pago.
### Dónde encontrarla en Mercado Pago

La clave se genera en el **portal de desarrolladores** de Mercado Pago. En Configuración → Credenciales de tu cuenta no aparece: ahí están el Access Token y el Client Secret, que son otra cosa.

1. Entrá al portal de desarrolladores de Mercado Pago, a **Tus integraciones**, con la misma cuenta que conectaste a la tienda. Usá el enlace de tu país:
    - **Uruguay:** [https://www.mercadopago.com.uy/developers/panel/app](https://www.mercadopago.com.uy/developers/panel/app)
    - **Argentina:** [https://www.mercadopago.com.ar/developers/panel/app](https://www.mercadopago.com.ar/developers/panel/app)
1. Abrí la aplicación de la que copiaste el Access Token (la que creaste al conectar Mercado Pago).
1. En el menú de la izquierda, entrá a **Webhooks** → **Configurar notificaciones** y elegí la pestaña **Modo productivo**.
1. Si todavía no hay ninguna URL guardada, pegá esta, cambiando tutienda.com por el dominio de tu tienda online: `https://tutienda.com/api/webhooks/mercadopago?source_news=webhooks`. Marcá el evento **Pagos** y hacé clic en **Guardar configuración**. Si ya había una URL, dejala como está.
1. Mercado Pago muestra la **clave secreta** en esa misma pantalla. Revelala y copiala.
### Dónde pegarla en tu backoffice

1. Entrá a **Mi sitio web → Configuraciones** y abrí la pestaña **Checkout**.
1. En la sección **Mercado Pago**, pegá la clave en el campo **Secreto del webhook**.
1. Guardá los cambios.
1. Probala enseguida: en Mercado Pago, en **Webhooks**, hacé clic en **Simular**, elegí la URL de tu tienda y el evento Pagos, poné cualquier número como ID y hacé clic en **Enviar prueba**. La respuesta tiene que ser **200**. Si es **401**, la clave quedó mal pegada: copiala de nuevo y volvé a guardarla.
!!! tip "Tip"
    Copiá y pegá la clave completa, sin espacios antes ni después. Apenas la guardás, el sistema empieza a usarla para validar los avisos: si quedó mal pegada, los pagos se acreditan en Mercado Pago pero las órdenes no se actualizan. Si te pasa eso, volvé a copiar la clave desde Mercado Pago y pegala de nuevo.

!!! tip "Tip"
    Tratá la clave como una contraseña: no la publiques ni la compartas con nadie. Si en algún momento la regenerás desde Mercado Pago, acordate de pegar la clave nueva en el backoffice.

<p class="doc-aliases" markdown>Términos relacionados: clave secreta de mercado pago, secreto del webhook, webhook de mercado pago, secret del webhook, notificaciones de mercado pago, firma secreta, el pago está acreditado pero la orden sigue pendiente, los pagos no se reflejan en la orden, validar notificaciones de mercado pago, clave secreta webhooks, secret key de mp, dónde pego la clave secreta, client secret, tus integraciones, no encuentro webhooks en mercado pago</p>
