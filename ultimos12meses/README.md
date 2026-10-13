# Segmento "Rendimiento histórico · últimos 12 meses" · 00:00:14:15 → 00:00:21:10

Solo gráficos (sin subtítulos). Archivos de 6,93 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:14:15.**
Los tiempos por palabra se tomaron de los subtítulos de una versión anterior del mismo clip.
La franja de arriba al centro (y ≈ 230–390 px) queda libre para tus subtítulos; como la cabeza está alta (y ≈ 420), los gráficos van a los costados.

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:00:15:06 | "Pero este **top**…" | Badge lima "TOP 5" a la derecha | — |
| 00:00:15:12 | "…**octubre**…" | Calendario "OCTUBRE" a la izquierda | — |
| 00:00:15:27 | "…**2026**" | El año sube dentro del calendario con un golpe | — |
| 00:00:17:06 | corte · "es un **rendimiento**…" | Tarjeta verde a la derecha: reloj + "RENDIMIENTO HISTÓRICO" + gráfico que se dibuja | — |
| 00:00:17:21 | "…**histórico**" | Las agujas del reloj giran hacia atrás; aparece la línea punteada con "?" y la nota *No asegura rendimientos futuros* | Acercamiento suave **100 → 105 %** en 18 frames (hasta 00:00:18:09), *ease in-out* |
| 00:00:18:14 | corte · "por **dividendos**…" (00:00:18:21) | Píldora lima "DIVIDENDOS PAGADOS" a la derecha | Vuelve a 100 % |
| 00:00:19:09 | "…**pagados**…" | Se marca el ✓, caen 3 monedas y aparece el anillo de 12 segmentos con "$" | — |
| 00:00:20:06 | "…**últimos**…" | Los 12 segmentos se encienden uno a uno (de este mes hacia atrás) | — |
| 00:00:20:18 | "…**12**…" | El "$" cambia a "12" | **Golpe 100 → 110 %** en 4 frames (hasta 00:00:20:22) |
| 00:00:20:27 | "…**meses**" | Aparece "MESES" | — |

## Archivos (`output/`)
- `PREVIEW_12meses.mp4`: referencia con zoom y profundidad.
- `graficos-12meses_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-12meses_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-12meses_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-12meses.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 70,119      # cortes en 00:00:16:25 y 00:00:18:14
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_12meses.mp4
```
