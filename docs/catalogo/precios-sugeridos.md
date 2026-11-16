---
title: 'Precios sugeridos: que el panel proponga el precio de cada prenda'
slug: precios-sugeridos
order: 45
type: Guía
aliases: precio sugerido, cuánto cobro esta prenda, matriz de precios, lista de precios
  por categoría, precio base por categoría, factor por marca, factor por condición,
  usar sugerido, el empleado no puede cambiar el precio, el precio está bloqueado,
  lo define la matriz, guardar sin precio, producto sin precio, productos esperando
  precio, pendientes de precio, subir todos los precios, redondear precios, no hay
  precio sugerido, esta categoría no tiene precio base
---

# Precios sugeridos: que el panel proponga el precio de cada prenda

Con **Precios sugeridos** cargas una sola vez cuánto vale cada tipo de prenda —un precio base por categoría y factores por condición, marca u otros atributos— y el panel sugiere el precio de cada producto mientras lo cargas. Así todo el equipo pone precios parecidos a prendas parecidas.

También te deja guardar una prenda sin precio, para que alguien que sabe se lo ponga después.

!!! danger "Importante"
    **Viene apagado.** Lo arma y lo enciende un **Administrador**: la lista de precios está en **Inventario › Productos › Precios sugeridos** y el interruptor en **Configuración › Productos**. Mientras está apagado, el formulario de producto no muestra ninguna sugerencia.

!!! tip "Tip"
    La pantalla **Precios sugeridos** solo la ven los Administradores. La sugerencia en el formulario la ve cualquiera que cargue productos. Un Administrador puede hacer, además, que para los Encargados o los Empleados el precio lo ponga siempre la sugerencia.

### 1. Cargar los precios base (Administradores)

1. Entra a **Inventario › Productos › Precios sugeridos**.
1. Abre la pestaña **Precios base**.
1. Escribe el **Precio base** de cada categoría.
1. Toca **Guardar**, arriba a la derecha.
El precio base es lo que vale un producto de esa categoría en condición **Excelente** y sin marca destacada: lo demás lo mueven los factores. Una categoría sin precio propio hereda el de la categoría padre más cercana que lo tenga; la columna **Origen** dice si es **Propio** o **Heredado de …**.

Con **Solo sin precio base** ves las categorías que todavía no tienen ninguno. Un producto de una categoría sin precio base, propio ni heredado, no recibe sugerencia.

### 2. Ajustar con factores (opcional)

En la pestaña **Factores** elige, a la izquierda, la condición o el atributo que mueve el precio, y completa cada valor:

| Tipo | Qué hace | Neutro |
| --- | --- | --- |
| La opción que multiplica (**×**) | Multiplica el precio. Por ejemplo, 1,20 sube un 20 % y 0,80 lo baja un 20 %. | 1,00 |
| La opción que suma (**+**) | Suma un importe al precio base. | 0 |

Un valor sin factor no mueve el precio. Tienen factores la condición, los atributos con lista de valores (marca, talle, material…) y, por tramos, los atributos numéricos. Un atributo de texto libre no admite factores.

#### Cuando un factor vale solo para una categoría

En **Agregar un factor por categoría** elige el valor y la categoría, y toca **Agregar factor por categoría**. Vale para esa categoría y sus hijas, y gana sobre el factor general del mismo valor.

#### Cuando el atributo es un número

Para un atributo numérico se cargan tramos: completa **Desde** y **Hasta** y toca **Agregar tramo**. Un producto cae en el tramo que contiene su valor. Deja **Desde** vacío para un tramo abierto por abajo, y **Hasta** vacío para uno abierto por arriba. Dos tramos no pueden superponerse.

### 3. Ajustes del cálculo (opcional)

En la pestaña **Ajustes del cálculo**:

- **Ajuste general (%)** se aplica al final, a todos los precios. Sirve cuando la lista quedó vieja: 8 sube todo un 8 %. Puede ser negativo.
- **Redondeo** viene en **Sin redondeo**. Con **A un múltiplo** eliges el **Múltiplo**: con 1.000, un cálculo de 69.980 se sugiere como 70.000.
El precio sugerido es: (precio base + sumas) × factores × (1 + ajuste general / 100), redondeado.

### 4. Probar y guardar

En la pestaña **Probar** eliges una categoría y los valores de una prenda imaginaria y ves el precio sugerido, con el desglose de cómo se calculó. Usa la última versión guardada y no crea ningún producto.

Cada vez que tocas **Guardar** se crea una versión nueva de la lista. En **Historial** están todas: **Restaurar** crea una versión nueva igual a la que elegiste, y ninguna se borra.

### 5. Encender la sugerencia (Administradores)

1. Entra a **Configuración › Productos**.
1. Prende **Sugerir precios al cargar productos**.
1. Si quieres que Encargados o Empleados no escriban el precio, márcalos en **Roles que reciben el precio sugerido**.
1. Toca **Guardar**.
### Al cargar o editar un producto

Con la sugerencia encendida, en el formulario de producto **Categoría y atributos** aparece antes que el precio, porque la sugerencia sale de ahí. Debajo de **Precio de Venta** (o del precio base del alquiler) aparece **Precio sugerido: $ …**:

