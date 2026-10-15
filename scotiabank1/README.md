# Segmento "Top 1 · Cuenta Digital Scotiabank" · 00:00:11:22 → 00:00:14:28

Solo gráficos (sin subtítulos). Archivos de 3,3 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:11:22.**
Mismo lenguaje que `../minsur1` (estrella "#1", rayos de luz, placa con logo, corona y confeti). Todo va detrás de la persona.

## Pauta de tiempos
| Timecode | Voz | Gráfico | Cámara |
|---|---|---|---|
| 00:00:11:25 | "**Top**…" | Píldora morada "TOP…" que tiembla como redoble | — |
| 00:00:12:21 | "…**uno**" | Estrella lima gigante "TOP #1" + rayos de luz girando + confeti | **Golpe fuerte 100 → 120 %** en 4 frames |
| 00:00:13:02 | corte · "Cuenta…" | La estrella pasa a la esquina (mini "#1") | Vuelve a 100 % |
| 00:00:13:06 | "**Cuenta Digital**" | Píldora lima con ícono de celular "CUENTA DIGITAL" | — |
| 00:00:13:25 | "**Scotiabank**" | Placa con el logo de Scotiabank (entra con golpe), corona lima y segundo confeti; los rayos crecen | **Golpe 100 → 112 %** en 4 frames + giro de 2° |

Tiempos de cada palabra estimados con el audio (los cortes calzan con la transcripción).

## Archivos (`output/`)
- `PREVIEW_scotiabank1.mp4`: referencia con zoom y profundidad.
- `graficos-scotiabank_alfa.mov` (ProRes 4444) · `_relleno.mp4` + `_mate.mp4` (Track Matte Luma) · `_CROMA-MAGENTA.mp4` (CapCut / Ultra Key).
- `mate-persona-scotiabank.mp4`: silueta (blanco = persona).

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 40 700
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_scotiabank1.mp4
```
