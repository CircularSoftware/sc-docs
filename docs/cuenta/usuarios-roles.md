---
title: Usuarios y roles (Administrador, Encargado, Empleado)
slug: usuarios-roles
order: 30
type: Guía
aliases: crear un usuario, agregar a alguien del equipo, tipos de usuario, permisos,
  que solo cargue productos, no puedo entrar con el administrador
---

# Usuarios y roles (Administrador, Encargado, Empleado)

Podés crear usuarios para tu equipo con distinto nivel de acceso, sin costo adicional.

### Crear un usuario

1. Entrá al menú **usuarios**.
1. Hacé clic en **nuevo usuario**.
1. Asigná el rol según lo que tenga que hacer.
### Qué puede hacer cada rol

Los permisos son acumulativos: cada rol puede hacer lo del rol anterior, más lo suyo. La diferencia principal es el **alcance**: los roles operativos trabajan solo sobre su local, y el rol más alto puede elegir sobre qué local opera.

!!! tip "Tip"
    **ABM** significa alta, baja y modificación: poder crear, editar y dar de baja ese tipo de registro.

#### Vendedor

Es el rol operativo del día a día, siempre acotado a su local.

- Ingresa órdenes, cambia estados y ve las órdenes de su local.
- Ingresa productos y los modifica, **excepto la condición**, y no puede pasarlos a los estados "perdido" ni "robado".
- ABM de clientes, **excepto tocar la comisión**.
- Ve la caja de su local y agrega movimientos, **pero no puede descargarla**.
- Ve y paga comisiones, con la opción de pagar como voucher.
- Mesa de trabajo de su local.
- ABM de mantenimientos.
#### Encargado

Todo lo del vendedor, y además:

- Ve los reportes de su local.
- ABM de campañas.
- ABM de vouchers.
- Puede **descargar** la caja de su local.
- ABM de productos de su local.
- En clientes, **puede tocar la comisión**.
#### Master

Todo lo anterior, pero sin la restricción de local:

- Órdenes: lo mismo, pero eligiendo el local.
- Mesa de trabajo de cualquier local.
- Descarga la caja completa, de todos los locales.
- ABM de productos de cualquier local.
- Ve los reportes de cualquier local.
!!! warning "Atención"
    El alcance por local es real y se nota al operar: un usuario de venta de una sucursal **no ve los productos de otra**. Con un usuario master sí los ve todos, y ahí puede pasar que vendas sin querer una prenda de un local que no tiene conectada la facturación electrónica.

!!! tip "Tip"
    Si tenés varios locales, creá un usuario por local para no mezclar sucursales.

<p class="doc-aliases" markdown>Términos relacionados: crear un usuario, agregar a alguien del equipo, tipos de usuario, permisos, que solo cargue productos, no puedo entrar con el administrador</p>
