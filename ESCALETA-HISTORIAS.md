# Historias · Asistente BVL, Bolsa de Lima y Bolsa Extranjera

Tres historias de Instagram. Cada una tiene **un video** (9:16, 30 fps, con música y efectos a −14 LUFS) y **una imagen** con espacio libre para el sticker de link. No llevan precios.

Usan el estilo del Kit Inversor v2: degradado morado o verde con cuadrícula, Poppins, Playfair cursiva lima, etiquetas Oswald con punto lima, íconos 3D (Fluent Emoji, MIT), estrellas y puntos, y el logo oficial SVG abajo. El estilo y el motor de animación son compartidos: `lib/estilo.css` y `lib/motor.js`.

> **Contenido:** freenanzas.app no abre desde el entorno de producción, así que los textos salen de lo que muestran los buscadores sobre `/herramientas` y `/bolsa-lima`. Conviene revisarlos contra la web antes de publicar, sobre todo las funciones del Asistente BVL y cuál es el **regalo** por registrarse.

## Archivos
| Historia | Video | Video solo con efectos | Imagen | Fuentes |
|---|---|---|---|---|
| 1 · Asistente BVL | `output/historia-asistente-bvl.mp4` (15 s) | `output/historia-asistente-bvl-solo-efectos.mp4` | `output/historia-asistente-bvl-imagen.png` | `historia-asistente-bvl.html`, `historia-asistente-bvl-imagen.html`, `audio/historia_asistente_bvl_audio.py` |
| 2 · Bolsa de Lima | `output/historia-bolsa-lima.mp4` (20 s) | `output/historia-bolsa-lima-solo-efectos.mp4` | `output/historia-bolsa-lima-imagen.png` | `historia-bolsa-lima.html`, `historia-bolsa-lima-imagen.html`, `audio/historia_bolsa_lima_audio.py` |
| 3 · Bolsa Extranjera | `output/historia-bolsa-extranjera.mp4` (16 s) | `output/historia-bolsa-extranjera-solo-efectos.mp4` | `output/historia-bolsa-extranjera-imagen.png` | `historia-bolsa-extranjera.html`, `historia-bolsa-extranjera-imagen.html`, `audio/historia_bolsa_extranjera_audio.py` |

Render: `node render.mjs <archivo>.html` (video) · `python3 audio/<nombre>_audio.py` (audio) · mezcla con `ffmpeg` (igual que en las demás escaletas) · `node render.mjs <archivo>-imagen.html --stills` (imagen).

## Historia 1 · Asistente BVL
| Tiempo | Escena | Contenido y animación |
|---|---|---|
| 0–2,5 s | Hook (morado) | 🤖 El robot 3D entra con rebote. Luego "◉ HERRAMIENTA FREENANZAS", "Tu Asistente" y "*BVL*" (cursiva lima de 280 px, con impacto) |
| 2,5–6,5 s | Proyecta (verde) | "Proyecta tus ganancias *antes de invertir un sol*". Tarjeta "Tu proyección" con 5 barras que crecen (la última en lima) y la píldora "SIMULACIÓN" |
| 6,5–11,5 s | Qué puedes hacer (morado) | Tres tarjetas, una cada 1 s: 🔍 "Analiza acciones de la BVL · con datos reales de la Bolsa de Lima", 📊 "Proyecta tus ganancias · simula escenarios antes de comprar" y 📱 "Sigue tu inversión · mira cuánto vas ganando" |
| 11,5–15 s | Regalo (verde) | 🎁 El regalo entra y se sacude, 🎉 serpentina, "◉ SOLO POR REGISTRARTE", "Regístrate y *llévate un regalo*" |

**Imagen:** "Regístrate en el *Asistente BVL*" con dos tarjetas lima: 🎁 "REGALO POR REGISTRARTE · Regístrate y llévate un regalo" y 📊 "DATOS REALES DE LA BVL · Proyecta tus ganancias antes de invertir". Debajo queda el espacio para el link.

## Historia 2 · Bolsa de Lima (Nivel 1) · v2
| Tiempo | Escena | Contenido y animación |
|---|---|---|
| 0–2,5 s | Hook (morado) | 🏛️ Edificio de la bolsa, "◉ NIVEL 1 · EL FAVORITO", "Invierte en la *Bolsa de Lima*" |
| 2,5–6,5 s | **Empresas que ya conoces (verde, nueva)** | Etiqueta "◉ EMPRESAS QUE YA CONOCES" y 4 tarjetas que entran con pop: **BCP** (banca), **BBVA** (banca), **Alicorp** (consumo) y **Minsur** (minería). Luego "con retornos de *+13% anual*" (impacto y pop) y la nota "Rentabilidad histórica referencial. No garantiza resultados futuros." |
| 6,5–11 s | Ruta (morado) | "¿Nunca has invertido? *Empieza aquí*". Ruta animada: broker verificado → analiza acciones y dividendos → proyecta ganancias → **compra tu primera acción** ⛳ |
| 11–16 s | Qué incluye (verde) | 🎬 5 clases grabadas (1 año) · 📅 30 días de acompañamiento · 🧰 plantillas (Proyección de ganancias, Jubilación, Lista de acciones) |
| 16–20 s | Cierre (morado) | 🚀 "Tu primera acción *está más cerca*" y "✓ SIN ERRORES DE PRINCIPIANTE" |

**Imagen (v2):** cohete pequeño, "◉ BOLSA DE LIMA · NIVEL 1", "Tu primera acción" y "*está más cerca*" con subrayado, más el espacio libre para el link. Se quitaron las tarjetas para que respire más.

> **Verificar:** "BCP" se interpretó de "MCP" en el audio. El "+13% anual" es el dato que pidió el equipo: conviene tener su fuente a mano y mantener la nota de que la rentabilidad pasada no garantiza resultados futuros.

## Historia 3 · Bolsa Extranjera (Nivel 2)
Contenido según la página `/bolsa-extranjera` (vía buscador): 5 clases grabadas, 30 días de acompañamiento, guía para abrir tu broker internacional, ETFs y fondos mutuos, y plantilla de impuestos para declarar a SUNAT. No lleva precio.

| Tiempo | Escena | Contenido y animación |
|---|---|---|
| 0–2,5 s | Hook (morado) | 🌎 El globo entra girando, "◉ NIVEL 2 · BOLSA EXTRANJERA", "Invierte en el *mundo*" |
| 2,5–7 s | Ruta (verde) | "Desde Perú, *paso a paso*": 1 Abre tu broker internacional → 2 Haz tu primer depósito → 3 Compra tu primer ETF → 4 **Diversifica tu portafolio** 📈 |
| 7–12 s | Qué incluye (morado) | 🎬 5 clases grabadas · 📅 30 días de acompañamiento · 🧰 guías y plantillas (**Plantilla de impuestos**, Broker internacional, ETFs vs. fondos mutuos) |
| 12–16 s | Cierre (verde) | 🌎 + 🚀 "Invierte *sin fronteras*" y "✓ Y DECLARA TUS IMPUESTOS SIN MIEDO" |

**Imagen:** globo pequeño, "◉ BOLSA EXTRANJERA · NIVEL 2", "Invierte" y "*sin fronteras*", más el espacio libre para el link.
