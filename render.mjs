// Renderiza index.html a MP4 vertical 1080x1920 @30fps, fotograma a fotograma.
// Uso:  node render.mjs                 → output/sorteo-freenanzas.mp4
//       node render.mjs --stills        → output/stills/*.png (fotogramas clave)
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { mkdirSync, rmSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const FPS = 30;
const stillsOnly = process.argv.includes('--stills');
const outDir = resolve(here, 'output');
const framesDir = resolve(outDir, stillsOnly ? 'stills' : '.frames');
rmSync(framesDir, { recursive: true, force: true });
mkdirSync(framesDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(here, 'index.html')).href + '?render');
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const duration = await page.evaluate(() => window.__DURATION);
const stage = page.locator('#stage');

if (stillsOnly) {
  const keys = { '1-hook': 1.9, '2-dolor': 6.2, '3-sorpresa': 8.3, '4-premios': 12.5, '5-cta': 17.5 };
  for (const [name, t] of Object.entries(keys)) {
    await page.evaluate((t) => window.__render(t), t);
    await stage.screenshot({ path: `${framesDir}/${name}.png` });
  }
} else {
  const total = Math.round(duration * FPS);
  for (let f = 0; f < total; f++) {
    await page.evaluate((t) => window.__render(t), f / FPS);
    await stage.screenshot({ path: `${framesDir}/f${String(f).padStart(4, '0')}.png` });
  }
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-framerate', String(FPS), '-i', `${framesDir}/f%04d.png`,
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'slow', '-movflags', '+faststart',
    resolve(outDir, 'sorteo-freenanzas.mp4')], { stdio: 'inherit' });
  rmSync(framesDir, { recursive: true, force: true });
}
await browser.close();
console.log('Listo →', stillsOnly ? framesDir : resolve(outDir, 'sorteo-freenanzas.mp4'));
