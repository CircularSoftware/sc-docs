---
title: 'Extras: cobrar la bolsa, la garantía y otros conceptos'
slug: adicionales-bolsa-envio
order: 30
type: Guía
aliases: agregar la bolsa a la venta, cobrar el envío, adicionales no me aparece,
  sumar el costo de la bolsa, envío editable, qué son los extras, agregar un extra
  a la orden, crear un extra, dar de baja un extra, precio fijo del extra, extra reembolsable,
  cobrar un porcentaje de la orden, otros conceptos
---

# Extras: cobrar la bolsa, la garantía y otros conceptos

Un **extra** es todo lo que una orden cobra además de los productos: la bolsa, la garantía de un alquiler, un recargo por servicio. Cada tienda arma su propia lista de extras, y al crear una orden el sistema solo ofrece los de esa lista.

Son dos momentos distintos: el extra se crea **una sola vez** en la sección **Extras**, y después se agrega a cada orden que lo necesite.

!!! tip "Tip"
    El **envío no es un extra**. Su costo se carga dentro de la orden, en el bloque **Entrega**, en el campo **Costo de envío**. En los alquileres, la devolución tiene su propio campo **Costo de retiro**.

### Crear los extras de tu tienda

Ingresa a **Extras** en el menú lateral. La lista muestra una fila por extra, con las columnas **Nombre**, **Precio**, **Precio fijo**, **Reembolsable** y **Acciones**.

!!! danger "Importante"
    Solo los usuarios con rol **Administrador** ven la sección **Extras**. Si tu usuario es **Encargado** o **Empleado** no la vas a encontrar en el menú: pídele a un administrador de tu tienda que cree el extra. Agregarlo a una orden, en cambio, lo puede hacer cualquier usuario.

Haz clic en **Nuevo extra** y completa el formulario:

| Campo | Qué cargar |
| --- | --- |
| **Nombre** | Cómo se va a llamar al agregarlo a una orden. Es obligatorio. |
| **Cómo se cobra** | **Un monto fijo** o **Un % de los productos de la orden**. |
| **Precio** | El importe, cuando elegiste monto fijo. |
| **Precio fijo** | Si lo activas, el precio no se puede cambiar al agregar el extra a una orden. Solo aparece con monto fijo. |
| **% de los productos** | Un número entero entre 1 y 100, cuando elegiste porcentaje. |
| **% reembolsable** | Un número entero entre 0 y 100. Es el tope de lo que se le puede devolver al cliente: 0 para una bolsa, 100 para una garantía. |

Haz clic en **Guardar**.

#### Cómo se calcula el porcentaje

Cuando el extra se cobra como un porcentaje, el cálculo toma los **productos** de la orden con sus descuentos ya aplicados, y antes de los descuentos por medio de pago. Los otros extras, el envío y el mantenimiento no cuentan. El monto se recalcula cada vez que la orden cambia.

### Agregar un extra a una orden

Dentro de la orden, el bloque **Extras** empieza vacío: solo se ven los extras que ya agregaste.

1. Haz clic en **Agregar extra**.
1. En **Extra**, elige uno de la lista.
1. Completa **Precio unitario** y **Cantidad**. Si el extra se cobra como porcentaje no hay nada que completar: la fila te avisa qué porcentaje se va a cobrar.
1. Haz clic en **Agregar**, o en **Cancelar** si te arrepentiste.
Cada extra ocupa una fila, que muestra la cantidad o el porcentaje y, si corresponde, hasta cuánto es reembolsable. Para sacarlo de la orden, usa **Quitar**.

!!! tip "Tip"
    Un extra que ya está en la orden no se vuelve a ofrecer en la lista. Si necesitas dos bolsas, no agregues la bolsa dos veces: sube la **Cantidad** de la fila que ya existe.

### Qué pasa después

El extra suma al total de la orden en la línea **Otros conceptos**, y el cliente lo paga junto con el resto.

!!! warning "Atención"
    **Los descuentos no se aplican sobre los extras.** Tanto el descuento a un producto como el descuento a la orden entera se calculan solo sobre las prendas: si agregas una bolsa de 30, ese importe se cobra completo.

Si el extra tiene un **% reembolsable** mayor que 0, la orden queda con un tope de devolución para ese concepto. Eso es lo que se usa para las garantías de alquiler: mira *Garantías en alquileres*.

Editar un extra del catálogo **no cambia las órdenes ya hechas**: cada orden conserva congelados el nombre, el precio y el porcentaje con los que se vendió. Lo mismo al usar **Dar de baja**: el extra se archiva y deja de ofrecerse al armar una orden, pero las órdenes que ya lo llevan no cambian y se pueden seguir editando.

<p class="doc-aliases" markdown>Términos relacionados: agregar la bolsa a la venta, cobrar el envío, adicionales no me aparece, sumar el costo de la bolsa, envío editable, qué son los extras, agregar un extra a la orden, crear un extra, dar de baja un extra, precio fijo del extra, extra reembolsable, cobrar un porcentaje de la orden, otros conceptos</p>
