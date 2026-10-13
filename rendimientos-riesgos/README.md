# Segmento "Buenos rendimientos… y también riesgos" · 00:00:53:25 → 00:00:59:11

Solo gráficos (sin subtítulos). Archivos de 5,63 s, 1080×1920, 30 fps. **Colócalos empezando en 00:00:53:25.**
Tiempos por palabra estimados con la energía del audio (ajústalos unos frames si hace falta).

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:00:54:17 | "…dan **buenos**…" | Tarjeta morada "RENDIMIENTO" baja desde arriba | — |
| 00:00:54:26 | "…**rendimientos**" | Barra lima "ACCIONES QUE PAGAN DIVIDENDOS" crece · "TOP 5: 5,96 % – 10,14 %" | — |
| 00:00:55:25 | "y **mejores** rendimientos…" | Chip "▲ MEJORES" | — |
| 00:00:56:25 | "…que las **cuentas de ahorro**" | Aparece "CUENTA DE AHORRO" con una barra corta (comparación cualitativa, sin cifra) | — |
| 00:00:57:15 | "**Sí.**" | Sello lima "¡SÍ!" | **Golpe 100 → 108 %** en 4 frames |
| 00:00:57:27 | corte · "Y de que hay **riesgos**…" (00:00:58:04) | La tarjeta cambia a blanca: ⚠ "RIESGOS" · *El precio puede subir o bajar* · línea en zigzag que se dibuja; el triángulo tiembla | Vuelve a 100 % y **acercamiento lento 100 → 106 %** en 1,5 s (tono serio) |
| 00:00:58:20 | corte · "…también los hay" | El triángulo vuelve a temblar; la línea termina cayendo | — |

La gorra colgada en la pared se excluyó del recorte (`segment.py … 700`) para que no tape los gráficos.

## Archivos (`output/`)
- `PREVIEW_rendimientos-riesgos.mp4`: referencia con zoom y profundidad.
- `graficos-rendimientos-riesgos_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-rendimientos-riesgos_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-rendimientos-riesgos_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-rendimientos-riesgos.mp4`: silueta (blanco = persona).

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 122,145 700   # cortes + quita accesorios (gorra) por encima de y=700
node render.mjs work/g
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW_rendimientos-riesgos.mp4
```
