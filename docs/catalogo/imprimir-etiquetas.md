---
title: Imprimir etiquetas de productos
slug: imprimir-etiquetas
order: 60
type: Guía
aliases: generar etiquetas, imprimir el código de la prenda, configurar la impresora,
  me sale cortado, descargar etiquetas, etiquetas en excel o csv, imprimir solo las
  prendas nuevas, el archivo me trae todos los productos, las etiquetas salen sin
  precio, no aparece el precio en la etiqueta, el nombre sale cortado en la etiqueta,
  imprimir etiquetas de una proveedora
---

# Imprimir etiquetas de productos

Las etiquetas no se imprimen desde el sistema. Lo que hace Software Circular es generar un **archivo** con los datos de tus productos; ese archivo se carga después en el software de tu impresora de etiquetas, que es donde se arma el diseño y se manda a imprimir.

### 1. Elige qué productos entran

Este es el paso que más se saltea, y es el que más problemas evita: el archivo trae **exactamente los productos que tengas filtrados en pantalla**, no todo tu catálogo.

Ingresa a **Productos** y usa el buscador y los filtros de la lista —**Fecha de Creación**, **Estado**, **Propiedad**, **Local** y **Canal de Venta**— para quedarte solo con las prendas que vas a etiquetar. Lo más habitual es filtrar por fecha, para imprimir únicamente lo que cargaste ese día.

!!! tip "Tip"
    También puedes hacerlo desde la ficha de una proveedora, en su pestaña **Productos**: ahí la lista ya viene acotada a sus prendas, así que no necesitas filtrar nada más.

### 2. Descarga el archivo

Haz clic en **Etiquetas**, al lado del buscador y del botón **Descargar**. No es un botón simple: se despliega para que elijas el formato.

| Formato | Qué descarga |
| --- | --- |
| **Etiquetas (Excel)** | Una planilla `.xlsx`. Es la opción más común. |
| **Etiquetas (CSV)** | Un archivo de texto separado por comas, para los programas de impresión que no aceptan Excel. |

Si no sabes cuál pide tu impresora, prueba primero con Excel.

### 3. Qué trae el archivo

Una fila por producto, con estas columnas:

- **Id** — el código del producto, el `PR_…` que ves en el listado.
- **Nombre** — el nombre de la prenda, **recortado a los primeros 25 caracteres**.
- **Precio_venta** y **Precio_alquiler**, y una columna por cada perfil de precio que tengas activo.
!!! warning "Atención"
    Si el archivo te sale **sin ninguna columna de precio**, no está fallando: los precios aparecen solo si pediste que se muestren en las etiquetas. Eso se activa en **Pagos → Configuración**, en la opción **Etiquetas de productos** de cada perfil de precio. Si no tienes perfiles configurados, el archivo sale sin esas columnas.

### 4. Carga el archivo en tu impresora

Abre el software de tu impresora de etiquetas e importa el archivo que descargaste. Desde ahí eliges qué columnas se imprimen y cómo se ven.

!!! tip "Tip"
    El diseño, el tamaño y la distribución de la etiqueta se configuran en el software de la impresora, no en el sistema. Si la etiqueta sale cortada o descuadrada, el ajuste va por ahí. La única excepción es el **nombre**: ese ya viene recortado a 25 caracteres desde el archivo, y no se puede alargar.

Si todavía no tienes impresora o estás por comprar una, mira [Qué impresora de etiquetas comprar para el local](../preguntas-frecuentes.md#que-impresora-comprar).

### Qué pasa después

Generar el archivo no modifica nada: tus productos quedan igual y puedes volver a descargarlo las veces que quieras. El archivo tampoco queda guardado en el sistema — es una descarga, así que si lo necesitas de nuevo, repite los pasos con el mismo filtro.

<p class="doc-aliases" markdown>Términos relacionados: generar etiquetas, imprimir el código de la prenda, configurar la impresora, me sale cortado, descargar etiquetas, etiquetas en excel o csv, imprimir solo las prendas nuevas, el archivo me trae todos los productos, las etiquetas salen sin precio, no aparece el precio en la etiqueta, el nombre sale cortado en la etiqueta, imprimir etiquetas de una proveedora</p>