1. Elige la categoría, la condición y los atributos.
1. Toca **Usar sugerido** para copiarlo en el precio, o escribe otro.
1. Guarda como siempre.
Nada se completa solo: el precio sigue siendo editable. Mientras el campo tiene el precio sugerido, al lado dice **Sugerido**; si escribiste otro, dice cuánto por encima o por debajo está. **Cómo se calculó** abre el desglose.

| Dice | Significa | Qué hacer |
| --- | --- | --- |
| *Elegí la categoría para ver el precio sugerido.* | Todavía no hay categoría. | Elígela en **Categoría y atributos**. |
| *Esta categoría no tiene precio base, propio ni heredado: no hay precio sugerido.* | Ni la categoría ni sus padres tienen precio base. | Escribe el precio a mano, o pídele a un Administrador que cargue la base. |
| *Todavía no hay una matriz de precios guardada: no hay precio sugerido.* | La sugerencia está encendida pero nadie guardó la lista. | Un Administrador tiene que cargar y guardar los precios base. |

#### Cuando tu rol recibe el precio sugerido

Si un Administrador marcó tu rol en **Roles que reciben el precio sugerido**, el precio y el descuento quedan bloqueados y el campo muestra el precio sugerido, con la etiqueta **Lo define la matriz**. Al guardar, el producto queda con ese precio aunque se haya escrito otro.

Al editar un producto que ya tiene precio, se conserva el precio guardado (**Se conserva el precio guardado**). Si cambias la categoría, la condición o un atributo, el precio se recalcula y el formulario avisa *Pasa de … a …: cambiaste la categoría, la condición o un atributo.*

Si el producto no tiene precio sugerido, el botón dice **Guardar sin precio**: el producto se guarda **Sin precio** y un Administrador se lo pone después.

### Productos sin precio

Al cargar un producto nuevo puedes dejar el precio vacío y tocar **Guardar sin precio**, arriba junto a **Guardar**. El botón se habilita solo mientras el precio está vacío, y no hace falta tener la sugerencia encendida.

Un producto **Sin precio** no se muestra en la tienda online ni se puede vender. En el listado de productos lo encuentras con el filtro de estado **Sin precio**. Para ponerle precio, ábrelo con **Editar**, escribe el precio y guarda: pasa solo a **Disponible**, o a **Pendiente de aprobación** si tu tienda aprueba los productos antes de publicarlos. Desde el cambio de estado no se lo puede pasar a **Disponible**: solo se le pone precio editándolo.

#### La pestaña Pendientes (Administradores)

Cuando hay productos sin precio, **Precios sugeridos** abre en la pestaña **Pendientes** y la fila del menú muestra cuántos esperan.

- **Productos sin precio**: agrupados por categoría, con el precio **Sugerido hoy**. **Aplicar** le pone ese precio a un producto, y **Aplicar sugerido a los …**, a todos los de la categoría. **Poner precio a mano** abre la edición del producto.
- **Categorías sin precio base con productos esperando**: escribe la base ahí mismo y toca **Guardar**. Los productos de esa categoría pasan a tener sugerencia.
#### En la importación masiva

En la planilla de productos la columna **precio** puede quedar vacía. Con la sugerencia encendida y una categoría con precio base, el producto entra con el precio sugerido; si no, entra **Sin precio**. El resumen de la importación dice cuántos quedaron sin precio. Mira [Cargar clientes y productos de forma masiva (planilla)](../primeros-pasos/carga-masiva.md).

### Tener en cuenta

- **Cambiar la lista no cambia los precios ya guardados.** La sugerencia se usa al cargar o editar un producto. En la ficha de cada producto, la tarjeta **Precio sugerido** muestra lo que se sugirió al guardar, qué se decidió (**Aceptado**, **Cambiado a …** o **Fijado por la matriz**) y lo que sugiere hoy.
- **Un Administrador siempre decide el precio.** Solo los Encargados y los Empleados pueden recibir el precio bloqueado.
- **Con la sugerencia apagada no se sugiere ni se aplica nada.** Los productos sin precio siguen en **Pendientes**, pero se les pone precio a mano.
- **Las copias de un producto y los productos de precio fijo de la venta llevan su propio precio:** no pasan por la sugerencia.
- **Una categoría o un valor que borraste del catálogo sale de la lista.** La pantalla avisa cuáles y desaparecen con el próximo **Guardar**.
### Qué pasa después

Con la lista guardada y la sugerencia encendida, cada producto que se carga muestra su precio sugerido. Cómo completar el resto del formulario está en [Cargar un producto nuevo](cargar-producto.md) y [Editar un producto](editar-producto.md).

<p class="doc-aliases" markdown>Términos relacionados: precio sugerido, cuánto cobro esta prenda, matriz de precios, lista de precios por categoría, precio base por categoría, factor por marca, factor por condición, usar sugerido, el empleado no puede cambiar el precio, el precio está bloqueado, lo define la matriz, guardar sin precio, producto sin precio, productos esperando precio, pendientes de precio, subir todos los precios, redondear precios, no hay precio sugerido, esta categoría no tiene precio base</p>
