"""Música + efectos de sonido sincronizados para el logo animado (logo-animado.html).

Todo se sintetiza aquí (sin samples ni pistas con derechos):
  · Colchón grave que crece hasta el golpe y acorde cálido que se queda sonando.
  · SFX en los mismos tiempos que la línea de tiempo T de logo-animado.html:
    caída del óvalo, estrella-shuriken, dos pinceladas, notas por cada trazo blanco, subida y golpe final.

Uso:  python3 audio/logo_animado_audio.py   → audio/logo-animado-mix.wav (+ stems música/sfx)
"""
import wave
from pathlib import Path

import numpy as np

SR = 44100
DUR = 8.0
N = int(SR * DUR)
rng = np.random.default_rng(11)
OUT = Path(__file__).resolve().parent

# Línea de tiempo (igual que T en logo-animado.html)
OVAL, IMPACT = 0.10, 0.28
STAR = (0.38, 1.45)
DIAG, HORIZ = (1.55, 2.12), (2.08, 2.62)
WHITES = [(2.78, 2.98), (2.93, 3.13), (3.08, 3.28), (3.36, 3.78), (3.86, 4.02), (4.0, 4.2), (4.26, 4.7)]
BOOM = 4.8


def buf():
    return np.zeros((N, 2))


def t_axis(sec):
    return np.arange(int(SR * sec)) / SR


def add(dst, sig, at, gain=1.0, pan=0.0):
    i = int(at * SR)
    if i >= N:
        return
    sig = sig[: N - i]
    l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
    dst[i:i + len(sig), 0] += sig * gain * l * 1.414
    dst[i:i + len(sig), 1] += sig * gain * r * 1.414


def env(n, a=0.005, d=0.3, curve=4.0):
    t = np.arange(n) / SR
    return np.clip(t / max(a, 1e-4), 0, 1) * np.exp(-curve * t / max(d, 1e-4))


def box(x, k):
    return np.convolve(x, np.ones(k) / k, mode='same')


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def saw(f, t):
    return 2 * ((f * t) % 1.0) - 1


def reverb(x, taps=((0.029, .55), (0.043, .45), (0.067, .36), (0.101, .28), (0.149, .2), (0.211, .14), (0.307, .09))):
    y = x.copy()
    for d, g in taps:
        k = int(d * SR)
        y[k:] += x[:-k] * g
    return y


def whoosh(dur, up=True, bright=1.0):
    tt = t_axis(dur)
    n = rng.standard_normal(len(tt))
    soft, hi = box(n, 40), n - box(n, 4)
    p = tt / dur if up else 1 - tt / dur
    s = soft * (1 - p) + hi * p * 0.5 * bright
    return s * np.sin(np.pi * np.clip(tt / dur, 0, 1)) ** 2 * 1.6


def brush(dur):
    """Pincelada: ruido rasposo con textura de cerdas, filtro que se abre y se cierra."""
    tt = t_axis(dur + 0.12)
    n = rng.standard_normal(len(tt))
    grit = (box(n, 3) - box(n, 18)) * (0.6 + 0.4 * np.abs(np.sin(2 * np.pi * 37 * tt + 3 * np.sin(2 * np.pi * 5 * tt))))
    e = np.clip(tt / 0.03, 0, 1) * np.clip((dur + 0.12 - tt) / 0.18, 0, 1) * (0.7 + 0.3 * np.sin(np.pi * tt / dur))
    return grit * e * 1.4


def thump(f0=120, f1=42, dur=0.5):
    tt = t_axis(dur)
    f = f1 + (f0 - f1) * np.exp(-tt * 22)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt * 7)


def splat(dur=0.18):
    tt = t_axis(dur)
    n = rng.standard_normal(len(tt))
    return (box(n, 6) - box(n, 30)) * np.exp(-tt * 28) * 1.6


def pluck(m, dur=0.9):
    tt = t_axis(dur)
    f = hz(m)
    s = np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt * 6) + 0.15 * np.sin(2 * np.pi * 3 * f * tt) * np.exp(-tt * 10)
    return s * env(len(tt), 0.002, 0.45, 4)


def shing(dur=0.7):
    """Brillo metálico (inarmónico) para la estrella-shuriken."""
    tt = t_axis(dur)
    s = sum(np.sin(2 * np.pi * f * tt) * g for f, g in ((2793, .5), (3950, .35), (5274, .25), (6644, .15)))
    return s * env(len(tt), 0.002, dur, 5)


# =========================== MÚSICA ===========================
music = buf()

