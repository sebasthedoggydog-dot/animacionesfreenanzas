# Escaleta técnica · Reel "Nuevos lanzamientos · Preventas"

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 17 s (510 frames) · H.264 + audio AAC (−14 LUFS)
**Ritmo:** 120 BPM (1 beat = 0,5 s), el mismo motor y el mismo ritmo que el Reel del sorteo.
**Archivos:**
- `output/preventas-freenanzas.mp4`: Reel con música y efectos
- `output/preventas-freenanzas-solo-efectos.mp4`: el mismo Reel solo con efectos, para usar una canción de Instagram
- `output/separa-tu-cupo-preventa.png`: **imagen fija** del llamado a la acción (Historia 9:16, dentro de márgenes, con espacio libre para el sticker de link)
- `preventas-freenanzas.html` / `cta-preventa.html`: fuentes · `audio/preventas_audio.py`: música y efectos
- `assets/logo-freenanzas-blanco.png`: logo en blanco (provisional, ver nota)
**Render:**
```
node render.mjs preventas-freenanzas.html             # video (sin audio)
python3 audio/preventas_audio.py                      # música + efectos
ffmpeg -i output/preventas-freenanzas.mp4 -i audio/preventas-mix.wav -map 0:v -map 1:a -c:v copy \
  -af loudnorm=I=-14:TP=-1 -c:a aac -b:a 192k -shortest output/final.mp4
node render.mjs cta-preventa.html --stills            # imagen del CTA
```

## Cambios de la versión 2 (pedidos por el equipo)
- Hook: solo "Nuevos lanzamientos · *Preventas*" (se quitaron la etiqueta "Freenanzas · Se viene" y las píldoras Nivel 3 / Nivel 4).
- Tarjetas Nivel 3 y Nivel 4: se quitó "Ver cómo funciona el programa →".
- El video **termina en la tarjeta del Nivel 4**. "Separa tu cupo en preventa" pasó a ser una imagen aparte para poner el link.
- Logo Freenanzas en blanco en la parte inferior de todas las escenas y de la imagen.
- Se agregaron música y efectos de sonido sincronizados.

> **Logo:** se reconstruyó a partir de una captura de 173 px. Funciona al tamaño del video, pero para la versión final conviene reemplazar `assets/logo-freenanzas-blanco.png` por el logo original (PNG transparente o SVG) y volver a renderizar.

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
- Las tarjetas de curso replican el componente de la web: degradado lavanda → blanco, borde morado claro, píldora lima "Preventa" y checks en cuadros lima.
- Colores: `#5723f4` · `#1a6f66` · `#c6fd34` · `#fdfdfc`, más tintes de apoyo tomados de la web (texto `#14112a`, lavanda `#f1edfe`).

## Escaleta

| # | Escena | Tiempo | Fondo | Transición de entrada |
|---|---|---|---|---|
| 1 | Hook: "Nuevos lanzamientos · *Preventas*" | 0,0–2,5 s | Morado | — |
| 2 | Identificación: dos dolores, uno por curso | 2,5–6,0 s | Verde | Wipe circular (2,2–2,6) |
| 3 | Tarjeta Nivel 3 | 6,0–12,0 s | Morado con trama de puntos | Panel sube desde abajo (5,7–6,1) |
| 4 | Tarjeta Nivel 4 (cierre del video) | 12,0–17,0 s | Verde con trama de puntos | Wipe lateral; la tarjeta 3 sale por la izquierda y la 4 entra por la derecha, como un carrusel (11,55–12,35) |

## Keyframes

"Entrada palabra": texto dentro de una máscara; sube de Y +150 → 0 y O 0 → 1 en 0,45 s, con Out Back (Overshoot ≈ 1,7).

### 1 · Hook (0–2,5 s)
| t | Capa | Animación |
|---|---|---|
| 0,15 / 0,35 | "Nuevos" / "lanzamientos" (serif 150 px) | Entrada palabra |
| 0,55–0,80 | Punto "·" lima | Pop de escala, Out Back Big |
| 0,60–1,00 | **"*Preventas*"** (serif cursiva lima 260 px) | Escala 1,8 → 1 · Blur 16 → 0 · O 0 → 1, Out Expo; pop en el beat a 1,5 s |
| 1,00–1,35 | Subrayado lima | Escala X 0 → 1 desde la izquierda, Out Expo |
| 0,90–1,40 | Logo Freenanzas blanco (abajo, 400 px de ancho) | Y 30 → 0 con fundido; queda fijo hasta el final |
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
| salida | N3: sale a X −1250 con rotación −8° (In Expo). N4: se queda fija hasta el final del video | |

