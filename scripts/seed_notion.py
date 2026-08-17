#!/usr/bin/env python3
"""Seed the Notion `Docs` database with help articles mined from real support chats.

Articles are created with Status = Draft (NOT Published) so they land in Notion for human
review and never reach the live site until someone flips them to Published. Idempotent:
skips any slug that already exists. All content is Spanish; aliases are real (anonymized)
customer phrasings. A runtime scrub strips emails/phones as a backstop.

Run:  ./.venv/bin/python scripts/seed_notion.py            (create Drafts, skip existing)
      ./.venv/bin/python scripts/seed_notion.py --dry-run  (print plan, write nothing)
"""
from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
NOTION_VERSION = "2022-06-28"
DEFAULT_DB_ID = "REDACTED-NOTION-DB-ID"


def load_env() -> None:
    p = ROOT / ".env"
    if p.exists():
        for line in p.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


# --- Anonymization backstop -----------------------------------------------------------
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_RE = re.compile(r"\+?\d[\d\s().-]{6,}\d")


def scrub(text: str) -> str:
    text = EMAIL_RE.sub("[correo]", text)
    text = PHONE_RE.sub("[teléfono]", text)
    return text


# --- Tiny markdown -> Notion blocks ---------------------------------------------------
def rt(content: str, link: str | None = None) -> dict:
    o = {"type": "text", "text": {"content": content}}
    if link:
        o["text"]["link"] = {"url": link}
    return o


def md_to_blocks(md: str) -> list[dict]:
    blocks: list[dict] = []
    for raw in md.strip("\n").split("\n"):
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("## "):
            blocks.append({"type": "heading_2", "heading_2": {"rich_text": [rt(line[3:])]}})
        elif re.match(r"^\d+\.\s", line):
            blocks.append({"type": "numbered_list_item",
                           "numbered_list_item": {"rich_text": [rt(re.sub(r'^\d+\.\s', '', line))]}})
        elif line.startswith("- "):
            blocks.append({"type": "bulleted_list_item",
                           "bulleted_list_item": {"rich_text": [rt(line[2:])]}})
        elif line.startswith("> "):
            blocks.append({"type": "callout",
                           "callout": {"icon": {"emoji": "💡"}, "rich_text": [rt(line[2:])]}})
        else:
            blocks.append({"type": "paragraph", "paragraph": {"rich_text": [rt(line)]}})
    return blocks


def video_block(url: str) -> dict:
    return {"type": "callout", "callout": {"icon": {"emoji": "📹"},
            "rich_text": [rt("Ver el video tutorial: "), rt(url, link=url)]}}


# --- Articles (title, slug, category, order, aliases, video, body) --------------------
A = []
def art(title, slug, category, order, aliases, body, video=None):
    A.append(dict(title=title, slug=slug, category=category, order=order,
                  aliases=aliases, body=body, video=video))

# Articles that answer a specific recurring question / explain a behavior or limitation
# (the kind that can be retired once a bug is fixed) are FAQ; task walkthroughs are Guía.
FAQ_SLUGS = {
    "errores-importacion", "estados-producto", "fotos-productos", "varias-unidades",
    "finalizar-ordenes", "errores-facturacion", "email-obligatorio-cliente",
    "proveedoras-comisiones-web",
}
def _classify():
    for a in A:
        a["type"] = "FAQ" if a["slug"] in FAQ_SLUGS else "Guía"


# ===== Primeros pasos =====
art("Primer acceso: usuario, contraseña y panel general", "primer-acceso",
    "Primeros pasos", 10,
    "no puedo entrar, no me llegó el usuario, cómo accedo al sistema, cambiar contraseña, dónde están los videos, ya puedo usar el sistema",
    """Cuando damos de alta tu cuenta te enviamos el enlace a tu panel (termina en **/admin**), junto con un usuario y una contraseña.

## Pasos
1. Entrá al enlace que termina en /admin.
2. Ingresá con tu usuario (tu correo completo) y la contraseña que te enviamos.
3. El primer paso recomendado es cambiar la contraseña.
4. Desde el menú lateral accedés a: inicio, nueva venta, órdenes, pagos, clientes, productos, vales y mi sitio web.

> Si tenés varios locales, usá "Cambiar de local" abajo a la izquierda para no mezclar sucursales.""",
    "https://youtu.be/AeVLgKNBVMQ")

