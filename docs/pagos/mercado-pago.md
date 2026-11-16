---
title: Conectar Mercado Pago a la tienda
slug: mercado-pago
order: 30
type: Guía
aliases: token de mercado pago, APP_USR, no encuentro el token, integrar mercado pago
  al checkout, cobrar online, credenciales de MP, crear aplicación en mercado pago,
  credenciales de producción, checkout pro, tus integraciones, access token de producción,
  qué datos pongo en la aplicación, token de aplicación, dónde pego el token, activar
  mercado pago, cobrar con mercado pago, configuración mercado pago, gestión de integraciones,
  credenciales de prueba, ambiente de producción
---

# Conectar Mercado Pago a la tienda

Para cobrar en tu tienda online necesitas conectar Mercado Pago: creas una aplicación en Mercado Pago, copias su Access Token y lo pegas en tu backoffice. Después configuras la clave secreta del webhook y haces una compra de prueba.

### Crear la aplicación en Mercado Pago

1. Entra a **mercadopago.com.uy/developers** con la cuenta que va a recibir los pagos y haz clic en **Ingresar**. Si tu tienda no es de Uruguay, cambia el dominio por el de tu país.
    ![La página de Mercado Pago Developers, con el botón Ingresar arriba a la derecha](/assets/mercado-pago/633fbe270494.webp)

1. Arriba a la derecha haz clic en **Integraciones** y, en **Gestión de integraciones**, elige **Crear aplicación**.
    ![Gestión de integraciones: el botón Integraciones arriba y Crear aplicación a la derecha](/assets/mercado-pago/90ffdd1d80be.webp)

1. Completa **Configuraciones básicas** así y haz clic en **Crear aplicación**:
    - **Nombre de la aplicación**: el que quieras, por ejemplo SoftwareCircular.
    - **¿Qué tipo de solución de pago vas a integrar?**: Pagos online.
    - **¿Estás usando una plataforma de e-commerce?**: Sí.
    - **Selecciona la plataforma que utilizarás para integrar**: Otras plataformas.
    - **¿Qué producto estás integrando?**: Checkout Pro.
    ![El formulario Crear aplicación con los valores que hay que elegir](/assets/mercado-pago/e9ba525d4e7e.webp)

1. Dentro de la aplicación, elige **Producción** arriba de todo (la aplicación abre en **Prueba**), entra a **Credenciales** en el menú de la izquierda y copia el **Access Token** con el ícono de copiar.
    ![Credenciales de producción, con Producción elegido arriba y el Access Token](/assets/mercado-pago/57841ac0145c.webp)

!!! warning "Atención"
    Esa pantalla muestra varios códigos: Public Key, **Access Token**, Client ID y Client Secret. El que necesitas es el Access Token, que empieza con `APP_USR-`. Fíjate que el título diga **Credenciales de producción**: las de prueba no sirven para cobrar. Trátalo como una contraseña: con él se cobran pagos reales.

### Pegar el token en tu backoffice

1. Entra a **Configuración › Mercado Pago**, en el grupo **Ventas y dinero**.
1. Enciende **Cobrar con Mercado Pago**. Mientras está apagado, la tienda online no ofrece Mercado Pago.
1. Pega el Access Token en **Token de aplicación** y haz clic en **Guardar**, arriba a la derecha.
### Qué sigue

1. Configura la clave secreta del webhook, para que la tienda compruebe que cada aviso de pago viene de Mercado Pago: [La clave secreta del webhook de Mercado Pago](https://ayuda.softwarecircular.com/pagos/webhook-mercado-pago/).
1. Haz una compra de prueba de bajo monto para confirmar que todo quedó funcionando. Los pasos están en [Probar que funciona](https://ayuda.softwarecircular.com/pagos/webhook-mercado-pago/#probar-que-funciona).
!!! tip "Tip"
    Conviene asociar una única cuenta de Mercado Pago a la web para poder conciliar por local.

<p class="doc-aliases" markdown>Términos relacionados: token de mercado pago, APP_USR, no encuentro el token, integrar mercado pago al checkout, cobrar online, credenciales de MP, crear aplicación en mercado pago, credenciales de producción, checkout pro, tus integraciones, access token de producción, qué datos pongo en la aplicación, token de aplicación, dónde pego el token, activar mercado pago, cobrar con mercado pago, configuración mercado pago, gestión de integraciones, credenciales de prueba, ambiente de producción</p>
