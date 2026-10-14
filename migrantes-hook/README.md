# Hook "migrantes" · 00:00:00:03 → 00:00:03:29

Fondo de dinero con la paleta de marca + texto animado **detrás** de la persona. 1080×1920, 30 fps, 4,07 s.

## Resultado (`output/`)
| Archivo | Qué es |
|---|---|
| `hook-migrantes_FINAL.mp4` | Montaje completo con el audio original |
| `fondo-dinero-marca.mp4` | Solo el fondo (degradado + dinero teñido + blur + viñeta), para usarlo en Premiere |
| `texto-animado_alfa.mov` | Texto con transparencia (ProRes 4444) |
| `texto-animado_relleno.mp4` + `_mate.mp4` | Texto en MP4 para Track Matte Key (Luma) |
| `mate-persona-migrantes.mp4` | Silueta (blanco = persona) para recortarla en Premiere |

Orden en Premiere: V1 `fondo-dinero-marca` · V2 texto · V3 video de la persona con `mate-persona-migrantes` como Track Matte (Luma).

## Capas (de abajo hacia arriba)
1. **Degradado de marca** `#5723f4` (arriba) → `#1a6f66` (abajo) con un brillo suave detrás de la persona.
2. **Dinero**: el video de billetes viene en croma verde → se quita el verde (HSV + despill), se tiñe 18 % con la paleta, desenfoque ligero (σ 1,6) y opacidad 90 %.
3. **Viñeta** morada oscura en los bordes.
4. **Texto animado** (Montserrat Black, igual que los otros videos), palabra por palabra con pop de escala; blanco `#fdfdfc` y palabras clave en lima `#c6fd34`.
5. **Persona** recortada con MediaPipe (selfie multiclass) — queda intacta delante de todo.

## Tiempos del texto
| Timecode | Texto |
|---|---|
| 00:00:00:03 → 00:00:02:11 | ESTE ES UN VIDEO / PARA LAS PERSONAS / **MIGRANTES** (lima, entra en 00:00:01:24) |
| 00:00:02:11 → 00:00:03:03 | QUE BUSCAN / HACER |
| 00:00:03:03 → 00:00:03:29 | CRECER SU / **PLATITA** (lima, entra en 00:00:03:14) |

Las frases respetan la transcripción; el momento de cada palabra se estimó con el audio (editable en `GROUPS` de `overlay.html`).

## Cómo automatizarlo (paso a paso)
```bash
W=work                                                    # carpeta de trabajo
mkdir -p $W/src && ffmpeg -i hook.mp4 $W/src/f%04d.png    # 1. frames de la persona
cp selfie_multiclass.tflite $W/                           #    modelo de MediaPipe (image_segmenter/selfie_multiclass_256x256)
python3 ../hook-dividendos/segment.py $W 71,93            # 2. máscaras (71 y 93 = frames de los cortes de cámara)
node render-texto.mjs $W/txt                              # 3. texto animado → PNG transparentes (Playwright/Chromium)
python3 compose.py hook.mp4 dinero.mp4 $W/src $W/masks $W/txt output 1.0   # 4. montaje (1.0 = segundo del video de dinero desde el que empieza)
```
Dependencias: `ffmpeg`, Python 3 con `opencv-python-headless`, `numpy`, `mediapipe`; Node con `playwright`.
Ajustes rápidos en `compose.py`: `0.18` = fuerza del tinte, `1.6` = blur del dinero, `0.9` = opacidad del dinero, `0.55` = fuerza de la viñeta.