art("Cargar clientes y productos de forma masiva (planilla)", "carga-masiva",
    "Primeros pasos", 20,
    "importación masiva, subir excel, cargar muchos productos, migrar stock, planilla de migración, cómo paso todos los productos, tengo 500 proveedoras",
    """Para migrar tu stock y tu base de contactos existente usamos una planilla de Excel.

## Pasos
1. Ingresá al menú de Importación Masiva y descargá la planilla.
2. Completá primero la hoja de CLIENTES (cada producto necesita un dueño/proveedor ya cargado).
3. Luego completá la hoja de PRODUCTOS.
4. Las columnas obligatorias están pintadas de color.
5. Subí la planilla completa.

> La primera migración la podemos hacer nosotros con tu planilla. Las fotos se cargan después, en una segunda instancia.""")

art("Errores al importar la planilla masiva", "errores-importacion",
    "Primeros pasos", 30,
    "subida fallida, generic error, me da error el documento, proveedor original incorrecto, la categoría no existe, caracteres raros por las tildes",
    """Si la subida falla, el sistema te devuelve la misma planilla con una hoja extra que indica el error y la fila exacta.

## Causas más comunes
- Usar una planilla vieja: descargá siempre la versión actualizada.
- Una categoría que no existe: elegí una categoría válida del desplegable.
- Un proveedor que todavía no fue cargado: cargá primero los clientes.
- Tildes o caracteres especiales mal codificados en los nombres.

## Pasos
1. Abrí la planilla de errores que devuelve el sistema.
2. Corregí las filas indicadas.
3. Volvé a subir la planilla.""")

# ===== Catálogo =====
art("Cargar un producto nuevo", "cargar-producto",
    "Catálogo", 10,
    "ingresar una prenda, dar de alta un producto, cargar mercadería, qué datos van, el precio es obligatorio, pendiente de aprobación",
    """Los productos se cargan desde el menú **Productos → Nuevo producto**.

## Pasos
1. Entrá a Productos y tocá "Nuevo producto".
2. Completá nombre, precio y los datos de categorización (categoría, talle, género según corresponda).
3. Asigná el proveedor/dueño de la prenda.
4. Guardá.

> El precio siempre es obligatorio. Los productos nuevos entran en estado "Pendiente de aprobación": no se muestran en la tienda ni se pueden vender hasta pasarlos a "Disponible".""",
    "https://youtu.be/bs36QKdaB3k")

art("No puedo subir las fotos de un producto", "fotos-productos",
    "Catálogo", 20,
    "no me deja subir la foto, qué formato, las fotos quedan en baja calidad, HEIC, se ven como iconos, no acepta la imagen",
    """Las imágenes deben ser JPG, PNG o WEBP y medir al menos 500x500 píxeles.

## Si usás iPhone (fotos HEIC)
1. Abrí Ajustes → Cámara → Formatos.
2. Elegí "Más compatible" para que las fotos se guarden como JPEG.

## Pasos para cargarlas
1. Entrá al producto ya creado.
2. Subí las fotos (el sistema ajusta el tamaño para la web).
3. Elegí la portada.

> Si una foto pesa mucho o tiene un formato no aceptado, dará error. Bajá la resolución o convertila a JPG.""")

art("Agregar marcas, talles y otros atributos", "atributos",
    "Catálogo", 30,
    "no aparece la marca, falta el talle, no me deja escribir el material, talles americanos, agregar color, solo hay menú desplegable",
    """Los atributos (marca, talle, color, material, etc.) se eligen de un desplegable. Para sumar un valor nuevo:

## Pasos
1. Entrá a **Catálogo → Atributos**.
2. Elegí el atributo (por ejemplo Marca, Talle o Material).
3. Tocá "Añadir valor" y escribí el nuevo valor.
4. Ese valor ya aparece en el desplegable al cargar productos.

> Si un valor te aparece bloqueado o no lo podés agregar, envianos el listado y lo cargamos.""")

art("Agregar o modificar categorías y subcategorías", "categorias",
    "Catálogo", 40,
    "agregar una categoría, falta zapatos, unificar categorías repetidas, cambiar el nombre de una categoría, un producto en más de una categoría",
    """Las categorías y subcategorías organizan tu catálogo y tu tienda online.

## Pasos
1. Armá el listado de categorías y subcategorías que necesitás (o los cambios a hacer).
2. Envíanoslo y lo aplicamos en el sistema.

> Por el momento las altas y cambios de categorías los aplica el equipo. Estamos trabajando para que puedas editarlas vos directamente.""")

