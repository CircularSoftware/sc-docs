---
title: Crear y usar vales (cambios, señas y devoluciones)
slug: vales
order: 40
type: Guía
aliases: no me reconoce el vale, no genera el ID del vale, los vales no funcionan,
  la diferencia a favor, hice un vale por una seña, canjear un vale por efectivo,
  cambiar un vale por plata, cancelar un vale, anular un vale, quién emite el vale,
  de qué caja sale el vale, el vale está expirado, dónde se puede usar el vale, crear
  un vale a mano
---

# Crear y usar vales (cambios, señas y devoluciones)

El vale es un medio de pago más: un crédito a nombre de una persona para usar en la tienda. Se usa para cambios, señas y devoluciones, y también para pagarle las comisiones a una proveedora.

### De dónde sale un vale

Casi siempre se genera solo, como consecuencia de otra operación:

| Operación | Cómo se genera |
| --- | --- |
| **Devolución** | En la pantalla de devolución elegís *Generar un Vale* como método de pago. Ver la guía *Devoluciones y cambiar el estado de una orden*. |
| **Pago de comisiones** | Al pagarle a una proveedora elegís *Vale* como forma de pago. Ver la guía *Pagar comisiones a proveedoras*. |
| **Seña o diferencia a favor** | Queda como crédito de la persona para su próxima compra. |

En todos los casos se le envía por mail a la persona.

### La ficha del vale

En **vales** están todos los emitidos. Al abrir uno vas a ver:

- **Cliente** — a nombre de quién está.
- **Estado** — **Activo** mientras no se haya usado, **Canjeado** si ya se usó o se cambió por dinero, **Expirado** si pasó su fecha de vencimiento y **Cancelado** si se anuló. Los tres últimos son finales.
- **Monto**
- **Dónde se puede usar** — en qué tiendas se puede aplicar. Si está vacío, vale en todas.
- **Fecha de creación**, **Fecha vencimiento** y **Fecha de canje**
- **Origen Vale** — de dónde salió. Por ejemplo *Excedente de orden (OR_1541)* o *Pago comisiones*.
![Ficha de un vale generado por una devolución](/assets/vales/6f12076f10a4.webp)

![Ficha de un vale generado por el pago de comisiones](/assets/vales/6c0344dd9de2.webp)

!!! danger "Importante"
    El **título del vale** — por ejemplo `MACARENA-ZAS-46564` — es su identificador. Es el dato que necesita la persona para poder usarlo, y el que vas a buscar vos al aplicarlo.

### Cómo se usa

Dentro de una orden de venta, en el bloque **Pagos de la Orden**, usa el campo **Agregar Vale** y busca el vale por su id o por su nombre. Se descuenta del total como cualquier otro medio de pago.

Un vale se usa **una sola vez**: si intentas aplicar uno ya usado, el sistema lo rechaza.

Si el vale se usa por un monto menor al total del vale, el sistema genera **otro vale por la diferencia**, así no se pierde el saldo restante.

### Crear un vale a mano

También puedes emitir uno sin que venga de una devolución. En **Vales**, haz clic en **Nuevo Vale** y completa el **Cliente**, el **Monto** y **Quién emite el vale**.

!!! danger "Importante"
    **Quién emite el vale** es obligatorio: es la tienda de cuya caja sale el dinero del vale. El sistema lo dice así: *de esta caja sale la plata del vale*.

### Canjear o cancelar un vale

Desde el listado de **Vales**, en las acciones de cada fila, hay dos opciones además de usarlo en una compra:

| Acción | Qué hace |
| --- | --- |
| **Canjear vale** | Lo cambia por dinero, en **Efectivo** o por **Transferencia**. El vale pasa a Canjeado y queda el egreso registrado en la caja. |
| **Cancelar vale** | Lo anula. Solo se puede con un vale **Activo** que se haya creado a mano. |

### Si el buscador no encuentra un vale

!!! tip "Tip"
    Si no aparece en el buscador, revisa dos cosas: que su estado siga siendo **Activo** —un vale canjeado, expirado o cancelado ya no se puede usar— y que la tienda de la venta esté entre las de **Dónde se puede usar**.

<p class="doc-aliases" markdown>Términos relacionados: no me reconoce el vale, no genera el ID del vale, los vales no funcionan, la diferencia a favor, hice un vale por una seña, canjear un vale por efectivo, cambiar un vale por plata, cancelar un vale, anular un vale, quién emite el vale, de qué caja sale el vale, el vale está expirado, dónde se puede usar el vale, crear un vale a mano</p>
