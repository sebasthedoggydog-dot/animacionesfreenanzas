# Hook "migrantes" · 00:00:00:03 → 00:00:03:29

Sin subtítulos. El video queda tal cual hasta "crecer su platita"; desde ahí caen billetes **detrás** de la persona y sube una flecha de crecimiento. 1080×1920, 30 fps, 4,07 s.

## Resultado (`output/`)
| Archivo | Qué es |
|---|---|
| `hook-migrantes_FINAL.mp4` | Montaje completo con el audio original |
| `dinero-flecha_alfa.mov` | Billetes + flecha con transparencia (ProRes 4444) |
| `dinero-flecha_relleno.mp4` + `_mate.mp4` | Lo mismo en MP4 para Track Matte Key (Luma) |
| `mate-persona-migrantes.mp4` | Silueta (blanco = persona) |

Orden en Premiere (desde 00:00:00:00): V1 video · V2 `dinero-flecha` · V3 copia del video con `mate-persona-migrantes` como Track Matte (Luma).

## Tiempos
| Timecode | Voz | Qué pasa |
|---|---|---|
| 00:00:00:03 → 00:00:03:02 | "Este es un video para las personas migrantes que buscan hacer" | Video original, sin gráficos |
| 00:00:03:03 | corte · "**crecer**…" | Entran los billetes cayendo (fundido de 4 frames), teñidos sutilmente con #5723f4 → #1a6f66 y con blur ligero. La flecha lima con borde morado empieza a subir en zigzag desde abajo a la izquierda |
| 00:00:03:14 | "…su **platita**" | La punta de la flecha llega arriba a la derecha, aparece con pop, late y la flecha da un saltito |

## Cómo automatizarlo
```bash
W=work
mkdir -p $W/src && ffmpeg -i hook.mp4 $W/src/f%04d.png    # 1. frames de la persona
cp selfie_multiclass.tflite $W/                           #    modelo de MediaPipe (image_segmenter/selfie_multiclass_256x256)
python3 ../hook-dividendos/segment.py $W 71,93            # 2. máscaras (71 y 93 = frames de los cortes)
node render-flecha.mjs $W/arrow                           # 3. flecha → PNG transparentes (Playwright/Chromium)
python3 compose.py hook.mp4 dinero.mp4 $W/src $W/masks $W/arrow output 1.0   # 4. montaje (1.0 = segundo del video de dinero)
```
Ajustes en `compose.py`: `MONEY_IN` = cuándo entra el dinero, `0.2` = tinte, `1.4` = blur, `0.9` = opacidad. Tiempos de la flecha en `T` de `overlay.html`.
