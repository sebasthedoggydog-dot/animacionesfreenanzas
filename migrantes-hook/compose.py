"""Monta el hook "migrantes": fondo de marca + dinero (croma) + texto animado detrás de la persona.

Capas (de abajo hacia arriba):
  1. Degradado de marca #5723f4 → #1a6f66 con un brillo suave detrás de la cabeza
  2. Video de dinero: se quita el verde, se tiñe con la paleta, desenfoque leve
  3. Viñeta morada oscura en los bordes
  4. Texto animado (render de overlay.html)
  5. Persona recortada (máscaras de ../hook-dividendos/segment.py)

Uso:
  python3 compose.py <video_persona> <video_dinero> <frames_persona> <mascaras> <texto> <carpeta_salida> [segundo_inicio_dinero]

Escribe en <carpeta_salida>:
  hook-migrantes_FINAL.mp4        montaje completo con el audio original
  fondo-dinero-marca.mp4          solo capas 1–3 (para usarlo como fondo en Premiere)
"""
import glob
import subprocess
import sys

import cv2
import numpy as np

person_video, money_video, SRC, MASKS, TEXT, OUT = sys.argv[1:7]
MONEY_START = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
FPS, W, H = 30, 1080, 1920

MORADO = np.array([244, 35, 87], np.float32)    # BGR de #5723f4
VERDE = np.array([102, 111, 26], np.float32)    # BGR de #1a6f66
OSCURO = np.array([60, 10, 30], np.float32)     # morado muy oscuro para la viñeta

n = len(glob.glob(f'{SRC}/*.png'))

# ---- 1. Degradado de marca (fijo) ----
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
g = np.clip((yy / H) * 0.85 + (xx / W) * 0.15, 0, 1)[..., None]       # diagonal suave, morado arriba → verde abajo
grad = MORADO * (1 - g) + VERDE * g
glow = np.exp(-(((xx - 540) / 520) ** 2 + ((yy - 700) / 620) ** 2))[..., None]
grad = grad + (255 - grad) * 0.10 * glow                              # brillo sutil detrás de la persona
tint = MORADO * (1 - g) + VERDE * g                                   # color con el que se tiñen los billetes
vign = np.clip((np.sqrt(((xx - 540) / 540) ** 2 + ((yy - 900) / 1050) ** 2) - 0.55) / 0.6, 0, 1)[..., None] ** 1.5

# ---- 2. Video de dinero: se lee ya escalado a 1080×1920 ----
money = subprocess.Popen(
    ['ffmpeg', '-loglevel', 'error', '-ss', str(MONEY_START), '-i', money_video, '-vf',
     f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}', '-frames:v', str(n),
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


def writer(path, audio):
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
    if audio:
        cmd += ['-i', person_video, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-shortest']
    cmd += ['-c:v', 'libx264', '-crf', '17', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', path]
    return subprocess.Popen(cmd, stdin=subprocess.PIPE)


final = writer(f'{OUT}/hook-migrantes_FINAL.mp4', True)
plate = writer(f'{OUT}/fondo-dinero-marca.mp4', False)

for i in range(1, n + 1):
    raw = money.stdout.read(W * H * 3)
    mf = np.frombuffer(raw, np.uint8).reshape(H, W, 3) if len(raw) == W * H * 3 else np.zeros((H, W, 3), np.uint8)
    col, a = key_green(mf)
    col = col * 0.82 + tint * 0.18                                   # tinte sutil con la paleta
    col = cv2.GaussianBlur(col, (0, 0), 1.6)                         # blur ligero: el fondo no compite
    a = cv2.GaussianBlur(a[..., 0], (0, 0), 1.6)[..., None] * 0.9
    bg = grad * (1 - a) + col * a
    bg = bg * (1 - 0.55 * vign) + OSCURO * 0.55 * vign                 # viñeta
    plate.stdin.write(np.clip(bg, 0, 255).astype(np.uint8).tobytes())

    txt = cv2.imread(f'{TEXT}/f{i:04d}.png', cv2.IMREAD_UNCHANGED)
    ta = txt[..., 3:4].astype(np.float32) / 255
    comp = bg * (1 - ta) + txt[..., :3] * ta
    person = cv2.imread(f'{SRC}/f{i:04d}.png').astype(np.float32)
    m = cv2.imread(f'{MASKS}/f{i:04d}.png', 0).astype(np.float32)[..., None] / 255
    comp = person * m + comp * (1 - m)
    final.stdin.write(np.clip(comp, 0, 255).astype(np.uint8).tobytes())

for p in (final, plate):
    p.stdin.close()
    p.wait()
money.wait()
print('listo →', OUT)
