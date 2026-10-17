"""Separa el logo pintado a mano en capas para animarlo (logo-animado.html).

Capas (a 2x, 1280 px): estrella granate · óvalo azul · cruz naranja (trazo diagonal + barra horizontal)
· 7 trazos blancos. Cada trazo lleva además un "mapa de tiempo" (0 = donde empieza la pincelada,
1 = donde termina) para revelarlo como si se pintara en vivo.

Uso:  pip install opencv-python-headless numpy pillow
      python3 assets/logo-pintado/separar_capas.py   → assets/logo-pintado/capas.js
"""
import base64, io, json
from collections import deque
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
S = 2
img = cv2.resize(cv2.imread(str(HERE / 'logo-original.jpg')), None, fx=S, fy=S, interpolation=cv2.INTER_LANCZOS4)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(int)
H, Sa, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
K = lambda n: np.ones((n, n), np.uint8)
rng = np.random.default_rng(3)


def big_components(mask, min_area):
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask)
    return np.isin(lab, [i for i in range(1, n) if st[i, 4] > min_area]).astype(np.uint8) * 255


def fill_holes(mask):
    m = np.pad(mask, 1); ff = m.copy()
    cv2.floodFill(ff, None, (0, 0), 255)
    return (m | ~ff)[1:-1, 1:-1]


# Óvalo azul (la cruz lo parte en dos) → casco convexo
navy = big_components(cv2.morphologyEx(((V < 140) & (H > 85) & (H < 130)).astype(np.uint8) * 255, cv2.MORPH_OPEN, K(5)), 20000)
hull = cv2.convexHull(np.column_stack(np.nonzero(navy)[::-1]).astype(np.int32))
oval = np.zeros_like(navy); cv2.fillConvexPoly(oval, hull, 255)

# Naranja
orange = cv2.morphologyEx((((H >= 8) & (H <= 30) & (Sa > 90) & (V > 140))).astype(np.uint8) * 255, cv2.MORPH_CLOSE, K(5))
orange = big_components(orange, 300)

# Estrella: todo lo que no es papel blanco, fuera del óvalo
dist = np.abs(255 - rgb.astype(int)).sum(-1)
star = ((dist > 70).astype(np.uint8) * 255) & ~cv2.dilate(orange, K(3)) & ~oval
star[:, :60] = 0                       # borde izquierdo del escaneo
star = big_components(cv2.morphologyEx(star, cv2.MORPH_OPEN, K(3)), 5000)
star = fill_holes(cv2.morphologyEx(star | cv2.dilate(oval, K(3)), cv2.MORPH_CLOSE, K(15)))
# Bajo el óvalo la estrella se rellena solo donde el óvalo la tapa gire lo que gire: al girar no asoma
M = cv2.moments(oval); OCX, OCY = M['m10'] / M['m00'], M['m01'] / M['m00']
core = oval.copy()
for ang in range(10, 360, 10):
    R = cv2.getRotationMatrix2D((OCX, OCY), ang, 1.0)
    core &= cv2.warpAffine(oval, R, oval.shape[::-1])
star = (star & ~oval) | cv2.erode(core, K(81))   # margen para el rebote de escala al entrar

# Trazos blancos dentro del óvalo
white = (((Sa < 95) & (V > 95)).astype(np.uint8) * 255) & cv2.erode(oval, K(9)) & ~orange
white = cv2.morphologyEx(white, cv2.MORPH_OPEN, K(3))
n, lab, st, _ = cv2.connectedComponentsWithStats(white)
strokes = [i for i in range(1, n) if st[i, 4] > 150]


def soft(mask, f=1.2):
    return np.clip(cv2.GaussianBlur(mask.astype(np.float32), (0, 0), f), 0, 255).astype(np.uint8)