art("Estados de un producto y por qué no se pueden eliminar", "estados-producto",
    "Catálogo", 50,
    "cómo elimino un producto, borrar una prenda cargada mal, subí dos veces lo mismo, quedan dobles, cómo pauso un producto, anular un código",
    """Los productos no se eliminan: se **pausan**. Así dejan de estar disponibles sin perder su historial.

## Pasos
1. Entrá a Productos y buscá el producto.
2. En la columna "Acciones" cambiá el estado a "Pausado".

## Estados posibles
- **Pendiente de aprobación**: recién cargado, no se vende ni se muestra en la web.
- **Disponible**: a la venta.
- **Vendido**: se marca solo al concretar la venta.
- **Pausado**: fuera de circulación.

> Si duplicaste un producto por error, pausalo. Para eliminarlo definitivamente, pasanos el código y lo damos de baja.""")

art("Imprimir etiquetas de productos", "imprimir-etiquetas",
    "Catálogo", 60,
    "generar etiquetas, imprimir el código de la prenda, configurar la impresora, me sale cortado, descargar etiquetas",
    """Podés generar un archivo con el nombre y el código de tus productos para imprimir etiquetas.

## Pasos
1. Entrá a Productos (o al proveedor, en su pestaña Productos).
2. Tocá el botón "Etiquetas" para descargar el archivo.
3. Cargá ese archivo en el software de tu impresora de etiquetas.

> El diseño y el ajuste del tamaño de la etiqueta se configuran en el software de la impresora, no en el sistema.""",
    "https://youtu.be/hJ0d2pn555o")

# ===== Stock =====
art("Cargar varias unidades iguales de un producto", "varias-unidades",
    "Stock", 10,
    "tengo 12 iguales, cómo cargo varias unidades, vender por cantidad, tengo que crear 12 productos, poner la cantidad que hay, 5 del mismo",
    """El sistema maneja productos únicos (un código por prenda), algo pensado para segunda mano. Para artículos repetidos usá las copias.

## Pasos
1. Cargá un producto como de costumbre.
2. Indicá la cantidad de copias a generar.
3. El sistema crea varios artículos individuales, cada uno con su propio código.

> Cada copia es un producto independiente (se vende y se etiqueta por separado).""")

# ===== Ventas =====
art("Registrar una nueva venta", "nueva-venta",
    "Ventas", 10,
    "cómo hago una venta, no me deja hacer la orden, consumidor final, buscar el producto por código, siempre tengo que agregar al cliente",
    """Las ventas se hacen desde **Nueva venta** en el menú lateral.

## Pasos
1. Tocá "Nueva venta".
2. Elegí el cliente. Si no querés registrar a la persona, usá un cliente "Consumidor Final".
3. Agregá los productos buscándolos por nombre o código.
4. Confirmá la entrega y guardá.

> Se puede buscar por código nuevo y por código alternativo (respetando mayúsculas). Los campos con asterisco rojo son obligatorios.""",
    "https://youtu.be/PBsSGpr0zOY")

art("Aplicar descuentos en una venta", "descuentos-venta",
    "Ventas", 20,
    "cómo aplico un descuento, descuento a toda la orden, descuento a una sola prenda, una en sale y otra no, excepciones en una campaña",
    """Podés aplicar descuentos en dos niveles dentro de una orden de venta.

## A toda la orden
1. En la orden, abrí la sección "Descuentos".
2. Elegí el tipo (por ejemplo variable en %) y el valor.

## A un solo producto
1. Tocá el lápiz sobre el producto dentro de la orden.
2. Cargá el descuento solo para ese ítem.

> Un producto también puede tener un descuento asignado desde "editar producto" (por ejemplo para SALE u Outlet).""",
    "https://youtu.be/EXqYtoTkk4Q")

art("Cobrar la bolsa y el envío (adicionales)", "adicionales-bolsa-envio",
    "Ventas", 30,
    "agregar la bolsa a la venta, cobrar el envío, adicionales no me aparece, sumar el costo de la bolsa, envío editable",
    """La bolsa y el envío se agregan como "Adicionales" dentro de la orden de venta.

## Pasos
1. En la nueva orden, buscá la sección "Adicionales".
2. Elegí la bolsa o el envío.
3. Editá el monto si hace falta.
4. Tocá "Agregar adicionales".

> Si no te aparece la opción, escribinos para dejar cargados los adicionales (bolsa y envío) de tu local.""")

