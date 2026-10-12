# Segmento "BCP · ranking 5" · 00:00:59:14 → 00:01:08:09

Solo gráficos (sin subtítulos). Todos los archivos duran 8,93 s, 1080×1920, 30 fps.
**Colócalos en la línea de tiempo empezando en 00:00:59:14.**

## Pauta de tiempos (línea de tiempo de Premiere)
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:00:17 | "…del **BCP**" | Entra la tarjeta del logo BCP con pop y destellos | **ZOOM IN 100 % → 115 %** en 12 frames (hasta 00:01:00:29), curva *ease out*, ancla en la cara (x 540, y 760). Luego deriva lenta a 117 % hasta el corte |
| 00:01:01:22 | "**Credicorp uno**" | Píldora lima "CREDITC1 · BANCOS" | — |
| 00:01:03:23 | "ranking **cinco**" | Badge morado "RANKING #5" | — |
| 00:01:04:17 | — | Sale la parte 1 hacia arriba | — |
| 00:01:04:25 | **corte** · "Con un…" | Entra la tarjeta verde "RETORNO POR DIVIDENDO" + mini logo + #5 | Vuelve a 100 % (toma nueva). Opcional: empuje lento 100 → 106 % hasta 00:01:08:09 |
| 00:01:05:08 → 00:01:06:25 | "cinco punto noventa y seis" | Contador 0,00 → **5,96 %** + barra (escala vs. 10,14 % del puesto 1) con golpe al llegar | — |

## Archivos (`output/`)
- `PREVIEW_bcp-ranking5.mp4`: referencia con zoom y profundidad ya aplicados (no es para el montaje).
- `graficos-bcp_relleno.mp4` + `graficos-bcp_mate.mp4`: recorte exacto en Premiere (Track Matte Key → Luma).
- `graficos-bcp_CROMA-MAGENTA.mp4`: alternativa rápida con Ultra Key sobre magenta `#FF00FF`. Esta vez no es rojo porque el logo BCP tiene naranja.
- `graficos-bcp_alfa.mov`: ProRes 4444 con transparencia (lo más cómodo en Premiere: se arrastra y listo).
- `mate-persona-bcp.mp4`: máscara de la persona (blanco = persona) para ponerla delante de los gráficos.

Pistas: V1 video · V2 gráficos · V3 copia del video con `mate-persona-bcp.mp4` como Track Matte (Luma) · V4 tus subtítulos.
Si aplicas el zoom, anida V1 + V3 + mate y haz el zoom sobre el anidado, para que el recorte calce.

## Regenerar
```bash
ffmpeg -i bcp.mp4 work/src/f%04d.png
python3 ../hook-dividendos/segment.py work 161      # 161 = frame del corte
node render.mjs work/back
python3 preview.py bcp.mp4 work/src work/masks work/back output/PREVIEW_bcp-ranking5.mp4
```
Tiempos editables en el objeto `T` de `overlay.html`.
