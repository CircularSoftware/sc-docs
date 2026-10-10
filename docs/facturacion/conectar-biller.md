---
title: Conectar la facturación electrónica (Biller)
slug: conectar-biller
order: 10
type: Guía
aliases: cómo integro Biller, facturación electrónica, qué es Biller, access token
  de biller, id de sucursal, empezar a facturar, dónde cargo el token de biller, no
  encuentro donde poner biller, cuándo se emite la factura, disparadores de emisión,
  facturar la comisión del local, facturar alquileres, CFE uruguay
---

# Conectar la facturación electrónica (Biller)

Si tu tienda está en Uruguay, los comprobantes fiscales (CFE) se emiten a través de **Biller**. Una vez conectada, la facturación sale sola al vender: no hay que emitir nada a mano en cada orden.

La conexión tiene dos partes. Las credenciales las cargamos nosotros, y el momento en que se emite cada comprobante lo defines tú.

### 1. Pásanos los datos de tu cuenta de Biller

Las credenciales de Biller no se cargan desde tu panel: las configuramos de nuestro lado, una vez.

1. En tu cuenta de Biller, genera el **API token** e identifica tu sucursal.
1. Envíanos el token, el **ID de sucursal**, el **RUT** y tu tipo de tributación (IVA).
1. Lo dejamos cargado en el sistema.
Si tienes más de un local, cada sucursal necesita su propio token, RUT y código.

!!! danger "Importante"
    Requiere el plan de Biller **con acceso a la API**. Sin ese plan no hay forma de conectar la facturación automática.

### 2. Define cuándo se emite cada comprobante

Esto sí lo configuras tú, en **Configuración → Facturación Electrónica**. En **Sistema fiscal** vas a ver tu país, **Uruguay (Biller)**, y debajo el bloque **Disparadores de emisión** con tres opciones.

| Ajuste | Qué define |
| --- | --- |
| **Comprobante de venta** | Se emite al finalizar la orden. Una orden no puede finalizar con saldo pendiente, así que el total ya es definitivo. |
| **Comprobante por la comisión del local** | Es el segundo comprobante de una venta de terceros: lo que se queda el local, emitido a nombre de la dueña del producto. Puedes emitirlo **cuando se le paga al dueño** o **al finalizar la orden**. |
| **Alquileres** | Como el total de un alquiler puede cambiar hasta cerrarse, la opción **por pago** evita facturar un total que todavía no es definitivo. |

Haz clic en **Guardar**.

!!! tip "Tip"
    Los cambios aplican a las órdenes que se finalicen después de guardar. Lo ya facturado no se vuelve a emitir y lo pendiente no se pierde: cada comisión se factura una sola vez.

### Qué pasa después

Con la conexión activa, cada venta genera sus comprobantes automáticamente. Para entender qué se emite y por qué —un comprobante por cada dueña de mercadería, más uno por los extras— mira [Cómo se factura al vender y al pagar comisiones](../facturacion/como-se-factura.md).

Lo emitido y lo que falló lo ves en **Dinero › Facturación**, con el estado de cada comprobante. Si algo da error, mira [Errores de facturación y notas de crédito](../preguntas-frecuentes.md#errores-facturacion).

!!! tip "Tip"
    ¿Tu tienda factura en Argentina? El circuito es otro y se configura desde tu panel. Mira [Conectar la facturación electrónica en Argentina (ARCA)](../facturacion/conectar-arca.md).

<p class="doc-aliases" markdown>Términos relacionados: cómo integro Biller, facturación electrónica, qué es Biller, access token de biller, id de sucursal, empezar a facturar, dónde cargo el token de biller, no encuentro donde poner biller, cuándo se emite la factura, disparadores de emisión, facturar la comisión del local, facturar alquileres, CFE uruguay</p>
