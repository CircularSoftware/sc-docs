---
title: Usuarios y roles (Administrador, Encargado, Empleado)
slug: usuarios-roles
order: 30
type: Guía
aliases: crear un usuario, agregar a alguien del equipo, tipos de usuario, permisos,
  que solo cargue productos, no puedo entrar con el administrador
---

# Usuarios y roles (Administrador, Encargado, Empleado)

Puedes crear usuarios para tu equipo con distinto nivel de acceso, sin costo adicional. Cada usuario se define por dos cosas: el **rol**, que decide qué puede hacer, y las **tiendas asignadas**, que deciden sobre qué datos lo puede hacer.

### Crear un usuario

1. Ingresa a **Usuarios** en el menú lateral.
1. Haz clic en **Nuevo Usuario**.
1. Completa los **Datos del usuario** y elige el **Rol**.
1. En **Tiendas asignadas**, marca las tiendas en las que trabaja.
1. Revisa el bloque **Permisos** y guarda.
!!! danger "Importante"
    Un usuario que no es Administrador **necesita al menos una tienda asignada**: sin eso no se puede guardar. Un Administrador no se restringe: siempre opera todas las tiendas del negocio.

### Los tres roles

| Rol | Para quién |
| --- | --- |
| **Administrador** | Acceso total y a todas las tiendas. Es el único que entra a Tiendas, Usuarios, Catálogo, Importación masiva, Extras, Reportes, Mi sitio web y Configuración. |
| **Encargado** | Opera el día a día y además ve reportes, vales, promociones y remitos de sus tiendas. |
| **Empleado** | El rol operativo acotado: órdenes, reservas, clientes, productos, fotos y mantenimientos de sus tiendas. |

Los permisos son acumulativos: cada rol puede hacer lo del anterior más lo suyo. La diferencia práctica más visible es qué aparece en el menú lateral — un Empleado no ve Vales, Remitos ni Promociones, y ni Empleado ni Encargado ven Usuarios, Tiendas o Catálogo.

#### Diferencias dentro de la operación

- **Empleado**: ingresa órdenes y cambia estados; carga y edita productos, salvo la condición, y no puede pasarlos a perdido ni robado; da de alta clientes, pero sin tocar la comisión; ve la caja de su tienda y agrega movimientos, sin poder descargarla; ve y paga comisiones; gestiona mantenimientos.
- **Encargado**: todo lo anterior, y además puede **descargar** la caja, tocar la **comisión** de un cliente, y gestionar vales y promociones.
- **Administrador**: todo lo anterior sin la restricción de tiendas, más la configuración del sistema.
### Permisos por usuario

Debajo del rol hay un bloque **Permisos** que se pre-marca según el rol y se puede ajustar persona por persona. Hoy el permiso disponible es:

**Puede vender productos de otras tiendas** — deja ver el catálogo de las demás tiendas al armar una orden. La orden sigue siendo de la tienda de quien vende; lo único que cambia es de dónde puede salir la mercadería.

!!! tip "Tip"
    Un Administrador lo tiene siempre y no se puede desmarcar. Y si la venta de productos de otras tiendas está apagada para todo el negocio, el permiso queda sin efecto hasta que se encienda.

### Qué pasa después

Cada persona entra con su propio email y contraseña, y lo que ve en cada listado depende de sus tiendas asignadas. Si tiene más de una, puede elegir con cuál trabajar desde el selector del menú lateral: mira [Trabajar con varios locales](../cuenta/trabajar-con-varios-locales.md).

!!! warning "Atención"
    El alcance por tienda se nota al operar: alguien asignado a una sola tienda no ve los productos de las otras. Un Administrador sí los ve todos, y ahí puede pasar que venda sin querer una prenda de una tienda que no tiene conectada la facturación electrónica.

<p class="doc-aliases" markdown>Términos relacionados: crear un usuario, agregar a alguien del equipo, tipos de usuario, permisos, que solo cargue productos, no puedo entrar con el administrador</p>
