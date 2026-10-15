"""Música + efectos de sonido sincronizados para el Reel del Kit Inversor.

Todo se sintetiza aquí (sin samples ni pistas con derechos):
  · Pista pop/electrónica a 120 BPM, progresión C – G – Am – F (1 compás = 2 s).
  · SFX colocados en los mismos tiempos que los keyframes de kit-inversor.html.

Uso:  python3 audio/kit_audio.py   → audio/kit-mix.wav (+ stems música/sfx)
"""
import wave
from pathlib import Path

import numpy as np

SR = 44100
DUR = 19.0
MUSIC_END = 18.0   # el último compás resuelve aquí
BPM = 120
BEAT = 60 / BPM
N = int(SR * DUR)
rng = np.random.default_rng(7)
OUT = Path(__file__).resolve().parent


def buf():
    return np.zeros((N, 2))


def t_axis(sec):
    return np.arange(int(SR * sec)) / SR


def add(dst, sig, at, gain=1.0, pan=0.0):
    """Suma una señal mono (o estéreo) en el instante `at` (s) con paneo -1..1."""
    i = int(at * SR)
    if i >= N:
        return
    sig = sig[: N - i]
    if sig.ndim == 1:
        l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
        dst[i:i + len(sig), 0] += sig * gain * l * 1.414
        dst[i:i + len(sig), 1] += sig * gain * r * 1.414
    else:
        dst[i:i + len(sig)] += sig * gain


def env(n, a=0.005, d=0.3, curve=4.0):
    t = np.arange(n) / SR
    att = np.clip(t / max(a, 1e-4), 0, 1)
    return att * np.exp(-curve * t / max(d, 1e-4))


def box(x, k):
    return np.convolve(x, np.ones(k) / k, mode='same')


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def saw(f, t):
    return 2 * ((f * t) % 1.0) - 1


def reverb(x, taps=((0.031, .5), (0.047, .42), (0.071, .33), (0.113, .25), (0.163, .18), (0.229, .12))):
    y = x.copy()
    for d, g in taps:
        k = int(d * SR)
        y[k:] += x[:-k] * g
    return y


# =========================== MÚSICA ===========================
music = buf()
# Progresión (raíz MIDI, triada) — C, G, Am, F; el último compás resuelve en C
CHORDS = [(48, [60, 64, 67]), (43, [59, 62, 67]), (45, [60, 64, 69]), (41, [60, 65, 69])]
GROOVE_START = 0.5      # el beat completo entra junto al golpe de "Preventas"
END_FADE = (18.2, 19.0)


def chord_at(t):
    bar = int(t // 2)
    return CHORDS[bar % 4] if t < MUSIC_END else CHORDS[0]


# Pad (sierras desafinadas + filtro suave), entra desde 0 con filtro abriéndose
for bar in range(10):
    t0 = bar * 2.0
    root, triad = chord_at(t0 + 0.01)
    tt = t_axis(2.0)
    pad = np.zeros_like(tt)
    for m in triad:
        for det in (-0.08, 0.08):
            pad += saw(hz(m + det / 1.0) * (1 + det / 100), tt)
    pad = box(pad, 24 if bar == 0 else 14) / 6
    shape = np.clip(tt / 0.08, 0, 1) * np.clip((2.0 - tt) / 0.08, 0, 1)
    add(music, pad * shape, t0, gain=0.10 if bar else 0.07, pan=0)

# Bajo en corcheas (seno + armónico) con "pump"
for k in range(int((MUSIC_END - GROOVE_START) / (BEAT / 2))):
    t0 = GROOVE_START + k * BEAT / 2
    root, _ = chord_at(t0)
    tt = t_axis(BEAT / 2)
    f = hz(root)
    b = np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * 2 * f * tt)
    b = np.tanh(1.6 * b) * env(len(tt), a=0.004, d=0.22, curve=3)
    add(music, b, t0, gain=0.22)

# Kick (sweep 140→45 Hz) en cada negra
def kick():
    tt = t_axis(0.35)
    f = 45 + 95 * np.exp(-tt * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-tt * 9) + 0.15 * rng.standard_normal(len(tt)) * np.exp(-tt * 120)

for k in range(int((MUSIC_END - GROOVE_START) / BEAT) + 1):
    add(music, kick(), GROOVE_START + k * BEAT, gain=0.55)

# Clap en beats 2 y 4
def clap():
    tt = t_axis(0.25)
    n = rng.standard_normal(len(tt))
    n = box(n, 4) - box(n, 14)  # banda media (~1–5 kHz): menos chillón
    e = np.zeros_like(tt)
    for off in (0, 0.01, 0.022):
        e += np.where(tt >= off, np.exp(-(tt - off) * 38), 0)
    return n * e * 0.6

