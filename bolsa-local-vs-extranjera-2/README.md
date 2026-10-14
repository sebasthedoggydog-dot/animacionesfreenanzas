# Segmento "Bolsa local paga dividendos / extranjera crece más" · 00:00:46:23 → 00:00:58:10

Solo gráficos (sin subtítulos). Archivos de 11,7 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:46:23.**
Mismo sistema visual que `../bolsa-local-vs-extranjera` (tarjetas de marca, globo / pin con casa, medidor de 5 segmentos). Todo va arriba de la cabeza, detrás de la persona.

## Pauta de tiempos
| Timecode | Voz | Gráfico | Cámara |
|---|---|---|---|
| 00:00:46:26 | "pero la **bolsa local**" | Tarjeta verde BOLSA **LOCAL** (pin con casa) | — |
| 00:00:48:18 | "si lo compras a un **buen precio**" | Etiqueta lima "🏷 A BUEN PRECIO" | — |
| 00:00:49:06 → 00:00:49:26 | "paga **buenos dividendos**" | El medidor DIVIDENDOS se llena 5/5 y llueven monedas detrás | Golpe 100 → 106 % en "dividendos" (4 frames) |
| 00:00:50:21 | "o sea, **platita**" | Moneda grande `$` con pop y latido + segunda lluvia de monedas | — |
| 00:00:51:17 | corte · "y **anual**" | Chip "↻ CADA AÑO" | Vuelve a 100 % |
| 00:00:52:01 | corte · "para la **bolsa extranjera**" | La tarjeta LOCAL sale a la izquierda y entra la morada BOLSA **EXTRANJERA** (globo girando) | — |
| 00:00:53:17 | "si bien **crece más**" | Se dibuja la línea de crecimiento (primer tramo) + chip "▲ CRECE MÁS" | — |
| 00:00:54:29 | "y tu platita **crece más**" | La línea termina de subir, punto final con pop, el chip late | Golpe 100 → 106 % (4 frames) |
| 00:00:55:19 | corte · "es un promedio de" | Tarjeta blanca con reloj de arena (gira y la arena cae): "PROMEDIO PARA ESPERAR · 5 – 10 AÑOS" con línea de 10 años | Vuelve a 100 % |
| 00:00:57:05 | "esperar **cinco**…" | Se resalta el "5" y la barra llega a 5 AÑOS | — |
| 00:00:57:16 | "…**diez** años" | Se resalta el "10" y la barra llega a 10 AÑOS | Golpe 100 → 108 % (4 frames) |

Los tiempos de cada palabra dentro de la frase se estimaron con el audio (los cortes del clip coinciden con la transcripción).

## Archivos (`output/`)
- `PREVIEW_bolsa-local-vs-extranjera-2.mp4`: referencia con zoom y profundidad.
- `graficos-bolsas2_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-bolsas2_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-bolsas2_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-bolsas2.mp4`: silueta (blanco = persona).

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 34,125,143,158,230,266,297 700
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_bolsa-local-vs-extranjera-2.mp4
```
