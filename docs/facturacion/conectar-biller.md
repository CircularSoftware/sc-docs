---
title: Conectar la facturación electrónica (Biller)
slug: conectar-biller
order: 10
type: Guía
aliases: cómo integro Biller, facturación electrónica, qué es Biller, access token
  de biller, id de sucursal, empezar a facturar, dónde cargo el token de biller, no
  encuentro donde poner biller, cuándo se emite la factura, disparadores de emisión,
  facturar la comisión del local, facturar alquileres, CFE uruguay, crear api token
  en biller, api tokens, ajustes sucursales biller, id de sucursal biller, plan de
  biller, plan grande biller, qué plan necesito en biller, verificar conexión biller,
  código de sucursal, tienda sin verificar, no existe CAE para el tipo de comprobantes,
  CAE e-Ticket, régimen monotributo biller, biller no acepta este token, encender
  facturación biller
---

# Conectar la facturación electrónica (Biller)

Si tu tienda está en Uruguay, los comprobantes fiscales (CFE) se emiten a través de **Biller**. Una vez conectada, la facturación sale sola al vender: no hay que emitir nada a mano en cada orden.

La conexión tiene dos partes y las dos se hacen desde tu panel, en **Configuración › Facturación electrónica**: conectar cada tienda con tu cuenta de Biller y definir en qué momento se emite cada comprobante. Esa pantalla la ve un usuario con rol **Administrador**.

### 1. Conecta cada tienda con Biller

Primero busca en Biller los datos que vas a cargar, y después cárgalos en tu panel.

1. En Biller, entra a **API › Tokens** y haz clic en **Crear API Token**. Si ya tienes uno creado, sirve ese. El token es la llave con la que emitimos los comprobantes en tu nombre, así que trátalo como una contraseña.
    ![El menú API › Tokens de Biller, con el botón Crear API Token](/assets/conectar-biller/da8871ccea43.webp)

1. En **Ajustes › Sucursales**, anota el **ID** de la sucursal de cada tienda que vaya a facturar: es el **Código de sucursal** que te pide el panel (no es el número del token).
    ![La pestaña Sucursales de Ajustes, con las columnas ID y Nombre](/assets/conectar-biller/97e227027fbb.webp)

1. Ten a mano el **RUT** de la empresa: son 12 dígitos.
1. En tu panel, entra a **Configuración › Facturación electrónica**. En **Sistema fiscal** tiene que figurar **Uruguay (Biller)**.
1. Baja hasta la tarjeta **Conexión con Biller**, al final de la página. Ahí aparece cada una de tus tiendas, con su estado.
1. En la tienda que quieres conectar, completa **Token de Biller**, **Código de sucursal**, **RUT de la empresa** y **Régimen**. Si no sabes si facturas como **Régimen general (IVA tasa básica)** o como **Monotributo / IVA mínimo**, deja **Detectar al verificar**.
1. Toca **Guardar**, el botón de esa tienda dentro de la tarjeta. Al guardar se verifica la conexión: le preguntamos a Biller qué comprobantes puedes emitir, sin emitir ninguno, y configuramos el CAE solos. Si todo da bien, ves **Conexión verificada** y la tienda queda **Verificada**.
1. Repite los pasos 6 y 7 con cada tienda que vaya a facturar.
1. Enciende **Facturar las ventas con Biller**, arriba en la misma tarjeta. Se guarda al tocarlo: la tarjeta pasa a decir **Facturación encendida**.
Si tus tiendas son de la misma empresa en Biller, puedes cargar el mismo token en todas: lo que cambia por tienda es el código de sucursal.

!!! danger "Importante"
    Hay que contratar el **plan más grande de Biller**: la conexión por API viene solo con ese plan. Con uno menor no hay forma de conectar la facturación automática, y cada comprobante habría que emitirlo a mano en Biller.

### 2. Define cuándo se emite cada comprobante

Esto se configura en la misma pantalla, **Configuración › Facturación electrónica**. En **Sistema fiscal** vas a ver tu país, **Uruguay (Biller)**, y debajo el bloque **Disparadores de emisión** con tres opciones.

| Ajuste | Qué define |
| --- | --- |
| **Comprobante de venta** | Se emite al finalizar la orden. Una orden no puede finalizar con saldo pendiente, así que el total ya es definitivo. |
| **Comprobante por la comisión del local** | Es el segundo comprobante de una venta de terceros: lo que se queda el local, emitido a nombre de la dueña del producto. Puedes emitirlo **cuando se le paga al dueño** o **al finalizar la orden**. |
| **Alquileres** | Como el total de un alquiler puede cambiar hasta cerrarse, la opción **por pago** evita facturar un total que todavía no es definitivo. |

Haz clic en **Guardar**.

!!! tip "Tip"
    Los cambios aplican a las órdenes que se finalicen después de guardar. Lo ya facturado no se vuelve a emitir y lo pendiente no se pierde: cada comisión se factura una sola vez.

### Los estados de cada tienda

Cada tienda de la tarjeta **Conexión con Biller** muestra uno de estos estados:

| Estado | Qué significa |
| --- | --- |
| **Sin conectar** | La tienda no tiene datos de Biller cargados y no factura. |
| **Sin verificar** | Hay datos guardados que todavía no pasaron la verificación. Una tienda que nunca se verificó no factura hasta que tocas **Verificar conexión** y da bien. |
| **Verificada** | La tienda factura sus ventas con Biller. |
| **Con problemas** | La verificación encontró algo para corregir: lo ves debajo, en esa tienda. Corrígelo y verifica de nuevo. |
| **Revisando** | Biller rechazó un comprobante por el CAE y estamos revisando la conexión. |
| **Conectada** | La tienda factura con la configuración que ya tenía. Toca **Verificar conexión** para confirmar que el CAE está bien. |

