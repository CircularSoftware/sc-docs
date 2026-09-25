---
title: 'Puesta en marcha: qué configurar antes de tu primera venta'
slug: puesta-en-marcha
order: 12
type: Guía
aliases: por dónde empiezo, qué hago primero, acabo de contratar el sistema, configuración
  inicial, puesta en marcha, checklist inicial, qué necesito antes de vender, en qué
  orden cargo las cosas, no me deja importar productos, no puedo descargar la plantilla,
  no hay categorías configuradas, no hay tiendas activas, no me aparece la marca,
  no encuentro a la proveedora al cargar un producto
---

# Puesta en marcha: qué configurar antes de tu primera venta

Esta guía es el orden en el que conviene dejar el sistema listo antes de hacer tu primera venta. No es una lista de sugerencias: el sistema tiene dependencias reales entre una cosa y la otra, y si te saltas un paso, el siguiente se bloquea. El caso más común es querer importar los productos el primer día y encontrarte con que no se puede, porque todavía no existen las categorías.

Léela de arriba hacia abajo una sola vez. Cada paso enlaza a la guía que lo explica en detalle, así que aquí solo vas a encontrar qué hacer, en qué orden y por qué.

!!! danger "Importante"
    Casi toda la configuración inicial la hace un usuario con rol **Administrador**. Las secciones **Tiendas**, **Catálogo**, **Importación masiva**, **Extras**, **Usuarios** y **Mi sitio web** no aparecen en el menú de un **Encargado** ni de un **Empleado**. Haz la puesta en marcha con el usuario administrador que te entregamos.

### Por qué importa el orden

Estas son las dependencias reales del sistema. Si te falta lo de la izquierda, lo de la derecha no se puede hacer:

| Si todavía no tienes… | No vas a poder… |
| --- | --- |
| Ninguna tienda activa | Descargar la plantilla de productos, ni guardar un producto: el **Local** es obligatorio |
| Ninguna categoría | Descargar la plantilla de productos, ni guardar un producto: la categoría es obligatoria |
| Los atributos con sus valores cargados | Completar la marca, el talle o el color de un producto. Esos valores **solo** se crean en Catálogo, nunca mientras cargas un producto |
| Clientes con rol **Dueño** o **Marca** | Asignarle un producto a su proveedora, ni en el alta individual ni en la planilla |
| Los períodos de alquiler definidos (solo si alquilas) | Importar productos |

### Lo que dejamos listo nosotros

Hay cuatro cosas que se configuran de nuestro lado y que no vas a encontrar en tu panel. Las dejamos puestas al darte de alta, pero conviene que confirmes que están como las necesitas:

- Si tu tienda **vende o alquila.**
- Los **períodos de alquiler**: cuántos días dura un alquiler y cómo se calcula su precio.
- La **comisión por defecto** que se propone al dar de alta a una proveedora.
- El **día del mes** en que las comisiones pasan a estar disponibles para pagar.
Si algo de eso no coincide con cómo trabajas, escríbenos antes de empezar a cargar datos: cambiarlo después es más incómodo.

---

### Paso 1 — Revisa tus tiendas y su moneda

Ingresa a **Tiendas** y confirma que estén todos tus locales, con su nombre y su dirección. Cada tienda define su propia moneda: código, símbolo, posición, espaciado y **cantidad de decimales**.

!!! warning "Atención"
    Define bien los **decimales** ahora. Cada orden congela sus precios con la cantidad de decimales que tenía la moneda en ese momento, así que una vez que existan órdenes el sistema no te va a dejar cambiarlos.

Una aclaración de vocabulario que confunde al principio: la pantalla se llama **Tiendas**, pero dentro de un producto o de una orden ese mismo dato aparece como **Local**.

### Paso 2 — Arma el árbol de categorías

Sin categorías no hay productos. Entra a **Catálogo → Categorías** y arma la estructura con la que organizas tu mercadería.

El detalle está en [Agregar o modificar categorías y subcategorías](../catalogo/categorias.md).

!!! tip "Tip"
    La plantilla de importación masiva solo ofrece las categorías **hoja**, las que no tienen subcategorías colgando. Si vas a importar, asegúrate de que las ramas terminen donde realmente quieres clasificar la ropa.

### Paso 3 — Carga los atributos y sus valores

Los atributos son las características de la prenda: marca, talle, color, material. Entra a **Catálogo → Atributos** y carga los que uses, con sus valores.

El detalle está en [Agregar marcas, talles y otros atributos](../catalogo/atributos.md).

!!! danger "Importante"
    Este paso no se puede postergar. Los valores de un atributo **solo se crean en Catálogo → Atributos**: ni el formulario de producto ni la importación masiva te dejan inventar una marca nueva sobre la marcha. Si la marca no está en la lista, el producto se rechaza.

### Paso 4 — Da de alta a tus proveedoras

Este paso es obligatorio si trabajas con **consignación**, es decir, si vendes mercadería que le pertenece a otra persona. Un producto solo se le puede asignar a alguien que **ya existe** en el sistema con rol **Dueño** o **Marca**.

