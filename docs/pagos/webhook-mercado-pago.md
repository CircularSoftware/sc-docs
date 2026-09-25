---
title: La clave secreta del webhook de Mercado Pago
slug: webhook-mercado-pago
order: 35
type: Guía
aliases: clave secreta de mercado pago, secreto del webhook, webhook de mercado pago,
  secret del webhook, notificaciones de mercado pago, firma secreta, el pago está
  acreditado pero la orden sigue pendiente, los pagos no se reflejan en la orden,
  validar notificaciones de mercado pago, clave secreta webhooks, secret key de mp,
  dónde pego la clave secreta
---

# La clave secreta del webhook de Mercado Pago

Cuando alguien paga en tu tienda online, Mercado Pago le avisa automáticamente a tu tienda para que la orden quede como pagada. Ese aviso se llama webhook, y viene firmado con una clave secreta que permite comprobar que el aviso es realmente de Mercado Pago y no de un tercero.

### Qué es (y qué no es)

- La clave secreta (el "secreto del webhook") es un código largo de letras y números que Mercado Pago genera para tu aplicación.
- Sirve solo para validar los avisos de pago: no permite cobrar ni mover dinero.
- No es el Access Token (el que empieza con APP_USR-...): son dos códigos distintos y necesitás los dos.
### Dónde encontrarla en Mercado Pago

1. Entrá a tu cuenta de Mercado Pago → sección de desarrolladores ("Tus integraciones").
1. Abrí la aplicación que creaste al conectar Mercado Pago (la misma del Access Token).
1. En el menú de la aplicación, entrá a "Webhooks" (también aparece como "Notificaciones Webhooks").
1. Elegí el modo productivo. Ahí vas a ver la **Clave secreta**: tocá "Mostrar" y copiala.
### Dónde pegarla en tu backoffice

1. Entrá a **Mi sitio web → Configuraciones** y abrí la pestaña **Checkout**.
1. En la sección **Mercado Pago**, pegá la clave en el campo **Secreto del webhook**.
1. Guardá los cambios.
!!! tip "Tip"
    Copiá y pegá la clave completa, sin espacios antes ni después. Apenas la guardás, el sistema empieza a usarla para validar los avisos: si quedó mal pegada, los pagos se acreditan en Mercado Pago pero las órdenes no se actualizan. Si te pasa eso, volvé a copiar la clave desde Mercado Pago y pegala de nuevo.

!!! tip "Tip"
    Tratá la clave como una contraseña: no la publiques ni la compartas con nadie. Si en algún momento la regenerás desde Mercado Pago, acordate de pegar la clave nueva en el backoffice.

<p class="doc-aliases" markdown>Términos relacionados: clave secreta de mercado pago, secreto del webhook, webhook de mercado pago, secret del webhook, notificaciones de mercado pago, firma secreta, el pago está acreditado pero la orden sigue pendiente, los pagos no se reflejan en la orden, validar notificaciones de mercado pago, clave secreta webhooks, secret key de mp, dónde pego la clave secreta</p>
