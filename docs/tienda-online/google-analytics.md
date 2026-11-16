---
title: Cómo medir las visitas de tu tienda con Google Analytics
slug: google-analytics
order: 85
type: Guía
aliases: como instalar google analytics, google tag manager, google analytics
---

# Cómo medir las visitas de tu tienda con Google Analytics

## 

Esta guía te acompaña, paso a paso, para que puedas ver cuánta gente visita tu
tienda, qué productos miran y de dónde vienen. No necesitas saber de tecnología:
alcanza con seguir los pasos en orden.

**Tiempo estimado:** 20 a 30 minutos.
**Qué vas a necesitar:** una cuenta de Google (la misma de tu correo de Gmail
sirve) y acceso a tu backoffice.

---

### Cómo funciona, en palabras simples

Vas a usar dos herramientas gratuitas de Google que trabajan juntas:

- **Google Analytics** es el "tablero de resultados": ahí ves las visitas, los
usuarios, las páginas más miradas y de dónde llega la gente.
- **Google Tag Manager** es el "conector": es lo que hace que tu tienda le
empiece a mandar información a Google Analytics.
Piénsalo así: **Analytics es el velocímetro y Tag Manager es el cable que lo
conecta al motor de tu tienda.** Necesitas los dos.

El proceso completo es:

1. Creas el conector (Tag Manager) y copias su código.
1. Pegas ese código en tu backoffice.
1. Creas el tablero (Analytics) y copias su código.
1. Enlazas el tablero dentro del conector.
1. Publicas y verificas que todo mida bien.
> **Dato clave para no confundirse:** Google te va a dar dos códigos parecidos
> pero distintos. Uno empieza con **`GTM-`** (el conector) y otro con **`G-`**
> (el tablero). En el **backoffice se pega el que empieza con ****`GTM-`**. El que
> empieza con `G-` se usa más adelante, dentro de Tag Manager. Si los confundes,
> no va a funcionar.

---

### Paso 1 — Crear el conector en Google Tag Manager