El detalle está en [Crear un cliente](../clientes/crear-cliente.md). Si son muchas, puedes cargarlas por planilla en el mismo paso que los productos.

### Paso 5 — Carga tus productos

Recién ahora. Tienes dos caminos:

| Cuántos productos | Por dónde |
| --- | --- |
| Pocos, o para probar | Uno por uno, desde **Productos**. Mira [Cargar un producto nuevo](../catalogo/cargar-producto.md) |
| Todo tu stock inicial | Por planilla, desde **Importación masiva**. Mira [Cargar clientes y productos de forma masiva](https://carga-masiva.md/) |

Si vas por la planilla, el orden dentro de ese paso también importa: **primero los clientes y después los productos**, porque la plantilla de productos viene con tus proveedoras ya cargadas en un desplegable. Si algo falla, [Errores al importar la planilla masiva](../preguntas-frecuentes.md#errores-importacion) explica cómo leer el archivo de errores.

### Paso 6 — Suma las fotos

Las fotos se cargan después de los productos. Puedes hacerlo desde la ficha de cada producto, desde **Fotos de productos** —una pantalla pensada para el teléfono— o en lote desde **Importación masiva**, nombrando cada archivo con el código del producto.

Los formatos y tamaños aceptados están en la pregunta frecuente [No puedo subir las fotos de un producto](../preguntas-frecuentes.md#fotos-productos).

### Paso 7 — Define tus extras

Un extra es todo lo que cobras además de los productos: la bolsa, la garantía de un alquiler, un recargo. Si no los creas antes, no vas a poder agregarlos a una venta.

Mira [Extras: cobrar la bolsa, la garantía y otros conceptos](../ventas/adicionales-bolsa-envio.md), y si alquilas, también [Garantías en alquileres](../ventas/garantias.md).

### Paso 8 — Crea los usuarios de tu equipo

Da de alta a las personas que van a trabajar en el sistema, con su rol y las tiendas en las que trabajan. Mira [Usuarios y roles](../cuenta/usuarios-roles.md).

### Paso 9 — Conecta la facturación electrónica

Solo si tu tienda emite comprobantes fiscales. Conviene dejarlo listo antes de la primera venta: las órdenes que hagas sin la facturación conectada no generan comprobante, y no se emite después de forma automática.

Mira [Conectar la facturación electrónica (Biller)](../facturacion/conectar-biller.md) y [Cómo se factura al vender y al pagar comisiones](../facturacion/como-se-factura.md).

### Paso 10 — Precios por medio de pago (opcional)

Si cobras distinto según cómo te paguen —descuento por efectivo, recargo por tarjeta—, configúralo antes de empezar a vender: cada orden congela el precio con el que se cerró. Mira [Precios por medio de pago](../pagos/perfiles-precio.md).

### Paso 11 — Tu tienda online (si vas a vender por la web)

Este bloque es independiente del resto y puede hacerse después, pero ninguna de estas cosas funciona sin los pasos anteriores:

- [Publicar productos en la tienda online](../tienda-online/publicar-en-web.md) — un producto se muestra en la web solo con el canal web activado.
- [Editar tu web: banners, textos y botón de WhatsApp](../tienda-online/editar-mi-web.md)
- [Configurar envíos y medios de pago en la web](../tienda-online/envios-y-pagos-web.md)
- [Conectar Mercado Pago a la tienda](../pagos/mercado-pago.md)
- [Conectar tu propio dominio](../tienda-online/conectar-dominio.md)
---

### Cómo saber que estás listo

La forma de comprobarlo no es releer esta lista: es **hacer una venta de prueba** con un producto real y mirar qué pasa después. Sigue [Registrar una nueva venta](../ventas/nueva-venta.md) y, al guardar, revisa que se hayan generado las cuatro cosas:

1. La orden, en **Ordenes**.
1. El movimiento de caja, en **Pagos → Movimiento de Caja**.
1. La comisión de la proveedora, en la ficha de esa persona, pestaña **Comisiones** (solo si la prenda tenía dueña).
1. El comprobante fiscal, si conectaste la facturación electrónica.
Si las cuatro aparecen, la configuración está completa. Después puedes deshacer esa venta siguiendo [Devoluciones y cambiar el estado de una orden](../ventas/devoluciones-estados-orden.md), y el producto vuelve a quedar disponible.

!!! tip "Tip"
    Haz la venta de prueba con un importe chico y con un producto que puedas volver a poner a la venta. Es la única forma de ver el circuito completo antes de que lo recorra un cliente de verdad.

<p class="doc-aliases" markdown>Términos relacionados: por dónde empiezo, qué hago primero, acabo de contratar el sistema, configuración inicial, puesta en marcha, checklist inicial, qué necesito antes de vender, en qué orden cargo las cosas, no me deja importar productos, no puedo descargar la plantilla, no hay categorías configuradas, no hay tiendas activas, no me aparece la marca, no encuentro a la proveedora al cargar un producto</p>
