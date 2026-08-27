---
title: Crear y usar vales (cambios, señas y devoluciones)
slug: vales
order: 40
type: Guía
aliases: no me reconoce el vale, no genera el ID del vale, los vales no funcionan,
  la diferencia a favor, hice un vale por una seña
---

# Crear y usar vales (cambios, señas y devoluciones)

El vale es un medio de pago más: un crédito a nombre de una persona para usar en la tienda. Se usa para cambios, señas y devoluciones, y también para pagarle las comisiones a una proveedora.

### De dónde sale un vale

Casi nunca se crea un vale "suelto" — se genera solo, como consecuencia de otra operación:

| Operación | Cómo se genera |
| --- | --- |
| **Devolución** | En la pantalla de devolución elegís *Generar un Vale* como método de pago. Ver la guía *Devoluciones y cambiar el estado de una orden*. |
| **Pago de comisiones** | Al pagarle a una proveedora elegís *Vale* como forma de pago. Ver la guía *Pagar comisiones a proveedoras*. |
| **Seña o diferencia a favor** | Queda como crédito de la persona para su próxima compra. |

En todos los casos se le envía por mail a la persona.

### La ficha del vale

En **vales** están todos los emitidos. Al abrir uno vas a ver:

- **Cliente** — a nombre de quién está.
- **Estado** — *Activo* mientras no se haya usado.
- **Monto**
- **Locales que aplica** — en qué sucursales se puede canjear.
- **Fecha de creación**, **Fecha vencimiento** y **Fecha de canje**
- **Origen Vale** — de dónde salió. Por ejemplo *Excedente de orden (OR_1541)* o *Pago comisiones*.
![Ficha de un vale generado por una devolución](/assets/vales/6f12076f10a4.webp)

![Ficha de un vale generado por el pago de comisiones](/assets/vales/6c0344dd9de2.webp)

!!! danger "Importante"
    El **título del vale** — por ejemplo `MACARENA-ZAS-46564` — es su identificador. Es el dato que necesita la persona para poder usarlo, y el que vas a buscar vos al aplicarlo.

### Cómo se usa

Dentro de una orden de venta, en el bloque **Pagos de la Orden**, usá el campo **Agregar Vale** y buscá el vale por su id o por el nombre. Se descuenta del total como cualquier otro medio de pago.

Si el vale se usa por un monto menor al total del vale, el sistema genera **otro vale por la diferencia**, así no se pierde el saldo restante.

### Si el buscador no encuentra un vale

!!! tip "Tip"
    El vale se asocia a una orden, no se canjea suelto. Si no aparece en el buscador, verificá que tenga asignado el local correcto en **Locales que aplica** y que su estado siga siendo *Activo*.

<p class="doc-aliases" markdown>Términos relacionados: no me reconoce el vale, no genera el ID del vale, los vales no funcionan, la diferencia a favor, hice un vale por una seña</p>
