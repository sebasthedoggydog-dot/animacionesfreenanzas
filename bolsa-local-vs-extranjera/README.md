# Segmento "Bolsa extranjera vs. bolsa local" · 00:00:39:16 → 00:00:46:19

Solo gráficos (sin subtítulos). Archivos de 7,23 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:39:16.**
Diseño propio: duelo "VS" con tarjetas de marca (EXTRANJERA morada con globo · LOCAL verde azulado con pin/casa), medidores de 5 segmentos y la insignia "▲ GANA". Todo va arriba de la cabeza (y ≈ 500), detrás de la persona.

## Pauta de tiempos
| Timecode | Voz | Gráfico | Cámara |
|---|---|---|---|
| 00:00:39:18 | "La **bolsa extranjera**" | Tarjeta grande morada con globo girando: BOLSA **EXTRANJERA** | — |
| 00:00:40:29 | "a nivel de **crecimiento**" | Dentro de la tarjeta se dibuja una línea que sube + chip "▲ CRECIMIENTO" | Golpe 100 → 106 % (4 frames) |
| 00:00:41:27 | corte · "da más que…" | La tarjeta pasa a la izquierda; medidor "CRECIMIENTO" 5/5 + "▲ GANA" | Vuelve a 100 % |
| 00:00:42:15 | "…la **bolsa local**" | Entra la tarjeta verde BOLSA **LOCAL** (medidor 2/5) y el sello lima "VS" en el centro | — |
| 00:00:43:04 | "**pero** la bolsa local" | Foco en LOCAL (borde lima); EXTRANJERA se atenúa | — |
| 00:00:43:29 | corte · "paga más…" | Los medidores cambian a "DIVIDENDOS": extranjera 2/5 | — |
| 00:00:44:19 | "…**dividendos**" | LOCAL se llena 5/5, llueven monedas `$` detrás y "▲ GANA" pasa a LOCAL | Golpe 100 → 108 % (4 frames) |
| 00:00:45:21 | corte · "que **bolsa extranjera**" | Foco vuelve a EXTRANJERA (pulso y borde lima); LOCAL se atenúa | — |

Los medidores son una comparación cualitativa (sin cifras), igual que lo que se dice en el audio.

## Archivos (`output/`)
- `PREVIEW_bolsa-local-vs-extranjera.mp4`: referencia con zoom y profundidad.
- `graficos-bolsas_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-bolsas_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-bolsas_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-bolsas.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 31,71,133,185 700   # cortes + quita la gorra de la pared
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_bolsa-local-vs-extranjera.mp4
```