art("Crear y usar vales (cambios, señas y devoluciones)", "vales",
    "Ventas", 40,
    "no me reconoce el vale, no genera el ID del vale, los vales no funcionan, la diferencia a favor, hice un vale por una seña",
    """El vale es un medio de pago más. Se usa para cambios, señas y devoluciones.

## Pasos
1. Al hacer una devolución o recibir una seña, el sistema genera un vale.
2. Para usarlo, agregalo como forma de pago dentro de una orden de venta.
3. Si el vale se usa por un monto menor, el sistema genera otro vale por la diferencia.

> El vale se asocia a una orden (no se canjea suelto). Si no lo encuentra el buscador, verificá que tenga asignado el local correcto.""")

art("Devoluciones y cambiar el estado de una orden", "devoluciones-estados-orden",
    "Ventas", 50,
    "cómo cancelo una venta, hacer un cambio, no me deja devolver, devuelto al cliente, revertir una orden finalizada",
    """Para deshacer o cambiar una venta se usa la devolución de productos.

## Pasos
1. Entrá a la orden.
2. Elegí "Devolución de productos" (total o de a un producto).
3. Las prendas vuelven a "Disponible" y se genera un vale al cliente.
4. Si necesitás cancelar la orden, hacelo luego de la devolución.

> El estado "Devuelto al cliente" es final: no se puede volver a "Disponible" desde el panel. Si te pasó por error, escribinos y lo corregimos.""")

art("Finalizar órdenes para habilitar las comisiones", "finalizar-ordenes",
    "Ventas", 60,
    "las comisiones no aparecen, no me figura la comisión, hasta que no entrego no la pasa, cerrar el mes, marcar como finalizada",
    """Las comisiones de las proveedoras recién quedan disponibles para pagar cuando la orden está **finalizada**.

## Pasos (cierre de mes)
1. Entrá a Órdenes.
2. Filtrá por fecha y local.
3. Cambiá a "Finalizada" cada orden ya entregada.

> Hasta que la orden no queda finalizada, su comisión no aparece en Pagos → Comisiones.""")

art("Movimiento de caja: saldo inicial y cierre", "movimiento-caja",
    "Ventas", 70,
    "abrir caja, cerrar caja, ingresar el efectivo inicial, el saldo no coincide, retirar de caja, ver el total de ventas del día",
    """El movimiento de caja concilia el dinero físico con el sistema.

## Cargar el saldo inicial
1. Entrá a **Pagos → Movimiento de caja**.
2. Agregá un movimiento de ingreso con el concepto "saldo inicial".

## Notas importantes
- Los medios que no son efectivo (débito, transferencia, vales) no restan del saldo en caja, porque el saldo refleja el efectivo físico.
- Para sumar esos medios, descargá el Excel filtrando por medio de pago.

> El total facturado de un período se ve en Órdenes, filtrando por fechas y descargando el Excel.""")

# ===== Pagos =====
art("Pagar comisiones a proveedoras", "pagar-comisiones",
    "Pagos", 10,
    "cómo pago las comisiones, comisiones a abonar, dónde veo lo que tengo que pagar, registrar el pago a la proveedora, comisiones pendientes",
    """Las comisiones se gestionan en **Pagos → Comisiones**.

## Estados de una comisión
- **Pendiente**: generada por una venta, todavía no llegó su fecha de pago.
- **Para abonar**: lista para pagar.
- **Vencida**: no se cobró dentro del plazo.
- **Cancelada**: la venta se devolvió/canceló.
- **Abonada**: ya se pagó.

## Pasos
1. Entrá a la proveedora (muestra su comisión pendiente).
2. Tocá "Pagar" y elegí la forma (por ejemplo Transferencia).

> El día de habilitación del pago de comisiones es configurable; el cambio aplica al mes siguiente.""",
    "https://youtu.be/F0PAr31s0I0")

