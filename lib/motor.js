/* Motor de keyframes compartido de los Reels/Historias Freenanzas.
   render(t) es determinista: render.mjs captura cada fotograma llamando a window.__render(t).
   Uso en cada pieza:
     Motor.config({ duration, scenes, stills, custom })
     Motor.track(id, [[t, {props}, easing], ...])   props: x y s sx sy r o blur
     Motor.wordIn / accIn / makeFx / floatAfter
     Motor.shift(s): suma s segundos a todos los keyframes que se declaren después
     Motor.start() */
(function () {
  const $ = (id) => (typeof id === 'string' ? document.getElementById(id) : id);
  const E = {
    lin: (p) => p,
    outCubic: (p) => 1 - Math.pow(1 - p, 3),
    inCubic: (p) => p * p * p,
    inOutCubic: (p) => (p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2),
    outExpo: (p) => (p === 1 ? 1 : 1 - Math.pow(2, -10 * p)),
    inExpo: (p) => (p === 0 ? 0 : Math.pow(2, 10 * p - 10)),
    inOutExpo: (p) => p === 0 ? 0 : p === 1 ? 1 : p < .5 ? Math.pow(2, 20 * p - 10) / 2 : (2 - Math.pow(2, -20 * p + 10)) / 2,
    outBack: (p) => { const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(p - 1, 3) + c1 * Math.pow(p - 1, 2); },
    outBackBig: (p) => { const c1 = 2.6, c3 = c1 + 1; return 1 + c3 * Math.pow(p - 1, 3) + c1 * Math.pow(p - 1, 2); },
  };
  const clamp01 = (x) => Math.max(0, Math.min(1, x));
  const DEF = { x: 0, y: 0, s: 1, sx: 1, sy: 1, r: 0, o: 1, blur: 0 };
  const tracks = [], floaters = [];
  let cfg = { duration: 10, scenes: [], stills: {}, custom: null };
  let OFF = 0;   // desplazamiento de tiempo para insertar escenas sin reescribir los keyframes siguientes

  function track(id, keys) { tracks.push({ el: $(id), keys: keys.map(([t, p, e]) => [t + OFF, p, e]) }); }
  function sample(keys, t) {
    const out = { ...DEF }; const full = []; let acc = { ...DEF };
    for (const [kt, props, ease] of keys) { acc = { ...acc, ...props }; full.push([kt, acc, ease || 'outCubic']); }
    if (t <= full[0][0]) return { ...full[0][1] };
    for (let i = 1; i < full.length; i++) {
      const [t0, a] = full[i - 1], [t1, b, ease] = full[i];
      if (t <= t1) { const p = E[ease]((t - t0) / (t1 - t0)); for (const k in b) out[k] = a[k] + (b[k] - a[k]) * p; return out; }
    }
    return { ...full[full.length - 1][1] };
  }
  function apply(el, v) {
    el.style.transform = `translate(${v.x}px, ${v.y}px) rotate(${v.r}deg) scale(${v.s * v.sx}, ${v.s * v.sy})`;
    el.style.opacity = clamp01(v.o);
    el.style.filter = v.blur > 0.05 ? `blur(${v.blur}px)` : 'none';
  }
  // Texto que sube desde su máscara
  function wordIn(id, t, from = 150) { track(id, [[t, { y: from, o: 0 }], [t + .42, { y: 0, o: 1 }, 'outBack']]); }
  // Palabra clave en cursiva lima: entra con escala y desenfoque
  function accIn(id, t) { track(id, [[t, { s: 1.7, o: 0, blur: 14 }], [t + .38, { s: 1, o: 1, blur: 0 }, 'outExpo']]); }
  function popIn(id, t, r = -20) { track(id, [[t, { s: 0, r }], [t + .38, { s: 1, r: 0 }, 'outBackBig']]); }
  function floatAfter(id, t0, amp = 8, period = 1.8, rot = 3) { floaters.push({ el: $(id), t0: t0 + OFF, amp, period, rot }); }
  // Estrellas y puntos de decoración dentro de una escena
  function makeFx(hostId, t0, tEnd, sparks, dots = []) {
    const host = $(hostId);
    sparks.forEach(([x, y, size, white], i) => {
      const s = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      s.setAttribute('width', size); s.setAttribute('height', size); s.setAttribute('viewBox', '0 0 40 40');
      s.setAttribute('class', 'spark el'); s.style.left = x + 'px'; s.style.top = y + 'px';
      s.innerHTML = `<path d="M20 0 C22 14 26 18 40 20 C26 22 22 26 20 40 C18 26 14 22 0 20 C14 18 18 14 20 0Z" fill="${white ? '#fdfdfc' : '#c6fd34'}"/>`;
      host.appendChild(s);
      const ts = t0 + i * 0.1;
      track(s, [[ts, { s: 0, r: -90 }], [ts + .4, { s: 1, r: 0 }, 'outBackBig'], [ts + .9, { s: .8, r: 30 }, 'inOutCubic'], [tEnd, { s: 1, r: 70 }, 'lin']]);
    });
    dots.forEach(([x, y, size, white], i) => {
      const d = document.createElement('i'); d.className = 'dot el';
      Object.assign(d.style, { left: x + 'px', top: y + 'px', width: size + 'px', height: size + 'px', background: white ? '#fdfdfc' : '#c6fd34' });
      host.appendChild(d);
      const ts = t0 + 0.15 + i * 0.07;
      track(d, [[ts, { s: 0, y: 0 }], [ts + .35, { s: 1 }, 'outBackBig'], [tEnd, { y: -40 - (i % 3) * 20 }, 'lin']]);
    });
  }

  function renderScenes(t) {
    cfg.scenes.forEach((sc, i) => {
      const el = $(sc.id);
      const last = i === cfg.scenes.length - 1;
      const visible = t >= sc.in && t < sc.out + (last ? 1 : 0.0001);
      el.style.display = visible ? 'block' : 'none';
      el.style.zIndex = i + 1;
      if (!visible || !sc.wipe) { el.style.clipPath = 'none'; return; }
      const w = sc.wipe;
      const p = E.inOutExpo(clamp01((t - w.t0) / (w.t1 - w.t0)));
      if (p >= 1) { el.style.clipPath = 'none'; return; }
      if (w.type === 'circle') el.style.clipPath = `circle(${p * 1250}px at ${w.cx ?? 540}px ${w.cy ?? 900}px)`;
      if (w.type === 'up') el.style.clipPath = `inset(${(1 - p) * 100}% 0 0 0 round ${80 * (1 - p)}px)`;
      if (w.type === 'left') el.style.clipPath = `inset(0 0 0 ${(1 - p) * 100}% round ${80 * (1 - p)}px)`;
    });
  }
  function render(t) {
    renderScenes(t);
    for (const tr of tracks) apply(tr.el, sample(tr.keys, t));
    for (const f of floaters) {
      if (t < f.t0) continue;
      const k = t - f.t0, ph = (2 * Math.PI * k) / f.period, ramp = clamp01(k / 0.4);
      f.el.style.transform += ` translateY(${Math.sin(ph) * f.amp * ramp}px) rotate(${Math.sin(ph * 0.7) * f.rot * ramp}deg)`;
    }
    if (cfg.custom) cfg.custom(t);
  }
  function start() {
    window.__render = render; window.__DURATION = cfg.duration; window.__STILLS = cfg.stills;
    if (new URLSearchParams(location.search).has('render')) { document.body.classList.add('render'); render(0); return; }
    const stage = $('stage');
    const fit = () => { const s = Math.min(innerWidth / 1080, (innerHeight - 52) / 1920); stage.style.transform = `scale(${s}) translateY(-26px)`; };
    addEventListener('resize', fit); fit();
    let playing = true, t = 0, last = null;
    const scrub = $('scrub'), time = $('time'), btn = $('play');
    scrub.max = cfg.duration;
    btn.onclick = () => { playing = !playing; btn.textContent = playing ? 'Pausa' : 'Play'; last = null; };
    scrub.oninput = () => { t = +scrub.value; render(t); time.textContent = t.toFixed(2) + 's'; };
    const loop = (now) => {
      if (playing) { if (last !== null) t = (t + (now - last) / 1000) % cfg.duration; last = now; render(t); scrub.value = t; time.textContent = t.toFixed(2) + 's'; }
      requestAnimationFrame(loop);
    };
    document.fonts.ready.then(() => requestAnimationFrame(loop));
  }
  window.Motor = { E, clamp01, $, track, shift: (s) => { OFF = s; }, wordIn, accIn, popIn, floatAfter, makeFx, start, config: (c) => { cfg = { ...cfg, ...c }; } };
})();
