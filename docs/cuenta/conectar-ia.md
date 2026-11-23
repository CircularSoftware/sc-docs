---
title: Conectar tu tienda a Claude o ChatGPT
slug: conectar-ia
order: 60
type: Guía
aliases: conectar claude, conectar chatgpt, conexiones ia, inteligencia artificial,
  preguntarle a la ia por mi tienda, mcp, chat gpt no ve mis datos, ia no encuentra
  mis productos, conectar claude code, chatgpt no conecta, claude no ve mis datos,
  la ia dejó de funcionar, conector apagado, add custom connector
---

# Conectar tu tienda a Claude o ChatGPT

Puedes conectar un asistente de inteligencia artificial a los datos de tu tienda y hacerle preguntas en lenguaje común: cuánto vendiste este mes, qué proveedor te deja más margen, qué prendas llevan meses sin moverse. El asistente consulta tus datos en el momento y te responde en el chat, sin que exportes planillas ni armes un reporte.

Esta guía explica qué necesitas, cómo se conecta cada app, qué puede ver del otro lado, qué hacer si algo no funciona y cómo se desconecta.

!!! danger "Importante"
    La conexión la hace un usuario con rol **Administrador**. Cada app ve lo mismo que el administrador que la autorizó y actúa con sus permisos. Con otro rol, la app no se puede conectar: mira [Usuarios y roles](../cuenta/usuarios-roles.md).

### El acceso es de solo lectura

La app puede consultar tus datos, pero **no puede crear, editar ni borrar nada**. No puede registrar una venta, cambiar un precio ni modificar un producto: solo leer y responder.

Como cada app actúa con los permisos del administrador que la conectó, ve lo mismo que esa persona ve en el sistema.

Para responderte, la app envía lo que consulta a la empresa que la ofrece: Anthropic en el caso de Claude, OpenAI en el de ChatGPT. Si preguntas por tus clientes, la respuesta puede incluir nombres, correos o teléfonos: trátala con el mismo cuidado que el sistema.

### Qué le puedes preguntar

Las preguntas útiles son las que hoy resolverías mirando el panel o un reporte.

| Si quieres saber | Pregúntale algo así |
| --- | --- |
| Cómo viene el mes | "¿Cuánto vendí este mes comparado con el anterior?" |
| Qué proveedor conviene | "¿Qué proveedor me dejó más dinero en los últimos tres meses?" |
| Qué no se mueve | "¿Qué productos llevan más de 60 días sin venderse?" |
| Cómo está la caja | "¿Cuánto efectivo hay en caja en cada local?" |
| Quién compra | "¿Cuáles son mis diez clientes que más gastaron este año?" |
| Qué tienes disponible | "¿Cuántas camperas de cuero tengo disponibles?" |
| Cuánto debes de comisiones | "¿Cuánto debo de comisiones este mes y a quién?" |
| Qué falta preparar | "¿Cuántas órdenes tengo por preparar o listas para enviar?" |

La respuesta sale de los datos de tu tienda en ese momento, no de una copia vieja. Cuanto más concreta sea la pregunta (fechas, local, categoría), mejor va a ser la respuesta.

### Antes de empezar

Necesitas tres cosas:

| Qué | Detalle |
| --- | --- |
| **Un usuario Administrador** | El mismo correo y contraseña con los que entras al backoffice, con rol **Administrador**. |
| **Una cuenta de Claude o ChatGPT** | En Claude sirve cualquier plan, incluido el gratuito, que admite un solo conector propio. En ChatGPT necesitas un plan Business, Enterprise, Edu o Pro: en Plus y en el plan gratuito, hoy no ofrece esta opción. |
| **Una computadora** | La conexión se agrega desde la web o la aplicación de escritorio, no desde el teléfono. Una vez hecha, en Claude también funciona en la aplicación del teléfono. |

### Copiar la dirección del conector

Entra a **Configuración › Integraciones › Conexiones IA**. En **Dirección del conector** está la dirección de tu tienda, con un botón **Copiar** al lado. Es lo que vas a pegar del otro lado.

![](/assets/conectar-ia/2c444ce9718d.webp)

La pantalla de Conexiones IA: la dirección del conector, las instrucciones para cada app y la lista de apps conectadas.

