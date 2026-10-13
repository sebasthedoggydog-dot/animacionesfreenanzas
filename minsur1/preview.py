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
UNO, LOGO, LAND = 2.15, 2.70, 5.90   # "puesto uno" · "Minsur" · llega al 10,14 %


def ease(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


def ease_in_out(p):
    p = min(1.0, max(0.0, p))
    return 4 * p ** 3 if p < .5 else 1 - (-2 * p + 2) ** 3 / 2


def zoom(t):
    """Devuelve (escala, rotación en grados)."""
    z = 1.0 + 0.25 * ease_out((t - UNO) / (4 / 30))                    # golpe fuerte 100 → 125 % en 4 frames
    z -= 0.17 * ease_out((t - LOGO) / (8 / 30))                         # abre a 108 % para ver la placa
    z -= 0.08 * ease_out((t - 4.20) / (6 / 30))                         # "Con un…": vuelve a 100 %
    z += 0.30 * ease_out((t - LAND) / (6 / 30))                         # cierre: 100 → 130 % en 6 frames
    rot = 3.0 * ease_out((t - LAND) / (6 / 30))                          # + giro de 3° para celebrar
    return z, rot


def ease_out(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


def warp(img, zr, cx=540, cy=900):
    z, rot = zr
    m = cv2.getRotationMatrix2D((cx, cy), rot, z)
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
