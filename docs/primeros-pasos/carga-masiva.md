---
title: Cargar clientes y productos de forma masiva (planilla)
slug: carga-masiva
order: 20
type: Guía
aliases: importación masiva, subir excel, cargar muchos productos, migrar stock, planilla
  de migración, cómo paso todos los productos, tengo 500 proveedoras
---

# Cargar clientes y productos de forma masiva (planilla)

Cuando tenés que cargar muchos clientes o muchas prendas de una vez, no hace falta hacerlo uno por uno. La importación masiva funciona con plantillas de Excel: descargás la plantilla, la completás y la subís.

Entrá a **importación masiva** en el menú lateral.

![Menú lateral con importación masiva](/assets/carga-masiva/5e5b3a976b28.webp)

!!! warning "Atención"
    **Siempre importar primero los clientes y después los productos.** Los productos hacen referencia a las personas dueñas, así que si el cliente no existe todavía, la prenda no se le puede asignar. El propio sistema te lo recuerda arriba de la pantalla.
    Para importar productos es necesario haber creado las categorias previamente, ya que estas se van a importar dentro del archivo excel.

La pantalla tiene dos pestañas — **Importar clientes** e **Importar productos** — y las dos funcionan igual: **descargar plantilla**, completarla, **subir archivo**.

![Pantalla de importación masiva](/assets/carga-masiva/f3727f63c929.webp)

### Paso 1 — Clientes

En la pestaña **Importar clientes**, hacé clic en **descargar plantilla**. Se baja un Excel con dos hojas: **Instrucciones** y **Clientes**.

Las columnas de la hoja Clientes son: nombre, email, teléfono, tipo documento, documento, rol, comisión %, email ficticio, dirección, cuenta bancaria y validaciones.

Lo mínimo que necesitás cargar por fila:

- **nombre**
- **email**
- **rol** — cliente, o dueño si es proveedor
- **comisión %** — solo si el rol es dueño
![Plantilla de clientes](/assets/carga-masiva/0b08c6b80643.webp)

!!! tip "Tip"
    La última columna, **validaciones**, se completa sola y te avisa qué le falta a cada fila — *Nombre vacío*, *Email vacío*, *Rol vacío*. Revisala antes de subir el archivo: te ahorra la mitad de los errores.

### Paso 2 — Productos

Recén cuando los clientes están cargados, pasá a **Importar productos** y descargá esa plantilla. La gracia es que **viene con los clientes que acabás de importar ya cargados**, para poder elegirlos desde un desplegable.

![Pestaña Importar productos](/assets/carga-masiva/9c7613c1f29c.webp)

Las columnas son: nombre, descripción, código alternativo, categoría, precio, condición, tienda, fecha de ingreso, propiedad, proveedor original, dueño actual y comentarios.

![Plantilla de productos](/assets/carga-masiva/b1e348950009.webp)

!!! warning "Atención"
    Las **categorías tienen que existir antes en el sistema** para aparecer en la plantilla. Si vas a usar una categoría nueva, creadá primero.

#### Propiedad y dueño

La columna **propiedad** define de quién es la prenda. Si ponés **Consignación**, la columna **dueño actual** se despliega con la lista de clientes que ya cargaste y elegís la persona que corresponde.

![Columna dueño actual con la lista de clientes](/assets/carga-masiva/59d55c962c4f.webp)

La columna **tienda** también es un desplegable, útil cuando tenés más de un local.

### Paso 3 — Subir el archivo

Guardá el Excel completo, volvé a la pantalla de importación y hacé clic en **subir archivo**. Arrastrá el archivo y el sistema procesa todas las filas de una vez.

### Revisar el resultado

Abajo está el **Historial de importaciones**, con una fila por cada carga: fecha, estado, filas totales, registros creados y filas con errores.

| Estado | Qué significa |
| --- | --- |
| **Completada** | Entraron todas las filas. Registros creados coincide con filas totales. |
| **Fallida** | Hubo filas con problemas. Fijate en la columna *filas con errores* cuántas fueron. |

#### Corregir una importación fallida

Hacé clic en la flecha de la columna **ACCIONES** de esa fila. Tenés dos opciones: **Descargar archivo de errores** y **Descargar archivo original**.

![Menú para descargar el archivo de errores](/assets/carga-masiva/f5de82283017.webp)

El archivo de errores es el mismo Excel que subíste pero con una **hoja extra** que detalla qué estuvo mal en cada fila. Corregis lo que indica y volvés a subir el archivo.

!!! tip "Tip"
    La primera migración la podemos hacer nosotros con tu planilla. Las fotos se cargan después, en una segunda instancia.

<p class="doc-aliases" markdown>Términos relacionados: importación masiva, subir excel, cargar muchos productos, migrar stock, planilla de migración, cómo paso todos los productos, tengo 500 proveedoras</p>
