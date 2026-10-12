# Escaleta técnica · Reel "¡SORTEO FREENANZAS!"

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 18 s (540 frames) · H.264
**Ritmo:** pista a **120 BPM** → 1 beat = 0,5 s · 1 compás (4 beats) = 2 s. Todas las entradas caen en beat o medio beat.
**Archivos:** `index.html` (animación real, abre en navegador) · `render.mjs` (exporta a MP4) · `output/sorteo-freenanzas.mp4` · `output/stills/` (fotogramas de cada escena)

> Las referencias de Instagram no se pudieron abrir desde el entorno de producción (acceso bloqueado). El sistema visual se construyó a partir de la paleta oficial y el estilo descrito en el brief. Conviene comparar los stills con los posts de referencia antes de publicar.

---

## 1. Sistema visual

| Token | HEX | Uso |
|---|---|---|
| Morado principal | `#5723f4` | Fondo de Hook, Sorpresa y CTA · tarjeta premio 1 · texto sobre lima |
| Verde institucional | `#1a6f66` | Fondo de Dolor · tarjeta premio 2 |
| Verde lima acento | `#c6fd34` | **Solo** palabras clave y CTA: SORTEO, miedo, empezar?, SORPRESA, marcas, caja "SORTEO" |
| Blanco | `#fdfdfc` | Texto principal · fondo de Premios |

**Regla de contraste:** lima nunca sobre blanco; sobre lima siempre texto morado o verde.

**Tipografía:** Poppins (Google Fonts), sans geométrica.
- Titulares: ExtraBold 800, tracking −2 %, interlineado 0,98
- Texto de apoyo: SemiBold 600
- Escala: H-Hero 150–178 px · H1 100–118 px · Body 66–84 px · Etiqueta 40 px (tracking +6 %)
- Alternativas si no hay Poppins: Montserrat ExtraBold, Gilroy ExtraBold, Outfit 800.

**Iconografía:** íconos de línea (trazo grueso y redondeado) dentro de círculos sólidos. Reemplazan a los emojis 🎁📈🎓👀 para que el video se vea igual en cualquier dispositivo. Los emojis quedan para el copy del post.

**Zonas seguras para Reels/TikTok:** el contenido crítico queda entre y = 250 y y = 1500 px y entre x = 90 y x = 990 px. Fuera de esa zona caen la interfaz de la app (caption, botones, avatar).

---

## 2. Escaleta por escenas

| # | Escena | In → Out | Duración | Beats | Fondo | Transición de salida |
|---|---|---|---|---|---|---|
| 1 | Hook | 0,00 → 2,50 | 2,5 s | 5 | Morado | Wipe circular verde desde el centro (2,20–2,60) |
| 2 | Dolor | 2,50 → 6,50 | 4,0 s | 8 | Verde | Panel morado sube desde abajo (6,20–6,60) |
| 3 | Sorpresa | 6,50 → 9,00 | 2,5 s | 5 | Morado + glow lima | Empuje a cámara del texto y wipe circular blanco (8,55–9,10) |
| 4 | Premios | 9,00 → 14,00 | 5,0 s | 10 | Blanco con trama de puntos | Tarjetas caen y wipe morado desde la derecha (13,60–14,10) |
| 5 | CTA | 14,00 → 18,00 | 4,0 s | 8 | Morado | Fin: el último frame funciona como portada y como loop |

Todas las transiciones de escena usan **Ease In-Out Expo** en 0,4 s, con bordes redondeados que se cierran durante el wipe. No hay cortes secos.

---

## 3. Keyframes por escena

Notación: `t` en segundos · `S` escala · `Y` desplazamiento vertical (px, + = abajo) · `R` rotación · `O` opacidad · `Blur` desenfoque gaussiano.
Equivalencias en After Effects: **Out Back** ≈ Overshoot 1,7 · **Out Back Big** ≈ Overshoot 2,6 · **Out Expo** ≈ influencia 90 % de salida · **Elastic** ≈ expresión `inertialBounce` (amp 0,06 · freq 3 · decay 6).

"Entrada palabra" (patrón base de kinetic typography): el texto está dentro de una máscara (track matte del alto de la línea) y sube de Y +140 → 0, con O 0 → 1, en 0,45 s y Out Back.

### Escena 1 · Hook: 🎁 ¡SORTEO FREENANZAS!
| t | Capa | Keyframe | Easing |
|---|---|---|---|
| 0,00–0,60 | Anillos lima (16 % opacidad) | S 0,4 → 1 · R 0 → 20° · O 0 → 1; luego rotan sin parar hasta 45° | Out Expo, luego lineal |
| 0,00–0,45 | Ícono regalo (círculo lima) | S 0 → 1 · R −25° → 0° | Out Back Big |
| 0,25–0,60 | **"¡SORTEO"** (lima, 178 px) | S 1,9 → 1 · O 0 → 1 · Blur 14 → 0 (el golpe "explosivo") | Out Expo |
| 0,30–1,70 | Confeti (22 piezas lima/blanco/verde) | Ráfaga radial de 380–640 px con leve caída por gravedad; gira 260° y O 1 → 0 | Out Expo |
| 0,60–1,05 | "FREENANZAS!" (blanco, 118 px) | Entrada palabra | Out Back |
| 0,75–1,30 | Ícono regalo | Sacudida: S 1,08 · R −6° → 4° → 0° | Out Cubic |
| 0,95–1,35 | Barra lima bajo el título | Escala X 0 → 1 desde la izquierda | Out Expo |
| 1,50–1,80 | "¡SORTEO" | Pop en el beat: S 1 → 1,07 → 1 | Out Back |