### Imagen CTA: "Separa tu cupo en preventa" (estática)
Historia 9:16 sobre morado con trama de puntos. Lleva "Separa tu cupo" (sans 84 px) y "*en preventa*" (serif cursiva lima 156 px) con subrayado lima. Debajo van dos tarjetas blancas: "NIVEL 3 · Tu primer *depa de inversión.*" y "NIVEL 4 · Declara tus inversiones *sin miedo.*".
- **Márgenes:** el contenido queda dentro de x 120–960 px y empieza en y = 400 px, sin tocar los bordes ni la zona de la interfaz.
- El espacio entre las tarjetas y el logo queda libre para poner el sticker de link.
- El logo blanco va en la misma posición que en el video: 400 px de ancho, centrado, y = 1625 px.

## Audio (incluido)
Sintetizado por código en `audio/preventas_audio.py`: sin samples ni pistas con derechos de autor.
- **Música:** pop electrónico a 120 BPM. Progresión C – G – Am – F (un compás = 2 s): pad, bajo en corcheas, kick en negras, clap en 2 y 4, hi-hats en contratiempo y arpegio de campanitas. Tiene efecto *sidechain* (la música "respira" con el kick), resuelve en C a los 16 s y hace fade out.
- **Efectos, en los mismos tiempos que la animación:** riser de entrada · swish en cada palabra · **impacto** en "*Preventas*" (0,6 s) · destellos sonoros · *whoosh* en cada transición (2,2 · 5,7 · 11,6 s) · golpe suave cuando aterriza cada tarjeta · tecleo en "NIVEL 3/4" · *pop* en las píldoras y chips · campanita en "Excel de 59 depas de regalo" (9,6 s) · *tick* en cada check.
- Mezcla normalizada a −14 LUFS (estándar de Instagram y TikTok). También se exportan los stems `preventas-musica.wav` y `preventas-sfx.wav`.
- Si prefieres un audio de tendencia de Instagram, usa `preventas-freenanzas-solo-efectos.mp4` y agrega la canción desde la app.

## Prompts visuales (fondos y variantes con IA)
**Estilo base:** flat vector motion graphics, editorial fintech style, elegant condensed serif headlines with italic accent words, clean sans-serif body, monospace uppercase labels, palette electric purple #5723f4, deep teal #1a6f66, neon lime #c6fd34, off-white #fdfdfc, soft lavender card surfaces, subtle dot grid, generous negative space, vertical 9:16, no photorealism, no clutter

1. **Hook:** solid electric purple background, huge italic serif word in neon lime with a lime underline, small monospace pill label at top, two lime rounded badges, scattered four-pointed lime and white sparkles, launch announcement mood
2. **Identificación:** deep teal background, left-aligned bold white sans questions, one phrase in lime italic serif, another phrase inside a lime marker box, calm and relatable
3. **Nivel 3:** purple dot-grid background, a large rounded white card with lavender gradient top, lime "Preventa" pill, small purple uppercase category label, serif headline with purple italic accent, a lime highlighted chip with a gift icon, three lime checkbox list items, minimal real estate investment course theme
4. **Nivel 4:** teal dot-grid background, same card system, serif headline "declare your investments without fear" mood, tax and dividends theme, lime checkboxes, clean and trustworthy
5. **Imagen CTA:** electric purple story background, big white sans headline with lime italic serif accent, two small white rounded cards listing the courses, monospace "tap the link" label with a lime down arrow pointing to empty space reserved for a link sticker, white wordmark logo at the bottom

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
> 👉 Separa tu cupo en preventa: link en la bio / en nuestra historia

*Si la preventa tiene un precio especial o cupos limitados, conviene sumarlo al copy y al CTA: es el mayor motivador de compra en una preventa.*
