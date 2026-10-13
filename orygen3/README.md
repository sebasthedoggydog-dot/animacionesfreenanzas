# Segmento "Orygen · puesto 3" · 00:01:15:24 → 00:01:24:10

Solo gráficos (sin subtítulos). Archivos de 8,7 s, 1080×1920, 30 fps. **Colócalos empezando en 00:01:15:24.**
Dato: ORYGENC1 · Energía · 6,92 % (coincide con la tabla oficial, `../TOP5-DIVIDENDOS.md`).

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:15:27 | "Orygen…" | Tarjeta blanca con el logo, pop · píldora "ORYGENC1 · ENERGÍA" (00:01:16:06) | — |
| **00:01:17:09** | "…acciones **que yo tengo**" | Chip morado "★ EN MI PORTAFOLIO" | **ZOOM SUTIL 100 → 108 %** en 1 s (hasta 00:01:18:09), curva *ease in-out* (suave al entrar y al salir), ancla en la cara. Mantener hasta el corte de 00:01:20:14 |
| 00:01:18:17 → 00:01:18:20 | "…están en **OPA**" | La tarjeta gira a morado: "ACCIONES EN **OPA**" + *Oferta Pública de Adquisición* | — |
| 00:01:20:14 | corte · "6,92 %" | Tarjeta vertical verde a la derecha de tu cabeza (tu pelo la tapa = profundidad) + chip "EN OPA" | Vuelve a 100 % |
| 00:01:20:16 → 00:01:22:03 | "seis punto noventa y dos" | Contador 0,00 → **6,92 %** + barrita (escala vs. 10,14 % del puesto 1) con golpe al llegar | — |
| 00:01:22:25 | corte · "Quedando…" | Mini logo Orygen a la izquierda | — |
| 00:01:24:00 | "puesto **tres**" | Badge lima "PUESTO #3" a la izquierda (tu mano marca el 3 a la derecha) | — |

## Archivos (`output/`)
- `PREVIEW_orygen3.mp4`: referencia con zoom y profundidad.
- `graficos-orygen_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-orygen_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF` (el naranja del logo no se afecta).
- `graficos-orygen_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-orygen.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 140,211     # cortes en los frames 140 y 211
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_orygen3.mp4
```