!!! tip "Tip"
    La dirección solo se muestra si entras al backoffice por el dominio de tu tienda. Si alguien de Software Circular está viendo tu tienda para ayudarte, en esa pantalla no aparece.

Si en lugar de la dirección ves el aviso *El conector está apagado para esta tienda*, escríbenos y lo activamos.

### Conectar la app

| App | Qué hacer |
| --- | --- |
| **Claude** | Agrega un conector personalizado y pega la dirección, con los pasos de abajo. |
| **Claude Code** | Ejecuta el comando que aparece en pantalla, con los pasos de abajo. |
| **ChatGPT** | Se agrega como servidor MCP personalizado, con los pasos de abajo. |
| **Cualquier otra app compatible** | Si la app admite conectores MCP con autenticación OAuth, usa la misma dirección. |

El paso de ingresar con tu usuario del backoffice es el que autoriza la conexión: la app no entra con una clave aparte, entra como tú.

#### Pasos para Claude

Esto se hace en la computadora, desde claude.ai o la aplicación de escritorio de Claude.

1. Entra a **Customize › Connectors**.
1. Haz clic en **+ Add** y elige **Add custom connector**.
1. Escribe un **nombre** para la conexión, por ejemplo el de tu tienda, y pega la dirección del conector. Haz clic en **Continue**.
1. Deja la autenticación como viene y haz clic en **Add**.
1. Haz clic en **Connect**. Se abre el ingreso de Software Circular: entra con tu usuario del backoffice y acepta el acceso.
1. En una conversación, haz clic en el botón **+**, entra a **Connectors** y activa la conexión.
!!! tip "Tip"
    En los planes Team y Enterprise de Claude, los pasos 1 a 4 los hace un Owner de la organización, desde **Organization settings › Connectors**. Después, cada persona busca la conexión en **Customize › Connectors** y hace clic en **Connect**.

La primera vez que Claude use la conexión en una conversación, puede pedirte permiso para consultar tu tienda: puedes permitirlo siempre para que no vuelva a preguntar. Los nombres de los botones son los de Claude en inglés; si usas Claude en otro idioma, pueden aparecer traducidos.

#### Pasos para Claude Code

En la terminal, ejecuta el comando que aparece en **Conexiones IA**. Ya trae la dirección de tu tienda y tiene esta forma:

```bash
claude mcp add --transport http circular https://<dominio-de-tu-tienda>/mcp
```

Después, dentro de Claude Code, escribe `/mcp`, elige **circular** y sigue los pasos para ingresar con tu usuario del backoffice. Si trabajas en una computadora sin navegador, `claude mcp login circular --no-browser` te da el enlace para ingresar desde otro equipo.

#### Pasos para ChatGPT

Esto se hace desde ChatGPT en la computadora, no desde la aplicación del teléfono.

