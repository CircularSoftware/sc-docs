---
title: Preguntas frecuentes
icon: material/help-circle
hide:
  - toc
---

# Preguntas frecuentes

Respuestas rápidas a las dudas más comunes. Tocá una pregunta para ver la respuesta.

## Catálogo

<a id="fotos-productos"></a>
??? question "No puedo subir las fotos de un producto"
    Las imágenes deben ser JPG, PNG o WEBP y medir al menos 500x500 píxeles.

    ### Si usás iPhone (fotos HEIC)

    1. Abrí Ajustes → Cámara → Formatos.
    1. Elegí "Más compatible" para que las fotos se guarden como JPEG.
    ### Pasos para cargarlas

    1. Entrá al producto ya creado.
    1. Subí las fotos (el sistema ajusta el tamaño para la web).
    1. Elegí la portada.
    !!! tip "Tip"
        Si una foto pesa mucho o tiene un formato no aceptado, dará error. Bajá la resolución o convertila a JPG.
    <p class="doc-aliases" markdown>Términos relacionados: no me deja subir la foto, qué formato, las fotos quedan en baja calidad, HEIC, se ven como iconos, no acepta la imagen</p>

<a id="estados-producto"></a>
??? question "Estados de un producto y por qué no se pueden eliminar"
    Los productos no se eliminan: se **pausan**. Así dejan de estar disponibles sin perder su historial.

    ### Pasos

    1. Entrá a Productos y buscá el producto.
    1. En la columna "Acciones" cambiá el estado a "Pausado".
    ### Estados posibles

    - **Pendiente de aprobación**: recién cargado, no se vende ni se muestra en la web.
    - **Disponible**: a la venta.
    - **Vendido**: se marca solo al concretar la venta. Si esa venta después se devuelve, el producto vuelve automáticamente a **Disponible** y se puede vender de nuevo (ver la guía *Devoluciones y cambiar el estado de una orden*).
    - **Pausado**: fuera de circulación.
    !!! tip "Tip"
        Si duplicaste un producto por error, pausalo. Para eliminarlo definitivamente, pasanos el código y lo damos de baja.
    <p class="doc-aliases" markdown>Términos relacionados: cómo elimino un producto, borrar una prenda cargada mal, subí dos veces lo mismo, quedan dobles, cómo pauso un producto, anular un código</p>

