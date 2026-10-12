// Renderiza overlay.html como secuencia PNG transparente 1080x1920 @30fps.
// Uso: node render.mjs <carpeta_salida> [porcentaje, ej. 6.46]
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const out = resolve(process.argv[2] || resolve(here, 'output/.frames'));
mkdirSync(out, { recursive: true });
const FPS = 30;
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(here, 'overlay.html')).href + '?render' + (process.argv[3] ? '&pct=' + process.argv[3] : ''));
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const total = Math.round((await page.evaluate(() => window.__DURATION)) * FPS);
const stage = page.locator('#stage');
for (let f = 0; f < total; f++) {
  await page.evaluate((t) => window.__render(t), f / FPS);
  await stage.screenshot({ path: `${out}/f${String(f + 1).padStart(4, '0')}.png`, omitBackground: true });
}
await browser.close();
console.log('gráficos →', out, total, 'frames');
