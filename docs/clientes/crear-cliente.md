---
title: Crear un cliente
slug: crear-cliente
order: 10
type: Guía
aliases: dar de alta un cliente, cargar un dueño, agregar una marca, cliente con comisión,
  datos bancarios del dueño, cargar proveedor
---

# Crear un cliente

Hay dos formas de dar de alta a una persona en el sistema: el **alta rápida** desde una venta en curso, o el **alta completa** desde la sección Clientes. Las dos crean el mismo cliente; cambia cuánta información cargás en el momento.

!!! note "⚠️ Nota"
    El **correo electrónico** es el campo más importante del formulario: muchas notificaciones del sistema se envían ahí. Pedilo y verificalo antes de guardar.

### Opción 1 — Alta rápida desde una venta

Si ya estás cargando una venta y la persona todavía no existe, no hace falta salir de la pantalla.

1. Entrá a **nueva venta**.
1. En el bloque **Cliente**, hacé clic en **nuevo**, al lado del buscador.
![Botón "nuevo" en el bloque Cliente de una nueva orden de venta](/assets/crear-cliente/060fa076d4c2.webp)

Se abre la ventana **Nuevo Cliente** con los campos mínimos: Email, Nombre, Apellido, Tipo ID, Número ID, Teléfono, Dirección, Departamento/Estado y Ciudad. Los marcados con asterisco son obligatorios. Completá los datos y hacé clic en **confirmar**.

![Ventana Nuevo Cliente dentro de la orden de venta](/assets/crear-cliente/2aab7358c095.webp)

El cliente queda creado y asociado a esa venta. Más adelante podés completar el resto de la ficha desde Clientes.

---

### Opción 2 — Alta completa desde Clientes

Es el camino recomendado cuando la persona va a ser dueña de mercadería o marca, porque permite cargar roles, comisión y datos bancarios.

1. Entrá a **clientes** en el menú lateral.
1. Hacé clic en **nuevo cliente**, arriba a la derecha.
![Formulario completo de alta de cliente](/assets/crear-cliente/30a3faeeee6c.webp)

#### Datos generales

Completá Email, Nombre y Apellido (obligatorios) y, si los tenés, Teléfono, Dirección, Ciudad y Departamento/Estado.

#### Roles

En el panel derecho asignás uno o más roles:

| Rol | Cuándo usarlo |
| --- | --- |
| **Cliente** | Persona que compra. Viene activado por defecto. |
| **Dueño** | Persona que nos trae mercadería para vender. |
| **Marca** | Cuando quien entrega mercadería es una marca o empresa, no una persona física. |

Al activar **Dueño**, el sistema completa automáticamente la **Comisión** en 40%. Ese valor es editable: si tenés un acuerdo comercial distinto con esa persona, sobrescribilo.

![Rol Dueño activado y comisión autocompletada en 40](/assets/crear-cliente/dd4dba7c9afa.webp)

#### Identificador

!!! note "🔑 Nota"
    Siempre que des de alta a una persona **dueña**, cargale el documento de identidad. Es el dato con el que el sistema se conecta con Biller: si falta o está mal, la facturación de esa persona no va a funcionar.

En **Tipo ID** elegí según el caso y completá **Número ID**:

- Persona física → documento de identidad.
- Marca o empresa → RUT.
![Número de documento cargado en el formulario](/assets/crear-cliente/0f55968505ed.webp)

#### Guardar

Bajá hasta el final del formulario y hacé clic en **guardar**.

![Botón guardar al pie del formulario](/assets/crear-cliente/6d001b3f6d0f.webp)

---

### Encontrar al cliente después

Una vez guardado, volvé a **clientes**. El buscador acepta nombre, email, teléfono o documento.

![Listado de clientes con el buscador](/assets/crear-cliente/4083dff67bbf.webp)

Escribí el dato y hacé clic en **buscar**. Cada resultado muestra el nombre, su código interno (por ejemplo `CL_1004`), email, teléfono y comisión.

![Resultado de la búsqueda de un cliente](/assets/crear-cliente/62a816351d83.webp)

### Qué ves en la ficha del cliente

Al hacer clic sobre el nombre entrás a la ficha, organizada en pestañas:

- **Detalles** — los datos con los que lo diste de alta. Se editan con el botón **editar**.
- **Productos** — la mercadería que tiene asignada.
- **Ordenes** — sus ventas.
- **Comisiones** — lo que le corresponde cobrar.
- **Archivos** — documentación adjunta, con el botón **subir archivo**.
![Ficha del cliente con sus pestañas](/assets/crear-cliente/e09d9cfdc03e.webp)

!!! note "💡 Nota"
    Una **Marca** siempre es además **Dueño** y necesita RUT. Si el documento es RUT, la dirección pasa a ser obligatoria. Para cargar muchos clientes de una vez, mirá la guía *Cargar clientes y productos de forma masiva (planilla)*.

<p class="doc-aliases" markdown>Términos relacionados: dar de alta un cliente, cargar un dueño, agregar una marca, cliente con comisión, datos bancarios del dueño, cargar proveedor</p>
