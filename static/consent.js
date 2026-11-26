/* Nadri cookie consent (2026-11-26). Affiliate scripts listed in window.NADRI_DEFER load only after "Accept".
   "Reject", or a Global Privacy Control signal, keeps them off. Choice is stored in localStorage only. */
(function () {
  var KEY = 'nadri-consent', box = null;
  var cfg = document.getElementById('nadri-consent-cfg');
  function load() {
    (window.NADRI_DEFER || []).forEach(function (src) {
      if (document.querySelector('script[src="' + src + '"]')) return;
      var s = document.createElement('script'); s.async = true; s.src = src; document.body.appendChild(s);
    });
  }
  function hide() { if (box) { box.remove(); box = null; } }
  function choose(v) { try { localStorage.setItem(KEY, v); } catch (e) {} hide(); if (v === 'yes') load(); }
  function show() {
    if (box || !cfg) return;
    box = document.createElement('div');
    box.setAttribute('role', 'dialog'); box.setAttribute('aria-live', 'polite');
    box.style.cssText = 'position:fixed;left:12px;right:12px;bottom:12px;z-index:9999;max-width:720px;margin:0 auto;background:#fff;color:#1f2328;border:1px solid #c9ccd1;border-radius:12px;box-shadow:0 6px 24px rgba(0,0,0,.15);padding:14px 16px;font-size:14px;line-height:1.5;display:flex;flex-wrap:wrap;gap:10px;align-items:center';
    var p = document.createElement('p'); p.style.cssText = 'margin:0;flex:1 1 280px';
    p.textContent = cfg.dataset.text + ' ';
    var a = document.createElement('a'); a.href = cfg.dataset.privacy; a.textContent = cfg.dataset.more; p.appendChild(a);
    function btn(label, v, primary) {
      var b = document.createElement('button'); b.type = 'button'; b.textContent = label;
      // Same look for both choices: no "false hierarchy" dark pattern (strategy doc; e-commerce law).
      b.style.cssText = 'font:inherit;padding:8px 14px;border-radius:8px;cursor:pointer;border:1px solid #1f2328;background:#fff;color:#1f2328;min-width:84px';
      b.addEventListener('click', function () { choose(v); }); return b;
    }
    box.appendChild(p); box.appendChild(btn(cfg.dataset.reject, 'no', false)); box.appendChild(btn(cfg.dataset.accept, 'yes', true));
    document.body.appendChild(box);
  }
  var v = null; try { v = localStorage.getItem(KEY); } catch (e) {}
  if (v === 'yes') load();
  else if (v !== 'no') { if (navigator.globalPrivacyControl) { try { localStorage.setItem(KEY, 'no'); } catch (e) {} } else show(); }
  document.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('a[href="#consent-reset"]');
    if (!t) return; e.preventDefault(); try { localStorage.removeItem(KEY); } catch (e2) {} show();
  });
})();