### Escena 2 · Dolor: ¿Aún te da miedo invertir y no sabes por dónde empezar?
Texto alineado a la izquierda (margen 96 px), en dos bloques de tres líneas. Un "?" gigante (1100 px, blanco al 6 %) sube en parallax de fondo.

| t | Capa | Keyframe | Easing |
|---|---|---|---|
| 2,60 | "¿Aún te da" (104 px) | Entrada palabra | Out Back |
| 3,00–3,55 | **"miedo"** (lima, 176 px) | Y 160 → 0 · S 0,6 → 1,12 → 1 | Out Back |
| 3,60–3,90 | "miedo" | Temblor en X: −10 / +9 / −7 / +5 / 0 px (expresa miedo) | Lineal |
| 3,50 | "invertir" | Entrada palabra | Out Back |
| 4,25 | "y no sabes" | Entrada palabra | Out Back |
| 4,75 | "por dónde" | Entrada palabra | Out Back |
| 5,25–5,70 | **"empezar?"** (verde sobre caja lima, 150 px) | Y 170 → 0 · S 0,8 → 1 | Out Back |
| 5,60–5,95 | Caja lima detrás de "empezar?" | Escala X 0 → 1 desde la izquierda (efecto marcador) | Out Expo |

### Escena 3 · Sorpresa: ¡Tenemos una sorpresa para ti! 👀
| t | Capa | Keyframe | Easing |
|---|---|---|---|
| 6,55 | "¡Tenemos una" (100 px) | Entrada palabra | Out Back |
| 6,60–7,30 | Glow radial lima detrás | S 0,3 → 1 · O 0 → 1, luego crece a 1,15 hasta el final | Out Expo |
| 6,85–7,55 | **"SORPRESA"** (lima, 150 px) | S 0,2 → 1 con rebote · Blur 10 → 0 | Elastic |
| 7,00–7,70 | 6 destellos (estrellas de 4 puntas) | S 0 → 1 · R −90° → 0°, escalonados cada 0,12 s; luego flotan | Out Back Big |
| 7,40 | "para ti!" | Entrada palabra | Out Back |
| 7,60–8,00 | Ojos 👀 (ilustración vectorial) | S 0 → 1 · R −20° → 0° | Out Back Big |
| 8,00–8,50 | Pupilas | Miran a la izquierda (−14 px) y después a la derecha (+14 px) | In-Out Cubic |
| 8,55–9,00 | Bloque de texto | S 1 → 1,9 · O 1 → 0 · Blur 0 → 8 (empuje a cámara) | In Expo |

### Escena 4 · Premios
| t | Capa | Keyframe | Easing |
|---|---|---|---|
| 9,00–9,35 | Píldora "SORTEO FREENANZAS" | S 0 → 1 | Out Back Big |
| 9,20 | "Te puedes llevar:" (morado, 96 px) | Entrada palabra | Out Back |
| 9,60 / 10,10 / 10,60 | Tarjetas 1 / 2 / 3 (de arriba hacia abajo, un beat entre cada una) | Y −120 → 0 · O 0 → 1 · S 0,92 → 1 en 0,5 s | Out Back |
| +0,20 de cada tarjeta | Ícono de la tarjeta | S 0 → 1 · R −30° → 0° | Out Back Big |
| 11,60 / 11,85 / 12,10 | Íconos | "Respiración" en cadena: S 1 → 1,15 → 1 (recordatorio visual de los tres premios) | Out Back |
| 13,60–14,01 | Tarjetas (desfase de 0,06 s) | Y 0 → 80 · O 1 → 0 | In Cubic |

Diseño de tarjetas (900 × 250 px, radio 44, sombra morada al 18 %):
- **📈 Una cuenta Trii Pro:** fondo morado · ícono de gráfico al alza en círculo lima · "Trii Pro" en lima 84 px
- **🎓 Una beca Bursen:** fondo verde · birrete en círculo lima · "Bursen" en lima
- **🎁 Bono especial de Freenanzas:** fondo lima · regalo en círculo morado · "Freenanzas" en morado

