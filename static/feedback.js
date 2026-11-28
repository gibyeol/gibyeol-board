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
    s.onerror = function () { loading = false; queue = []; };
    document.head.appendChild(s);
  }
  document.querySelectorAll('details.fb').forEach(function (det) {
    var form = det.querySelector('form.fb-form'); if (!form) return;
    var box = form.querySelector('.fb-ts'), status = form.querySelector('.fb-status'), btn = form.querySelector('button[type=submit]');
    var key = form.dataset.key, widget = null;
    function say(t, cls) { status.textContent = t; status.className = 'fb-status' + (cls ? ' ' + cls : ''); }
    // on failure keep what the visitor wrote: offer the same text as an email
    function fail(t) {
      say(t, 'bad');
      var k = form.querySelector('input[name=kind]:checked');
      var a = document.createElement('a');
      a.href = form.dataset.mail + '&body=' + encodeURIComponent(form.dataset.url + '\n' + (k ? k.parentNode.textContent.trim() : '') + '\n\n' + form.elements.body.value);
      a.textContent = form.dataset.mailtext;
      status.appendChild(document.createTextNode(' ')); status.appendChild(a);
    }
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
      if (!window.turnstile || widget === false) { fail(form.dataset.fail); widget = null; return; }
      if (!token) { say(form.dataset.check, 'bad'); return; }
      var kind = form.querySelector('input[name=kind]:checked');
      btn.disabled = true; say(form.dataset.sending, '');
      fetch('/api/feedback', {
        method: 'POST', headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ kind: kind ? kind.value : '', body: form.elements.body.value, page: form.dataset.page, lang: form.dataset.lang, token: token })
      }).then(function (r) { return r.json().catch(function () { return {}; }); })
        .then(function (d) {
          if (d && d.ok) { form.reset(); say(form.dataset.ok, 'good'); }
          else fail(form.dataset.fail);
        })
        .catch(function () { fail(form.dataset.fail); })
        .then(function () { btn.disabled = false; if (window.turnstile && widget) window.turnstile.reset(widget); });
    });
  });
})();
