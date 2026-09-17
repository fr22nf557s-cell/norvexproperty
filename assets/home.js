/* Norvex Property home: the manor film scrubbed by scroll, plus the working tools. */
(function () {
  'use strict';
  var MEDIA = { desktop: '/assets/manor.mp4', mobile: '/assets/manor-mobile.mp4', poster: '/assets/manor-poster.jpg', mobilePoster: '/assets/manor-mobile-poster.jpg' };
  var CUTS = [0, 4, 10, 15, 20, 22.5, 24.042];
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var clamp = function (v, a, b) { return Math.min(b, Math.max(a, v)); };
  var gbp = new Intl.NumberFormat('en-GB', { style: 'currency', currency: 'GBP', maximumFractionDigits: 0 });
  var fmtGBP = function (v) { return gbp.format(Math.round(v)); };
  var fmtPct = function (v) { return Number(v).toFixed(2) + '%'; };
  function setText(id, v) { var el = document.getElementById(id); if (el) el.textContent = v; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

  /* ---------- the film ---------- */
  var film = $('#film');
  if (film) {
    var video = $('#video'), poster = $('#poster'), bar = $('#progress');
    var chapters = $$('.chapter', film), rail = $$('.rail button', film);
    var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    var mobile = matchMedia('(max-width: 860px), (hover: none) and (pointer: coarse)').matches;
    poster.src = mobile ? MEDIA.mobilePoster : MEDIA.poster;
    var duration = CUTS[CUTS.length - 1], active = -1, target = 0, current = 0, dirty = true, painted = false;
    var setActive = function (p) {
      var t = p * duration, i = 0;
      for (var k = 0; k < CUTS.length - 1; k++) { if (t >= CUTS[k]) i = k; }
      if (i === active) return;
      active = i;
      chapters.forEach(function (c, k) { c.classList.toggle('is-active', k === i); });
      rail.forEach(function (b, k) { if (k === i) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); });
    };
    var progress = function () { var total = film.offsetHeight - innerHeight; if (total <= 0) return 0; return clamp(-film.getBoundingClientRect().top / total, 0, 1); };
    var goTo = function (i) { var total = film.offsetHeight - innerHeight; var p = (CUTS[i] + 0.35) / duration; window.scrollTo({ top: film.offsetTop + p * total, behavior: reduce ? 'auto' : 'smooth' }); };
    rail.forEach(function (b) { b.addEventListener('click', function () { goTo(Number(b.dataset.go)); }); });
    $$('[data-go].cta-tour').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); goTo(Number(a.dataset.go)); }); });
    if (!reduce) {
      video.src = mobile ? MEDIA.mobile : MEDIA.desktop;
      video.addEventListener('loadedmetadata', function () { if (video.duration) duration = video.duration; dirty = true; });
      video.addEventListener('seeked', function () { if (!painted) { painted = true; film.classList.add('is-painted'); } });
      var prime = function () { video.play().then(function () { video.pause(); }).catch(function () {}); };
      window.addEventListener('touchstart', prime, { once: true, passive: true });
      window.addEventListener('pointerdown', prime, { once: true, passive: true });
      window.addEventListener('scroll', function () { dirty = true; if (scrollY > 40) film.classList.add('is-scrolled'); }, { passive: true });
      window.addEventListener('resize', function () { dirty = true; });
      (function tick() {
        if (dirty) { dirty = false; var p = progress(); target = p; setActive(p); bar.style.transform = 'scaleX(' + p + ')'; }
        current += (target - current) * 0.2;
        if (video.readyState >= 1 && !video.seeking) {
          var t = clamp(current, 0, 0.999) * duration;
          if (Math.abs(video.currentTime - t) > (mobile ? 0.02 : 0.008)) { try { video.currentTime = t; } catch (e) {} }
        }
        requestAnimationFrame(tick);
      })();
    } else {
      chapters.forEach(function (c) { c.classList.add('is-active'); });
    }
  }

  /* ---------- listings ---------- */
  var LISTINGS = [
    { id: 1, name: 'Hawthorne House', area: 'Hampstead', region: 'London', intent: 'buy', price: 4250000, beds: 5, baths: 4, sqft: 4820, tone: 'a' },
    { id: 2, name: 'The Penthouse, Albion Wharf', area: 'Richmond', region: 'London', intent: 'buy', price: 2750000, beds: 3, baths: 3, sqft: 2150, tone: 'b' },
    { id: 3, name: 'Orchard Lodge', area: 'Chipping Campden', region: 'Cotswolds', intent: 'buy', price: 1650000, beds: 4, baths: 3, sqft: 2900, tone: 'c' },
    { id: 4, name: 'Wexcombe Park', area: 'Surrey Hills', region: 'Surrey', intent: 'buy', price: 7900000, beds: 8, baths: 7, sqft: 11200, tone: 'd' },
    { id: 5, name: 'Marlow riverside apartment', area: 'Marlow', region: 'Buckinghamshire', intent: 'buy', price: 985000, beds: 2, baths: 2, sqft: 1180, tone: 'b' },
    { id: 6, name: 'Eaton Terrace apartment', area: 'Belgravia', region: 'London', intent: 'let', price: 5200, beds: 2, baths: 2, sqft: 1240, tone: 'c' },
    { id: 7, name: 'Mill House', area: 'Bath', region: 'Somerset', intent: 'let', price: 6900, beds: 4, baths: 3, sqft: 3100, tone: 'a' },
    { id: 8, name: 'Kensington Gate townhouse', area: 'Kensington', region: 'London', intent: 'let', price: 14500, beds: 5, baths: 4, sqft: 3800, tone: 'd' }
  ];
  var BANDS = {
    buy: [['any', 'Any price'], ['0-1000000', 'Up to £1m'], ['1000000-2500000', '£1m to £2.5m'], ['2500000-5000000', '£2.5m to £5m'], ['5000000-', '£5m and above']],
    let: [['any', 'Any rent'], ['0-5000', 'Up to £5,000 pcm'], ['5000-10000', '£5,000 to £10,000 pcm'], ['10000-', '£10,000 pcm and above']]
  };
  var search = $('#search');
  if (search) {
    var intent = 'buy', bandSel = $('#band'), bedsSel = $('#beds'), grid = $('#listing-grid'), status = $('#search-status');
    var fillBands = function () { bandSel.innerHTML = BANDS[intent].map(function (b) { return '<option value="' + b[0] + '">' + b[1] + '</option>'; }).join(''); $('#band-label').textContent = intent === 'buy' ? 'Price' : 'Rent'; };
    var renderListings = function () {
      var band = bandSel.value, lo = 0, hi = Infinity;
      if (band !== 'any') { var parts = band.split('-'); lo = Number(parts[0]); hi = parts[1] === '' ? Infinity : Number(parts[1]); }
      var beds = Number(bedsSel.value);
      var rows = LISTINGS.filter(function (l) { return l.intent === intent && l.price >= lo && l.price <= hi && l.beds >= beds; });
      status.textContent = rows.length === 1 ? '1 home matches' : rows.length + ' homes match';
      grid.innerHTML = rows.map(function (l) {
        return '<li class="listing"><div class="listing__media tone-' + l.tone + '"><span class="badge">' + (l.intent === 'let' ? 'To let' : 'For sale') + '</span></div>' +
          '<div class="listing__body"><p class="listing__price">' + fmtGBP(l.price) + (l.intent === 'let' ? ' <small>pcm</small>' : '') + '</p>' +
          '<h3 class="listing__name">' + esc(l.name) + '</h3><p class="listing__where">' + esc(l.area) + ', ' + esc(l.region) + '</p>' +
          '<p class="listing__meta">' + l.beds + ' bed · ' + l.baths + ' bath · ' + l.sqft.toLocaleString('en-GB') + ' sq ft</p>' +
          '<a class="cta-viewing" href="/contact/?service=' + (l.intent === 'let' ? 'letting' : 'buying') + '">Arrange a viewing</a></div></li>';
      }).join('') || '<li class="empty">Nothing in that band today. Widen the search or ask us to look off-market.</li>';
    };
    $$('#search [data-intent]').forEach(function (b) { b.addEventListener('click', function () { intent = b.dataset.intent; $$('#search [data-intent]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); fillBands(); renderListings(); }); });
    bandSel.addEventListener('change', renderListings); bedsSel.addEventListener('change', renderListings);
    search.addEventListener('submit', function (e) { e.preventDefault(); });
    fillBands(); renderListings();
  }

  /* ---------- mortgage ---------- */
  function monthly(P, annual, years, type) { var r = annual / 100 / 12, n = years * 12; if (type === 'interest') return P * r; if (r === 0) return P / n; return (P * r) / (1 - Math.pow(1 + r, -n)); }
  var PRODUCTS = [['2-year fixed', 4.19], ['5-year fixed', 4.02], ['Lifetime tracker', 4.70]];
  var mcalc = $('#mortgage-calc');
  if (mcalc) {
    var mtype = 'repayment', mp = $('#m-price'), md = $('#m-deposit'), mr = $('#m-rate'), mt = $('#m-term');
    var mortgage = function () {
      var P = Number(mp.value), dep = Number(md.value), R = Number(mr.value), Y = Number(mt.value), loan = P * (1 - dep / 100), m = monthly(loan, R, Y, mtype);
      setText('m-price-out', fmtGBP(P)); setText('m-deposit-out', dep + '% · ' + fmtGBP(P * dep / 100)); setText('m-rate-out', fmtPct(R)); setText('m-term-out', Y + ' years');
      setText('m-monthly', fmtGBP(m)); setText('m-loan', fmtGBP(loan)); setText('m-ltv', Math.round(100 - dep) + '%');
      setText('m-total', fmtGBP(mtype === 'interest' ? m * Y * 12 + loan : m * Y * 12)); setText('m-stress', fmtGBP(monthly(loan, R + 3, Y, mtype)));
      $('#products').innerHTML = PRODUCTS.map(function (p) { return '<li class="product"><span>' + p[0] + '</span><span class="product__rate">' + fmtPct(p[1]) + '</span><span class="product__monthly">' + fmtGBP(monthly(loan, p[1], Y, mtype)) + '</span><button type="button" class="rate-use" data-rate="' + p[1] + '">Use rate</button></li>'; }).join('');
    };
    [mp, md, mr, mt].forEach(function (el) { el.addEventListener('input', mortgage); });
    $$('#mortgage-calc [data-mtype]').forEach(function (b) { b.addEventListener('click', function () { mtype = b.dataset.mtype; $$('#mortgage-calc [data-mtype]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); mortgage(); }); });
    $('#products').addEventListener('click', function (e) { var b = e.target.closest('[data-rate]'); if (b) { mr.value = b.dataset.rate; mortgage(); } });
    mcalc.addEventListener('submit', function (e) { e.preventDefault(); });
    mortgage();
  }

  /* ---------- bridging ---------- */
  var bcalc = $('#bridging-calc');
  if (bcalc) {
    var method = 'retained', bg = $('#b-gross'), bt = $('#b-term'), br = $('#b-rate');
    var bridging = function () {
      var G = Number(bg.value), n = Number(bt.value), r = Number(br.value) / 100, mo = G * r, interest = mo * n, fee = G * 0.02, net = method === 'retained' ? G - fee - interest : G - fee;
      setText('b-gross-out', fmtGBP(G)); setText('b-term-out', n + (n === 1 ? ' month' : ' months')); setText('b-rate-out', fmtPct(br.value));
      setText('b-net', fmtGBP(net)); setText('b-monthly', fmtGBP(mo) + (method === 'retained' ? ' (retained)' : '')); setText('b-interest', fmtGBP(interest)); setText('b-fee', fmtGBP(fee)); setText('b-repay', fmtGBP(G));
      setText('b-note', method === 'retained' ? 'Retained interest is deducted from the advance, so there are no monthly payments during the term.' : 'Serviced interest is paid monthly, so more of the gross loan reaches you on day one.');
    };
    [bg, bt, br].forEach(function (el) { el.addEventListener('input', bridging); });
    $$('#bridging-calc [data-method]').forEach(function (b) { b.addEventListener('click', function () { method = b.dataset.method; $$('#bridging-calc [data-method]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); bridging(); }); });
    bcalc.addEventListener('submit', function (e) { e.preventDefault(); });
    bridging();
  }

  /* ---------- surveys ---------- */
  var SURVEYS = [
    { id: 'l1', name: 'Level 1', sub: 'Condition Report', fee: 450, depth: 35, days: 3, blurb: 'A traffic-light snapshot for a conventional, newer home in good order. No advice on repairs and no valuation.', inspects: { roof: 'visual', walls: 'visual', floors: 'none', services: 'visual', drainage: 'none', loft: 'none', outbuildings: 'none', costs: 'none' } },
    { id: 'l2', name: 'Level 2', sub: 'HomeBuyer Survey', fee: 700, depth: 65, days: 5, blurb: 'The most-chosen survey for conventional properties under about 100 years old. Flags the defects that affect value and tells you what to do next.', inspects: { roof: 'visual', walls: 'full', floors: 'visual', services: 'visual', drainage: 'visual', loft: 'visual', outbuildings: 'visual', costs: 'none' } },
    { id: 'l3', name: 'Level 3', sub: 'Building Survey', fee: 1250, depth: 95, days: 7, blurb: 'A full structural inspection for older, listed, unusual or heavily altered homes, and anything you plan to renovate. Includes repair options and indicative costs.', inspects: { roof: 'full', walls: 'full', floors: 'full', services: 'full', drainage: 'full', loft: 'full', outbuildings: 'full', costs: 'full' } },
    { id: 'defect', name: 'Defect report', sub: 'Single issue', fee: 400, depth: 25, days: 4, blurb: 'One issue investigated properly: damp, cracking, roof movement or timber decay, with a clear remedial plan and cost band.', inspects: { roof: 'visual', walls: 'full', floors: 'visual', services: 'none', drainage: 'none', loft: 'none', outbuildings: 'none', costs: 'full' } }
  ];
  var ITEMS = [['roof', 'Roof structure & coverings'], ['walls', 'Walls, damp & movement'], ['floors', 'Floors & timbers'], ['services', 'Electrics, gas & plumbing'], ['drainage', 'Drainage'], ['loft', 'Loft & roof void'], ['outbuildings', 'Outbuildings & grounds'], ['costs', 'Repair cost estimates']];
  var LEVEL = { full: 'Full', visual: 'Visual', none: 'Not included' };
  var METRICS = { fee: { max: 1400, fmt: fmtGBP }, depth: { max: 100, fmt: function (v) { return v + ' / 100'; } }, days: { max: 8, fmt: function (v) { return v + ' working days'; } } };
  var bars = $('#bars');
  if (bars) {
    var metric = 'fee', selected = 'l2';
    var rowsEl = $('#survey-rows');
    if (rowsEl) rowsEl.innerHTML = SURVEYS.map(function (s) { return '<tr><th scope="row">' + s.name + ' · ' + s.sub + '</th><td>' + METRICS.fee.fmt(s.fee) + '</td><td>' + METRICS.depth.fmt(s.depth) + '</td><td>' + METRICS.days.fmt(s.days) + '</td></tr>'; }).join('');
    var surveys = function () {
      bars.innerHTML = SURVEYS.map(function (s) { var v = s[metric], pct = Math.round(v / METRICS[metric].max * 100); return '<button type="button" role="listitem" class="bar" data-survey="' + s.id + '" aria-pressed="' + (s.id === selected) + '"><span class="bar__label">' + s.name + '<small>' + s.sub + '</small></span><span class="bar__track" aria-hidden="true"><span style="width:' + pct + '%"></span></span><span class="bar__value">' + METRICS[metric].fmt(v) + '</span></button>'; }).join('');
      var s = SURVEYS.filter(function (x) { return x.id === selected; })[0];
      setText('survey-name', s.name + ' · ' + s.sub); setText('survey-blurb', s.blurb);
      $('#inspect').innerHTML = ITEMS.map(function (it) { var lv = s.inspects[it[0]]; return '<li data-level="' + lv + '"><span>' + it[1] + '</span><b>' + LEVEL[lv] + '</b></li>'; }).join('');
    };
    $$('#metrics [data-metric]').forEach(function (b) { b.addEventListener('click', function () { metric = b.dataset.metric; $$('#metrics [data-metric]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); surveys(); }); });
    bars.addEventListener('click', function (e) { var b = e.target.closest('[data-survey]'); if (b) { selected = b.dataset.survey; surveys(); } });
    surveys();
  }
})();
