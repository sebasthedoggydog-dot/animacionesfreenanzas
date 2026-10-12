// Renderiza overlay.html en dos secuencias PNG transparentes 1080x1920 @30fps:
//   <out>/back/fNNNN.png  (gráficos que van DETRÁS de la persona)
//   <out>/front/fNNNN.png (subtítulos y destellos que van DELANTE)
// Uso: node render-layers.mjs <carpeta_salida> [--stills t1,t2,...]
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const out = resolve(process.argv[2] || resolve(here, 'output/.layers'));
const FPS = 30;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(here, 'overlay.html')).href + '?render');
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const total = Math.round((await page.evaluate(() => window.__DURATION)) * FPS);
const stage = page.locator('#stage');
for (const layer of ['back', 'front']) {
  mkdirSync(`${out}/${layer}`, { recursive: true });
  for (let f = 0; f < total; f++) {
    await page.evaluate(([t, l]) => window.__render(t, l), [f / FPS, layer]);
    await stage.screenshot({ path: `${out}/${layer}/f${String(f + 1).padStart(4, '0')}.png`, omitBackground: true });
  }
}
await browser.close();
console.log('capas →', out, total, 'frames');
