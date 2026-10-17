# Escaleta técnica · Logo animado (logo pintado a mano)

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 8 s · H.264 + audio AAC (−14 LUFS).
También hay una versión cuadrada 1080 × 1080 para el feed o una intro de video.

**Archivos**
- `output/logo-animado.mp4`: vertical, con música y efectos
- `output/logo-animado-cuadrado.mp4`: cuadrado, con música y efectos
- `logo-animado.html`: la animación (canvas, determinista fotograma a fotograma)
- `assets/logo-pintado/logo-original.jpg`: el logo tal cual se recibió
- `assets/logo-pintado/separar_capas.py` → `assets/logo-pintado/capas.js`: separa el logo en capas
- `audio/logo_animado_audio.py`: música y efectos sintetizados (sin samples con derechos)

**Render**
```
pip install opencv-python-headless numpy pillow          # solo si se vuelven a separar las capas
python3 assets/logo-pintado/separar_capas.py
node render.mjs logo-animado.html                         # → output/logo-animado.mp4 (sin audio)
node render.mjs logo-animado.html --cuadrado              # → output/logo-animado-cuadrado.mp4
python3 audio/logo_animado_audio.py
ffmpeg -i output/logo-animado.mp4 -i audio/logo-animado-mix.wav -map 0:v -map 1:a -c:v copy \
  -af loudnorm=I=-14:TP=-1 -c:a aac -b:a 192k -shortest output/final.mp4
node render.mjs logo-animado.html --stills                # fotogramas clave
```

## Cómo se anima un logo pintado
El logo es una imagen pintada a mano, no un vector. Para animarlo sin perder la textura del pincel se separa en capas por color:
estrella granate · óvalo azul · cruz naranja (trazo diagonal y barra horizontal) · 7 trazos blancos (≡, S, T, Q).
- El azul que queda tapado por la cruz y las letras se rellena (inpainting), así el óvalo puede aparecer solo.
- La estrella se completa por detrás del óvalo, así puede girar sin dejar huecos.
- Cada trazo lleva un **mapa de tiempo**, que indica por dónde avanza la pincelada. La S y la Q se recorren siguiendo su curva y la cruz va de punta a punta.
  Así cada trazo **se pinta en vivo**, con el borde húmedo más brillante y un borde de avance irregular, como las cerdas de un pincel.

## Cambios de la v2
- Sin estrellitas decorativas (ni el estallido del golpe, ni el polvo brillante, ni los destellos al terminar cada letra).
- La estrella granate gira sin parar hasta el golpe y ahí frena.

## Escaleta

| # | Momento | Tiempo | Qué pasa | Sonido |
|---|---|---|---|---|
| 1 | Cae el óvalo | 0,10–0,70 s | Cae desde arriba, se aplasta al tocar (squash & stretch), onda expansiva y temblor de cámara | Whoosh + golpe grave + salpicón |
| 2 | Estrella shuriken | 0,38–4,80 s | Sale girando desde detrás del óvalo, con estela de movimiento, y **no para de girar**: acelera hacia el final y frena en seco en el golpe, quedando en su posición original | Remolino continuo que acelera + "clac" metálico al frenar |
| 3 | Cruz naranja | 1,55–2,62 s | Dos pinceladas: la diagonal de arriba abajo y la horizontal de izquierda a derecha, con salpicaduras de pintura | Pinceladas rasposas + gotitas; pulso de bombo |
| 4 | Letras | 2,78–4,70 s | ≡ (3 barras), S, T y Q se escriben una a una, con una luz en la punta | Una nota ascendente por trazo + raspado de tiza |
| 5 | Golpe | 4,80 s | La estrella frena (se pasa un poco y vuelve), flash, el logo late (encoge y rebota) y onda dorada | Subida + sub grave + crash |
| 6 | Brillo | 5,05–5,80 s | Un reflejo barre el logo, solo sobre la pintura | — |
| 7 | Reposo | 5,6–8 s | El logo flota, la estrella oscila suave y el resplandor cálido respira | Acorde cálido que se desvanece |

**Fondo:** azul tinta con viñeta, resplandor naranja-granate detrás del logo y grano de papel animado, que acompaña la textura de la pintura.
