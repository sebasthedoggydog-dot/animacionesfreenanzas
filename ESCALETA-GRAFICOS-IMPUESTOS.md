# Gráficos · "Impuestos al comprar acciones"

Gráficos animados sobre el video original (fondo verde con cuadrícula animada y voz en off, 12,36 s, 1080×1920, 25 fps), con el sistema visual del Kit Inversor v2:
- Tipografía: **Poppins** ExtraBold en los titulares, **Playfair Display** cursiva lima en la palabra clave y **Oswald** con punto lima en las etiquetas.
- Paleta oficial (#5723f4 · #1a6f66 · #c6fd34 · #fdfdfc), íconos 3D (Fluent Emoji, MIT), estrellas y puntos, y logo oficial SVG abajo.

**Archivos**
- `output/graficos-impuestos-final.mp4`: video final (original + gráficos, con el audio original)
- `output/graficos-impuestos-capa.mov`: **solo los gráficos con fondo transparente** (QuickTime PNG con alfa), para montarlos en el editor encima del video
- `graficos-impuestos.html`: animación (al abrirla en el navegador se previsualiza sobre el video)
- `render-overlay.mjs`: `node render-overlay.mjs graficos-impuestos.html assets/video/impuestos-original.mp4` (con `--stills` exporta los fotogramas clave)

## Sincronización con la voz
Las pausas de la locución se detectaron en 1,52 · 4,64 · 7,72 y 8,5 s. Cada bloque entra con su frase:

| Tiempo | Locución | Gráfico |
|---|---|---|
| 0,0–1,5 s | "Cuando compras una acción" | 🛒 carrito 3D, "Cuando compras" y "*una acción*" |
| 1,6–4,7 s | "no pagas impuesto a la renta simplemente por comprarla" | "No pagas *impuesto a la renta*". Debajo, una tarjeta tipo recibo: "Compra de acciones ✓" e "Impuesto a la renta **S/ 0**" (pop lima), más el chip "…solo por comprarla" |
| 4,9–7,8 s | "El impuesto entra en juego cuando generas ganancias" | Etiqueta "◉ EL IMPUESTO ENTRA EN JUEGO". Una tarjeta "Tu inversión" con un gráfico que sube y se dibuja (5,6–6,9 s). Luego "cuando generas *ganancias*", la etiqueta "+ GANANCIA" y el billete con alas 💸 |
| 7,9–8,8 s | "Por ejemplo" | "◉ EJEMPLOS · *Por ejemplo*" a pantalla completa; luego sube y queda como encabezado |
| 8,9–12,36 s | "cuando vendes una acción con ganancia o recibes dividendos" | 📈 "Vendes una acción *con ganancia*" entra por la izquierda (9,0 s) · "*o*" · 💰 "Recibes *dividendos*" entra por la derecha (10,85 s). Cada tarjeta lleva la etiqueta "→ IMPUESTO A LA RENTA" |

Si en la locución final cambia el ritmo, se ajustan los tiempos de cada bloque en `graficos-impuestos.html` (llamadas `block()`, `wordIn()` y `track()`).