1. Entra a [**https://tagmanager.google.com**](https://tagmanager.google.com/) e
inicia sesión con tu cuenta de Google.
1. Haz clic en el botón **Crear cuenta**.
1. Completa los datos que te pide:
    - **Nombre de la cuenta:** el nombre de tu empresa o marca.
    - **País:** el tuyo.
    - **Nombre del contenedor:** escribe la dirección de tu tienda, por ejemplo
`mitienda.com`.
    - **Plataforma de destino:** elige la opción **Web**.
1. Haz clic en **Crear** y acepta los términos que aparecen.
1. Se va a abrir una ventana con un código para instalar. **No hace falta que
copies ese bloque de código.** Ciérrala con la **X**.
1. Arriba de la pantalla vas a ver un código que empieza con **`GTM-`**
(por ejemplo, `GTM-AB12CD3`). **Ese es el que necesitas.** Cópialo o anótalo
en un lugar seguro.
✅ **Al terminar este paso tienes:** tu código `GTM-XXXXXXX`.

---

### Paso 2 — Pegar ese código en tu backoffice

1. Ingresa a tu **backoffice**.
1. En el menú, abre **Configuración** y entra a **Ajustes de la tienda**.
1. Haz clic en la pestaña **SEO**.
1. Busca el campo que dice **"ID de Google Tag Manager"**.
1. Pega ahí el código que empieza con **`GTM-`** que copiaste en el Paso 1.
1. Haz clic en **Guardar**.
✅ **Al terminar este paso:** tu tienda ya está conectada a Tag Manager. Todavía
falta enlazar el tablero de Analytics para empezar a ver datos.

> Si algún día quieres dejar de medir, vuelve a este campo, bórralo y guarda.

---

### Paso 3 — Crear el tablero en Google Analytics

Si ya tienes un código de Analytics que empieza con `G-`, pasa directo al Paso 4.

1. Entra a [**https://analytics.google.com**](https://analytics.google.com/) con
la misma cuenta de Google.
1. Abajo a la izquierda, haz clic en el engranaje **Administrar**.
1. Haz clic en **Crear** y luego en **Propiedad**.
1. Pon un nombre (por ejemplo, el de tu tienda), elige tu **zona horaria** y tu
**moneda**, y sigue adelante.
1. Cuando te pregunte por la plataforma, elige **Web**.
1. Ingresa la dirección de tu tienda (por ejemplo, `https://mitienda.com`) y
crea el flujo de datos.
1. Vas a ver un código que empieza con **`G-`** (por ejemplo, `G-AB12CD34EF`),
llamado **ID de medición**. Cópialo o anótalo.
✅ **Al terminar este paso tienes:** tu código `G-XXXXXXXXXX`.

---

### Paso 4 — Enlazar el tablero dentro del conector

Este es el paso que une todo. Se hace dentro de Tag Manager.

1. Vuelve a [**https://tagmanager.google.com**](https://tagmanager.google.com/) y
abre el contenedor que creaste en el Paso 1.
1. En el menú de la izquierda, haz clic en **Etiquetas** y después en el botón
**Nueva**.
1. Haz clic en el recuadro de arriba, **Configuración de la etiqueta**.
1. En la lista que aparece, elige **Google Analytics** y luego la opción
**Etiqueta de Google** (en inglés puede figurar como "Google Tag").
1. En el campo **ID de la etiqueta**, pega el código que empieza con **`G-`**
que copiaste en el Paso 3.
1. Haz clic en el recuadro de abajo, **Activación**, y elige **All Pages**
(Todas las páginas). Esto hace que mida en todo el sitio.
1. Haz clic en **Guardar** (arriba a la derecha). Si te pide un nombre, pon
algo como "Analytics - Todas las páginas".
✅ **Al terminar este paso:** el tablero y el conector ya están enlazados. Falta
un último paso para activarlo.

---

### Paso 5 — Publicar los cambios

En Tag Manager, nada se activa hasta que aprietas **Publicar**.

1. Arriba a la derecha, haz clic en el botón **Enviar**.
1. Pon un nombre a la versión (por ejemplo, "Instalé Analytics") y haz clic en
**Publicar**.
✅ **Listo.** A partir de ahora tu tienda le manda datos a Google Analytics.

---

### Paso 6 — Comprobar que esté funcionando

1. En **Google Analytics**, entra a **Informes** y luego a **Tiempo real**.
1. En otra pestaña (o desde tu teléfono), abre tu tienda y navega un poco.
1. En unos segundos, en el informe de Tiempo real deberías verte a ti mismo como
una visita activa.
Si te ves en el informe, ¡quedó todo funcionando! 🎉

> Los informes completos (visitas por día, productos más vistos, de dónde viene
> la gente) empiezan a llenarse con las horas. Es normal que al principio se vean
> vacíos, salvo el de Tiempo real.

---

### Preguntas frecuentes

**Tengo el código que empieza con ****`G-`****. ¿Lo pego directo en el backoffice?**
No. En el backoffice solo va el código que empieza con **`GTM-`**. El que empieza
con `G-` se usa dentro de Tag Manager, en el Paso 4.

**¿Tiene costo?**
No. Tanto Google Analytics como Google Tag Manager son gratuitos.

**¿Qué voy a poder ver?**
Cuántas personas entran, qué páginas y productos miran, desde qué país y
dispositivo, y por qué medio llegaron (Google, redes sociales, enlaces, etc.).

**Ya pasó un rato y no veo nada en Tiempo real.**
Revisa tres cosas: (1) que en el backoffice hayas pegado el código `GTM-` y
guardado; (2) que en Tag Manager hayas apretado **Publicar** (Paso 5); (3) que
en el Paso 4 hayas pegado bien el código `G-`. Si tienes un bloqueador de
publicidad activo en tu navegador, puede ocultar tu propia visita: prueba desde
el teléfono con datos móviles.

**¿Puedo sumar otras herramientas más adelante (Meta, Google Ads)?**
Sí. Esa es la ventaja de Tag Manager: puedes agregar más etiquetas desde su panel,
sin tener que tocar de nuevo el backoffice.

**¿Cómo desactivo la medición?**
Entra al backoffice, en **Configuración › Ajustes de la tienda › SEO**, borra el código del campo
"ID de Google Tag Manager" y guarda.

<p class="doc-aliases" markdown>Términos relacionados: como instalar google analytics, google tag manager, google analytics</p>
