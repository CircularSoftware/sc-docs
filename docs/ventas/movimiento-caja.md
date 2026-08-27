---
title: 'Movimiento de caja: saldo inicial y cierre'
slug: movimiento-caja
order: 70
type: Guía
aliases: abrir caja, cerrar caja, ingresar el efectivo inicial, el saldo no coincide,
  retirar de caja, ver el total de ventas del día
---

# Movimiento de caja: saldo inicial y cierre

El movimiento de caja concilia el dinero físico con el sistema. Está en **pagos → movimiento de caja**.

### Qué se registra solo

La mayoría de los movimientos no los cargás a mano: el sistema los genera al operar.

- Cada **venta** genera un ingreso, desglosado por la forma en que se cobró.
- Cada **pago de comisiones** genera un egreso, que aparece **en rojo**.
![Ingresos generados por ventas del día](/assets/movimiento-caja/84c537822d44.webp)

![Egreso por el pago de una comisión](/assets/movimiento-caja/8cb01f5718dc.webp)

### Cómo leer la pantalla

Arriba a la derecha está el **Saldo en Caja**. Cada fila muestra fecha, descripción, local y el importe en la columna del medio de pago que corresponda: **CONTADO**, **C.D.T.** (crédito, débito y transferencia), **VALE** o **MP** (Mercado Pago). Al pie de la lista tenés el total del día.

Podés filtrar por rango de fechas, tipo de movimiento, local y medio de pago, y bajar el resultado con **descargar**.

### Cargar el saldo inicial

1. Entrá a **pagos → movimiento de caja**.
1. Hacé clic en **nuevo movimiento** y agregá un ingreso con el concepto "saldo inicial".
### Notas importantes

- Los medios que no son efectivo (débito, transferencia, vales) **no restan del saldo en caja**, porque ese saldo refleja el efectivo físico. Igual quedan registrados en su columna.
- Para sumar esos medios, descargá el Excel filtrando por medio de pago.
!!! tip "Tip"
    El total facturado de un período se ve en Órdenes, filtrando por fechas y descargando el Excel.

<p class="doc-aliases" markdown>Términos relacionados: abrir caja, cerrar caja, ingresar el efectivo inicial, el saldo no coincide, retirar de caja, ver el total de ventas del día</p>
