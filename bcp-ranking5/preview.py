"""Vista previa: video + zoom + gráficos detrás de la persona (solo referencia para el editor).

Uso: python3 preview.py <video> <frames_src> <masks> <graficos> <salida.mp4>
"""
import subprocess
import sys

import cv2
import numpy as np

video, SRC, MASKS, GFX, OUT = sys.argv[1:6]
FPS, W, H = 30, 1080, 1920
ZOOM_IN, ZOOM_DUR, CUT = 1.10, 0.40, 5.37   # zoom al decir "BCP" · corte de cámara


def ease(p):
    p = min(1.0, max(0.0, p))
    return 1 - (1 - p) ** 3


def zoom(t):
    if t < CUT:
        return 1.0 + 0.15 * ease((t - ZOOM_IN) / ZOOM_DUR) + 0.02 * ease((t - ZOOM_IN - ZOOM_DUR) / 3.5)
    return 1.0 + 0.06 * (t - CUT) / 3.6           # empuje lento opcional durante el 5,96 %


def warp(img, z, cx=540, cy=760):
    m = np.float32([[z, 0, cx * (1 - z)], [0, z, cy * (1 - z)]])
    return cv2.warpAffine(img, m, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)


n = len(__import__('glob').glob(f'{SRC}/*.png'))
ff = subprocess.Popen(
    ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS),
     '-i', '-', '-i', video, '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium',
     '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', OUT], stdin=subprocess.PIPE)
for i in range(1, n + 1):
    z = zoom((i - 1) / FPS)
    frame = warp(cv2.imread(f'{SRC}/f{i:04d}.png'), z).astype(np.float32)
    mask = warp(cv2.imread(f'{MASKS}/f{i:04d}.png', 0), z).astype(np.float32)[..., None] / 255
    g = cv2.imread(f'{GFX}/f{i:04d}.png', cv2.IMREAD_UNCHANGED)
    a = g[..., 3:4].astype(np.float32) / 255
    out = frame * (1 - a) + g[..., :3] * a
    out = frame * mask + out * (1 - mask)
    ff.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close()
ff.wait()
print('listo →', OUT)
