# Cómo escribir artículos de ayuda (contrato del editor)

Copia este texto en una página de Notion fijada donde trabajan las editoras. Es el
acuerdo entre quien escribe y el sistema que publica.

## La base de datos `Docs`

Cada fila es un artículo. Rellena estas propiedades:

| Propiedad | Para qué |
|-----------|----------|
| **Title** | El encabezado del artículo. |
| **Slug** | La parte final de la URL. **No se cambia nunca.** Minúsculas, guiones, sin acentos. |
| **Category** | La sección. Se convierte en la carpeta y el grupo del menú. |
| **Order** | Orden dentro de la categoría. Usa saltos de 10 (10, 20, 30…). |
| **Status** | `Draft` mientras escribes; `Published` cuando esté lista. Solo se publica lo `Published`. |
| **Type** | `Guía` (paso a paso) o `FAQ` (una pregunta puntual). Las `FAQ` aparecen juntas en la página "Preguntas frecuentes". |
| **Aliases** | Las palabras REALES que escriben los clientes, separadas por comas. Lo más valioso. |

### Sobre `Aliases`

Es el campo más importante y el que más se olvida. Aquí van las frases tal como las
escribe la gente en WhatsApp: *«no me aparecen los productos», «no se actualiza el stock»*.
No las inventes — sácalas de las conversaciones de soporte. Alimentan el buscador.

### Sobre `Slug`

Cambiar el `Slug` rompe todos los enlaces que ya enviaste a clientes. Si necesitas
cambiar el nombre del artículo, cambia el **Title**, nunca el **Slug**.

## Qué bloques SÍ se publican

Encabezados, párrafos, listas (con viñetas o numeradas), imágenes, callouts, código,
citas, separadores y tablas.

## Qué bloques NO se publican

Bases de datos incrustadas, bloques sincronizados, columnas, embeds, botones y vistas
enlazadas. **Si parece un truco ingenioso, no aparecerá en el sitio.**

## Imágenes

Pega las imágenes directamente en el cuerpo de la página. **No enlaces a Google Drive.**

## Para publicar

Cambia `Status` a `Published`. El sitio se actualiza automáticamente cada media hora, o
usa el botón de publicar si tu espacio lo tiene. Si algo falla al publicar, el equipo
recibe una alerta — tu cambio no se pierde.
