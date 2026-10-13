# Escaleta técnica · Reel "Nuevos lanzamientos · Preventas"

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 21 s (630 frames) · H.264
**Ritmo:** 120 BPM (1 beat = 0,5 s), el mismo motor y el mismo ritmo que el Reel del sorteo.
**Archivos:** `preventas-freenanzas.html` (animación) · `output/preventas-freenanzas.mp4` · `output/stills/preventas-freenanzas/`
**Render:** `node render.mjs preventas-freenanzas.html` (con `--stills` exporta solo los fotogramas clave)

## Fuente del contenido
El contenido sale de la sección "Nuevos lanzamientos · Preventas" de freenanzas.app (captura compartida por el equipo). No se pudo abrir la web desde el entorno de producción, así que **no hay precios, cupos ni descuentos de preventa en el video**: solo aparece lo que muestra la web.

| | Nivel 3 | Nivel 4 |
|---|---|---|
| Categoría | Inversión inmobiliaria | Declaración de impuestos |
| Título | Tu primer *depa de inversión.* | Declara tus inversiones *sin miedo.* |
| Promesa | Elige tu depa, conoce los gastos y aprende a alquilarlo. | Prepara tu declaración anual de acciones con más claridad. |
| Temario | Qué depa te conviene · Cómo comprarlo con el banco · Cómo alquilarlo en Airbnb | Dividendos y ganancias · Brokers y reportes · Caso práctico real |
| Bono | Excel de 59 depas de regalo | — |
| Disponible | Diciembre 2026 | Marzo 2027 |

## Sistema visual
Toma la paleta del sorteo y suma el lenguaje tipográfico de la web:
- **Instrument Serif** (con su cursiva) para titulares; la palabra clave va en cursiva morada o lima, igual que en la web ("*depa de inversión.*", "*sin miedo.*", "*Preventas*").
- **Plus Jakarta Sans** 800 para las frases de impacto y 500 para el texto de apoyo.
- **DM Mono** en mayúsculas con tracking amplio para etiquetas ("NIVEL 3", "LINK EN NUESTRA BIO").
- Las tarjetas de curso replican el componente de la web: degradado lavanda → blanco, borde morado claro, píldora lima "Preventa", checks en cuadros lima y el link "Ver cómo funciona el programa →".
- Colores: `#5723f4` · `#1a6f66` · `#c6fd34` · `#fdfdfc`, más tintes de apoyo tomados de la web (texto `#14112a`, lavanda `#f1edfe`).

## Escaleta

| # | Escena | Tiempo | Fondo | Transición de entrada |
|---|---|---|---|---|
| 1 | Hook: "Nuevos lanzamientos · *Preventas*" | 0,0–2,5 s | Morado | — |
| 2 | Identificación: dos dolores, uno por curso | 2,5–6,0 s | Verde | Wipe circular (2,2–2,6) |
| 3 | Tarjeta Nivel 3 | 6,0–12,0 s | Morado con trama de puntos | Panel sube desde abajo (5,7–6,1) |
| 4 | Tarjeta Nivel 4 | 12,0–17,0 s | Verde con trama de puntos | Wipe lateral; la tarjeta 3 sale por la izquierda y la 4 entra por la derecha, como un carrusel (11,55–12,35) |
| 5 | CTA: separa tu cupo en freenanzas.app | 17,0–21,0 s | Morado | Wipe circular (16,7–17,1) |

## Keyframes

"Entrada palabra": texto dentro de una máscara; sube de Y +150 → 0 y O 0 → 1 en 0,45 s, con Out Back (Overshoot ≈ 1,7).

### 1 · Hook (0–2,5 s)
| t | Capa | Animación |
|---|---|---|
| 0,00–0,35 | Etiqueta mono "FREENANZAS · SE VIENE" | Escala 0,6 → 1, Out Back |
| 0,15 / 0,35 | "Nuevos" / "lanzamientos" (serif 150 px) | Entrada palabra |
| 0,55–0,80 | Punto "·" lima | Pop de escala, Out Back Big |
| 0,60–1,00 | **"*Preventas*"** (serif cursiva lima 260 px) | Escala 1,8 → 1 · Blur 16 → 0 · O 0 → 1, Out Expo; pop en el beat a 1,5 s |
| 1,00–1,35 | Subrayado lima | Escala X 0 → 1 desde la izquierda, Out Expo |
| 1,25 / 1,40 | Píldoras "Nivel 3" / "Nivel 4" | Y 60 → 0 · escala 0,5 → 1, Out Back Big |
| 0,8 → | 6 destellos | Aparecen girando cada 0,1 s |

### 2 · Identificación (2,5–6 s)
"¿Quieres tu *primer depa* de inversión?" y "¿Y declarar tus inversiones *sin miedo*?"
- Las líneas entran a 2,55 · 2,85 · 3,25 · 4,00 · 4,35 · 4,75 s, en beat y medio beat.
- "*primer depa*" (serif lima 140 px) sale con pop de escala hasta 1,08.
- "*sin miedo?*" queda en una caja lima que barre de izquierda a derecha (5,05–5,40), efecto marcador.

### 3 · Nivel 3 (6–12 s) y 4 · Nivel 4 (12–17 s)
La tarjeta se construye por capas, en el mismo orden en que se lee:

