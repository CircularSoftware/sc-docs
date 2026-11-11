---
title: Conectar tu tienda a Claude o ChatGPT
slug: conectar-ia
order: 60
type: Guía
aliases: conectar claude, conectar chatgpt, conexiones ia, inteligencia artificial,
  preguntarle a la ia por mi tienda, mcp, chat gpt no ve mis datos, ia no encuentra
  mis productos
---

# Conectar tu tienda a Claude o ChatGPT

Puedes conectar un asistente de inteligencia artificial a los datos de tu tienda y hacerle preguntas en lenguaje común: cuánto vendiste este mes, qué proveedor te deja más margen, qué prendas llevan meses sin moverse. El asistente consulta tus datos en el momento y te responde en el chat, sin que exportes planillas ni armes un reporte.

Esta guía explica cómo se conecta, qué puede ver del otro lado y cómo se desconecta.

!!! danger "Importante"
    La conexión la hace un usuario con rol **Administrador**. Cada app ve lo mismo que el administrador que la autorizó y actúa con sus permisos.

### El acceso es de solo lectura

La app puede consultar tus datos, pero **no puede crear, editar ni borrar nada**. No puede registrar una venta, cambiar un precio ni modificar un producto: solo leer y responder.

Como cada app actúa con los permisos del administrador que la conectó, ve lo mismo que esa persona ve en el sistema.

### Qué le puedes preguntar

Las preguntas útiles son las que hoy resolverías mirando el panel o un reporte.

| Si quieres saber | Pregúntale algo así |
| --- | --- |
| Cómo viene el mes | "¿Cuánto vendí este mes comparado con el anterior?" |
| Qué proveedor conviene | "¿Qué proveedor me dejó más dinero en los últimos tres meses?" |
| Qué no se mueve | "¿Qué productos llevan más de 60 días sin venderse?" |
| Cómo está la caja | "¿Cuánto efectivo hay en caja en cada local?" |
| Quién compra | "¿Cuáles son mis diez clientes que más gastaron este año?" |

La respuesta sale de los datos de tu tienda en ese momento, no de una copia vieja.

### Copiar la dirección del conector

Entra a **Configuración › Integraciones › Conexiones IA**. En **Dirección del conector** está la dirección de tu tienda, con un botón **Copiar** al lado. Es lo que vas a pegar del otro lado.

![](/assets/conectar-ia/2c444ce9718d.webp)

La pantalla de Conexiones IA: la dirección del conector, las instrucciones para cada app y la lista de apps conectadas.

!!! tip "Tip"
    La dirección solo se muestra si entras al backoffice por el dominio de tu tienda. Si alguien de Software Circular está viendo tu tienda para ayudarte, en esa pantalla no aparece.

### Conectar la app

| App | Qué hacer |
| --- | --- |
| **Claude** | Agrega un conector personalizado y pega la dirección. Después ingresa con tu usuario del backoffice y acepta el acceso. |
| **Claude Code** | Ejecuta el comando que aparece en pantalla, que ya trae la dirección de tu tienda, y sigue los pasos para ingresar. |
| **ChatGPT** | Se agrega como servidor MCP personalizado, con los pasos de abajo. |
| **Cualquier otra app compatible** | Si la app admite conectores MCP con autenticación OAuth, usa la misma dirección. |

El paso de ingresar con tu usuario del backoffice es el que autoriza la conexión: la app no entra con una clave aparte, entra como tú.

#### Pasos para ChatGPT

Esto se hace desde ChatGPT en la computadora, no desde la aplicación del teléfono.

1. Entra a [**chatgpt.com/plugins**](http://chatgpt.com/plugins).
1. Haz clic en el botón **+** y elige **Add custom MCP server**.
1. Escribe un **nombre** para la conexión, por ejemplo el de tu tienda. La descripción es opcional.
1. En **Connection**, pega la dirección del conector en **Server URL**.
1. En la autenticación, elige **OAuth**.
1. Lee el aviso de riesgo y marca **I understand and want to continue**.
1. Haz clic en **Create as a plugin** e instálalo.
1. En una conversación, escribe **@** y elige la conexión. La primera vez te va a pedir que ingreses con tu usuario del backoffice y aceptes el acceso.
!!! tip "Tip"
    Los nombres de los botones son los de ChatGPT y aparecen en inglés aunque uses la aplicación en español. Si los menús no coinciden, es porque ChatGPT cambió su pantalla: busca la opción para agregar un servidor MCP propio.

### Ver y desconectar las apps

En la misma pantalla, el bloque **Apps conectadas** lista las aplicaciones que hoy tienen acceso a tu tienda. Cuando no hay ninguna, avisa que todavía no hay ninguna app conectada.

Si una app deja de hacerte falta, o no la reconoces, desconéctala desde ahí: deja de poder consultar tus datos.

### Qué pasa después

La app queda listada en **Apps conectadas** y puede consultar tus datos cada vez que le preguntes algo, sin volver a pedirte permiso. Nada de lo que haga queda registrado como un movimiento de tu tienda, porque no puede modificar nada.

Si cambias los permisos del administrador que autorizó la conexión, la app pasa a ver lo mismo que vea esa persona a partir de ese momento.

<p class="doc-aliases" markdown>Términos relacionados: conectar claude, conectar chatgpt, conexiones ia, inteligencia artificial, preguntarle a la ia por mi tienda, mcp, chat gpt no ve mis datos, ia no encuentra mis productos</p>
