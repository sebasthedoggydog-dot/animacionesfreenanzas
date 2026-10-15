# Segmento "Top 2 · Financiera Surgir Gold Select" · 00:00:30:14 → 00:00:33:23

Solo gráficos (sin subtítulos). Archivos de 3,37 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:30:14.**
Misma plantilla que `../scotiabank1` en su versión final: estrella desde el primer frame, sin rayos de fondo. Todo va detrás de la persona.

## Pauta de tiempos
| Timecode | Voz | Gráfico | Cámara |
|---|---|---|---|
| 00:00:30:14 | "**Top**…" (primer frame) | Estrella lima "TOP #2" entra de frente con pop + confeti | — |
| 00:00:30:25 | "…**dos**" | La estrella da un latido | Golpe 100 → 115 % (4 frames) |
| 00:00:31:14 | "**Financiera**…" | La estrella pasa a la esquina (mini "#2") + píldora morada "FINANCIERA" | Vuelve a 100 % (8 frames) |
| 00:00:32:04 | "…**Surgir**…" | Placa blanca con borde lima y el logo de Surgir (entra con golpe) y segundo confeti (sin corona) | Golpe 100 → 110 % + giro de 2° |
| 00:00:32:29 | "…**Gold Select**" | Píldora lima "★ GOLD SELECT" debajo de la placa | — |

Tiempos de cada palabra estimados con el audio (el clip no tiene cortes).

## Archivos (`output/`)
- `PREVIEW_surgir2.mp4`: referencia con zoom y profundidad.
- `graficos-surgir_alfa.mov` (ProRes 4444) · `_relleno.mp4` + `_mate.mp4` (Track Matte Luma) · `_CROMA-MAGENTA.mp4` (CapCut / Ultra Key).
- `mate-persona-surgir.mp4`: silueta (blanco = persona).

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 0 700
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_surgir2.mp4
```
