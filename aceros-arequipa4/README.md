# Segmento "Aceros Arequipa · puesto 4" · 00:01:08:12 → 00:01:15:19

Solo gráficos (sin subtítulos). Archivos de 7,5 s, 1080×1920, 30 fps. **Colócalos empezando en 00:01:08:12.**

> ⚠️ **Dato a confirmar:** la tabla oficial (`../TOP5-DIVIDENDOS.md`) dice **6,46 %** para Aceros Arequipa (CORAREI1); el guion dice **6,26 %**.
> Hay dos versiones de todo: `_6-46` (tabla) y `_6-26` (guion). Diferencia vs. BCP (5,96 %): +0,50 pp o +0,30 pp.

## Pauta de tiempos
| Timecode | Voz | Gráfico (detrás de la persona) | Cámara |
|---|---|---|---|
| 00:01:09:08 | "…**Aceros Arequipa**" | Tarjeta con el logo, pop + píldora "CORAREI1 · SIDERURGIA" (00:01:09:15) | — |
| 00:01:10:24 | corte · "quedó en el…" | El logo sube un poco (la cabeza queda más alta en esta toma) | — |
| 00:01:11:15 | "**4.º puesto**" | Badge lima "PUESTO #4" a la izquierda (tu mano marca el 4 a la derecha) | — |
| 00:01:12:12 | corte · "Con un…" | Tarjeta verde arriba: logo + "RETORNO POR DIVIDENDO" | Empuje lento 100 → 104 % hasta 00:01:14:24 |
| 00:01:13:06 → 00:01:14:08 | "seis punto…" | Contador 0,00 → 6,46 % (o 6,26 %) con golpe al llegar | — |
| **00:01:14:24** | "**le ganó al BCP**" | Dos barras a los lados de tu cabeza: Aceros (lima) más alta que BCP (blanca), línea punteada al nivel del BCP y chip "▲ +0,50 pp" | **PUNCH-IN 104 → 116 % en 4 frames** (corte seco, sin suavizado de entrada, *ease out*), ancla en la cara. Mantener hasta el final de la frase |
| 00:01:15:19 | fin de la frase | Todo sale hacia arriba/abajo (8 frames) | — |

**Ojo:** el clip que me pasaste termina en 00:01:14:26, antes de que termine "le ganó al BCP". El momento de "le ganó" (00:01:14:24) es estimado: ajusta el punch-in y el inicio de las barras a lo que escuches en tu línea de tiempo. En las vistas previas, el último frame del video se congela para mostrar las barras.

## Archivos (`output/`)
- `PREVIEW_aceros-arequipa_6-46.mp4` / `_6-26.mp4`: referencia con zoom y profundidad.
- `graficos-aceros_<versión>_relleno.mp4` + `_mate.mp4`: Track Matte Key (Luma) en Premiere.
- `graficos-aceros_<versión>_CROMA-MAGENTA.mp4`: Ultra Key sobre `#FF00FF`.
- `graficos-aceros_<versión>_alfa.mov`: ProRes 4444 con transparencia.
- `mate-persona-aceros.mp4`: silueta (blanco = persona). Pistas: V1 video · V2 gráficos · V3 copia del video con este mate · V4 subtítulos.

## Regenerar
```bash
python3 ../hook-dividendos/segment.py work 72,120     # cortes en los frames 72 y 120
node render.mjs work/g 6.46                            # o 6.26
python3 preview.py clip.mp4 work/src work/masks work/g output/PREVIEW.mp4
```