### Escena 5 · CTA: ¿Quieres participar? Comenta "SORTEO" y te contamos cómo.
| t | Capa | Keyframe | Easing |
|---|---|---|---|
| 14,15 / 14,35 | "¿Quieres" / "participar?" (104 px) | Entrada palabra | Out Back |
| 14,85 | "Comenta" (84 px, SemiBold) | Entrada palabra | Out Back |
| 15,10–15,60 | **Caja lima "SORTEO"** (texto morado, 150 px) | S 0 → 1 · R −12° → −3° (queda ligeramente inclinada, estilo sticker) | Out Back Big |
| 15,60 → fin | Caja "SORTEO" | **Pulso** cada 1 s (2 beats): S 1 → 1,045 → 1 en 0,35 s | Seno |
| 15,60 → fin | Anillo lima alrededor de la caja | Onda que se expande cada 1 s: S 1 → 1,22 · O 0,9 → 0 | Out Cubic |
| 15,60 | "y te contamos cómo" (66 px) | Entrada palabra | Out Back |
| 16,00–16,40 | Burbuja de comentario + flecha ↓ | Y 60 → 0 · O 0 → 1; la flecha rebota 16 px cada medio beat (señala la caja de comentarios) | Out Back |
| 16,30–16,80 | Firma "FREENANZAS" (tracking +32 %, blanco al 75 %) | O 0 → 1 · Y 20 → 0 | Out Cubic |

---

## 4. Audio (recomendación de edición)
- Pista: pop/electrónica motivacional a **120 BPM**, sin voz, con drop o golpe en **0,25 s** (entrada de "¡SORTEO").
- SFX sutiles: *whoosh* en cada wipe (2,2 · 6,2 · 8,6 · 13,7) · *pop* en "miedo", "SORPRESA", cada tarjeta y la caja SORTEO · *sparkle* en los destellos (7,0) · *tick* suave en cada pulso del CTA.
- Si la pista es de otro BPM, multiplica los tiempos por 120/BPM o mueve solo los keyframes "Entrada palabra" al beat más cercano.

---

## 5. Prompts visuales por bloque
Sirven para generar fondos, variantes o storyboards en Midjourney, Firefly, Ideogram, Runway o Canva AI. El texto final siempre se monta en edición, nunca generado por IA.

**Prompt de estilo base** (añadir a todos):
> flat vector motion graphics, bold geometric sans-serif typography, clean minimal layout, generous negative space, strict brand palette: electric purple #5723f4, deep teal green #1a6f66, neon lime #c6fd34, off-white #fdfdfc, no gradients except soft radial glow, no 3D, no photorealism, no clutter, vertical 9:16, social media reel frame, fintech education brand

**Escena 1 · Hook**
> Solid electric purple #5723f4 background, a neon lime #c6fd34 circular badge with a minimal outline gift box icon in purple at center, burst of small lime and white geometric confetti radiating outward, faint thin concentric lime rings rotating behind, empty space for a huge bold headline, energetic celebratory giveaway announcement, flat vector, 9:16

**Escena 2 · Dolor**
> Solid deep teal green #1a6f66 background, giant semi-transparent white question mark on the right edge as a background shape, left-aligned stacked bold white typography blocks, one word highlighted with a neon lime #c6fd34 marker rectangle, calm but tense mood, editorial minimal layout, flat vector, 9:16

**Escena 3 · Sorpresa**
> Electric purple #5723f4 background with a soft neon lime radial glow in the center, small four-pointed lime and white sparkle stars scattered, a pair of cute cartoon eyes (white with dark pupils) looking sideways, surprise reveal moment, playful but clean, flat vector, 9:16

**Escena 4 · Premios**
> Off-white #fdfdfc background with a subtle purple dot grid pattern, three stacked rounded rectangle cards with soft purple shadow: first card electric purple with a lime circle containing a rising chart icon, second card teal green with a lime circle containing a graduation cap icon, third card neon lime with a purple circle containing a gift icon, clean UI card layout, fintech prize list, flat vector, 9:16

**Escena 5 · CTA**
> Electric purple #5723f4 background, a bold neon lime #c6fd34 rounded sticker-style box slightly tilted at the center with a glowing lime outline ring pulsing around it, below it a minimal lime chat bubble icon and a downward arrow, strong call to action to comment, clean and bold, flat vector, 9:16

**Negative prompt:** photorealistic, 3D render, gradient mesh, busy background, extra text, misspelled letters, watermark, stock photo people, drop shadows heavy, neon glow overload, colors outside palette

---

## 6. Copy sugerido para el post
> 🎁 ¡SORTEO FREENANZAS! 🎁
> ¿Aún te da miedo invertir? Tenemos una sorpresa para ti 👀
> 📈 Una cuenta Trii Pro
> 🎓 Una beca Bursen
> 🎁 Bono especial de Freenanzas
> 👉 Comenta **SORTEO** y te contamos cómo participar.

*(Agregar bases legales, fechas y mecánica del sorteo en el comentario fijado o en el link de la bio.)*

---

## 7. Cómo usar los archivos
- **Ver / revisar:** abre `index.html` en Chrome. Se reproduce en loop y tiene barra para ir a cualquier segundo.
- **Exportar MP4:** `npm i playwright` (o usa una instalación global) y ejecuta `node render.mjs` (requiere `ffmpeg`). Sale `output/sorteo-freenanzas.mp4`.
- **Stills por escena:** `node render.mjs --stills` → `output/stills/`.
- **Para After Effects o CapCut:** usa las tablas de la sección 3 como hoja de keyframes. Los tiempos están en segundos; para pasarlos a frames multiplica × 30.