# Colchón grave (Do + Sol) que crece hasta el golpe
tt = t_axis(BOOM)
drone = sum(saw(hz(m) * (1 + d), tt) for m in (36, 43) for d in (-0.002, 0.002))
drone = box(drone, 60) * (0.25 + 0.75 * (tt / BOOM) ** 2)
add(music, drone / 4 * np.clip(tt / 0.4, 0, 1), 0, gain=0.22)

# Pulso suave de bombo bajo los trazos (negras a 120 BPM)
for k in range(6):
    add(music, thump(90, 45, 0.3), 1.55 + k * 0.5, gain=0.18)

# Acorde cálido tras el golpe: Do mayor 9 (pad de sierras desafinadas + campanas)
tt = t_axis(DUR - BOOM)
pad = sum(saw(hz(m) * (1 + d), tt) for m in (48, 55, 60, 64, 67, 74) for d in (-0.003, 0.003))
pad = box(pad, 30) / 12 * np.clip(tt / 0.05, 0, 1) * np.clip((DUR - BOOM - tt) / 1.2, 0, 1)
add(music, reverb(pad), BOOM, gain=0.30)
for i, m in enumerate((72, 76, 79, 84, 86)):
    add(music, reverb(pluck(m, 1.6)), BOOM + 0.05 + i * 0.09, gain=0.09, pan=(-0.4, 0.4)[i % 2])

# =========================== SFX ===========================
sfx = buf()

# Óvalo: cae (whoosh) y aterriza (golpe + salpicón)
add(sfx, whoosh(0.2, up=False), OVAL, gain=0.25)
add(sfx, thump(150, 48, 0.6), IMPACT, gain=0.75)
add(sfx, splat(0.22), IMPACT, gain=0.35)

# Estrella: remolino que gira (trémolo) y "shing" al asentarse
dur = STAR[1] - STAR[0]
tt = t_axis(dur)
spin = whoosh(dur, up=False) * (0.55 + 0.45 * np.sin(2 * np.pi * (14 - 10 * tt / dur) * tt))
for i, pan in enumerate((-0.5, 0.5)):
    add(sfx, spin, STAR[0] + i * 0.012, gain=0.22, pan=pan)
add(sfx, reverb(shing()), STAR[0] + 0.5, gain=0.12, pan=0.2)

# Pinceladas naranjas + gotitas
for (a, b), pan in ((DIAG, -0.15), (HORIZ, 0.25)):
    add(sfx, brush(b - a), a, gain=0.28, pan=pan)
    for k in range(5):
        add(sfx, splat(0.06), a + 0.08 + k * (b - a) / 5 + rng.uniform(0, 0.05), gain=0.12, pan=rng.uniform(-0.7, 0.7))

# Trazos blancos: una nota ascendente por trazo (pentatónica de Do) + raspado de tiza
NOTES = (72, 74, 76, 79, 81, 84, 86)
for (a, b), m in zip(WHITES, NOTES):
    add(sfx, reverb(pluck(m)), a, gain=0.16, pan=(m - 79) / 12)
    add(sfx, brush(b - a) * 0.5, a, gain=0.12, pan=0)

# Subida antes del golpe (ruido + tono que asciende)
rise = 1.0
tt = t_axis(rise)
f = hz(48) * 2 ** (2 * tt / rise)
riser = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.4 + whoosh(rise, up=True, bright=1.4) * 0.6
add(sfx, riser * (tt / rise) ** 2, BOOM - rise, gain=0.25)

# Golpe: sub que cae + crash + destellos
add(sfx, thump(180, 38, 1.4), BOOM, gain=0.95)
tt = t_axis(1.6)
crash = rng.standard_normal(len(tt))
crash = (crash - box(crash, 6)) * np.exp(-tt * 3.2)
add(sfx, reverb(crash), BOOM, gain=0.16)
for k in range(14):
    m = 84 + int(rng.choice([0, 2, 4, 7, 9, 12, 14]))
    add(sfx, pluck(m, 0.35) * 0.6, BOOM + 0.1 + k * 0.07 + rng.uniform(0, 0.04), gain=0.06, pan=rng.uniform(-0.8, 0.8))

# =========================== MEZCLA ===========================


def write(name, x):
    x = x / max(1e-9, np.abs(x).max()) * 0.89
    with wave.open(str(OUT / name), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((x * 32767).astype('<i2').tobytes())
    print('→', OUT / name)


write('logo-animado-mix.wav', np.tanh(1.2 * (music + sfx)))
write('logo-animado-musica.wav', music)
write('logo-animado-sfx.wav', sfx)
