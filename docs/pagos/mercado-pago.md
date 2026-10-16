---
title: Conectar Mercado Pago a la tienda
slug: mercado-pago
order: 30
type: Guía
aliases: token de mercado pago, APP_USR, no encuentro el token, integrar mercado pago
  al checkout, cobrar online, credenciales de MP, crear aplicación en mercado pago,
  credenciales de producción, checkout pro, tus integraciones, access token de producción,
  qué datos pongo en la aplicación
---

# Conectar Mercado Pago a la tienda

Para cobrar en tu tienda online necesitás conectar Mercado Pago. La aplicación y el token los creás vos en Mercado Pago; cargarlos en el sistema lo hacemos nosotros.

### Crear la aplicación en Mercado Pago

1. Entrá a **mercadopago.com.uy/developers** con la cuenta que va a recibir los pagos y hacé clic en **Ingresar**. Si tu tienda no es de Uruguay, cambiá el dominio por el de tu país.
    ![La página de Mercado Pago Developers, con el botón Ingresar arriba a la derecha](/assets/mercado-pago/633fbe270494.webp)

1. Arriba a la derecha abrí **Tus integraciones** y elegí **Crear aplicación**.
    ![El menú Tus integraciones abierto, con la opción Crear aplicación](/assets/mercado-pago/f62d6fc51708.webp)

1. Completá **Configuraciones básicas** así y hacé clic en **Crear aplicación**:
    - **Nombre de la aplicación**: el que quieras, por ejemplo SoftwareCircular.
    - **¿Qué tipo de solución de pago vas a integrar?**: Pagos online.
    - **¿Estás usando una plataforma de e-commerce?**: Sí.
    - **Selecciona la plataforma que utilizarás para integrar**: Otras plataformas.
    - **¿Qué producto estás integrando?**: Checkout Pro.
    ![El formulario Crear aplicación con los valores que hay que elegir](/assets/mercado-pago/e9ba525d4e7e.webp)

1. Dentro de la aplicación, en el menú de la izquierda, entrá a **Credenciales de producción** y copiá el **Access Token**.
    ![La pantalla Credenciales de producción, con el Access Token resaltado](/assets/mercado-pago/8eb104b49585.webp)

!!! warning "Atención"
    Esa pantalla muestra cuatro datos: Public Key, **Access Token**, Client ID y Client Secret. El que necesitamos es el Access Token, que empieza con `APP_USR-`. Tratalo como una contraseña: con él se cobran pagos reales.

### Qué sigue

1. Pasanos el Access Token y lo dejamos conectado. No hay campo en tu panel para cargarlo: la conexión la hacemos nosotros, una vez.
1. Después configurá la clave secreta del webhook, para que la tienda compruebe que cada aviso de pago viene de Mercado Pago: [La clave secreta del webhook de Mercado Pago](https://ayuda.softwarecircular.com/pagos/webhook-mercado-pago/).
!!! tip "Tip"
    Conviene asociar una única cuenta de Mercado Pago a la web para poder conciliar por local. Hacemos una compra de prueba para confirmar que quedó funcionando.

<p class="doc-aliases" markdown>Términos relacionados: token de mercado pago, APP_USR, no encuentro el token, integrar mercado pago al checkout, cobrar online, credenciales de MP, crear aplicación en mercado pago, credenciales de producción, checkout pro, tus integraciones, access token de producción, qué datos pongo en la aplicación</p>
