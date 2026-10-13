# Segmento "Minsur · puesto 1" · 00:01:31:02 → 00:01:37:26

Solo gráficos (sin subtítulos). Archivos de 6,93 s, 1080×1920, 30 fps. **Colócalos empezando en 00:01:31:02.**
Dato: MINSURI1 · Minería · 10,14 % (coincide con `../TOP5-DIVIDENDOS.md`).

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:31:11 | "Y quién sí en el puesto…" | Píldora de suspenso "Y EL PUESTO **#1** ES…" que tiembla como redoble | — |
| **00:01:33:04** | "…**uno**" | Estrella lima gigante "PUESTO #1" + rayos de luz girando detrás | **ZOOM IN FUERTE 100 → 125 % en 4 frames** (hasta 00:01:33:08). Opcional: *Dip to White* de 2 frames en 00:01:33:04 |
| 00:01:33:16 | corte · "**Minsur** Minera" | La estrella se va a la esquina (mini "#1") y entra la placa blanca con el logo + "MINSURI1 · MINERÍA" | Abre a 108 % en 8 frames (hasta 00:01:33:24) para que se vea la placa |
| 00:01:35:08 | corte · "Con un…" | La placa gira a la **placa destacada** morada con borde lima y **corona** encima | Vuelve a 100 % (6 frames) |
| 00:01:35:17 → 00:01:36:16 | "diez punto catorce" | Contador 0,00 → **10,14 %** | — |
| **00:01:36:16** | llega al "…catorce" | Golpe del número, la corona salta, los rayos crecen y explota **confeti** | **CIERRE: 100 → 130 % en 6 frames + giro de 3°** (hasta 00:01:36:22). Mantén hasta "por ciento" y corta seco al CTA en 00:01:37:26 |

## Archivos (`output/`)
- `PREVIEW_minsur1.mp4`: referencia con zoom y profundidad.
- `graficos-minsur_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-minsur_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-minsur_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-minsur.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 74,126      # cortes en los frames 74 (1:33:16) y 126 (1:35:08)
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_minsur1.mp4
```
