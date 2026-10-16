# Escaleta técnica · Reel "Kit Inversor" (v2)

**Formato:** vertical 9:16 · 1080 × 1920 px · 30 fps · 17 s · H.264 + audio AAC (−14 LUFS)
**Ritmo:** 120 BPM (1 beat = 0,5 s).

**Archivos**
- `output/kit-inversor.mp4`: Reel con música y efectos
- `output/kit-inversor-solo-efectos.mp4`: solo efectos, para usar una canción de Instagram
- `output/kit-inversor-cta.png`: **imagen fija** del CTA (Historia, con espacio libre para el sticker de link)
- `kit-inversor.html` / `cta-kit-inversor.html` / `audio/kit_audio.py`: fuentes
- `assets/iconos-3d/`: íconos 3D Fluent Emoji de Microsoft (licencia MIT, incluida)
- `assets/logo-freenanzas-blanco.svg`: logo oficial en HD

**Render**
```
node render.mjs kit-inversor.html
python3 audio/kit_audio.py
ffmpeg -i output/kit-inversor.mp4 -i audio/kit-mix.wav -map 0:v -map 1:a -c:v copy \
  -af loudnorm=I=-14:TP=-1 -c:a aac -b:a 192k -shortest output/final.mp4
node render.mjs cta-kit-inversor.html --stills
```

## Cambios de la v2 (pedidos por el equipo)
- **Sin precio:** se eliminaron la escena de precio, el widget "Mi inversión" y el precio de la imagen CTA.
- **Estilo de la pieza "Tu turno":**
  - Fondo morado en degradado, con luz en las esquinas y una cuadrícula fina. Las escenas en verde usan el mismo tratamiento.
  - Tipografía: **Poppins** ExtraBold en los titulares, **Playfair Display** cursiva en lima para la palabra clave y **Oswald** con un punto lima en las etiquetas ("◉ MÁS POPULAR", "◉ EXCLUSIVO").
  - **Íconos 3D:** cohete, gráfico, globo, birrete, caja de herramientas, calendario y micrófono. Entran con pop y luego flotan.
  - Decoración con **estrellas y puntos** lima y blancos.
- **"Guías y herramientas" con más protagonismo:** en lugar de una línea de texto ahora tiene chips ("**Guía de impuestos**" en lima, más Plantillas, Calculadoras y Recursos). "Guía de impuestos" vuelve a hacer pop para destacarse.
- **Logo oficial en SVG (HD),** también aplicado a los Reels y a la imagen de Preventas.
- El video **cierra en la escena "Exclusivo · 10 primeros"**.

## Escaleta

| # | Escena | Tiempo | Fondo | Entrada |
|---|---|---|---|---|
| 1 | Hook: 🚀 ◉ MÁS POPULAR · "El Kit *Inversor*" | 0–2,5 s | Morado + cuadrícula | — |
| 2 | "Los dos bootcamps completos, *en un solo kit.*" | 2,5–6,5 s | Verde + cuadrícula | Wipe circular (2,2–2,6) |
| 3 | ¿Qué *incluye?*: 3 tarjetas con íconos 3D | 6,5–12,5 s | Morado + cuadrícula | Panel sube (6,2–6,6) |
| 4 | 🎙️ ◉ EXCLUSIVO · Solo para los *10* primeros · Q&A en vivo (cierre) | 12,5–17 s | Morado + cuadrícula | Wipe lateral (12,2–12,6) |

## Keyframes clave
**1 · Hook**
- 0–0,65 s: el cohete 3D despega desde abajo a la izquierda y luego flota.
- 0,35 s: aparece la etiqueta "◉ MÁS POPULAR".
- 0,45 s: "El Kit".
- 0,75–1,15 s: "*Inversor*" entra con escala 1,8 → 1 y desenfoque, con un golpe de sonido.
- 1,1 s: subrayado lima.
- 0,9 s: estrellas y puntos.
- 1,0 s: logo.

**2 · Dos bootcamps**
- 2,55 / 2,85 s: entran las líneas del titular.
- 3,2 s: "*en un solo kit.*" y su subrayado.
- 4,0 s: 📈 Nivel 1 · Bolsa Local entra desde la izquierda; 4,25 s: 🌎 Nivel 2 · Bolsa Extranjera entra desde la derecha.
- 4,8 s: el marco lima se cierra sobre ambos y aparece la etiqueta "KIT INVERSOR".

**3 · Qué incluye**
- Las tarjetas caen a 7,25 · 8,0 · 9,6 s y cada ícono 3D hace pop.
- 8,45–9,2 s: los chips de "Guías y herramientas" entran uno por uno, con un tick cada uno.
- 9,4 s: "Guía de impuestos" hace un pop extra con destellos.

**4 · Exclusivo**
- 12,55 s: el micrófono 3D entra con rebote.
- 13,0 s: "Solo para los".
- 13,3 s: el "*10*" (lima, 270 px) entra con impacto.
- 13,9 s: se encienden los 10 cupos, uno a uno.
- 14,4 s: aparece la caja "● EN VIVO · Sesión de preguntas y respuestas (Q&A) con el equipo Freenanzas", con el punto rojo que late.

## Audio
Sintetizado en `audio/kit_audio.py` a 120 BPM. Incluye:
- Riser y whoosh cuando despega el cohete.
- Golpes en "*Inversor*", "*en un solo kit.*" y "*10*".
- Whooshes laterales cuando entran los niveles.
- Ticks en los chips y en los 10 cupos.
- Destellos en "Guía de impuestos".

## Imagen CTA (sin precio)
- Fondo morado con cuadrícula. Lleva "Llévate el" y "*Kit Inversor*" con subrayado; sin cohete ni etiqueta "Más popular".
- Dos tarjetas lima gruesas con íconos 3D: "DOS BOOTCAMPS COMPLETOS · Bolsa Local + Bolsa Extranjera" y "EXCLUSIVO · 10 PRIMEROS · Q&A en vivo con el equipo".
- El bloque está centrado y más arriba, para dejar libre una zona amplia (≈ 320 px) para el sticker de link entre las tarjetas y el logo.

## Copy sugerido
> 🚀 El **Kit Inversor**: los dos bootcamps completos en un solo kit.
> 📈 Nivel 1 · Bolsa Local + 🌎 Nivel 2 · Bolsa Extranjera
> 🧰 Guías y herramientas: guía de impuestos, plantillas, calculadoras y recursos
> 📅 Acompañamiento por 60 días
> 🎙️ Exclusivo para los 10 primeros: Q&A en vivo con el equipo Freenanzas
> 👉 Link en nuestra historia