Después de verificar, debajo de la tienda ves la lista de comprobantes que puede emitir. **Listo** quiere decir que hay un CAE para ese tipo. El único imprescindible es el **e-Ticket**: los otros hacen falta solo si emites ese comprobante, por ejemplo en ventas en consignación o a empresas con RUT.

### Qué significa cada mensaje

| Dice | Significa | Qué hacer |
| --- | --- | --- |
| *Biller no acepta este token.* | El token está mal copiado o ya no sirve. | Genera uno nuevo en Biller › **API › Tokens**, toca **Editar** en la tienda, pégalo y guarda. |
| *La sucursal … no existe en tu cuenta de Biller.* | El código de sucursal no corresponde a tu cuenta. | Revísalo en Biller › **Ajustes › Sucursales** y corrígelo con **Editar**. |
| *No tenés un CAE cargado para e-Ticket* | Tu cuenta de Biller no tiene CAE para el comprobante principal: la tienda no puede facturar. | Pide el CAE en DGI, cárgalo en Biller › **Ajustes › CAEs** y toca **Verificar conexión**. |
| *Sin CAE para …: hace falta solo si emitís ese comprobante* | Falta el CAE de un comprobante que no todas las tiendas usan. | Si emites ese comprobante, pídelo en DGI y cárgalo en Biller › **Ajustes › CAEs**. |
| *Biller indica que esta cuenta factura como …* | El régimen que elegiste no coincide con el de tu cuenta de Biller. | Si Biller tiene razón, toca **Editar**, cambia el **Régimen** y verifica de nuevo. |
| *Biller no respondió. Probá de nuevo en unos minutos.* | Biller no estaba disponible. | Toca **Verificar conexión** más tarde. |
| *Biller respondió algo que no esperábamos.* | Una respuesta de Biller que no pudimos leer. | Prueba de nuevo; si sigue, escríbenos. |
| *No pudimos verificar sin emitir: avisamos al equipo de Circular.* | La verificación no pudo hacerse sin emitir un comprobante. | No hagas nada: nosotros lo revisamos. |
| *El código de sucursal tiene que ser un número.* | En **Código de sucursal** hay algo que no es un número. | Copia el **ID** de Biller › **Ajustes › Sucursales**. |
| *El RUT tiene que tener 12 dígitos.* | El RUT está incompleto. | Escribe los 12 dígitos del RUT de la empresa. |
| *Pegá el token de Biller de esta tienda.* | Es la primera vez que conectas la tienda y el token está vacío. | Pega el token de Biller › **API › Tokens**. |
| *Para encenderla, conectá y verificá al menos una tienda.* | No hay ninguna tienda que pueda facturar todavía. | Conecta una tienda y espera a que quede **Verificada**. |

### Cambiar o quitar la conexión de una tienda

- Para cambiar un dato, toca **Editar** en la tienda, corrige lo que haga falta y toca **Guardar**. Si no vas a cambiar el token, deja ese campo vacío: se conserva el que está.
- Para verificar de nuevo sin cambiar nada, toca **Verificar conexión**.
- Para desconectar una tienda, toca **Quitar** y confirma con **Quitar la conexión**. La tienda deja de facturar y se borra su token.
### Tener en cuenta

- **El token no se vuelve a mostrar.** Después de guardarlo solo ves sus últimos cuatro caracteres. Si lo pierdes, genera uno nuevo en Biller.
- **La tarjeta de Biller guarda por su cuenta.** El **Guardar** de cada tienda y el interruptor **Facturar las ventas con Biller** se guardan al tocarlos. Los disparadores de emisión, en cambio, se guardan con el **Guardar** de arriba de la página.
- **Si Biller rechaza un comprobante por el CAE**, volvemos a verificar esa tienda y te llega un mail que dice qué hacer. La orden no se reintenta sola: cuando esté resuelto, abre la orden y toca **Reintentar facturación**. El reintento usa los datos de Biller que la tienda tiene en ese momento.
- **Si apagas Facturar las ventas con Biller**, las ventas se siguen registrando pero no se facturan.
### Qué pasa después

Con la conexión activa, cada venta genera sus comprobantes automáticamente. Para entender qué se emite y por qué —un comprobante por cada dueña de mercadería, más uno por los extras— mira [Cómo se factura al vender y al pagar comisiones](../facturacion/como-se-factura.md).

Lo emitido y lo que falló lo ves en **Dinero › Facturación**, con el estado de cada comprobante. Si algo da error, mira [Errores de facturación y notas de crédito](../preguntas-frecuentes.md#errores-facturacion).

!!! tip "Tip"
    ¿Tu tienda factura en Argentina? El circuito es otro y se configura desde tu panel. Mira [Conectar la facturación electrónica en Argentina (ARCA)](../facturacion/conectar-arca.md).

<p class="doc-aliases" markdown>Términos relacionados: cómo integro Biller, facturación electrónica, qué es Biller, access token de biller, id de sucursal, empezar a facturar, dónde cargo el token de biller, no encuentro donde poner biller, cuándo se emite la factura, disparadores de emisión, facturar la comisión del local, facturar alquileres, CFE uruguay, crear api token en biller, api tokens, ajustes sucursales biller, id de sucursal biller, plan de biller, plan grande biller, qué plan necesito en biller, verificar conexión biller, código de sucursal, tienda sin verificar, no existe CAE para el tipo de comprobantes, CAE e-Ticket, régimen monotributo biller, biller no acepta este token, encender facturación biller</p>
