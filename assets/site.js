/* Norvex Property: shared behaviour. Header state, menus, in-page anchors, forms. */
(function () {
  'use strict';
  var d = document, w = window;
  d.documentElement.classList.add('js');
  var reduce = w.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || d).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || d).querySelectorAll(s)); };

  /* header: solid once the page has scrolled */
  var hdr = $('.hdr');
  if (hdr && !hdr.classList.contains('hdr--solid')) {
    var ticking = false;
    var paint = function () { hdr.classList.toggle('is-scrolled', w.scrollY > 24); ticking = false; };
    w.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(paint); } }, { passive: true });
    paint();
  }

  /* services dropdown */
  $$('.nav > li[data-menu]').forEach(function (li) {
    var btn = $('.nav__btn', li);
    if (!btn) return;
    var set = function (open) { li.dataset.open = open ? 'true' : 'false'; btn.setAttribute('aria-expanded', open ? 'true' : 'false'); };
    btn.addEventListener('click', function () { var hover = w.matchMedia('(hover: hover)').matches && li.dataset.hovered === 'true'; set(hover ? true : li.dataset.open !== 'true'); });
    li.addEventListener('mouseenter', function () { li.dataset.hovered = 'true'; if (w.matchMedia('(hover: hover)').matches) set(true); });
    li.addEventListener('mouseleave', function () { li.dataset.hovered = 'false'; if (w.matchMedia('(hover: hover)').matches) set(false); });
    li.addEventListener('focusout', function (e) { if (!li.contains(e.relatedTarget)) set(false); });
    d.addEventListener('click', function (e) { if (!li.contains(e.target)) set(false); });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  });

  /* mobile menu */
  var menuBtn = $('#menu-btn'), menu = $('#menu'), menuClose = $('#menu-close');
  if (menuBtn && menu) {
    var lastFocus = null;
    var openMenu = function () { lastFocus = d.activeElement; menu.classList.add('is-open'); menu.removeAttribute('hidden'); d.body.classList.add('menu-open'); menuBtn.setAttribute('aria-expanded', 'true'); var f = $('a, button', menu); if (f) f.focus(); };
    var closeMenu = function () { menu.classList.remove('is-open'); menu.setAttribute('hidden', ''); d.body.classList.remove('menu-open'); menuBtn.setAttribute('aria-expanded', 'false'); if (lastFocus) lastFocus.focus(); };
    menuBtn.addEventListener('click', function () { menu.classList.contains('is-open') ? closeMenu() : openMenu(); });
    if (menuClose) menuClose.addEventListener('click', closeMenu);
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('is-open')) closeMenu(); });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', closeMenu); });
  }

  /* same-page anchors scroll themselves */
  d.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#"]');
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    var el = id ? d.getElementById(id) : null;
    if (!el) return;
    e.preventDefault();
    el.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    try { history.replaceState(null, '', '#' + id); } catch (err) {}
  });

  /* preselect a service from the address, e.g. /contact/?service=surveying */
  try {
    var svc = new URLSearchParams(w.location.search).get('service'), sel = $('#c-service');
    if (svc && sel && $$('option', sel).some(function (o) { return o.value === svc; })) sel.value = svc;
  } catch (err) {}

  /* footer year */
  $$('[data-year]').forEach(function (el) { el.textContent = String(new Date().getFullYear()); });

  /* forms: validate, send by email relay, fall back to the visitor's mail app */
  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/, PHONE_RE = /^[+\d][\d\s().-]{6,}$/;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function check(el) {
    var v = el.type === 'checkbox' ? el.checked : el.value.trim();
    var msg = el.dataset.msg || 'This field is required';
    if (el.type === 'checkbox') return v || msg;
    if (el.required && !v) return msg;
    if (v && el.type === 'email' && !EMAIL_RE.test(v)) return el.dataset.msg || 'Enter an email address we can reply to';
    if (v && el.type === 'tel' && !PHONE_RE.test(v)) return el.dataset.msg || 'Enter a phone number, or leave this blank';
    if (v && el.minLength > 0 && v.length < el.minLength) return el.dataset.msg || ('Please add a little more detail (at least ' + el.minLength + ' characters)');
    return true;
  }
  function paint(el, r) {
    var err = d.getElementById(el.id + '-error'), wrap = el.closest('.field, .check');
    if (r === true) { el.removeAttribute('aria-invalid'); el.removeAttribute('aria-describedby'); if (err) { err.textContent = ''; err.hidden = true; } if (wrap) wrap.classList.remove('is-invalid'); return true; }
    el.setAttribute('aria-invalid', 'true'); el.setAttribute('aria-describedby', el.id + '-error'); if (err) { err.textContent = r; err.hidden = false; } if (wrap) wrap.classList.add('is-invalid'); return false;
  }
  $$('form[data-form]').forEach(function (form) {
    var fields = $$('input, select, textarea', form).filter(function (el) { return el.name && el.type !== 'hidden' && !el.closest('.hp'); });
    fields.forEach(function (el) {
      el.addEventListener('blur', function () { if (el.value || el.type === 'checkbox') paint(el, check(el)); });
      el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') paint(el, check(el)); });
      el.addEventListener('change', function () { if (el.getAttribute('aria-invalid') === 'true') paint(el, check(el)); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var errors = [];
      fields.forEach(function (el) { var r = check(el); if (!paint(el, r)) errors.push([el.id, r]); });
      var box = $('.form__errors', form), list = box && $('ul', box);
      if (errors.length) {
        if (box && list) { list.innerHTML = errors.map(function (x) { return '<li><a href="#' + x[0] + '">' + esc(x[1]) + '</a></li>'; }).join(''); box.hidden = false; box.focus(); }
        return;
      }
      if (box) box.hidden = true;
      var honey = $('.hp input', form);
      if (honey && honey.value) return;
      var data = {}, lines = [];
      fields.forEach(function (el) {
        var label = form.querySelector('label[for="' + el.id + '"]');
        var name = el.dataset.label || (label ? label.textContent.trim() : el.name);
        var val = el.type === 'checkbox' ? (el.checked ? 'Yes' : 'No') : el.value.trim();
        data[name] = val; lines.push(name + ': ' + val);
      });
      var to = d.body.dataset.email || '';
      var subject = form.dataset.subject || 'Website enquiry';
      var submit = $('[type=submit]', form);
      if (submit) { submit.disabled = true; submit.dataset.label = submit.textContent; submit.textContent = 'Sending'; }
      var first = (data['Full name'] || data['Your name'] || '').split(' ')[0];
      var done = function (relayed) {
        var wrap = form.closest('[data-form-slot]') || form.parentNode;
        var html = '<div class="card success" role="status" tabindex="-1">' +
          '<h3 class="h3">Thank you' + (first ? ', ' + esc(first) : '') + '.</h3>' +
          (relayed
            ? '<p class="bodytext">Your message has reached us. Expect a reply within one working day.</p>'
            : '<p class="bodytext">Your email app should have opened with your message ready to send. If it did not, email us at <a href="mailto:' + esc(to) + '">' + esc(to) + '</a> and we will reply within one working day.</p>') +
          '</div>';
        wrap.innerHTML = html; var s = $('.success', wrap); if (s) s.focus();
      };
      var fallback = function () {
        if (to) { w.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n')); }
        done(false);
      };
      if (!to || !w.fetch) { fallback(); return; }
      var payload = Object.assign({}, data, { _subject: subject, _template: 'table', _captcha: 'false' });
      var timer = setTimeout(fallback, 9000);
      fetch('https://formsubmit.co/ajax/' + encodeURIComponent(to), { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); })
        .then(function (res) { clearTimeout(timer); if (res.ok && (res.j.success === true || res.j.success === 'true')) done(true); else fallback(); })
        .catch(function () { clearTimeout(timer); fallback(); });
    });
  });
})();
