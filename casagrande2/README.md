# Segmento "Casa Grande · puesto 2" · 00:01:26:10 → 00:01:31:00

Solo gráficos (sin subtítulos). Archivos de 4,73 s, 1080×1920, 30 fps. **Colócalos empezando en 00:01:26:10.**
Dato: CASAGRC1 · Agroindustrial · 8,83 % (coincide con `../TOP5-DIVIDENDOS.md`).

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:26:12 | "**Casa Grande**" | Tarjeta blanca con el logo + píldora "CASAGRC1 · AGROINDUSTRIAL" | Empujón rápido **100 → 106 %** en 6 frames (hasta 00:01:26:18) |
| 00:01:26:20 | — | Chip "✓ ME PAGÓ DIVIDENDOS" arriba a la izquierda (referencia personal, se queda todo el segmento) | — |
| 00:01:27:05 | corte · "Con un…" | La tarjeta gira a verde "RETORNO POR DIVIDENDO" | — |
| 00:01:27:18 → 00:01:28:00 | "ocho punto ochenta y tres" | Contador 0,00 → **8,83 %** + barra (escala vs. 10,14 % del puesto 1) | — |
| **00:01:28:00** | llega al "…tres" | Golpe del número + rayos lima/blancos de "sorpresa" | **PUNCH-IN 106 → 120 % en 5 frames** (hasta 00:01:28:05) con **rotación −2° que vuelve a 0°** en 10 frames (hasta 00:01:28:10). Mantener hasta el corte |
| 00:01:29:28 | corte · "en el puesto" | — | Vuelve a 100 % (toma nueva) |
| 00:01:30:22 | "**dos**" | Badge lima "PUESTO #2" a la izquierda de tu cabeza | Golpe corto **100 → 108 %** en 4 frames |

## Archivos (`output/`)
- `PREVIEW_casagrande2.mp4`: referencia con zoom y profundidad.
- `graficos-casagrande_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-casagrande_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-casagrande_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-casagrande.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 25,108      # cortes en los frames 25 (1:27:05) y 108 (1:29:28)
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_casagrande2.mp4
```
