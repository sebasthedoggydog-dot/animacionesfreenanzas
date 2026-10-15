// Renderiza una animación HTML a MP4 vertical 1080x1920 @30fps, fotograma a fotograma.
// Uso:  node render.mjs [archivo.html]            → output/<nombre>.mp4
//       node render.mjs [archivo.html] --stills   → output/stills/<nombre>/*.png
// Sin archivo usa index.html (Reel del sorteo → output/sorteo-freenanzas.mp4).
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { mkdirSync, rmSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const FPS = 30;
const stillsOnly = process.argv.includes('--stills');
const input = process.argv.slice(2).find((a) => a.endsWith('.html')) || 'index.html';
const name = input === 'index.html' ? 'sorteo-freenanzas' : input.replace(/\.html$/, '');
const outDir = resolve(here, 'output');
const framesDir = resolve(outDir, stillsOnly ? (name === 'sorteo-freenanzas' ? 'stills' : `stills/${name}`) : '.frames');
rmSync(framesDir, { recursive: true, force: true });
mkdirSync(framesDir, { recursive: true });

const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(here, input)).href + '?render');
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const duration = await page.evaluate(() => window.__DURATION);
const stage = page.locator('#stage');

if (stillsOnly) {
  const keys = (await page.evaluate(() => window.__STILLS)) ||
    { '1-hook': 1.9, '2-dolor': 6.2, '3-sorpresa': 8.3, '4-premios': 12.5, '5-cta': 17.5 };
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
    resolve(outDir, `${name}.mp4`)], { stdio: 'inherit' });
  rmSync(framesDir, { recursive: true, force: true });
}
await browser.close();
console.log('Listo →', stillsOnly ? framesDir : resolve(outDir, `${name}.mp4`));