art("Configurar comisiones: porcentaje, monto a recuperar y decimales", "configurar-comisiones",
    "Pagos", 20,
    "qué es el monto a recuperar, el porcentaje de comisión, comisión especial, no me deja poner decimales, comisión por defecto",
    """En la ficha del cliente/proveedor se define cuánto se le paga por cada venta.

## Conceptos
- **Comisión (%)**: el porcentaje que se le paga al proveedor.
- **Monto a recuperar**: un monto fijo (por ejemplo lo que costó el producto), en lugar de un porcentaje.
- **Comisión especial**: un porcentaje distinto para un producto puntual.

> Las comisiones admiten decimales (por ejemplo 81,7%). El monto de una comisión ya generada no se edita, pero sí su estado.""")

art("Conectar Mercado Pago a la tienda", "mercado-pago",
    "Pagos", 30,
    "token de mercado pago, APP_USR, no encuentro el token, integrar mercado pago al checkout, cobrar online, credenciales de MP",
    """Para cobrar en tu tienda online necesitás conectar Mercado Pago con su Access Token.

## Pasos
1. Entrá a tu cuenta de Mercado Pago → sección de desarrolladores.
2. Creá la aplicación y copiá el **Access Token de producción** (empieza con APP_USR-...).
3. Envíanos ese token (o cargalo en el panel) para completar la integración.

> Conviene asociar una única cuenta de Mercado Pago a la web para poder conciliar por local. Hacemos una compra de prueba para confirmar que quedó funcionando.""")

# ===== Facturación =====
art("Conectar la facturación electrónica (Biller)", "conectar-biller",
    "Facturación", 10,
    "cómo integro Biller, facturación electrónica, qué es Biller, access token de biller, id de sucursal, empezar a facturar",
    """La facturación electrónica se integra con Biller para que se generen facturas automáticamente al vender.

## Pasos
1. En tu cuenta de Biller, generá el API token e identificá tu sucursal.
2. Envíanos: token, ID de sucursal, RUT y tipo de tributación (IVA).
3. Lo cargamos en el sistema.

> Requiere el plan de Biller con acceso a la API. Una vez conectado, aparece el botón de facturación electrónica al crear una orden.""")

art("Cómo se factura al vender y al pagar comisiones", "como-se-factura",
    "Facturación", 20,
    "cómo figura en biller una venta, cómo se factura la comisión, cuenta ajena, qué se factura al pagar al proveedor, diferencia con biller",
    """El sistema emite comprobantes en Biller en dos momentos.

## Al vender
Se emite el comprobante de la venta (e-Ticket), incluyendo las prendas por cuenta ajena de tus proveedores.

## Al pagar comisiones
Se genera un comprobante por tu ganancia, que es la diferencia entre el precio de venta y la comisión que le pagás al proveedor (con IVA incluido).

> Si el total del sistema no coincide con Biller, acotá por rango de fechas para ubicar órdenes sin comprobante o con error.""",
    "https://youtu.be/fY3mX2gMoPU")

art("Errores de facturación y notas de crédito", "errores-facturacion",
    "Facturación", 30,
    "facturación electrónica error, no me sale la factura para imprimir, notas de crédito de más, no aparece el comprobante, cuenta ajena con IVA",
    """Cuando una orden queda con "facturación electrónica: Error" casi siempre es un problema de conexión con Biller o de datos fiscales.

## Pasos
1. Abrí la orden para ver el detalle del error.
2. Verificá que el RUT del cliente/proveedor esté bien cargado (si tributa IVA, el RUT es obligatorio).
3. Reprocesá las órdenes con error o escribinos para reprocesarlas.

> Las devoluciones generan una nota de crédito automática, que debe referenciar el comprobante original.""")

# ===== Tienda online =====
art("Publicar productos en la tienda online", "publicar-en-web",
    "Tienda online", 10,
    "no aparecen en la web, subí productos y no se ven, activar el canal web, publicar en la tienda, aparece en el admin pero no en la web",
    """Un producto se muestra en tu tienda online solo si tiene activado el **canal web**.

## Pasos
1. Entrá al producto.
2. Activá el botón de canal "web".
3. Verificá que tenga al menos una foto y que esté en estado "Disponible".

> Recomendación: activá el canal web recién cuando el producto ya tiene foto. Si no aparece en una categoría, revisá en qué categoría/subcategoría quedó cargado.""")

art("Editar tu web: banners, textos y botón de WhatsApp", "editar-mi-web",
    "Tienda online", 20,
    "cambiar los banners, editar la página, cambiar el logo, poner el botón de whatsapp, formato de los banners, textos de la web",
    """El contenido de tu tienda se edita desde **Mi sitio web → Editar mi web**.

## Qué podés editar
- Página principal: banners y secciones de imagen + texto.
- Pie de página: botón de WhatsApp y datos de contacto.
- Páginas institucionales: preguntas frecuentes y términos y condiciones.

> Usá los banners con las medidas indicadas para que se vean bien. Si necesitás una medida, escribinos.""")