for k in range(int((MUSIC_END - GROOVE_START) / BEAT) + 1):
    if k % 2 == 1:
        add(music, reverb(clap()), GROOVE_START + k * BEAT, gain=0.3, pan=0.05)

# Hi-hats en contratiempo
def hat(open_=False):
    tt = t_axis(0.18 if open_ else 0.06)
    n = rng.standard_normal(len(tt))
    n = box(n, 2) - box(n, 5)
    return n * np.exp(-tt * (22 if open_ else 70))

for k in range(int((MUSIC_END - GROOVE_START) / (BEAT / 2))):
    if k % 2 == 1:
        add(music, hat(k % 8 == 7), GROOVE_START + k * BEAT / 2, gain=0.07, pan=0.3)

# Pluck arpegiado (campanita brillante) en corcheas desde el compás 2
for k in range(int((MUSIC_END - 2.5) / (BEAT / 2))):
    t0 = 2.5 + k * BEAT / 2
    _, triad = chord_at(t0)
    m = triad[k % 3] + 12
    tt = t_axis(0.4)
    f = hz(m)
    p = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 3 * f * tt)) * env(len(tt), 0.002, 0.25, 5)
    add(music, p, t0, gain=0.045, pan=-0.25 if k % 2 else 0.25)

# Acorde final que resuelve
tt = t_axis(1.2)
fin = sum(np.sin(2 * np.pi * hz(m + 12) * tt) for m in (60, 64, 67, 72)) * env(len(tt), 0.01, 1.0, 3)
add(music, reverb(fin), MUSIC_END, gain=0.06)

# Sidechain (la música "respira" con el kick)
side = np.ones(N)
for k in range(int((MUSIC_END - GROOVE_START) / BEAT) + 1):
    i = int((GROOVE_START + k * BEAT) * SR)
    tt = t_axis(BEAT)
    seg = 1 - 0.55 * np.exp(-tt * 14)
    side[i:i + len(seg)] = np.minimum(side[i:i + len(seg)], seg[: N - i])
# Se aplica suave a toda la mezcla musical
music *= (0.35 + 0.65 * side)[:, None]

# Fade final
ft = np.arange(N) / SR
music *= np.clip((END_FADE[1] - ft) / (END_FADE[1] - END_FADE[0]), 0, 1)[:, None]

# =========================== SFX ===========================
sfx = buf()


def whoosh(dur=0.45, up=True):
    tt = t_axis(dur)
    n = rng.standard_normal(len(tt))
    # barrido de filtro: mezcla de versiones más/menos suavizadas
    soft, bright = box(n, 40), n - box(n, 4)
    p = tt / dur if up else 1 - tt / dur
    s = soft * (1 - p) + bright * p * 0.5
    e = np.sin(np.pi * np.clip(tt / dur, 0, 1)) ** 2
    return s * e * 1.6


def pop(f0=900, f1=300, dur=0.12):
    tt = t_axis(dur)
    f = f1 + (f0 - f1) * np.exp(-tt * 40)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(tt), 0.001, dur, 5)


def tick(f=2600):
    tt = t_axis(0.05)
    return np.sin(2 * np.pi * f * tt) * np.exp(-tt * 90)


def key_click():
    tt = t_axis(0.03)
    n = rng.standard_normal(len(tt))
    return (n - box(n, 3)) * np.exp(-tt * 160) * 0.6 + np.sin(2 * np.pi * 1800 * tt) * np.exp(-tt * 200) * 0.4


def impact():
    tt = t_axis(1.2)
    f = 38 + 80 * np.exp(-tt * 10)
    boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 3.2)
    n = rng.standard_normal(len(tt))
    crash = (n - box(n, 2)) * np.exp(-tt * 6) * 0.25
    return reverb(boom + crash)


def sparkle(count=5, base=84):
    out = np.zeros(int(SR * 0.9))
    for j in range(count):
        m = base + [0, 4, 7, 12, 16, 19][j % 6]
        tt = t_axis(0.5)
        s = np.sin(2 * np.pi * hz(m) * tt) * env(len(tt), 0.002, 0.35, 6)
        i = int(j * 0.06 * SR)
        out[i:i + len(s)] += s[: len(out) - i]
    return reverb(out)


def riser(dur=0.6):
    tt = t_axis(dur)
    f = 300 + 1500 * (tt / dur) ** 2
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.3
    n = rng.standard_normal(len(tt)) * (tt / dur) ** 2 * 0.4
    return (s + n) * np.clip(tt / dur, 0, 1)


