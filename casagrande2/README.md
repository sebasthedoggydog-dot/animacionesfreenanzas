# Segmento "Casa Grande · puesto 2" · 00:01:24:15 → 00:01:31:00

Solo gráficos (sin subtítulos). Archivos de 6,7 s, 1080×1920, 30 fps. **Colócalos empezando en 00:01:24:15.**
Dato: CASAGRC1 · Agroindustrial · 8,83 % (coincide con `../TOP5-DIVIDENDOS.md`).

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:24:23 | "Incluso a mí me pagó mis dividendos" | Aviso blanco tipo notificación "✓ DIVIDENDO RECIBIDO · *Incluso a mí me pagó*" | — |
| 00:01:26:13 | "**Casa Grande**" | El aviso se vuelve chip "✓ ME PAGÓ DIVIDENDOS" (se queda todo el segmento) y entra la tarjeta con el logo + píldora "CASAGRC1 · AGROINDUSTRIAL" | Empujón rápido **100 → 106 %** en 6 frames (hasta 00:01:26:19) |
| 00:01:27:04 | "Con un…" | La tarjeta gira a verde "RETORNO POR DIVIDENDO" | — |
| 00:01:27:15 → 00:01:28:20 | "ocho punto ochenta y tres" | Contador 0,00 → **8,83 %** + barra (escala vs. 10,14 % del puesto 1) | — |
| **00:01:28:20** | llega al "…tres" | Golpe del número + rayos lima/blancos de "sorpresa" | **PUNCH-IN 106 → 120 % en 5 frames** (hasta 00:01:28:25) con **rotación −2° que vuelve a 0°** en 10 frames (hasta 00:01:29:00). Sensación de "¡wow!" |
| 00:01:30:22 | "puesto **dos**" | Badge lima "PUESTO #2" a la izquierda de tu cabeza | Si quieres, vuelve a 100 % en "en el puesto" (00:01:29:28) |

**Ojo:** el clip que me pasaste termina en 00:01:29:07, antes de "en el puesto dos". Los tiempos de 00:01:29:07 en adelante salen de tu transcripción; en la vista previa se congela el último frame.

## Archivos (`output/`)
- `PREVIEW_casagrande2.mp4`: referencia con zoom y profundidad.
- `graficos-casagrande_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-casagrande_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-casagrande_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-casagrande.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 25,108      # cortes en los frames 25 y 108
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_casagrande2.mp4
```
