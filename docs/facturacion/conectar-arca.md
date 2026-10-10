---
title: Conectar la facturación electrónica en Argentina (ARCA)
slug: conectar-arca
order: 15
type: Guía
aliases: arca, afip, facturación electrónica argentina, certificado arca, csr, punto
  de venta, wsfe, cae, factura a b c, monotributo, responsable inscripto, alícuota
  de iva, cuenta de venta y líquido producto, cvylp, homologación, conectar afip
---

# Conectar la facturación electrónica en Argentina (ARCA)

Si tu tienda está en Argentina, los comprobantes se emiten a través de **ARCA** (ex AFIP): facturas A, B o C con su CAE. Esta guía es el alta de esa conexión, que se hace una sola vez desde **Configuración → Facturación Electrónica**.

!!! warning "Atención"
    Esto no es una configuración de cinco minutos. El primer paso pide ejecutar un comando en una computadora para generar el certificado, y hay un trámite dentro del portal de ARCA que no se puede hacer desde nuestro sistema. Lo habitual es resolverlo entre quien lleva la contabilidad y quien se ocupa de la parte técnica. Si no tienes a nadie para esa parte, escríbenos antes de empezar.

### Antes de empezar

Ten a mano:

- El **CUIT** de tu negocio y la clave fiscal para entrar al portal de ARCA.
- El **punto de venta** habilitado para web services. Si todavía no lo diste de alta, se hace en el portal de ARCA.
- Tu **condición frente al IVA**: Responsable Inscripto, Monotributo o Exento.
- Una computadora donde se pueda ejecutar un comando de terminal.
### Elegir el sistema fiscal

Ingresa a **Configuración → Facturación Electrónica**. En el bloque **Sistema fiscal**, en el campo **País**, elige **Argentina (ARCA)**.

Al elegirlo aparece el bloque **Alta de certificado ARCA (AFIP)**, con sus cuatro pasos.

### Los cuatro pasos del certificado

#### Paso 1 — Generar CSR

El CSR es el pedido de firma del certificado. La pantalla te muestra el comando exacto, ya armado con tu CUIT: se ejecuta en tu computadora, no en el sistema. Genera dos archivos, un `.csr` y una clave privada `.key`.

El `.csr` se sube al portal de ARCA, que a cambio te devuelve el certificado `.crt`.

!!! danger "Importante"
    Guarda la **clave privada (.key)** en un lugar seguro. No se vuelve a mostrar y no debe salir de tu equipo: quien la tenga puede facturar en nombre de tu negocio.

#### Paso 2 — Subir el certificado

Carga el **certificado (.crt)** que emitió ARCA junto con tu **clave privada**, y completa:

| Campo | Qué poner |
| --- | --- |
| **CUIT** | El de tu negocio. |
| **Punto de venta** | El que habilitaste para web services en ARCA. |
| **Entorno** | **Homologación (pruebas)** para probar sin emitir nada real, o **Producción** cuando vayas a facturar de verdad. |
| **Tu condición frente al IVA** | Responsable Inscripto, Monotributo o Exento. |
| **Régimen Factura M (RG 1575)** | Solo si ARCA te incluyó en ese régimen. Ante la duda, consúltalo con tu contador. |

Haz clic en **Guardar credenciales**.

!!! tip "Tip"
    Conviene arrancar en **Homologación** y recién pasar a **Producción** cuando la prueba del paso 4 dé bien. Son dos entornos distintos de ARCA: lo que emitas en homologación no tiene validez fiscal.

#### Paso 3 — Autorización del DN

Este paso se hace en el portal de ARCA, no acá: hay que autorizar el certificado para el web service **wsfe** (Factura Electrónica).

!!! danger "Importante"
    Sin la autorización del Delegado de Negocio para wsfe, las llamadas devuelven error de permisos **aunque el certificado sea válido**. Es el paso que más veces queda a medias y el que explica casi todos los "ya cargué todo y no funciona".

#### Paso 4 — Prueba de humo

Haz clic en **Probar conexión**. El sistema se conecta a ARCA con las credenciales guardadas y te responde:

- **Conexión OK** y, si corresponde, que el punto de venta está registrado. Ya puedes facturar.
- **Falló la conexión**: revisa el certificado, la clave y el CUIT del paso 2, y que la autorización del paso 3 esté hecha.
Si la conexión da bien pero avisa que todavía no hay punto de venta de web services registrado, ese alta se hace en el portal de ARCA.

### Lo que queda por definir

En la misma pantalla hay tres ajustes que conviene repasar con tu contador antes de la primera venta.

**Liquidación al dueño o proveedor.** Define cómo se documenta lo que le corresponde a quien dejó la mercadería en consignación:

| Opción | Qué implica |
| --- | --- |
| **El dueño factura al local** (por defecto) | La venta al comprador es una factura normal a nombre del local. El dueño emite su propia factura al local por la liquidación. |
| **El local emite Cuenta de Venta y Líquido Producto** | El local emite la CVyLP al dueño. Solo está disponible si el local es Responsable Inscripto. |

!!! danger "Importante"
    La segunda opción cambia qué comprobantes emite tu negocio y a nombre de quién. Confírmala con tu contador antes de habilitarla.

**Disparadores de emisión.** Definen en qué momento sale cada comprobante: el de la venta al finalizar la orden, y el de la comisión del local al finalizar la orden o cuando se le paga al dueño. Los alquileres tienen su propia estrategia, porque su total no es definitivo hasta la liquidación.

**Alícuotas de IVA.** Se define una alícuota por defecto para todo el catálogo y, si hace falta, excepciones por categoría. Agrega una fila solo para las categorías que tengan una alícuota distinta.

### Qué pasa después

Con la conexión activa, los comprobantes se emiten solos cuando se cumple el disparador que elegiste: no hay que hacer nada a mano en cada venta.

Lo que se emitió y lo que falló lo ves en **Dinero › Facturación**, con el estado de cada comprobante y el detalle del error cuando algo no sale. Mira [Errores de facturación y notas de crédito](../preguntas-frecuentes.md#errores-facturacion).

Los ajustes de disparadores aplican a las órdenes que se finalicen después de guardar: lo ya facturado no se vuelve a emitir y lo pendiente no se pierde.

!!! warning "Atención"
    Esta guía describe cómo se conecta el sistema, no qué te corresponde emitir. Las decisiones sobre régimen, alícuotas y forma de liquidar a tus proveedoras valídalas con tu contador.

<p class="doc-aliases" markdown>Términos relacionados: arca, afip, facturación electrónica argentina, certificado arca, csr, punto de venta, wsfe, cae, factura a b c, monotributo, responsable inscripto, alícuota de iva, cuenta de venta y líquido producto, cvylp, homologación, conectar afip</p>
