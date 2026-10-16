# Historias · Asistente BVL y Bolsa de Lima

Dos historias de Instagram. Cada una tiene **un video** (9:16, 30 fps, con música y efectos a −14 LUFS) y **una imagen** con espacio libre para el sticker de link. No llevan precios.

Usan el estilo del Kit Inversor v2: degradado morado o verde con cuadrícula, Poppins, Playfair cursiva lima, etiquetas Oswald con punto lima, íconos 3D (Fluent Emoji, MIT), estrellas y puntos, y el logo oficial SVG abajo. El estilo y el motor de animación son compartidos: `lib/estilo.css` y `lib/motor.js`.

> **Contenido:** freenanzas.app no abre desde el entorno de producción, así que los textos salen de lo que muestran los buscadores sobre `/herramientas` y `/bolsa-lima`. Conviene revisarlos contra la web antes de publicar, sobre todo las funciones del Asistente BVL y cuál es el **regalo** por registrarse.

## Archivos
| Historia | Video | Video solo con efectos | Imagen | Fuentes |
|---|---|---|---|---|
| 1 · Asistente BVL | `output/historia-asistente-bvl.mp4` (15 s) | `output/historia-asistente-bvl-solo-efectos.mp4` | `output/historia-asistente-bvl-imagen.png` | `historia-asistente-bvl.html`, `historia-asistente-bvl-imagen.html`, `audio/historia_asistente_bvl_audio.py` |
| 2 · Bolsa de Lima | `output/historia-bolsa-lima.mp4` (16 s) | `output/historia-bolsa-lima-solo-efectos.mp4` | `output/historia-bolsa-lima-imagen.png` | `historia-bolsa-lima.html`, `historia-bolsa-lima-imagen.html`, `audio/historia_bolsa_lima_audio.py` |

Render: `node render.mjs <archivo>.html` (video) · `python3 audio/<nombre>_audio.py` (audio) · mezcla con `ffmpeg` (igual que en las demás escaletas) · `node render.mjs <archivo>-imagen.html --stills` (imagen).

## Historia 1 · Asistente BVL
| Tiempo | Escena | Contenido y animación |
|---|---|---|
| 0–2,5 s | Hook (morado) | 🤖 El robot 3D entra con rebote. Luego "◉ HERRAMIENTA FREENANZAS", "Tu Asistente" y "*BVL*" (cursiva lima de 280 px, con impacto) |
| 2,5–6,5 s | Proyecta (verde) | "Proyecta tus ganancias *antes de invertir un sol*". Tarjeta "Tu proyección" con 5 barras que crecen (la última en lima) y la píldora "SIMULACIÓN" |
| 6,5–11,5 s | Qué puedes hacer (morado) | Tres tarjetas, una cada 1 s: 🔍 "Analiza acciones de la BVL · con datos reales de la Bolsa de Lima", 📊 "Proyecta tus ganancias · simula escenarios antes de comprar" y 📱 "Sigue tu inversión · mira cuánto vas ganando" |
| 11,5–15 s | Regalo (verde) | 🎁 El regalo entra y se sacude, 🎉 serpentina, "◉ SOLO POR REGISTRARTE", "Regístrate y *llévate un regalo*" |

**Imagen:** "Regístrate en el *Asistente BVL*" con dos tarjetas lima: 🎁 "REGALO POR REGISTRARTE · Regístrate y llévate un regalo" y 📊 "DATOS REALES DE LA BVL · Proyecta tus ganancias antes de invertir". Debajo queda el espacio para el link.

## Historia 2 · Bolsa de Lima (Nivel 1)
| Tiempo | Escena | Contenido y animación |
|---|---|---|
| 0–2,5 s | Hook (morado) | 🏛️ Edificio de la bolsa, "◉ NIVEL 1 · EL FAVORITO", "Invierte en la *Bolsa de Lima*" |
| 2,5–7 s | Ruta (verde) | "¿Nunca has invertido? *Empieza aquí*". Una ruta paso a paso cuya línea avanza y enciende cada número: 1 Abre tu cuenta en un broker verificado → 2 Analiza acciones y dividendos → 3 Proyecta tus ganancias → 4 **Compra tu primera acción** ⛳ |
| 7–12 s | Qué incluye (morado) | 🎬 "5 clases grabadas · disponibles por 1 año", 📅 "30 días de acompañamiento" y 🧰 "Plantillas y herramientas", con chips de **Proyección de ganancias** (destacado), Jubilación y Lista de acciones |
| 12–16 s | Cierre (verde) | 🚀 El cohete despega, "Tu primera acción *está más cerca*" y la píldora "✓ SIN ERRORES DE PRINCIPIANTE" |

**Imagen:** "Empieza en la *Bolsa de Lima*" con dos tarjetas lima: ⛳ "NIVEL 1 · RUTA PASO A PASO · Hasta tu primera acción" y 🎬 "INCLUYE · 5 clases + 30 días de acompañamiento". Debajo queda el espacio para el link.