art("Conectar tu propio dominio", "conectar-dominio",
    "Tienda online", 30,
    "conectar mi dominio, comprarlo en godaddy, apuntar el dominio, a dónde apunto los DNS, delegar el dominio, sacar el softwarecircular.com.uy",
    """Tu tienda arranca en un subdominio nuestro, y podés conectar tu dominio propio.

## Pasos
1. Comprá tu dominio (por ejemplo en GoDaddy).
2. Escribinos dónde está alojado.
3. Te pasamos los servidores/registros DNS a los que apuntar (o coordinamos el acceso para configurarlo).

> El cambio puede tardar unos días en propagarse; durante ese tiempo la web puede no estar disponible.""")

art("Configurar envíos y medios de pago en la web", "envios-y-pagos-web",
    "Tienda online", 40,
    "configurar los envíos, opciones de envío, costo de envío, retiro en local, no se actualiza el total, eliminar pago en el local",
    """Las opciones de envío y de pago de tu tienda se configuran desde Mi sitio web.

## Pasos
1. Entrá a **Mi sitio web → Editar mi web → General**.
2. Agregá o editá las opciones de envío y sus costos.
3. Definí los medios de pago disponibles.

> Si el total no refleja el envío elegido, puede haber un costo por defecto viejo cargado. Escribinos para revisarlo.""")

art("Crear promociones y sección Outlet", "promociones-outlet",
    "Tienda online", 50,
    "poner un descuento en la web, cómo hago el outlet, armar una promoción, cupones, campañas, precio tachado",
    """En la web podés armar promociones de tipo Campaña y de tipo Cupón.

## Pasos
1. Entrá a la sección Promociones del menú.
2. Elegí Campaña (descuento general) o Cupón (código).
3. Definí el descuento y las fechas.

> Los productos con descuento aplicado desde "editar producto" aparecen en la sección Outlet.""")

# ===== Cuenta =====
art("Que tus proveedoras vean sus comisiones (activación)", "proveedoras-comisiones-web",
    "Cuenta", 10,
    "mi proveedora no puede entrar, no le llega el mail de activación, pendiente de activación, ver sus comisiones, la cuenta no puede ser confirmada",
    """Tus proveedoras pueden registrarse en la web para ver las comisiones que van generando.

## Pasos
1. La proveedora entra a la web y crea su cuenta con su correo.
2. Confirma la cuenta con el enlace que le llega por mail (paso indispensable; suele caer en Spam).
3. Ya activa, ingresa a su perfil y ve sus comisiones.

> Si figura como "pendiente de activación", reenviale el mail de activación desde la sección Clientes.""")

art("El email es obligatorio al crear un cliente", "email-obligatorio-cliente",
    "Cuenta", 20,
    "el mail es obligatorio, no tengo el correo de la clienta, nos manejamos por whatsapp, puedo inventar un correo, desactivar envío de mails",
    """Al crear un cliente el correo es obligatorio, porque por ahí viajan las ventas y comisiones.

## Si no tenés el correo real
1. Cargá un correo ficticio (por ejemplo nombre + gmail).
2. Activá la opción "desactivar envío de mails" en la ficha del cliente.
3. Para el identificador podés usar el tipo "Otros" con un código interno.

> Cuando consigas el correo real, cargalo para que la persona reciba sus comprobantes y avisos.""",
    "https://youtu.be/Y-75z5Cvny4")

art("Usuarios y roles (Administrador, Encargado, Empleado)", "usuarios-roles",
    "Cuenta", 30,
    "crear un usuario, agregar a alguien del equipo, tipos de usuario, permisos, que solo cargue productos, no puedo entrar con el administrador",
    """Podés crear usuarios para tu equipo con distinto nivel de acceso, sin costo adicional.

## Pasos
1. Entrá al menú Usuarios.
2. Tocá "Nuevo usuario".
3. Asigná el rol según lo que tenga que hacer.

## Roles
- **Administrador**: acceso total.
- **Encargado**: opera ventas, vales y descuentos.
- **Empleado**: acceso acotado (por ejemplo solo cargar productos).

> Si tenés varios locales, creá un administrador por local para no mezclar sucursales.""")


