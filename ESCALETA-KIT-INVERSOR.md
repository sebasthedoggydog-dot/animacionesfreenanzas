# Escaleta técnica · Reel "Kit Inversor"

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 19 s · H.264 + audio AAC (−14 LUFS)
**Ritmo:** 120 BPM (1 beat = 0,5 s). Usa el mismo motor, la misma tipografía y los mismos márgenes que los Reels de Sorteo y Preventas.

**Archivos**
- `output/kit-inversor.mp4`: Reel con música y efectos
- `output/kit-inversor-solo-efectos.mp4`: solo efectos, para usar una canción de Instagram
- `output/kit-inversor-cta.png`: **imagen fija** del CTA (Historia, con espacio libre para el sticker de link)
- `kit-inversor.html` / `cta-kit-inversor.html` / `audio/kit_audio.py`: fuentes
- `output/stills/kit-inversor/`: un fotograma de cada escena

**Render**
```
node render.mjs kit-inversor.html
python3 audio/kit_audio.py
ffmpeg -i output/kit-inversor.mp4 -i audio/kit-mix.wav -map 0:v -map 1:a -c:v copy \
  -af loudnorm=I=-14:TP=-1 -c:a aac -b:a 192k -shortest output/final.mp4
node render.mjs cta-kit-inversor.html --stills
```

## Contenido (tomado de la web)
- Etiqueta: ★ Kit Inversor · Más popular
- Titular: Los dos bootcamps completos, *en un solo kit.* Acceso a Bolsa Local (Nivel 1) y Bolsa Extranjera (Nivel 2).
- Incluye: dos bootcamps completos · guías y herramientas (guía de impuestos, plantillas, calculadoras y recursos) · acompañamiento por 60 días.
- Exclusivo, solo para los 10 primeros: sesión en vivo de preguntas y respuestas (Q&A) con el equipo Freenanzas.
- Precio: pago único de **$399 USD** (antes $559 USD). Ahorras $160.
- Widget "Mi inversión: +S/ 688.98 (11.60%)": recreado como gráfico vectorial a partir de la imagen de la web.

## Reglas aplicadas (feedback de los Reels anteriores)
- El contenido queda dentro de x 100–980 px y por encima del logo. Cada bloque va centrado verticalmente.
- El logo Freenanzas va en blanco, abajo, igual en todas las escenas (400 px de ancho, y = 1625).
- El video no lleva botones ni links ("Quiero el kit", WhatsApp). El CTA va en una imagen aparte, con hueco para el sticker de link.

## Escaleta

| # | Escena | Tiempo | Fondo | Entrada |
|---|---|---|---|---|
| 1 | Hook: ★ MÁS POPULAR · "El Kit *Inversor*" | 0–2,5 s | Morado | — |
| 2 | "Los dos bootcamps completos, *en un solo kit.*" | 2,5–6,5 s | Verde | Wipe circular (2,2–2,6) |
| 3 | ¿Qué *incluye?*: 3 tarjetas | 6,5–12 s | Morado con trama de puntos | Panel sube (6,2–6,6) |
| 4 | Exclusivo: solo para los *10* primeros, Q&A en vivo | 12–15 s | Degradado noche → morado | Wipe lateral (11,7–12,1) |
| 5 | Precio: $559 → **$399**, ahorras $160 (cierre) | 15–19 s | Verde con trama de puntos | Wipe circular (14,7–15,1) |

## Keyframes clave
**1 · Hook**
- 0,05 s: la píldora "★ MÁS POPULAR" entra con pop y giro.
- 0,25 s: "El Kit" sube desde la máscara.
- 0,55–0,95 s: "*Inversor*" (serif cursiva lima, 250 px) entra con escala 1,8 → 1 y desenfoque, con un golpe de sonido.
- 0,95 s: el subrayado lima barre de izquierda a derecha.
- 0,9 s: entra el logo.

**2 · Los dos bootcamps**
- 2,55 / 2,85 s: entran las líneas del titular.
- 3,25 s: "*en un solo kit.*" con marcador lima (3,55–3,9 s).
- 4,0 s: "NIVEL 1 · Bolsa Local" entra desde la izquierda; 4,25 s: "NIVEL 2 · Bolsa Extranjera" entra desde la derecha.
- 4,75 s: el marco lima se cierra sobre los dos (escala 1,12 → 1) y aparece la etiqueta "KIT INVERSOR". El kit literalmente "junta" los dos bootcamps.

**3 · Qué incluye**
- Las tarjetas entran de arriba hacia abajo a 7,25 · 8,0 · 8,75 s (Y −110 → 0, Out Back).
- Cada ícono hace pop y su check se dibuja. El calendario lleva "60".
- 10,4 s: los íconos "respiran" en cadena como repaso.

**4 · Exclusivo**
- 12,1 s: la estrella entra girando 120°.
- 12,5 s: "Solo para los".
- 12,8 s: el "*10*" (330 px, lima) entra con impacto.
- 13,3 s: se encienden 10 círculos, uno cada 0,05 s, con un tick cada uno.
- 13,75 s: aparece la caja "● EN VIVO · Sesión de preguntas y respuestas (Q&A) con el equipo Freenanzas"; el punto rojo late.

**5 · Precio**
- 15,0 s: la tarjeta sube.
- 15,5–16,6 s: el widget "Mi inversión" cuenta de +S/ 0.00 a +S/ 688.98 (11.60%) mientras su línea se dibuja.
- 16,3–17,05 s: el precio baja de **$559 a $399** con conteo y un pop al llegar.
- 17,35 s: se tacha "Antes $559 USD".
- 17,5 s: entra la píldora "AHORRAS $160", que vuelve a hacer pop a 18,35 s.

## Audio
Sintetizado por código en `audio/kit_audio.py`: la misma base musical de 120 BPM que el Reel de Preventas, más efectos en cada keyframe. Incluye:
- Golpes en "*Inversor*", "*10*" y "$399".
- Whooshes laterales cuando entran Nivel 1 (izquierda) y Nivel 2 (derecha).
- Ticks en los checks y en los 10 cupos.
- Tecleo durante la cuenta del precio y destellos en "Ahorras $160".

## Imagen CTA
Píldora "★ MÁS POPULAR", "Llévate el" y "*Kit Inversor*". Debajo, dos tarjetas lima gruesas: "PAGO ÚNICO · $399 USD ~~Antes $559~~" y "EXCLUSIVO · Q&A en vivo · 10 primeros". Bajo las tarjetas queda espacio para el sticker de link; el logo va abajo, en la misma posición que en el video.

## Copy sugerido
> ⭐ El **Kit Inversor**: los dos bootcamps completos en un solo kit.
> 📈 Nivel 1 · Bolsa Local + 🌎 Nivel 2 · Bolsa Extranjera
> 🧰 Guías y herramientas (impuestos, plantillas, calculadoras)
> 🤝 Acompañamiento por 60 días
> 🎙️ Exclusivo para los 10 primeros: Q&A en vivo con el equipo Freenanzas
> 💸 Pago único de $399 USD (antes $559). Ahorras $160.
> 👉 Link en nuestra historia / bio