def swipe(dur=0.3):
    tt = t_axis(dur)
    n = rng.standard_normal(len(tt))
    return (n - box(n, 5)) * np.sin(np.pi * tt / dur) ** 2 * 0.6


# --- 1 · Hook
add(sfx, riser(0.5), 0.0, 0.35)
add(sfx, pop(1300, 600, 0.09), 0.1, 0.25)                     # píldora MÁS POPULAR
add(sfx, whoosh(0.3), 0.22, 0.25, -0.3)                       # "El Kit"
add(sfx, impact(), 0.55, 0.6)                                 # "Inversor"
add(sfx, swipe(0.3), 0.95, 0.25)                              # subrayado
add(sfx, sparkle(6, 88), 0.85, 0.12, 0.2)
add(sfx, pop(700, 350, 0.1), 1.5, 0.2)
add(sfx, sparkle(3, 79), 0.95, 0.08, -0.2)                    # logo

# --- 2 · Los dos bootcamps
add(sfx, whoosh(0.5), 2.15, 0.5)
for t0, f0 in ((2.55, 800), (2.85, 900)):
    add(sfx, pop(f0, f0 * 0.4, 0.1), t0 + 0.05, 0.22)
add(sfx, pop(1050, 420, 0.1), 3.3, 0.24)
add(sfx, swipe(0.35), 3.55, 0.35)                             # marcador "en un solo kit."
add(sfx, whoosh(0.35), 4.0, 0.3, -0.6)                        # Nivel 1 entra por la izquierda
add(sfx, whoosh(0.35), 4.25, 0.3, 0.6)                        # Nivel 2 entra por la derecha
add(sfx, pop(260, 90, 0.25), 4.8, 0.4)                        # el kit "cierra"
add(sfx, pop(1300, 600, 0.09), 5.05, 0.25)                    # etiqueta KIT INVERSOR
add(sfx, sparkle(4, 86), 5.1, 0.1)

# --- 3 · Qué incluye
add(sfx, whoosh(0.5), 6.15, 0.5)
add(sfx, whoosh(0.3), 6.55, 0.2)
for i, t0 in enumerate((7.25, 8.0, 8.75)):
    add(sfx, pop(260, 100, 0.2), t0 + 0.1, 0.3)               # tarjeta aterriza
    add(sfx, pop(1100, 450, 0.09), t0 + 0.25, 0.22)           # icono
    add(sfx, tick(2400 + i * 300), t0 + 0.5, 0.3)             # check
for i in range(3):
    add(sfx, pop(900 + i * 150, 500, 0.06), 10.5 + i * 0.25, 0.12)   # "respiración" de iconos

# --- 4 · Exclusivo
add(sfx, whoosh(0.5), 11.65, 0.5)
add(sfx, sparkle(5, 91), 12.15, 0.14)                         # estrella
add(sfx, whoosh(0.3), 12.5, 0.2)
add(sfx, impact(), 12.85, 0.45)                               # "10"
add(sfx, whoosh(0.3), 13.0, 0.2)
for i in range(10):                                           # 10 cupos que se encienden
    add(sfx, tick(1800 + i * 120), 13.3 + i * 0.05, 0.14)
add(sfx, pop(700, 300, 0.12), 13.8, 0.25)                     # caja "en vivo"

# --- 5 · Precio
add(sfx, whoosh(0.5), 14.65, 0.5)
add(sfx, pop(260, 90, 0.25), 15.1, 0.4)                       # tarjeta aterriza
add(sfx, riser(1.0), 15.5, 0.15)                              # contador "Mi inversión"
for i in range(16):                                           # cuenta regresiva $559 → $399
    add(sfx, key_click(), 16.3 + i * 0.047, 0.18)
add(sfx, impact(), 17.05, 0.5)                                # llega a $399
add(sfx, swipe(0.25), 17.35, 0.25)                            # tachado "Antes $559"
add(sfx, pop(1300, 600, 0.09), 17.55, 0.3)                    # AHORRAS $160
add(sfx, sparkle(6, 91), 17.6, 0.14, 0.2)
add(sfx, pop(1500, 700, 0.07), 18.35, 0.18)

# =========================== MEZCLA ===========================
def norm(x, peak):
    m = np.max(np.abs(x)) or 1
    return x / m * peak


music_n = norm(music, 0.62)
sfx_n = norm(sfx, 0.55)
mix = np.tanh((music_n + sfx_n) * 1.1) * 0.92


def write(path, x):
    x16 = (np.clip(x, -1, 1) * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(x16.tobytes())


write(OUT / 'kit-musica.wav', music_n)
write(OUT / 'kit-sfx.wav', sfx_n)
write(OUT / 'kit-mix.wav', mix)
print('Listo →', OUT / 'kit-mix.wav')