| Desfase | Capa | Animación |
|---|---|---|
| +0,00 | Tarjeta | N3: Y +260 → 0 · escala 0,92 → 1 · rotación 2° → 0°. N4: entra desde X +1250 con rotación 8° → 0°. Out Back |
| +0,35 | "NIVEL 3/4" (mono) | Efecto máquina de escribir, 22 caracteres por segundo |
| +0,55 | Píldora "Preventa" | Pop con giro de −10°; segundo pop a +1,1 s |
| +0,70 | Categoría | X −40 → 0 con fundido |
| +0,95 | Líneas del título (serif 116 px) | Entrada palabra, una cada 0,25 s; la cursiva morada va al final |
| tras el título | Subrayado lima bajo la cursiva | Escala X 0 → 1, Out Expo |
| +0,15 | Texto de apoyo | Y 30 → 0 con fundido |
| +0,55 | Chips | Pop Out Back Big, cada 0,25 s. El chip "Excel de 59 depas de regalo" se sacude a los 9,6 s para destacar el bono |
| N3: 9,0 s · N4: 14,25 s | 3 ítems del temario | Uno por beat: X −60 → 0; el check se dibuja con trazo animado (0,3 s) |
| +1,4 | Línea punteada | Escala X 0 → 1 |
| +1,6 | "Ver cómo funciona el programa →" | Sube con fundido; la flecha empuja 12 px cada medio beat |
| salida | N3: sale a X −1250 con rotación −8° (In Expo). N4: cae Y +120 y se desvanece (In Cubic) | |

### 5 · CTA (17–21 s)
| t | Capa | Animación |
|---|---|---|
| 17,10 | "Separa tu cupo" (sans 112 px) | Entrada palabra |
| 17,35–17,75 | **"*en preventa*"** (serif cursiva lima 200 px) | Escala 1,7 → 1 con desenfoque, Out Expo |
| 17,80 | Barra de navegador con candado | Sube con escala 0,9 → 1 |
| 18,20 → | "freenanzas.app" | Se escribe letra a letra, con cursor de texto parpadeante |
| 18,60–19,25 | Puntero del mouse | Entra en diagonal y hace clic (escala 0,8 → 1) |
| 19,15–19,55 | Botón lima "Ver cómo funciona →" | Pop Out Back Big; desde ahí late cada 1 s con una onda lima expansiva |
| 19,60 | "LINK EN NUESTRA BIO" (mono) | Fundido hacia arriba |
| 19,80 / 19,95 | "NIVEL 3 · DIC 2026" / "NIVEL 4 · MAR 2027" | Suben, Out Back |

## Audio
- 120 BPM, pop/electrónica optimista. Un golpe fuerte en 0,6 s ("*Preventas*").
- SFX: *whoosh* en cada transición (2,2 · 5,7 · 11,6 · 16,7) · *pop* en las píldoras "Preventa" · *tick* suave en cada check · tecleo en "freenanzas.app" (18,2–18,9) · *clic* a 19,1 s.

## Prompts visuales (fondos y variantes con IA)
**Estilo base:** flat vector motion graphics, editorial fintech style, elegant condensed serif headlines with italic accent words, clean sans-serif body, monospace uppercase labels, palette electric purple #5723f4, deep teal #1a6f66, neon lime #c6fd34, off-white #fdfdfc, soft lavender card surfaces, subtle dot grid, generous negative space, vertical 9:16, no photorealism, no clutter

1. **Hook:** solid electric purple background, huge italic serif word in neon lime with a lime underline, small monospace pill label at top, two lime rounded badges, scattered four-pointed lime and white sparkles, launch announcement mood
2. **Identificación:** deep teal background, left-aligned bold white sans questions, one phrase in lime italic serif, another phrase inside a lime marker box, calm and relatable
3. **Nivel 3:** purple dot-grid background, a large rounded white card with lavender gradient top, lime "Preventa" pill, small purple uppercase category label, serif headline with purple italic accent, a lime highlighted chip with a gift icon, three lime checkbox list items, minimal real estate investment course theme
4. **Nivel 4:** teal dot-grid background, same card system, serif headline "declare your investments without fear" mood, tax and dividends theme, lime checkboxes, clean and trustworthy
5. **CTA:** electric purple background, white browser URL bar pill with a lock icon and a mouse pointer clicking it, pulsing lime rounded button below, monospace "link in bio" label, two outlined date pills at the bottom

**Negative prompt:** photorealistic, 3D, stock people, cluttered UI, fake prices, extra text, misspelled words, colors outside palette

## Copy sugerido para el post
> 🚀 Nuevos lanzamientos en **preventa**
>
> 🏠 **Nivel 3 · Tu primer depa de inversión**
> Elige tu depa, conoce los gastos y aprende a alquilarlo (sí, también en Airbnb).
> 🎁 Incluye un Excel de 59 depas de regalo · Disponible en diciembre 2026
>
> 🧾 **Nivel 4 · Declara tus inversiones sin miedo**
> Dividendos, ganancias, brokers y reportes, con un caso práctico real · Disponible en marzo 2027
>
> 👉 Separa tu cupo en freenanzas.app (link en la bio)

*Si la preventa tiene un precio especial o cupos limitados, conviene sumarlo al copy y al CTA: es el mayor motivador de compra en una preventa.*
