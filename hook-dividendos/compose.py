"""Compone el hook final, frame a frame:

    video (con zoom)  →  capa trasera (gráficos)  →  persona recortada  →  capa delantera (subtítulos)

Uso:
    python3 compose.py <video_original> <frames_src> <masks> <layers> <salida.mp4>

<frames_src>  PNG del video original (ffmpeg -i video.mp4 src/f%04d.png)
<masks>       máscaras de persona generadas por segment.py
<layers>      capas back/ y front/ generadas por render-layers.mjs
"""
import math
import subprocess
import sys

import cv2
import numpy as np

video, SRC, MASKS, LAYERS, OUT = sys.argv[1:6]
FPS, W, H = 30, 1080, 1920
CUT = 5.83  # corte de cámara del montaje original


def ease_out(p):
    return 1 - (1 - p) ** 3


def prog(t, a, b):
    return min(1.0, max(0.0, (t - a) / (b - a)))


def punch(t, at, amount, dur=0.45):
    """Golpe de zoom que entra rápido y se relaja."""
    if t < at:
        return 0.0
    p = (t - at) / dur
    return amount * math.exp(-4 * p) * min(1.0, p * 6)


def zoom(t):
    if t < CUT:
        # Zoom-in agresivo en el primer frame (1.00 → 1.22) y luego un push-in lento
        z = 1.0 + 0.22 * ease_out(prog(t, 0.0, 0.35))
        z -= 0.08 * ease_out(prog(t, 0.35, 1.6))          # se asienta a 1.14
        z += 0.05 * prog(t, 1.6, CUT)                     # empuje lento constante
        z += punch(t, 0.18, 0.05) + punch(t, 2.57, 0.04) + punch(t, 4.94, 0.07)
    else:
        # Tras el corte: entra cerrado y abre, con golpe en "top cinco"
        z = 1.24 - 0.10 * ease_out(prog(t, CUT, CUT + 0.5)) + 0.03 * prog(t, CUT + 0.5, 8.4)
        z += punch(t, 7.48, 0.08)
    return z


def warp(img, z, cx=540, cy=820, interp=cv2.INTER_LINEAR):
    """Escala alrededor de (cx, cy), ~a la altura de la cara."""
    m = np.float32([[z, 0, cx * (1 - z)], [0, z, cy * (1 - z)]])
    return cv2.warpAffine(img, m, (W, H), flags=interp, borderMode=cv2.BORDER_REFLECT)


def over(dst, rgba):
    a = rgba[..., 3:4].astype(np.float32) / 255
    return dst * (1 - a) + rgba[..., :3].astype(np.float32) * a


n = len(__import__('glob').glob(f'{SRC}/*.png'))
ff = subprocess.Popen(
    ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
     '-i', '-', '-i', video, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '17', '-preset', 'slow',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', OUT],
    stdin=subprocess.PIPE)
for i in range(1, n + 1):
    t = (i - 1) / FPS
    z = zoom(t)
    frame = warp(cv2.imread(f'{SRC}/f{i:04d}.png'), z, interp=cv2.INTER_CUBIC).astype(np.float32)
    mask = warp(cv2.imread(f'{MASKS}/f{i:04d}.png', 0), z).astype(np.float32)[..., None] / 255
    back = cv2.imread(f'{LAYERS}/back/f{i:04d}.png', cv2.IMREAD_UNCHANGED)
    front = cv2.imread(f'{LAYERS}/front/f{i:04d}.png', cv2.IMREAD_UNCHANGED)
    out = over(frame, back)                        # gráficos sobre el fondo del cuarto
    out = frame * mask + out * (1 - mask)          # la persona vuelve a quedar delante
    out = over(out, front)                         # subtítulos encima de todo
    ff.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close()
ff.wait()
print('listo →', OUT)
