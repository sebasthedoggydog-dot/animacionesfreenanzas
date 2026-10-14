# Hook "migrantes" · 00:00:00:03 → 00:00:03:29

Sin subtítulos. Ruta "PERÚ → mundo" en la primera frase y dinero cayendo **detrás** de la persona en "crecer su platita". 1080×1920, 30 fps, 4,07 s.

## Resultado (`output/`)
| Archivo | Qué es |
|---|---|
| `hook-migrantes_FINAL.mp4` | Montaje completo con el audio original |
| `graficos-ruta-dinero_alfa.mov` | Ruta + billetes con transparencia (ProRes 4444) |
| `graficos-ruta-dinero_relleno.mp4` + `_mate.mp4` | Lo mismo en MP4 para Track Matte Key (Luma) |
| `mate-persona-migrantes.mp4` | Silueta (blanco = persona) |

Orden en Premiere (desde 00:00:00:00): V1 video · V2 gráficos · V3 copia del video con `mate-persona-migrantes` como Track Matte (Luma).

## Tiempos
| Timecode | Voz | Qué pasa |
|---|---|---|
| 00:00:00:17 | "Este es un **video**…" | Pin lima "PERÚ" arriba a la izquierda |
| 00:00:00:26 | "…para las personas…" | Un avioncito despega y dibuja una ruta punteada en arco por encima de la cabeza |
| 00:00:01:24 | "**migrantes**" | Llega a un globo terráqueo (pop + destello); el globo gira suave |
| 00:00:03:01 | — | La ruta se desvanece |
| 00:00:03:03 | corte · "**crecer su platita**" | Entran los billetes cayendo detrás de la persona (fundido de 4 frames), con tinte sutil #5723f4 → #1a6f66 y blur ligero |

## Cómo automatizarlo
```bash
W=work
mkdir -p $W/src && ffmpeg -i hook.mp4 $W/src/f%04d.png    # 1. frames de la persona
cp selfie_multiclass.tflite $W/                           #    modelo de MediaPipe (image_segmenter/selfie_multiclass_256x256)
python3 ../hook-dividendos/segment.py $W 71,93            # 2. máscaras (71 y 93 = frames de los cortes)
node render-graficos.mjs $W/route                         # 3. ruta PERÚ → mundo → PNG transparentes (Playwright/Chromium)
python3 compose.py hook.mp4 dinero.mp4 $W/src $W/masks $W/route output 1.0   # 4. montaje (1.0 = segundo del video de dinero)
```
Ajustes en `compose.py`: `MONEY_IN` = cuándo entra el dinero, `0.2` = tinte, `1.4` = blur, `0.9` = opacidad. Tiempos de la ruta en `T` de `overlay.html`.