<a id="que-impresora-comprar"></a>
??? question "Qué impresora de etiquetas comprar para el local"
    El sistema genera el archivo con el nombre y el código de cada producto; la impresora la compra cada tienda. Aquí encuentras qué características debe cumplir para que funcione con el sistema, y cómo buscarla en el marketplace de tu país.

    Si ya tienes la impresora y lo que necesitas es imprimir, ve a [Imprimir etiquetas de productos](https://app.notion.com/p/3bf44bec05928164803fc3fddf5f89c9).

    ### Lo mínimo que debe cumplir

    No importa la marca. Lo que importa es que cumpla estas características.

    | Característica | Qué buscar | Por qué importa |
    | --- | --- | --- |
    | Tipo de impresora | De etiquetas, de escritorio (no una impresora de tickets ni una común de oficina) | Las de tickets imprimen en rollo continuo sin adhesivo y no sirven para etiquetar producto |
    | Tecnología | Transferencia térmica, idealmente que también haga térmica directa | La transferencia térmica usa una cinta y la etiqueta dura años. La térmica directa se borra con el calor, el sol y el roce |
    | Ancho de impresión | 4 pulgadas (entre 104 y 110 mm) | Te deja usar cualquier tamaño de etiqueta comercial y no te limita a futuro |
    | Resolución | 203 dpi como mínimo | Es suficiente para un código de barras en una etiqueta pequeña. 300 dpi solo hace falta en etiquetas muy pequeñas |
    | Conexión | USB. Ethernet (cable de red) si vas a imprimir desde más de una computadora | Con USB la impresora queda atada a una sola computadora |
    | Memoria | Cuanta más, mejor | Con poca memoria, mandar 300 etiquetas juntas puede trabar la impresión. Hay equipos de 8 MB y equipos de 128 MB en el mismo rango de precio |
    | Lenguaje de impresión | ZPL, EPL o TSPL (o que los emule) | Son los estándares del rubro: garantizan compatibilidad con el software de etiquetas |
    | Software incluido | Que permita importar un archivo con la lista de productos | Es el punto crítico. Lo explicamos abajo |
    | Servicio en tu país | Que la marca tenga distribuidor o servicio técnico local | El cabezal es la pieza que se gasta y es cara. Sin repuestos, la impresora se vuelve descartable |

    !!! tip "Tip"
        Marcas que cumplen y tienen presencia en la región: **Zebra**, **Honeywell**, **TSC**, **Godex**, **Argox**, **Bixolon** y **Elgin** (muy común en Brasil).

    ### El punto que más se pasa por alto: el software

    El sistema no imprime directo en la impresora. Genera un archivo con el nombre y el código de tus productos, y ese archivo se carga en el software de la impresora, que es donde se arma el diseño de la etiqueta.

    Aquí está el problema: **varios de los programas gratuitos que vienen con las impresoras no pueden importar archivos**. Sirven para diseñar una etiqueta y escribir el dato a mano, pero no para imprimir una lista.

    | Software | Con qué impresoras viene | ¿Importa una lista desde un archivo? |
    | --- | --- | --- |
    | BarTender UltraLite | Zebra, TSC, Honeywell y otras marcas, como versión gratuita | No. Imprimir desde hojas de cálculo, archivos de texto o bases de datos requiere pagar una edición superior |
    | ZebraDesigner Essentials | Zebra, versión gratuita | No. La conexión a Excel o CSV está solo en ZebraDesigner Professional, que es de pago |
    | GoLabel / GoLabel II | Godex, incluido y gratuito | Sí. Importa datos desde CSV, Excel o base de datos |

    !!! danger "Importante"
        Antes de comprar, hazle esta pregunta exacta al vendedor: **"¿el software que viene incluido permite imprimir una lista de etiquetas importando un archivo?"**. Si la respuesta es no, vas a tener que pagar una licencia aparte o elegir otro equipo. Es el costo oculto más común en esta compra.

    ### ¿Con cinta o sin cinta?

    Es la decisión que más cambia el resultado y la que más se subestima.

    |   | Térmica directa (sin cinta) | Transferencia térmica (con cinta) |
    | --- | --- | --- |
    | Cómo imprime | Quema un papel sensible al calor | Transfiere tinta desde una cinta al papel |
    | Cuánto dura la etiqueta | Meses. Se pone gris con el calor, el sol y el roce | Años |
    | Costo del equipo | Más bajo | Más alto |
    | Costo por etiqueta | Apenas más bajo | La cinta agrega muy poco: rinde miles de etiquetas por rollo |
    | Cuándo es suficiente | Etiquetas de envío, o producto que rota rápido | Producto que queda semanas o meses en exhibición |

    Para una tienda que etiqueta prendas que quedan colgadas en el local, la transferencia térmica es la opción correcta. El ahorro de la térmica directa está en el equipo, no en el uso diario.

    !!! tip "Tip"
        Los equipos que hacen las dos cosas te dejan empezar sin cinta y pasar a cinta más adelante, sin cambiar de impresora.

    ### Qué tipo de código de barras usar

    Cuando el software te pida elegir la simbología, usa **Code 128**.

    El otro código conocido, el EAN-13, es el de góndola de supermercado y requiere contratar un prefijo de empresa con GS1, que se paga y se renueva. Solo tiene sentido si tu producto se va a vender en el sistema de otro comercio. Code 128 no requiere registrarse con nadie, acepta letras y números, ocupa poco espacio y lo lee cualquier lector del mercado.

    ### Cómo buscarla en tu país

    Mercado Libre opera en la mayoría de los países de la región y suele ser el lugar más rápido para comparar. En varios mercados conviene además pedir cotización a un distribuidor local de Zebra o TSC: a veces el precio es parecido y el servicio posventa es mucho mejor.

    | País | Dónde buscar |
    | --- | --- |
    | Argentina | Mercado Libre Argentina, distribuidores locales de Zebra y TSC |
    | Uruguay | Mercado Libre Uruguay, distribuidores locales |
    | Paraguay | Mercado Libre Paraguay, importadores de equipamiento comercial |
    | Chile | Mercado Libre Chile, Falabella |
    | Colombia | Mercado Libre Colombia, Falabella |
    | Perú | Mercado Libre Perú, Falabella |
    | México | Mercado Libre México, Amazon México |
    | Brasil | Mercado Livre Brasil, Amazon Brasil |

    Qué escribir en el buscador:

    - `impresora de etiquetas térmica 4 pulgadas`
    - `impresora de código de barras transferencia térmica`
    - `etiquetadora código de barras`
    - En Brasil: `impressora de etiquetas transferência térmica`
    - O directo por marca y modelo: `Zebra ZD220`, `Honeywell PC42e`, `TSC TE200`, `Godex GE300`
    !!! warning "Atención"
        Las fichas técnicas de los marketplaces suelen estar mal cargadas. Es muy común encontrar equipos publicados como "transferencia térmica" cuya propia descripción aclara que no usan cinta. Lee siempre la descripción del vendedor, no solo el cuadro de características, y si hay contradicción pregunta antes de comprar.

    ### Cuánto cuesta

    Los precios cambian bastante entre países por impuestos de importación, así que tómalo como orientación y verifica en tu mercado:

    | Rango | Qué consigues |
    | --- | --- |
    | Desde unos USD 100 | Equipos genéricos de 4 pulgadas, solo térmica directa, USB, poca memoria y sin repuestos locales |
    | Entre USD 250 y 500 | Equipos de marca con transferencia térmica, el rango donde está la mayoría de las opciones recomendables |
    | Más de USD 900 | Equipos industriales, pensados para línea de producción. Sobredimensionados para una tienda |

    ### Qué más necesitas comprar

    - **Rollos de etiquetas autoadhesivas** del tamaño que uses. Los tamaños más comunes para etiquetar producto son 50 x 25 mm y 40 x 25 mm.
    - **Cinta (ribbon)**, si elegiste transferencia térmica. Tiene que coincidir en ancho con la etiqueta y en diámetro del tubo con la impresora.
    - **Un lector de código de barras USB**, del tipo que funciona como teclado: se conecta, escaneas y el código aparece donde esté el cursor, sin instalar nada. Para Code 128 es suficiente un lector 1D común.
    ### Qué pasa después

    Una vez que tienes la impresora conectada y su software instalado, el flujo queda así: descargas el archivo desde el botón **Etiquetas**, lo cargas en el software de la impresora y ajustas ahí el diseño y el tamaño. Cada etiqueta sale con el nombre del producto y con el mismo código con el que el sistema lo identifica.

    El diseño y el tamaño de la etiqueta se configuran una sola vez en el software de la impresora, no en el sistema. Después de eso, imprimir es solo repetir el paso de cargar el archivo.

    !!! tip "Tip"
        Si tienes dudas con la configuración de tu impresora, escríbenos y te ayudamos.
    <p class="doc-aliases" markdown>Términos relacionados: qué impresora necesito, cuál impresora me sirve, comprar impresora de etiquetas, impresora de códigos de barra, qué impresora recomiendan, dónde compro la impresora, impresora térmica para etiquetas, características de la impresora, la etiqueta se borra</p>

## Cuenta

<a id="proveedoras-comisiones-web"></a>
??? question "Que tus proveedoras vean sus comisiones (activación)"
    Tus proveedoras pueden registrarse en la web para ver las comisiones que van generando.

    ### Pasos

    1. La proveedora entra a la web y crea su cuenta con su correo.
    1. Confirma la cuenta con el enlace que le llega por mail (paso indispensable; suele caer en Spam).
    1. Ya activa, ingresa a su perfil y ve sus comisiones.
    !!! tip "Tip"
        Si figura como "pendiente de activación", reenviale el mail de activación desde la sección Clientes.

    Para ver cómo se ve del lado de la persona, qué encuentra en **mi cuenta** y qué revisar cuando las comisiones le figuran vacías, mirá la guía *Sección web para proveedores*.
    <p class="doc-aliases" markdown>Términos relacionados: mi proveedora no puede entrar, no le llega el mail de activación, pendiente de activación, ver sus comisiones, la cuenta no puede ser confirmada</p>

<a id="email-obligatorio-cliente"></a>
??? question "El email es obligatorio al crear un cliente"
    Al crear un cliente el correo es obligatorio, porque por ahí viajan las ventas y comisiones.

    ### Si no tenés el correo real

    1. Cargá un correo ficticio (por ejemplo nombre + gmail).
    1. Activá la opción "desactivar envío de mails" en la ficha del cliente.
    1. Para el identificador podés usar el tipo "Otros" con un código interno.
    !!! tip "Tip"
        Cuando consigas el correo real, cargalo para que la persona reciba sus comprobantes y avisos.

    !!! video "Video"
        Ver el video tutorial: [https://youtu.be/Y-75z5Cvny4](https://youtu.be/Y-75z5Cvny4)
    <p class="doc-aliases" markdown>Términos relacionados: el mail es obligatorio, no tengo el correo de la clienta, nos manejamos por whatsapp, puedo inventar un correo, desactivar envío de mails</p>

## Facturación

<a id="errores-facturacion"></a>
??? question "Errores de facturación y notas de crédito"
    Cuando una orden queda con "facturación electrónica: Error" casi siempre es un problema de conexión con Biller o de datos fiscales.

    ### Pasos

    1. Abrí la orden para ver el detalle del error.
    1. Verificá que el RUT del cliente/proveedor esté bien cargado (si tributa IVA, el RUT es obligatorio).
    1. Reprocesá las órdenes con error o escribinos para reprocesarlas.
    !!! tip "Tip"
        Las devoluciones generan una nota de crédito automática, que debe referenciar el comprobante original.
    <p class="doc-aliases" markdown>Términos relacionados: facturación electrónica error, no me sale la factura para imprimir, notas de crédito de más, no aparece el comprobante, cuenta ajena con IVA</p>

## Primeros pasos

<a id="errores-importacion"></a>
??? question "Errores al importar la planilla masiva"
    Si la subida falla, el sistema te devuelve la misma planilla con una hoja extra que indica el error y la fila exacta.

    ### Causas más comunes

    - Usar una planilla vieja: descargá siempre la versión actualizada.
    - Una categoría que no existe: elegí una categoría válida del desplegable.
    - Un proveedor que todavía no fue cargado: cargá primero los clientes.
    - Tildes o caracteres especiales mal codificados en los nombres.
    ### Pasos

    1. Abrí la planilla de errores que devuelve el sistema.
    1. Corregí las filas indicadas.
    1. Volvé a subir la planilla.
    <p class="doc-aliases" markdown>Términos relacionados: subida fallida, generic error, me da error el documento, proveedor original incorrecto, la categoría no existe, caracteres raros por las tildes</p>

## Stock

<a id="varias-unidades"></a>
??? question "Cargar varias unidades iguales de un producto"
    El sistema maneja productos únicos (un código por prenda), algo pensado para segunda mano. Para artículos repetidos usá las copias.

    ### Pasos

    1. Cargá un producto como de costumbre.
    1. Indicá la cantidad de copias a generar.
    1. El sistema crea varios artículos individuales, cada uno con su propio código.
    !!! tip "Tip"
        Cada copia es un producto independiente (se vende y se etiqueta por separado).
    <p class="doc-aliases" markdown>Términos relacionados: tengo 12 iguales, cómo cargo varias unidades, vender por cantidad, tengo que crear 12 productos, poner la cantidad que hay, 5 del mismo</p>

<a id="como-funciona-el-stock"></a>
??? question "Cómo funciona el stock"
    En el sistema cada producto es una unidad física, no una cantidad. Entender esto evita confusiones.

    ### La idea principal

    - Cada prenda o artículo se carga como un producto con su propio ID.
    - No hay un campo "cantidad en stock" por talle o color: el talle y el color son datos del producto, no unidades separadas.
    - Si tenés varias unidades iguales, creás copias (ver "Cargar varias unidades iguales de un producto").
    ### Cómo baja el stock

    - Un producto deja de estar disponible cuando se vende o cuando lo pausás.
    - Al venderse, pasa a "Vendido" y ya no aparece para vender ni en la web.
    - Para sacarlo de la venta sin venderlo, cambialo a "Pausado".
    !!! tip "Tip"
        El "stock" es la cantidad de productos "Disponibles" que tenés cargados. Para reponer, cargás nuevas unidades o copias.
    <p class="doc-aliases" markdown>Términos relacionados: no se actualiza el stock, cómo cargo cantidades, cuántas unidades tengo, control de inventario, el stock no baja, no me aparece la cantidad</p>

## Ventas

<a id="finalizar-ordenes"></a>
??? question "Finalizar órdenes para habilitar las comisiones"
    Las comisiones de las proveedoras recién quedan disponibles para pagar cuando la orden está **finalizada**.

    ### Pasos (cierre de mes)

    1. Entrá a Órdenes.
    1. Filtrá por fecha y local.
    1. Cambiá a "Finalizada" cada orden ya entregada.
    !!! tip "Tip"
        Hasta que la orden no queda finalizada, su comisión no aparece en Pagos → Comisiones.
    <p class="doc-aliases" markdown>Términos relacionados: las comisiones no aparecen, no me figura la comisión, hasta que no entrego no la pasa, cerrar el mes, marcar como finalizada</p>