1. En la barra lateral de ChatGPT, entra a **Complementos** (Plugins), o directo a [**chatgpt.com/plugins**](https://chatgpt.com/plugins).
1. Haz clic en el botón **+** y elige **Agregar servidor MCP personalizado** (Add custom MCP server).
1. Escribe un **nombre** para la conexión, por ejemplo el de tu tienda. La descripción es opcional.
1. En **Conexión** (Connection), pega la dirección del conector como URL del servidor (Server URL).
1. En **Autenticación** (Authentication), elige **OAuth**.
1. Lee el aviso de riesgo y marca **Entiendo y quiero continuar** (I understand and want to continue).
1. Haz clic en **Crear como complemento** (Create as a plugin) e instálalo.
1. En una conversación, escribe **@** y elige la conexión. La primera vez te va a pedir que ingreses con tu usuario del backoffice y aceptes el acceso.
!!! tip "Tip"
    Los nombres son los de ChatGPT en español, con el inglés entre paréntesis por si usas ChatGPT en inglés. Si los menús no coinciden, es porque ChatGPT cambió su pantalla: busca la opción para agregar un servidor MCP propio.

### Aceptar el acceso

Cuando ingresas con tu usuario, Software Circular te muestra qué **App** pide acceso, la **Dirección que va a recibir los datos**, la **Tienda** y el **Usuario**.

Antes de hacer clic en **Permitir acceso**, revisa que esa dirección sea de la app que estás conectando: claude.ai para Claude y chatgpt.com para ChatGPT. En Claude Code es una dirección `localhost`, de tu propia computadora. Si no la reconoces, o no fuiste tú quien empezó la conexión, haz clic en **Cancelar**.

### Probar la conexión

Abre una conversación nueva y pregunta algo simple, por ejemplo "¿Cuánto vendí esta semana?". Si la respuesta trae los números de tu tienda, la conexión funciona.

La app puede interpretar mal una pregunta. Antes de pagar comisiones o tomar una decisión con un número, confírmalo en el sistema.

### Ver y desconectar las apps

En la misma pantalla, el bloque **Apps conectadas** lista las aplicaciones que hoy tienen acceso a tu tienda, con quién autorizó cada una, cuándo se conectó y cuándo se usó por última vez. Cuando no hay ninguna, avisa que todavía no hay ninguna app conectada.

Si una app deja de hacerte falta, o no la reconoces, haz clic en **Desconectar** y confirma: desde su próxima consulta ya no puede ver tus datos. Cualquier administrador puede desconectar cualquier app de la tienda, aunque la haya conectado otra persona.

Desconectarla desde aquí es lo que corta el acceso. Si además quieres que deje de aparecer en Claude o ChatGPT, quítala también de los conectores de esa app.

### Qué pasa después

La app queda listada en **Apps conectadas** y puede consultar tus datos cada vez que le preguntes algo, sin pedirte que vuelvas a ingresar. Nada de lo que haga queda registrado como un movimiento de tu tienda, porque no puede modificar nada.

Si cambias los permisos del administrador que autorizó la conexión, la app pasa a ver lo mismo que vea esa persona a partir de ese momento.

#### Cuándo hay que volver a conectar

La conexión se corta, y hay que repetir el ingreso desde la app, en estos casos:

- Cambias la contraseña de tu usuario: se cortan todas las apps que conectaste con él.
- Tu usuario deja de tener rol **Administrador** o se desactiva.
- Pasan 30 días sin usar la conexión.
- Conectas más de 10 apps con el mismo usuario: se desconecta la que usaste hace más tiempo.
- Alguien la desconecta desde **Apps conectadas**.
### Si algo no funciona

| Problema | Qué hacer |
| --- | --- |
| No aparece la dirección del conector | Entra al backoffice por el dominio de tu tienda: si alguien de Software Circular está viendo tu tienda, la dirección no se muestra. Si ves el aviso *El conector está apagado para esta tienda*, escríbenos. |
| No puedes ingresar desde la app | Revisa que tu usuario tenga rol **Administrador** y que puedas entrar al backoffice con el mismo correo y contraseña. |
| En ChatGPT no aparece **Agregar servidor MCP personalizado** | Entra por **Complementos** en la barra lateral, o por chatgpt.com/plugins, no desde la configuración. Si igual no aparece, tu plan no lo incluye o el administrador de tu espacio de trabajo no lo habilitó. |
| Claude no te deja agregar el conector | El plan gratuito admite un solo conector propio: quita el que no uses. En Team y Enterprise, solo un Owner de la organización puede agregarlo. |
| La app responde sin usar tus datos | Revisa que la conexión esté activa en esa conversación: en Claude, desde **+ › Connectors**; en ChatGPT, escribiendo **@** y eligiéndola. |
| Funcionaba y dejó de funcionar | Mira la lista de cuándo hay que volver a conectar, más arriba. Lo más común es un cambio de contraseña: vuelve a ingresar desde la app. |
| Dice que no tiene permiso para ver algo | La app ve lo mismo que el administrador que la conectó. Si ese usuario no tiene acceso a esa información en el sistema, la app tampoco. |

<p class="doc-aliases" markdown>Términos relacionados: conectar claude, conectar chatgpt, conexiones ia, inteligencia artificial, preguntarle a la ia por mi tienda, mcp, chat gpt no ve mis datos, ia no encuentra mis productos, conectar claude code, chatgpt no conecta, claude no ve mis datos, la ia dejó de funcionar, conector apagado, add custom connector</p>
