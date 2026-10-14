"""Monta el hook "migrantes": ruta PERÚ → mundo y, en "crecer su platita", dinero (croma) detrás de la persona.

Capas (de abajo hacia arriba):
  1. Video original (el cuarto)
  2. Billetes (solo desde "crecer"): se quita el verde del croma, se tiñen con la paleta, desenfoque leve, fundido corto
  3. Gráficos de overlay.html (ruta con pin PERÚ, avión y globo)
  4. Persona recortada (máscaras de ../hook-dividendos/segment.py)

Uso:
  python3 compose.py <video_persona> <video_dinero> <frames_persona> <mascaras> <graficos> <carpeta_salida> [segundo_inicio_dinero]

Escribe en <carpeta_salida>:
  hook-migrantes_FINAL.mp4   montaje completo con el audio original
  .graficos/fNNNN.png        dinero + ruta con transparencia (para exportar a Premiere)
"""
import glob
import os
import subprocess
import sys

import cv2
import numpy as np

person_video, money_video, SRC, MASKS, ARROW, OUT = sys.argv[1:7]   # ARROW = carpeta de PNG de overlay.html
MONEY_START = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
FPS, W, H = 30, 1080, 1920
MONEY_IN, FADE = 3.10, 4 / 30          # "crecer su platita" (00:00:03:03) · fundido de 4 frames

MORADO = np.array([244, 35, 87], np.float32)    # BGR de #5723f4
VERDE = np.array([102, 111, 26], np.float32)    # BGR de #1a6f66

n = len(glob.glob(f'{SRC}/*.png'))
GFX = f'{OUT}/.graficos'
os.makedirs(GFX, exist_ok=True)
yy = np.mgrid[0:H, 0:W][0].astype(np.float32)
g = (yy / H)[..., None]
tint = MORADO * (1 - g) + VERDE * g             # morado arriba → verde azulado abajo

first = int(round(MONEY_IN * FPS))
money = subprocess.Popen(
    ['ffmpeg', '-loglevel', 'error', '-ss', str(MONEY_START), '-i', money_video, '-vf',
     f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}', '-frames:v', str(n - first),
     '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], stdout=subprocess.PIPE)


def key_green(frame):
    """Quita el verde del croma: devuelve (color sin derrame verde, alfa 0–1)."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    green = (np.abs(h - 60) < 22) & (s > 70) & (v > 60)
    a = 1 - cv2.GaussianBlur(green.astype(np.float32), (0, 0), 1.2)
    f = frame.astype(np.float32)
    f[..., 1] = np.minimum(f[..., 1], np.maximum(f[..., 0], f[..., 2]) * 1.05)   # despill
    return f, a[..., None]


final = subprocess.Popen(
    ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
     '-i', person_video, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-shortest',
     '-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
     f'{OUT}/hook-migrantes_FINAL.mp4'], stdin=subprocess.PIPE)

for i in range(1, n + 1):
    t = (i - 1) / FPS
    frame = cv2.imread(f'{SRC}/f{i:04d}.png').astype(np.float32)
    gfx = np.zeros((H, W, 4), np.float32)                      # dinero + gráficos (alfa no premultiplicado)
    if i - 1 >= first:
        raw = money.stdout.read(W * H * 3)
        mf = np.frombuffer(raw, np.uint8).reshape(H, W, 3) if len(raw) == W * H * 3 else np.zeros((H, W, 3), np.uint8)
        col, a = key_green(mf)
        col = cv2.GaussianBlur(col * 0.8 + tint * 0.2, (0, 0), 1.4)    # tinte sutil de la paleta + blur ligero
        a = cv2.GaussianBlur(a[..., 0], (0, 0), 1.4)[..., None] * 0.9 * min(1.0, (t - MONEY_IN) / FADE + 1 / 30)
        gfx[..., :3], gfx[..., 3:] = col, a
    ov = cv2.imread(f'{ARROW}/f{i:04d}.png', cv2.IMREAD_UNCHANGED).astype(np.float32)
    oa = ov[..., 3:4] / 255
    out_a = oa + gfx[..., 3:] * (1 - oa)
    gfx[..., :3] = (ov[..., :3] * oa + gfx[..., :3] * gfx[..., 3:] * (1 - oa)) / np.maximum(out_a, 1e-4)
    gfx[..., 3:] = out_a
    cv2.imwrite(f'{GFX}/f{i:04d}.png', np.dstack([np.clip(gfx[..., :3], 0, 255), gfx[..., 3:] * 255]).astype(np.uint8))
    comp = frame * (1 - gfx[..., 3:]) + gfx[..., :3] * gfx[..., 3:]
    m = cv2.imread(f'{MASKS}/f{i:04d}.png', 0).astype(np.float32)[..., None] / 255
    comp = frame * m + comp * (1 - m)                          # la persona queda delante
    final.stdin.write(np.clip(comp, 0, 255).astype(np.uint8).tobytes())

final.stdin.close()
final.wait()
money.wait()
print('listo →', OUT)
