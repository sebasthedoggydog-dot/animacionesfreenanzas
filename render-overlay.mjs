// Renderiza una capa de gráficos con fondo TRANSPARENTE y la combina con un video original.
// Uso:  node render-overlay.mjs graficos-impuestos.html assets/video/impuestos-original.mp4
//   → output/<nombre>-capa.mov   (QuickTime PNG con alfa, para el editor: Premiere, DaVinci, Final Cut, CapCut)
//   → output/<nombre>-final.mp4  (video original + gráficos, con su audio)
//   --stills → output/stills/<nombre>/*.png (fotogramas clave ya compuestos sobre el video)
import { chromium } from 'playwright';
import { execFileSync } from 'node:child_process';
import { mkdirSync, rmSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const stillsOnly = args.includes('--stills');
const input = args.find((a) => a.endsWith('.html'));
const video = resolve(here, args.find((a) => a.endsWith('.mp4') || a.endsWith('.mov')));
const name = input.replace(/\.html$/, '');
const outDir = resolve(here, 'output');
const framesDir = resolve(outDir, '.frames-' + name);
rmSync(framesDir, { recursive: true, force: true });
mkdirSync(framesDir, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(resolve(here, input)).href + '?render');
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(300);
const { duration, fps, stills } = await page.evaluate(() => ({ duration: window.__DURATION, fps: window.__FPS || 30, stills: window.__STILLS }));
const stage = page.locator('#stage');
const shot = async (t, path) => {
  await page.evaluate((t) => window.__render(t), t);
  await stage.screenshot({ path, omitBackground: true });
};

if (stillsOnly) {
  const dir = resolve(outDir, 'stills', name);
  rmSync(dir, { recursive: true, force: true }); mkdirSync(dir, { recursive: true });
  for (const [k, t] of Object.entries(stills)) {
    const tmp = `${framesDir}/${k}.png`;
    await shot(t, tmp);
    execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-ss', String(t), '-i', video, '-i', tmp,
      '-filter_complex', '[0:v][1:v]overlay=0:0', '-frames:v', '1', `${dir}/${k}.png`]);
  }
} else {
  const total = Math.round(duration * fps);
  for (let f = 0; f < total; f++) await shot(f / fps, `${framesDir}/f${String(f).padStart(4, '0')}.png`);
  const seq = ['-framerate', String(fps), '-i', `${framesDir}/f%04d.png`];
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', ...seq, '-c:v', 'png', '-pix_fmt', 'rgba',
    resolve(outDir, `${name}-capa.mov`)], { stdio: 'inherit' });
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', video, ...seq,
    '-filter_complex', '[0:v][1:v]overlay=0:0:shortest=1[v]', '-map', '[v]', '-map', '0:a?',
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'slow', '-c:a', 'copy', '-movflags', '+faststart',
    resolve(outDir, `${name}-final.mp4`)], { stdio: 'inherit' });
}
rmSync(framesDir, { recursive: true, force: true });
await browser.close();
console.log('Listo →', stillsOnly ? `output/stills/${name}` : `output/${name}-final.mp4 + output/${name}-capa.mov`);
