---
title: Cómo medir las visitas de tu tienda con Google Analytics
slug: google-analytics
order: 1000
type: Guía
aliases: como instalar google analytics, google tag manager, google analytics
---

# Cómo medir las visitas de tu tienda con Google Analytics

## 

Esta guía te acompaña, paso a paso, para que puedas ver cuánta gente visita tu
tienda, qué productos miran y de dónde vienen. No necesitás saber de tecnología:
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
Pensalo así: **Analytics es el velocímetro y Tag Manager es el cable que lo
conecta al motor de tu tienda.** Necesitás los dos.

El proceso completo es:

1. Creás el conector (Tag Manager) y copiás su código.
1. Pegás ese código en tu backoffice.
1. Creás el tablero (Analytics) y copiás su código.
1. Enlazás el tablero dentro del conector.
1. Publicás y verificás que todo mida bien.
> **Dato clave para no confundirse:** Google te va a dar dos códigos parecidos
> pero distintos. Uno empieza con **`GTM-`** (el conector) y otro con **`G-`**
> (el tablero). En el **backoffice se pega el que empieza con ****`GTM-`**. El que
> empieza con `G-` se usa más adelante, dentro de Tag Manager. Si los confundís,
> no va a funcionar.

---

### Paso 1 — Crear el conector en Google Tag Manager

1. Entrá a [**https://tagmanager.google.com**](https://tagmanager.google.com/) e
iniciá sesión con tu cuenta de Google.
1. Hacé clic en el botón **Crear cuenta**.
1. Completá los datos que te pide:
    - **Nombre de la cuenta:** el nombre de tu empresa o marca.
    - **País:** el tuyo.
    - **Nombre del contenedor:** escribí la dirección de tu tienda, por ejemplo
`mitienda.com`.
    - **Plataforma de destino:** elegí la opción **Web**.
1. Hacé clic en **Crear** y aceptá los términos que aparecen.
1. Se va a abrir una ventana con un código para instalar. **No hace falta que
copies ese bloque de código.** Cerrala con la **X**.
1. Arriba de la pantalla vas a ver un código que empieza con **`GTM-`**
(por ejemplo, `GTM-AB12CD3`). **Ese es el que necesitás.** Copialo o anotalo
en un lugar seguro.
✅ **Al terminar este paso tenés:** tu código `GTM-XXXXXXX`.

---

### Paso 2 — Pegar ese código en tu backoffice

1. Ingresá a tu **backoffice**.
1. En el menú, entrá a la sección **Sitio web**.
1. Hacé clic en la pestaña **SEO** (también aparece como "Posicionamiento en
buscadores").
1. Buscá el campo que dice **"ID de Google Tag Manager"**.
1. Pegá ahí el código que empieza con **`GTM-`** que copiaste en el Paso 1.
1. Hacé clic en **Guardar**.
✅ **Al terminar este paso:** tu tienda ya está conectada a Tag Manager. Todavía
falta enlazar el tablero de Analytics para empezar a ver datos.

> Si algún día querés dejar de medir, volvé a este campo, borralo y guardá.

---

### Paso 3 — Crear el tablero en Google Analytics

Si ya tenés un código de Analytics que empieza con `G-`, pasá directo al Paso 4.

1. Entrá a [**https://analytics.google.com**](https://analytics.google.com/) con
la misma cuenta de Google.
1. Abajo a la izquierda, hacé clic en el engranaje **Administrar**.
1. Hacé clic en **Crear** y luego en **Propiedad**.
1. Poné un nombre (por ejemplo, el de tu tienda), elegí tu **zona horaria** y tu
**moneda**, y seguí adelante.
1. Cuando te pregunte por la plataforma, elegí **Web**.
1. Ingresá la dirección de tu tienda (por ejemplo, `https://mitienda.com`) y
creá el flujo de datos.
1. Vas a ver un código que empieza con **`G-`** (por ejemplo, `G-AB12CD34EF`),
llamado **ID de medición**. Copialo o anotalo.
✅ **Al terminar este paso tenés:** tu código `G-XXXXXXXXXX`.

---

### Paso 4 — Enlazar el tablero dentro del conector

Este es el paso que une todo. Se hace dentro de Tag Manager.

1. Volvé a [**https://tagmanager.google.com**](https://tagmanager.google.com/) y
abrí el contenedor que creaste en el Paso 1.
1. En el menú de la izquierda, hacé clic en **Etiquetas** y después en el botón
**Nueva**.
1. Hacé clic en el recuadro de arriba, **Configuración de la etiqueta**.
1. En la lista que aparece, elegí **Google Analytics** y luego la opción
**Etiqueta de Google** (en inglés puede figurar como "Google Tag").
1. En el campo **ID de la etiqueta**, pegá el código que empieza con **`G-`**
que copiaste en el Paso 3.
1. Hacé clic en el recuadro de abajo, **Activación**, y elegí **All Pages**
(Todas las páginas). Esto hace que mida en todo el sitio.
1. Hacé clic en **Guardar** (arriba a la derecha). Si te pide un nombre, poné
algo como "Analytics - Todas las páginas".
✅ **Al terminar este paso:** el tablero y el conector ya están enlazados. Falta
un último paso para activarlo.

---

### Paso 5 — Publicar los cambios

En Tag Manager, nada se activa hasta que apretás **Publicar**.

1. Arriba a la derecha, hacé clic en el botón **Enviar**.
1. Poné un nombre a la versión (por ejemplo, "Instalé Analytics") y hacé clic en
**Publicar**.
✅ **Listo.** A partir de ahora tu tienda le manda datos a Google Analytics.

---

### Paso 6 — Comprobar que esté funcionando

1. En **Google Analytics**, entrá a **Informes** y luego a **Tiempo real**.
1. En otra pestaña (o desde tu teléfono), abrí tu tienda y navegá un poco.
1. En unos segundos, en el informe de Tiempo real deberías verte a vos mismo como
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
Revisá tres cosas: (1) que en el backoffice hayas pegado el código `GTM-` y
guardado; (2) que en Tag Manager hayas apretado **Publicar** (Paso 5); (3) que
en el Paso 4 hayas pegado bien el código `G-`. Si tenés un bloqueador de
publicidad activo en tu navegador, puede ocultar tu propia visita: probá desde
el teléfono con datos móviles.

**¿Puedo sumar otras herramientas más adelante (Meta, Google Ads)?**
Sí. Esa es la ventaja de Tag Manager: podés agregar más etiquetas desde su panel,
sin tener que tocar de nuevo el backoffice.

**¿Cómo desactivo la medición?**
Entrá al backoffice, en **Sitio web → SEO**, borrá el código del campo
"ID de Google Tag Manager" y guardá.

<p class="doc-aliases" markdown>Términos relacionados: como instalar google analytics, google tag manager, google analytics</p>
