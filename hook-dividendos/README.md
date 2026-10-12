# Hook "Dividendos de octubre" · 00:00 → 00:08:10

**Resultado:** `output/hook-dividendos.mp4` (1080×1920, 30 fps, 8,33 s, audio original).

## Capas (de atrás hacia adelante)
1. **Video original con zoom.** Golpe de zoom 1,00 → 1,22 en los primeros 0,35 s, luego se asienta en 1,14 y sigue empujando lento. Golpes cortos en "octubre", "mejores" y "dividendos". Tras el corte (5,83 s) entra cerrado (1,24) y abre, con otro golpe en "top".
2. **Gráficos detrás de la persona** (`overlay.html`, capa `back`):
   - 0,0–2,1 s: tarjeta morada `#5723f4` "RANKING DEL MES · OCTUBRE" que entra con pop y flota.
   - 2,1–5,8 s: la tarjeta gira a verde `#1a6f66` "LAS MEJORES ACCIONES · DIVIDENDOS", con una línea de crecimiento lima que se dibuja; monedas `$` lima salen desde detrás del cuerpo en "dividendos".
   - 5,83–8,33 s: disco morado + 5 filas de ranking que entran desde los lados, "LA LISTA" y, en "top", cambia de golpe a "TOP **5**".
3. **Persona recortada** (máscaras de `segment.py`, MediaPipe selfie multiclass), para que la cabeza, brazos y manos tapen los gráficos.
4. **Subtítulos cinéticos** (capa `front`): Montserrat 900, palabra por palabra con pop de escala, blanco con contorno morado; palabras clave en lima `#c6fd34` y más grandes: *octubre, mejores acciones, dividendos, top cinco*. Destello blanco breve en el corte.

Tipografías de marca en `fonts/`: Montserrat (700/800/900) y Free Serif.

## Cómo regenerar
```bash
ffmpeg -i inicio.mp4 work/src/f%04d.png                 # frames del video
python3 segment.py work                                  # usa work/selfie_multiclass.tflite → work/masks
node render-layers.mjs work/layers                       # capas back/front transparentes
python3 compose.py inicio.mp4 work/src work/masks work/layers output/hook-dividendos.mp4
```
Los tiempos de cada palabra están en `WORDS` dentro de `overlay.html` (estimados con la energía del audio). Si alguna palabra entra adelantada o tarde, se corrige ahí y se vuelve a renderizar. `overlay.html` también se puede abrir en el navegador para previsualizar la animación con un scrubber.

## Solo gráficos para tu editor (`output/graficos/`)
Todo dura 8,33 s, 1080×1920, 30 fps, y empieza en 00:00:00:00 del clip original.

| Archivo | Qué es | Pista |
|---|---|---|
| `1_graficos-detras-de-la-persona.mov` / `.webm` / `_png.zip` | Tarjetas, monedas, ranking y TOP 5 con fondo transparente | Encima del video |
| `3_mate-persona.mp4` | Máscara blanco = persona, negro = fondo | Para recortar a la persona |
| `2_subtitulos.mov` / `.webm` / `_png.zip` | Subtítulos cinéticos + destello del corte, con transparencia | Arriba de todo |

`.mov` = ProRes 4444 con alfa (Premiere, Final Cut, DaVinci, After Effects). `.webm` = VP9 con alfa (más liviano). `_png.zip` = secuencia PNG por si tu editor no lee alfa en video.

Orden de pistas para el efecto "detrás de la persona":
1. V1: video original
2. V2: `1_graficos-detras-de-la-persona`
3. V3: otra copia del video original con `3_mate-persona.mp4` como **mate de luminancia** (Track Matte Key en Premiere, Luma Keyer/Alpha en DaVinci)
4. V4: `2_subtitulos`

Si haces zoom al video, aplica el mismo zoom a V1, V3 y al mate (anídalos juntos) para que el recorte calce.

### Versiones en MP4 (H.264 no guarda transparencia, por eso hay dos formas)
- **`*_CROMA-ROJO.mp4`**: gráficos sobre rojo puro `#FF0000`. Quita el rojo con el croma de tu editor (CapCut: *Croma* → gotero sobre el rojo; Premiere: *Ultra Key*). Se usó rojo porque ningún color de la marca (morado, verdes, lima, blanco) está cerca.
- **`*_relleno.mp4` + `*_mate.mp4`**: recorte exacto, sin bordes. Pon el relleno y usa el mate como *mate de luminancia* (blanco = visible).
