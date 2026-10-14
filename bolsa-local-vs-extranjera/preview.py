"""Vista previa: video + zoom + gráficos detrás de la persona (solo referencia para el editor).

Uso: python3 preview.py <video> <frames_src> <masks> <graficos> <salida.mp4>
Si los gráficos duran más que el clip, se congela el último frame del video.
"""
import subprocess
import sys

import cv2
import numpy as np

video, SRC, MASKS, GFX, OUT = sys.argv[1:6]
FPS, W, H = 30, 1080, 1920
CREC, DIV, CUTS = 1.45, 5.10, (1.03, 2.37, 4.43, 6.17)   # "crecimiento" · "dividendos" · cortes


def ease(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


def ease_in_out(p):
    p = min(1.0, max(0.0, p))
    return 4 * p ** 3 if p < .5 else 1 - (-2 * p + 2) ** 3 / 2


def punch(t, at, amount, frames=4):
    p = min(1.0, max(0.0, (t - at) / (frames / 30)))
    return amount * (1 - (1 - p) ** 3)


def zoom(t):
    if CUTS[0] <= t < CUTS[1]:
        return 1.0 + punch(t, CREC, 0.06)          # "crecimiento": golpe 100 → 106 %
    if CUTS[2] <= t < CUTS[3]:
        return 1.0 + punch(t, DIV, 0.08)           # "dividendos": golpe 100 → 108 %
    return 1.0


def warp(img, z, cx=540, cy=760):
    m = np.float32([[z, 0, cx * (1 - z)], [0, z, cy * (1 - z)]])
    return cv2.warpAffine(img, m, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)


nsrc = len(__import__('glob').glob(f'{SRC}/*.png'))
n = len(__import__('glob').glob(f'{GFX}/*.png'))
ff = subprocess.Popen(
    ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
     '-i', '-', '-i', video, '-map', '0:v', '-map', '1:a', '-af', 'apad', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
for i in range(1, n + 1):
    z = zoom((i - 1) / FPS)
    k = min(i, nsrc)
    frame = warp(cv2.imread(f'{SRC}/f{k:04d}.png'), z).astype(np.float32)
    mask = warp(cv2.imread(f'{MASKS}/f{k:04d}.png', 0), z).astype(np.float32)[..., None] / 255
    g = cv2.imread(f'{GFX}/f{i:04d}.png', cv2.IMREAD_UNCHANGED)
    a = g[..., 3:4].astype(np.float32) / 255
    out = frame * (1 - a) + g[..., :3] * a
    out = frame * mask + out * (1 - mask)
    ff.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close()
ff.wait()
print('listo →', OUT)
