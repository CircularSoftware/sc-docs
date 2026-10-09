---
title: Cargar un producto nuevo
slug: cargar-producto
order: 10
type: Guía
aliases: ingresar una prenda, dar de alta un producto, cargar mercadería, qué datos
  van, el precio es obligatorio, pendiente de aprobación
---

# Cargar un producto nuevo

Los productos se cargan desde la sección **Productos**. El formulario reúne todo en una sola pantalla: los datos de la prenda, dónde y por qué canales se vende, de quién es, el precio, las fotos y la categoría.

!!! note "Nota"
    Para poner una prenda a nombre de un cliente —por ejemplo, mercadería en consignación— esa persona ya tiene que existir en el sistema. Si todavía no está cargada, créala primero desde [Clientes](../clientes/crear-cliente.md).

### Abrir el formulario

Ingresa a **Productos** en el menú lateral y haz clic en **Nuevo Producto**, arriba a la derecha.

![Listado de productos con el botón Nuevo Producto](/assets/cargar-producto/ade4ae1ba05c.webp)

### Datos del producto

| Campo | Qué cargar |
| --- | --- |
| **Nombre** (obligatorio) | Cómo se identifica la prenda. Por ejemplo: Campera de jean azul. |
| **Descripción corta** | Sale en la web, debajo del nombre del producto. |
| **Descripción larga** | Sale en la web, debajo de las fotos. Van ahí los detalles de la prenda: tela, calce, estado. |
| **Código Alternativo** | El código que ya usas para esa prenda. Sirve para no perder tu propia nomenclatura: por ejemplo, código de proveedor seguido del código de prenda (PV/1001). |
| **Condición** | **Excelente**, **Muy bueno**, **Bueno** o **Con detalles**. Viene en **Excelente**. |
| **Cantidad de copias** | Solo aparece en las tiendas que lo tienen habilitado. Crea varias unidades iguales de una vez; la propiedad de la prenda se replica en todas. |
| **Comentarios** y **Tags** | Opcionales, para uso interno. |

### Datos de venta

**Local** (obligatorio) — dónde está físicamente la prenda.

**Canales de venta** — **Web** y **Tiendas** vienen activados. Apaga **Web** si todavía no quieres publicarla online, por ejemplo mientras no tengas una foto buena.

![Datos del producto y datos de venta cargados](/assets/cargar-producto/9e5d40b4b80f.webp)

### Propiedad

**Proveedor original** — quién trajo la prenda. Al elegirlo, el sistema lo deja también como propietario actual.

**Propietario actual** — **Tienda** si la mercadería es tuya, o **Cliente** si es de una persona. Con **Cliente** aparece **Seleccionar cliente**, para indicar de quién es, y **Comisión especial**, que te permite usar en esta prenda un porcentaje distinto al que tiene configurado esa persona.

![Bloque de Propiedad con proveedor y propietario actual](/assets/cargar-producto/aecb2c91a35f.webp)

### Precio

En **Operación de Venta**, con **Este producto puede venderse** activado, completa **Precio de Venta**. Si corresponde, elige un **Descuento de Venta**: **Variable (%)** o **Fijo ($)**.

![Operación de venta con el precio cargado](/assets/cargar-producto/811b9b7208c4.webp)

### Imágenes

Haz clic sobre el primer recuadro —el que dice **PORTADA**— y elige la foto desde tu computadora. Esa es la imagen principal del producto; puedes sumar hasta cuatro más en los recuadros siguientes. Con las fotos ya cargadas, las flechas de cada recuadro te dejan cambiarlas de orden.

![Los cinco recuadros para subir fotos, con PORTADA en el primero](/assets/cargar-producto/7dd8c95cfd55.webp)

!!! tip "Tip"
    Si cargas mercadería desde el celular, es más rápido sacar las fotos con el atajo de **Fotos de productos**. Mira [Sacar fotos desde el celular](../catalogo/fotos-desde-el-celular.md).

### Categoría y atributos

En **Categoría y Atributos** (obligatorio) haz clic en **Elegir categoría**. Se abre el árbol de categorías de tu tienda: selecciona la que corresponda y haz clic en **Confirmar**.

![Selector de categorías con una categoría marcada](/assets/cargar-producto/ea53a7e6fad4.webp)

Debajo quedan los atributos que tenga configurados tu tienda —por ejemplo color, estado, marca o talle—. Cada uno se completa eligiendo un valor de la lista.

![Lista desplegable de valores de un atributo](/assets/cargar-producto/671fc89cfef3.webp)

![Categoría elegida y atributos cargados](/assets/cargar-producto/6fbcfcb9a990.webp)

Si el valor que buscas no está en la lista, el formulario te ofrece **Agregar nuevo**, que abre la pantalla de atributos en otra pestaña; al volver, la lista ya aparece actualizada. No se pueden escribir valores libres: es a propósito, para que el catálogo no termine con la misma marca escrita de cinco formas distintas.

El bloque **Información para SEO**, al lado, es opcional: sirve para que el producto aparezca en la web con un nombre o una descripción distintos a los internos.

### Guardar

Haz clic en **Guardar**, abajo a la derecha. El sistema confirma la creación y te muestra el código interno que le asignó a la prenda —por ejemplo `PR_02_00_1048`—.

![Aviso de producto creado con su código interno](/assets/cargar-producto/e0762c3b16f1.webp)

Haz clic en **Confirmar** y vuelves al listado, donde el producto ya aparece con su estado, su precio, de quién es y en qué local está.

!!! warning "Atención"
    Si tu tienda tiene activada la aprobación previa, los productos nuevos entran en estado **Pendiente de aprobación de precio**: no se muestran en la tienda ni se pueden vender hasta pasarlos a **Disponible**. Si no la tienes activada, nacen directamente en **Disponible**.

!!! video "Video"
    Ver el video tutorial: [https://youtu.be/bs36QKdaB3k](https://youtu.be/bs36QKdaB3k)

<p class="doc-aliases" markdown>Términos relacionados: ingresar una prenda, dar de alta un producto, cargar mercadería, qué datos van, el precio es obligatorio, pendiente de aprobación</p>
