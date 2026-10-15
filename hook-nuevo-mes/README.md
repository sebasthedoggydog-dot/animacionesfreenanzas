# Hook "Nuevo mes, nuevas formas de hacer platita" · 00:00:00:04 → 00:00:03:06

Texto dinámico detrás de la persona. 1080×1920, 30 fps, 3,2 s. **Coloca todo desde 00:00:00:00.**
Tipografías de la guía de marca: **Free Serif** (itálica, palabras de apoyo) + **Montserrat Black** (palabras fuertes, lima #c6fd34 con contorno morado #5723f4).

## Pauta
| Timecode | Voz | Gráfico | Cámara |
|---|---|---|---|
| 00:00:00:05 | "**Nuevo**…" | "Nuevo" en Free Serif cae desde cámara con desenfoque · aparece un calendario | — |
| 00:00:00:20 | "…**mes**" | "MES" gigante en lima con golpe + sacudida; la hoja vieja del calendario (31) se arranca y queda la nueva ✓ | Golpe 100 → 108 % (vuelve en 0,35 s) |
| 00:00:01:04 | "**Nuevas**…" | Lo anterior sale barrido; entra "Nuevas" | — |
| 00:00:01:15 | "…**formas**" | "FORMAS" con golpe + 3 íconos (crecimiento, moneda, globo) a la izquierda | Golpe 100 → 106 % (vuelve) |
| 00:00:01:27 | "de **hacer**…" | Barrido; entra "de hacer" | — |
| 00:00:02:10 | "…**platita**" | "PLATITA" gigante con golpe, sacudida y explosión de monedas | **Punch-in 100 → 114 %** en 5 frames y se queda |

La transcripción dice "hacer el platita"; en pantalla puse "de hacer PLATITA". Tiempos de cada palabra estimados con el audio (editables en `T` de `overlay.html`).

## Archivos (`output/`)
- `PREVIEW_hook-nuevo-mes.mp4`: montaje de referencia con zoom y profundidad.
- `graficos-hook-nuevo-mes_alfa.mov` (ProRes 4444) · `_relleno.mp4` + `_mate.mp4` (Track Matte Luma) · `_CROMA-MAGENTA.mp4`.
- `mate-persona-hook-nuevo-mes.mp4`: silueta para poner a la persona delante del texto.

En CapCut: video · gráficos (croma magenta o el .mov) · copia del video con "Quitar fondo" encima.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work
node render.mjs work/g
python3 preview.py hook.mp4 work/src work/masks work/g output/PREVIEW_hook-nuevo-mes.mp4
```

## Solo gráficos, sin letras (`output/solo-graficos/`)
Cada gráfico por separado, 3,2 s, misma posición y tiempos que en el montaje (colócalos desde 00:00:00:00 o muévelos libremente):
| Archivo | Qué es | Momento |
|---|---|---|
| `calendario.mov` / `_CROMA-MAGENTA.mp4` | Calendario: entra en "Nuevo" (00:00:00:08) y en "mes" (00:00:00:20) se arranca la hoja "31" y queda la nueva ✓ | 00:00:00:08 → 00:00:01:04 |
| `formas.mov` / `_CROMA-MAGENTA.mp4` | 3 íconos (crecimiento, moneda, globo) que aparecen escalonados | 00:00:01:17 → 00:00:01:27 |
| `monedas.mov` / `_CROMA-MAGENTA.mp4` | Explosión de monedas `$` que luego caen | 00:00:02:12 → 00:00:03:06 |

Se generan con `node render.mjs <carpeta> calendario|formas|monedas`.
