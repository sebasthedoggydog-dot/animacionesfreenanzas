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