# --- Create in Notion -----------------------------------------------------------------
def main() -> None:
    dry = "--dry-run" in sys.argv
    update_types = "--update-types" in sys.argv
    _classify()
    load_env()
    token = os.environ.get("NOTION_API_TOKEN") or os.environ.get("NOTION_TOKEN")
    if not token:
        sys.exit("NOTION_API_TOKEN not set")
    db = os.environ.get("NOTION_DATABASE_ID", DEFAULT_DB_ID)
    if len(re.sub(r"[^0-9a-f]", "", db)) == 32 and "-" not in db:
        s = re.sub(r"[^0-9a-f]", "", db)
        db = f"{s[0:8]}-{s[8:12]}-{s[12:16]}-{s[16:20]}-{s[20:32]}"
    h = {"Authorization": f"Bearer {token}", "Notion-Version": NOTION_VERSION,
         "Content-Type": "application/json"}

    # Existing slug -> page_id (dedup + type updates)
    slug_to_id: dict[str, str] = {}
    cursor = None
    while not dry:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        r = requests.post(f"https://api.notion.com/v1/databases/{db}/query", headers=h, json=body, timeout=30)
        r.raise_for_status()
        d = r.json()
        for pg in d["results"]:
            sp = pg["properties"].get("Slug", {}).get("rich_text", [])
            if sp:
                slug_to_id["".join(t["plain_text"] for t in sp)] = pg["id"]
        if not d.get("has_more"):
            break
        cursor = d["next_cursor"]
    existing = set(slug_to_id)

    # --update-types: PATCH Type on already-created pages, then stop.
    if update_types:
        n = 0
        for a in A:
            pid = slug_to_id.get(a["slug"])
            if not pid:
                continue
            r = requests.patch(f"https://api.notion.com/v1/pages/{pid}", headers=h,
                               json={"properties": {"Type": {"select": {"name": a["type"]}}}}, timeout=30)
            print(f"  {'ok ' if r.status_code == 200 else 'FAIL'} {a['type']:5} · {a['slug']}")
            n += r.status_code == 200
            time.sleep(0.34)
        print(f"\nUpdated Type on {n} article(s).")
        return

    # --publish-all: flip every article to Published, then stop.
    if "--publish-all" in sys.argv:
        n = 0
        for slug, pid in slug_to_id.items():
            r = requests.patch(f"https://api.notion.com/v1/pages/{pid}", headers=h,
                               json={"properties": {"Status": {"select": {"name": "Published"}}}}, timeout=30)
            print(f"  {'ok  ' if r.status_code == 200 else 'FAIL'} {slug}")
            n += r.status_code == 200
            time.sleep(0.34)
        print(f"\nPublished {n} article(s).")
        return

    created = skipped = 0
    for a in A:
        if a["slug"] in existing:
            print(f"  skip (exists): {a['slug']}")
            skipped += 1
            continue
        aliases = scrub(a["aliases"])
        blocks = md_to_blocks(scrub(a["body"]))
        if a["video"]:
            blocks.append(video_block(a["video"]))
        payload = {
            "parent": {"database_id": db},
            "properties": {
                "Name": {"title": [rt(a["title"])]},
                "Slug": {"rich_text": [rt(a["slug"])]},
                "Category": {"select": {"name": a["category"]}},
                "Order": {"number": a["order"]},
                "Status": {"select": {"name": "Draft"}},
                "Type": {"select": {"name": a["type"]}},
                "Aliases": {"rich_text": [rt(aliases)]},
            },
            "children": blocks,
        }
        if dry:
            print(f"  [dry] {a['category']:14} · {a['slug']}  ({len(blocks)} blocks, {len(aliases)} alias chars)")
            created += 1
            continue
        r = requests.post("https://api.notion.com/v1/pages", headers=h, json=payload, timeout=30)
        if r.status_code == 200:
            print(f"  created: {a['category']:14} · {a['slug']}")
            created += 1
        else:
            print(f"  FAIL {a['slug']}: {r.status_code} {r.text[:200]}")
        time.sleep(0.34)  # ~3 req/s

    print(f"\n{'[dry-run] would create' if dry else 'Created'} {created} article(s); skipped {skipped} existing.")
    print("All created as Status=Draft — review in Notion, then flip to Published to go live.")


if __name__ == "__main__":
    main()
