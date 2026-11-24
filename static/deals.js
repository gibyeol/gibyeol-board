// Deals board: live D-day, hide ended deals, category filter, copy-code buttons. Works without it too.
(function () {
  var list = document.querySelector('.deals[data-ends]');
  if (!list) return;
  var today = new Date(); today.setHours(0, 0, 0, 0);
  var day = function (s) { var p = s.split('-'); return new Date(+p[0], +p[1] - 1, +p[2]); };
  list.querySelectorAll('.deal').forEach(function (li) {
    var s = day(li.dataset.start), e = day(li.dataset.end), tag = li.querySelector('.deal-dday');
    if (e < today) { li.hidden = true; return; }
    var n;
    if (s > today) { n = Math.round((s - today) / 864e5); tag.textContent = list.dataset.starts.replace('{n}', n); }
    else { n = Math.round((e - today) / 864e5); tag.textContent = n === 0 ? list.dataset.today : list.dataset.ends.replace('{n}', n); }
  });
  var chips = document.querySelectorAll('.deal-filter .chip');
  chips.forEach(function (b) {
    b.addEventListener('click', function () {
      chips.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      var c = b.dataset.cat;
      list.querySelectorAll('.deal').forEach(function (li) {
        var ended = day(li.dataset.end) < today;
        li.hidden = ended || (c && li.dataset.cat !== c);
      });
    });
  });
  document.querySelectorAll('.deal-code .copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var label = b.textContent, done = function () { b.textContent = b.dataset.done; b.classList.add('done'); setTimeout(function () { b.textContent = label; b.classList.remove('done'); }, 1500); };
      if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.code).then(done, function () {});
    });
  });
})();
