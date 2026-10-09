---
title: Crear un cliente
slug: crear-cliente
order: 10
type: Guía
aliases: dar de alta un cliente, cargar un dueño, agregar una marca, cliente con comisión,
  datos bancarios del dueño, cargar proveedor, error de formato identificador CI,
  no me deja guardar el cliente, el documento no me lo acepta, cédula con puntos,
  nombre y apellido, nombre completo, de cuánto es la comisión por defecto, no encuentro
  al cliente, buscar un cliente
---

# Crear un cliente

Hay dos formas de dar de alta a una persona: el **alta rápida** desde una venta en curso, o el **alta completa** desde la sección Clientes. Las dos crean el mismo cliente; cambia cuánta información cargas en el momento.

!!! warning "Atención"
    El **correo electrónico** es el campo más importante del formulario: por ahí viajan las ventas, los vales y los avisos de comisiones. Pídelo y verifícalo antes de guardar.

### Opción 1 — Alta rápida desde una venta

Si ya estás cargando una venta y la persona todavía no existe, no hace falta salir de la pantalla. En el bloque **Cliente**, haz clic en **Nuevo**, al lado del buscador.

![El bloque Cliente de una nueva orden de venta, con el buscador y el botón Nuevo](/assets/crear-cliente/4b9bb4302913.webp)

Se abre la ventana **Nuevo Cliente** con los campos mínimos: **Email**, **Teléfono**, **Nombre completo**, **Tipo ID**, **Número ID**, **Dirección**, **Departamento/Estado** y **Ciudad**. Solo el email es obligatorio. Completa lo que tengas y haz clic en **Confirmar**.

![La ventana Nuevo Cliente dentro de la orden de venta](/assets/crear-cliente/337c25fa6e89.webp)

El cliente queda creado y asociado a esa venta. Más adelante puedes completar el resto de la ficha desde Clientes.

### Opción 2 — Alta completa desde Clientes

Es el camino recomendado cuando la persona va a dejar mercadería, porque permite cargar roles, comisión y datos bancarios.

Ingresa a **Clientes** en el menú lateral y haz clic en **Nuevo Cliente**, arriba a la derecha.

![El formulario de alta de cliente, con General, Identificador, Roles y Datos Comerciales](/assets/crear-cliente/8fae9740954c.webp)

#### Datos generales

Completa el **Email** —el único obligatorio de entrada— y, si los tienes, **Teléfono**, **Nombre completo**, **Dirección**, **Ciudad** y **Departamento/Estado**.

!!! tip "Tip"
    El interruptor **Emails deshabilitados** sirve para los casos en que cargas un correo inventado porque no tienes el real: con él activado, el sistema deja de enviarle avisos a esa dirección.

#### Roles

En el panel derecho asignas uno o más roles:

| Rol | Cuándo usarlo |
| --- | --- |
| **Cliente** | Persona que compra. Viene activado por defecto. |
| **Dueño** | Persona que te deja mercadería para vender. |
| **Marca** | Cuando quien entrega la mercadería es una marca o empresa, no una persona física. |

Al activar **Dueño** pasan dos cosas a la vez: se completa sola la **Comisión (%)** con el valor por defecto de tu tienda, y **Nombre completo** y **Número ID** pasan a ser obligatorios. La comisión es editable: si tienes un acuerdo distinto con esa persona, sobrescríbela.

![Al activar el rol Dueño, la comisión se completa sola y aparecen los campos obligatorios](/assets/crear-cliente/abc6daf9f8fb.webp)

#### Identificador

!!! danger "Importante"
    Siempre que des de alta a una persona **dueña**, cárgale su documento. Es el dato con el que el sistema se conecta con la facturación electrónica: si falta o está mal, los comprobantes de esa persona no se pueden emitir.

En **Tipo ID** eliges entre **Documento de Identidad**, **RUT**, **DNI**, **CUIT**, **CUIL** y **Otros**, según el país y el caso: documento de identidad para una persona física, y la identificación tributaria de la empresa cuando se trata de una marca.

!!! warning "Atención"
    **Escribe el número sin puntos ni guiones.** El campo admite entre 7 y 8 caracteres contando los separadores, así que un documento escrito como `4.567.890-5` se rechaza con el mensaje *Error de formato identificador CI*, aunque el número sea correcto. El mismo documento escrito `45678905` se guarda sin problema. El sistema además verifica el dígito verificador, así que no acepta números inventados.

#### Guardar

Baja hasta el final del formulario y haz clic en **Guardar**.

![El pie del formulario, con los botones Cancelar y Guardar](/assets/crear-cliente/e346c6e5d135.webp)

### Encontrar al cliente después

Vuelve a **Clientes**. El buscador acepta nombre, correo, teléfono o documento, y filtra a medida que escribes: no hay que apretar ningún botón. Al lado tienes los filtros **Estado** y **Rol**, y **Descargar** para bajar el listado a Excel.

![El listado de clientes con el buscador y los filtros](/assets/crear-cliente/931f1144ac75.webp)

Cada resultado muestra el nombre, su código interno —por ejemplo `CL_1020`—, el correo, el teléfono y la comisión.

![Un resultado de búsqueda, con el código interno y la comisión](/assets/crear-cliente/8ae1ca32404a.webp)

### Qué ves en la ficha del cliente

Al hacer clic sobre el nombre entras a la ficha, organizada en pestañas:

- **Detalles** — los datos con los que lo diste de alta, sus roles y sus datos comerciales. Se editan con el botón **Editar**.
- **Productos** — la mercadería que tiene asignada.
- **Ordenes** — sus compras.
- **Comisiones** — lo que le corresponde cobrar.
- **Archivos** — documentación adjunta.
![La ficha de un cliente con sus pestañas, roles y comisión](/assets/crear-cliente/13835c708b90.webp)

### Qué pasa después

El cliente queda disponible en todo el sistema: para asignarle productos, para elegirlo en una venta y para que el sistema le genere comisiones si dejó mercadería.

!!! tip "Tip"
    Una **Marca** siempre es además **Dueño** y necesita identificación tributaria. Para cargar muchos clientes de una vez, mira [Cargar clientes y productos de forma masiva](../primeros-pasos/carga-masiva.md).

<p class="doc-aliases" markdown>Términos relacionados: dar de alta un cliente, cargar un dueño, agregar una marca, cliente con comisión, datos bancarios del dueño, cargar proveedor, error de formato identificador CI, no me deja guardar el cliente, el documento no me lo acepta, cédula con puntos, nombre y apellido, nombre completo, de cuánto es la comisión por defecto, no encuentro al cliente, buscar un cliente</p>
