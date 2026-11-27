// Nadri site frame: Seoul-time sky, live D-day, copy buttons. The page works without it.
(function () {
  var r = (function (seed) { return function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }; })(7);
  var stars = document.getElementById('stars');
  if (stars) {
    var s = '';
    for (var i = 0; i < 170; i++) s += '<circle cx="' + (r() * 1200).toFixed(1) + '" cy="' + (r() * 320).toFixed(1) + '" r="' + (r() * 1.1 + .3).toFixed(2) +
      '" opacity="' + (r() * .6 + .2).toFixed(2) + '"' + (i % 5 ? '' : ' class="twinkle" style="animation-delay:' + (r() * 4).toFixed(2) + 's"') + '/>';
    stars.innerHTML = s;
  }

  // Seoul now: sky colour, sun and moon follow the real time in Seoul
  try {
    var parts = new Intl.DateTimeFormat('en-GB', { timeZone: 'Asia/Seoul', hour: '2-digit', minute: '2-digit', hour12: false }).formatToParts(new Date());
    var get = function (t) { return +parts.filter(function (x) { return x.type === t; })[0].value; };
    var hh = get('hour') % 24, mm = get('minute'), t = hh + mm / 60;
    var phase = t >= 5 && t < 7 ? 0 : t >= 7 && t < 17 ? 1 : t >= 17 && t < 19 ? 2 : 3;
    var head = document.querySelector('.site-head');
    if (head) head.dataset.phase = ['dawn', 'day', 'dusk', 'night'][phase];
    var now = document.getElementById('seoul-now');
    if (now) now.innerHTML = now.dataset.label + ' <b>' + String(hh).padStart(2, '0') + ':' + String(mm).padStart(2, '0') + '</b> · ' + now.dataset.phases.split('|')[phase];
    var arc = function (f) { return 'translate(' + (80 + f * 1040) + ' ' + (345 - Math.sin(f * Math.PI) * 112) + ')'; };
    var fs = (t - 6) / 13, fm = ((t + 24 - 18) % 24) / 12;
    var sun = document.getElementById('sun'), moon = document.getElementById('moon');
    if (sun && fs > 0 && fs < 1) { sun.setAttribute('transform', arc(fs)); sun.style.display = ''; }
    if (moon && fm > 0 && fm < 1) { moon.setAttribute('transform', arc(fm)); moon.style.display = ''; }
  } catch (e) {}

  // D-day on home cards and tables, counted in Seoul; ended rows disappear
  var seoulToday = (function () {
    try { var d = new Intl.DateTimeFormat('en-CA', { timeZone: 'Asia/Seoul' }).format(new Date()).split('-'); return new Date(+d[0], +d[1] - 1, +d[2]); }
    catch (e) { var x = new Date(); x.setHours(0, 0, 0, 0); return x; }
  })();
  var day = function (s) { var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); };
  document.querySelectorAll('.dc[data-end], .board tr[data-end], .codes tr[data-end]').forEach(function (el) {
    var e = day(el.dataset.end), s = day(el.dataset.start);
    if (e < seoulToday) { el.hidden = true; return; }
    var tag = el.querySelector('.dday');
    if (!tag || s > seoulToday) return;
    var n = Math.round((e - seoulToday) / 864e5);
    tag.textContent = n > 0 ? 'D-' + n : (tag.dataset.today || tag.textContent);
    tag.classList.toggle('hot', n <= 2);
    var cell = tag.closest('td'); if (cell) cell.classList.toggle('hot', n <= 2);
  });

  // Home headline: the soonest-ending sale that is on today in Seoul; none left → the plain fallback (no dates)
  var leads = document.querySelectorAll('.lead[data-end]'), fb = document.querySelector('.lead-fallback'), pick = null;
  leads.forEach(function (el) {
    if (!pick && day(el.dataset.start) <= seoulToday && day(el.dataset.end) >= seoulToday) pick = el;
    el.hidden = true;
  });
  if (pick) {
    pick.hidden = false;
    var lt = pick.querySelector('.dday'), ln = Math.round((day(pick.dataset.end) - seoulToday) / 864e5);
    if (lt) lt.textContent = ln > 0 ? 'D-' + ln : (lt.dataset.today || lt.textContent);
  }
  if (fb) fb.hidden = !!pick;

  // Header date and "N sales checked" count follow the Seoul date, not the day of the last build
  var dl = document.querySelector('.dl-date');
  if (dl) {
    var wd = dl.dataset.wd.split('|'), mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    dl.textContent = dl.dataset.fmt.replace('{Y}', seoulToday.getFullYear()).replace('{M}', seoulToday.getMonth() + 1)
      .replace('{D}', seoulToday.getDate()).replace('{Mon}', mon[seoulToday.getMonth()]).replace('{W}', wd[(seoulToday.getDay() + 6) % 7]);
  }
  var cnt = document.querySelector('.dl-count');
  if (cnt && cnt.dataset.ends !== undefined) {
    var nd = 0, nc = 0;
    cnt.dataset.ends.split(',').forEach(function (x) {
      if (!x) return;
      var p = x.split(':');
      if (day(p[0]) >= seoulToday) { nd++; nc += +p[1]; }
    });
    cnt.textContent = cnt.dataset.tpl.replace('{d}', nd).replace('{c}', nc).replace('{g}', cnt.dataset.g);
  }

  // official links: send phones to the right app store
  var ua = navigator.userAgent, os = /iPhone|iPad|iPod/.test(ua) || (/Macintosh/.test(ua) && 'ontouchend' in document) ? 'ios' : /Android/.test(ua) ? 'android' : '';
  if (os) document.querySelectorAll('a.go[data-' + os + ']').forEach(function (a) { a.href = a.dataset[os]; });

  document.querySelectorAll('.codes .copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var label = b.textContent;
      if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.code).then(function () {
        b.textContent = b.dataset.done; b.classList.add('done');
        setTimeout(function () { b.textContent = label; b.classList.remove('done'); }, 1500);
      }, function () {});
    });
  });
})();
/* 2026-11-28: wide wayfinding maps on phones start centred (the route and the target sit in the middle) */
(function () {
  function centre() {
    document.querySelectorAll('.fig').forEach(function (f) {
      if (f.scrollWidth > f.clientWidth + 4 && !f.dataset.centred) { f.scrollLeft = (f.scrollWidth - f.clientWidth) / 2; f.dataset.centred = '1'; }
    });
  }
  window.addEventListener('load', centre);
  document.addEventListener('toggle', function () { setTimeout(centre, 50); }, true);
  document.addEventListener('load', function (e) { if (e.target && e.target.tagName === 'IMG') centre(); }, true);
})();
