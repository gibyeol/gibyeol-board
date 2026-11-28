/* Page feedback form (owner 2026-11-28 [7eb4ec94#4885] [7eb4ec94#4932]).
   Turnstile (Cloudflare spam check) loads only when the visitor opens the form; sends to /api/feedback. */
(function () {
  var TS = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit&onload=nadriTsReady';
  var queue = [], loading = false;
  window.nadriTsReady = function () { var q = queue; queue = []; q.forEach(function (f) { f(); }); };
  function withTurnstile(f) {
    if (window.turnstile) return f();
    queue.push(f);
    if (loading) return;
    loading = true;
    var s = document.createElement('script'); s.src = TS; s.async = true; s.defer = true;
    s.onerror = function () { loading = false; };
    document.head.appendChild(s);
  }
  document.querySelectorAll('details.fb').forEach(function (det) {
    var form = det.querySelector('form.fb-form'); if (!form) return;
    var box = form.querySelector('.fb-ts'), status = form.querySelector('.fb-status'), btn = form.querySelector('button[type=submit]');
    var key = form.dataset.key, widget = null;
    function say(t, cls) { status.textContent = t; status.className = 'fb-status' + (cls ? ' ' + cls : ''); }
    det.addEventListener('toggle', function () {
      if (!det.open || widget !== null || !key) return;
      widget = false;
      withTurnstile(function () {
        widget = window.turnstile.render(box, { sitekey: key, language: form.dataset.tslang || 'auto' });
      });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var token = widget && window.turnstile ? window.turnstile.getResponse(widget) : '';
      if (!key || !token) { say(key ? form.dataset.check : form.dataset.fail, 'bad'); return; }
      var kind = form.querySelector('input[name=kind]:checked');
      btn.disabled = true; say(form.dataset.sending, '');
      fetch('/api/feedback', {
        method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ kind: kind ? kind.value : '', body: form.elements.body.value, page: form.dataset.page, lang: form.dataset.lang, token: token })
      }).then(function (r) { return r.json().catch(function () { return {}; }); })
        .then(function (d) {
          if (d && d.ok) { form.reset(); say(form.dataset.ok, 'good'); }
          else say(form.dataset.fail, 'bad');
        })
        .catch(function () { say(form.dataset.fail, 'bad'); })
        .then(function () { btn.disabled = false; if (window.turnstile && widget) window.turnstile.reset(widget); });
    });
  });
})();