def png(arr):
    b = io.BytesIO(); Image.fromarray(arr).save(b, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()


def geodesic(mask, start, block=None):
    """Distancia caminando dentro del trazo desde `start` (x, y): sigue curvas como la S o la Q."""
    m = mask > 0
    if block is not None: m &= ~block
    d = np.full(m.shape, -1.0); q = deque()
    sx, sy = start
    ys, xs = np.nonzero(m); j = np.argmin((xs - sx) ** 2 + (ys - sy) ** 2)
    d[ys[j], xs[j]] = 0; q.append((ys[j], xs[j]))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < m.shape[0] and 0 <= xx < m.shape[1] and m[yy, xx] and d[yy, xx] < 0:
                d[yy, xx] = d[y, x] + 1; q.append((yy, xx))
    full = mask > 0
    if (full & (d < 0)).any():         # píxeles no alcanzados (p. ej. tras la barrera): al final
        d[full & (d < 0)] = d.max() + 1
    return d


def projection(mask, p0, p1):
    ys, xs = np.mgrid[:mask.shape[0], :mask.shape[1]]
    v = np.array(p1, float) - p0; v /= np.dot(v, v)
    return (xs - p0[0]) * v[0] + (ys - p0[1]) * v[1]


layers = []


def add_layer(name, mask, color_src, t=None, feather=1.2, bristles=0.0):
    ys, xs = np.nonzero(mask)
    pad = 6
    x0, y0 = max(xs.min() - pad, 0), max(ys.min() - pad, 0)
    x1, y1 = min(xs.max() + pad + 1, mask.shape[1]), min(ys.max() + pad + 1, mask.shape[0])
    a = soft(mask, feather)[y0:y1, x0:x1]
    layer = {'name': name, 'x': int(x0), 'y': int(y0), 'w': int(x1 - x0), 'h': int(y1 - y0),
             'img': png(np.dstack([color_src[y0:y1, x0:x1], a]))}
    if t is not None:
        inside = mask > 0
        tt = t.astype(float).copy()
        lo, hi = tt[inside].min(), tt[inside].max()
        tt = np.clip((tt - lo) / (hi - lo + 1e-9), 0, 1)
        if bristles:                    # borde de avance irregular, como cerdas de pincel
            tt = np.clip(tt + bristles * cv2.GaussianBlur(rng.standard_normal(tt.shape), (0, 0), 2.2) * 3, 0, 1)
        # fuera del trazo: el tiempo del píxel interior más cercano (para el borde suavizado)
        _, idx = cv2.distanceTransformWithLabels((~inside).astype(np.uint8), cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
        iy, ix = np.nonzero(inside); lut = np.zeros(idx.max() + 1); lut[idx[iy, ix]] = tt[iy, ix]
        tt = lut[idx]
        crop = (tt[y0:y1, x0:x1] * 255).round().astype(np.uint8)
        layer['time'] = png(crop)
        # recorrido de la punta del pincel (para salpicaduras y destellos)
        path = []
        for k in np.linspace(0, 1, 24):
            sel = inside & (np.abs(tt - k) < 0.05)
            if sel.any():
                yy, xx = np.nonzero(sel); path.append([round(float(xx.mean()), 1), round(float(yy.mean()), 1), round(float(k), 3)])
        layer['path'] = path
    layers.append(layer)
    print(name, layer['w'], 'x', layer['h'])


# Estrella: bajo el óvalo se rellena con el granate medio
star_rgb = rgb.copy(); body = (cv2.erode(star, K(3)) > 0) & (cv2.dilate(oval, K(15)) == 0)
med = np.median(rgb[body & (dist > 150)], axis=0)
star_rgb[(star > 0) & ((oval > 0) | (cv2.dilate(orange, K(9)) > 0))] = med
add_layer('estrella', cv2.erode(star, K(5)), star_rgb)   # sin el halo blanco del papel

# Óvalo: se "repinta" el azul bajo la cruz y los trazos
hole = ((oval > 0) & (navy == 0)).astype(np.uint8) * 255
base = img.copy(); base[oval == 0] = np.median(img[navy > 0], axis=0)   # que el relleno no tome papel ni naranja de fuera
oval_rgb = cv2.cvtColor(cv2.inpaint(base, cv2.dilate(hole, K(5)), 9, cv2.INPAINT_TELEA), cv2.COLOR_BGR2RGB)
add_layer('ovalo', cv2.erode(oval, K(7)), oval_rgb)

# Cruz naranja: trazo diagonal (de arriba hacia abajo) y barra horizontal (de izquierda a derecha)
ys, xs = np.nonzero(orange)
top = (xs[np.argmin(ys)], ys.min()); bot = (xs[np.argmax(ys)], ys.max())
yy, xx = np.mgrid[:orange.shape[0], :orange.shape[1]]
d = np.array(bot, float) - top; nrm = np.array([-d[1], d[0]]) / np.hypot(*d)
perp = np.abs((xx - top[0]) * nrm[0] + (yy - top[1]) * nrm[1])
band = (yy > 495) & (yy < 665)
diag = orange & (((perp < 62) & ~band) | ((perp < 48) & band)).astype(np.uint8) * 255
diag = big_components(diag, 2000)
horiz = orange & ~cv2.erode(diag, K(7))   # se solapa un poco: sin costura entre pinceladas
horiz[(yy < 470) | (yy > 700)] = 0
horiz = big_components(cv2.morphologyEx(horiz, cv2.MORPH_OPEN, K(5)), 250)
add_layer('cruz-diagonal', diag, rgb, projection(diag, top, bot), bristles=0.012)
left = (xs.min(), ys[np.argmin(xs)]); right = (xs.max(), ys[np.argmax(xs)])
add_layer('cruz-horizontal', horiz, rgb, projection(horiz, left, right), bristles=0.012)

# Trazos blancos, en orden de escritura: ≡ (3 barras) · S · T (barra + palo) · Q
info = {i: tuple(st[i, :4]) for i in strokes}
def by(pred): return [i for i in strokes if pred(*info[i])]
bars = sorted(by(lambda x, y, w, h: x < 620 and h < 45 and y < 600), key=lambda i: info[i][1])
s_ = by(lambda x, y, w, h: x > 620 and y < 600)[0]
t_bar = by(lambda x, y, w, h: x < 620 and y > 600 and w > h)[0]
t_post = by(lambda x, y, w, h: x < 620 and y > 600 and h > w)[0]
q_ = by(lambda x, y, w, h: x > 620 and y > 600)[0]
for k, i in enumerate(bars):
    m = (lab == i).astype(np.uint8) * 255
    x, y, w, h = info[i]
    add_layer(f'barra{k + 1}', m, rgb, geodesic(m, (x, y + h // 2)), 0.8)
m = (lab == s_).astype(np.uint8) * 255; x, y, w, h = info[s_]
add_layer('s', m, rgb, geodesic(m, (x + w, y)), 0.8)
m = (lab == t_bar).astype(np.uint8) * 255; x, y, w, h = info[t_bar]
add_layer('t-barra', m, rgb, geodesic(m, (x, y + h)), 0.8)
m = (lab == t_post).astype(np.uint8) * 255; x, y, w, h = info[t_post]
add_layer('t-palo', m, rgb, geodesic(m, (x + w // 2, y)), 0.8)
m = (lab == q_).astype(np.uint8) * 255; x, y, w, h = info[q_]
blk = np.zeros(m.shape, bool); blk[y - 4:y + 70, x + 38:x + 48] = True   # corta el aro: se dibuja en un solo sentido
add_layer('q', m, rgb, geodesic(m, (x + 20, y + 20), blk), 0.8)

# Centro del óvalo (pivote de la estrella)
meta = {'size': int(img.shape[1]), 'cx': round(OCX, 1), 'cy': round(OCY, 1)}
(HERE / 'capas.js').write_text('// Generado por separar_capas.py: no editar a mano.\nwindow.LOGO_CAPAS = ' +
                               json.dumps({'meta': meta, 'layers': layers}) + ';\n')
print('→', HERE / 'capas.js', meta)
