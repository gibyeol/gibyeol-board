/* Nadri name stamp: write your name in Korean and stamp it like a seal (dojang).
   Runs entirely in the browser; nothing typed here is sent anywhere.
   Hangul -> Revised Romanization (personal-name rule: no sound changes between syllables)
   Kana   -> Hangul (National Institute of Korean Language, Japanese transcription rules)
   Kanji/Hanzi -> Korean reading of each character (data: hanja-ko.js)
   Latin  -> checked list of common names, else an approximate reading (labelled) */
(function () {
  'use strict';
  var root = document.getElementById('namer');
  if (!root) return;
  var LANG = root.getAttribute('data-lang') || 'en';

  var UI_ALL = {
    en: { ph: 'Type your name (Sophia, 田中 花子, 김민지…)', go: 'Stamp it', sound: 'In Korean letters', reading: 'Your characters read the Korean way', roman: 'In English letters (Revised Romanization)', approx: 'Approximate: this name is not on our checked list yet, so this is a best guess from the spelling.', checked: 'From our checked list of common names.', kana: 'Japanese sound written in Korean (official transcription rules).', hanja: 'Each character has its own Korean reading; the first sound follows Korean name rules (e.g. 李 is read 이).', rr: 'Official romanization, one syllable at a time as Korean names are written. Passports often use older spellings such as Lee, Park, Kim.', save: 'Save the stamp', share: 'Copy a link', copied: 'Link copied', empty: 'Type a name first.', none: 'We could not read that one. Try letters, kana, Hangul or Chinese characters.', privacy: 'Your name stays on this device: we never send it anywhere, and the share card is drawn right here. This page loads no affiliate or ad scripts. Cloudflare, our host, counts visits without cookies. A copied link contains the name.', wrong: 'Looks wrong? Tell us and we will fix the list.', secSound: 'Sound', secMeaning: 'Meaning', secChain: 'Where your name leads in Korea', lKo: 'Korean', lJa: 'Japanese', lZh: 'Chinese (Taiwan)', conf: { h: 'well documented', m: 'likely', l: 'uncertain' }, word: 'The meaning in each language', idea: 'A name with the same meaning', src: 'Source: Behind the Name', chars: 'Character by character (Korean meaning + sound, English)', kanaApprox: 'approximate', noMeaning: 'We have not checked the meaning of this name yet. Tell us and we will add it.' },
    ko: { ph: '이름을 입력하세요 (김민지, Sophia, 田中…)', go: '도장 찍기', sound: '한글로 쓰면', reading: '한국 한자음으로 읽으면', roman: '로마자로 쓰면 (국어의 로마자 표기법)', approx: '대략적인 소리예요. 아직 확인한 이름 목록에 없어서 철자로 추정했어요.', checked: '확인한 흔한 이름 목록에서 가져왔어요.', kana: '일본어 소리를 외래어 표기법대로 한글로 썼어요.', hanja: '글자마다 한국 한자음으로 읽고, 첫소리는 두음법칙을 따랐어요 (예: 李 → 이).', rr: '이름은 음절마다 따로 적는 공식 표기예요. 여권에는 Lee, Park, Kim처럼 관습 표기를 쓰는 경우가 많아요.', save: '도장 저장', share: '링크 복사', copied: '복사했어요', empty: '먼저 이름을 입력하세요.', none: '읽을 수 없는 글자예요. 로마자, 가나, 한글, 한자로 입력해 보세요.', privacy: '입력한 이름은 이 기기 밖으로 보내지 않고, 공유 카드도 이 기기에서 그려요. 이 페이지에는 제휴·광고 스크립트가 없어요. 사이트를 호스팅하는 Cloudflare가 쿠키 없이 방문 수를 세요. 링크를 복사하면 그 링크에는 이름이 들어가요.', wrong: '이상하게 나왔나요? 알려 주시면 목록을 고칠게요.', secSound: '소리', secMeaning: '뜻', secChain: '이 이름이 한국에서 이어지는 곳', lKo: '한국어', lJa: '일본어', lZh: '중국어(대만)', conf: { h: '확실', m: '유력', l: '불확실' }, word: '뜻을 각 언어로', idea: '같은 뜻의 이름', src: '출처: Behind the Name', chars: '글자마다 (훈과 음, 영어 뜻)', kanaApprox: '대략', noMeaning: '아직 뜻을 확인하지 않은 이름이에요. 알려 주시면 추가할게요.' },
    ja: { ph: '名前を入力(はなこ、田中 花子、Sophia…)', go: 'はんこを押す', sound: 'ハングルで書くと', reading: '韓国の漢字音で読むと', roman: 'ローマ字(韓国の公式表記)', approx: 'おおよその読みです。まだ確認済みリストにない名前なので、つづりから推定しました。', checked: '確認済みのよくある名前リストから。', kana: '日本語の音を、韓国の外来語表記法どおりにハングルで書きました。', hanja: '漢字は一字ずつ韓国語の音で読み、最初の音は韓国の名前のルールに従います(例:李→이)。', rr: '韓国の名前は一音節ずつ表記するのが公式。パスポートではLee、Park、Kimなど慣用表記も多いです。', save: 'はんこを保存', share: 'リンクをコピー', copied: 'コピーしました', empty: 'まず名前を入力してください。', none: '読めない文字でした。ひらがな・カタカナ・漢字・ローマ字で試してください。', privacy: '入力した名前はこの端末の外に送らず、共有カードもこの端末で描きます。このページにはアフィリエイトや広告のスクリプトはありません。サイトをホストするCloudflareが、Cookieを使わずに訪問数を数えます。リンクをコピーすると、そのリンクには名前が入ります。', wrong: 'おかしな結果?教えてもらえればリストを直します。', secSound: '音', secMeaning: '意味', secChain: 'この名前が韓国でつながる場所', lKo: '韓国語', lJa: '日本語', lZh: '中国語(台湾)', conf: { h: '確実', m: '有力', l: '不確か' }, word: '意味を各言語で', idea: '同じ意味の名前', src: '出典:Behind the Name', chars: '一字ずつ(韓国での訓と音・英語の意味)', kanaApprox: 'おおよそ', noMeaning: 'この名前の意味はまだ確認していません。教えてもらえれば追加します。' },
    'zh-tw': { ph: '輸入你的名字(陳怡婷、Sophia…)', go: '蓋章', sound: '用韓文字母寫', reading: '用韓國漢字音來讀', roman: '羅馬拼音(韓國官方標記)', approx: '這是大概的讀法。這個名字還不在我們確認過的清單裡,所以是照拼字推測的。', checked: '來自我們確認過的常見名字清單。', kana: '把日文發音照韓國外來語標記法寫成韓文。', hanja: '每個漢字照韓國的漢字音來讀,第一個音照韓國姓名規則(例:李→이)。韓國新聞寫台灣人名時,通常照華語發音另外標記。', rr: '韓國人名官方寫法是一個音節一個音節標記。護照上常見 Lee、Park、Kim 這類慣用拼法。', save: '儲存印章', share: '複製連結', copied: '已複製', empty: '請先輸入名字。', none: '看不懂這些字。請用中文、英文、假名或韓文試試。', privacy: '你輸入的名字不會傳出這台裝置,分享卡也是在這台裝置上畫出來的。這一頁沒有聯盟行銷或廣告程式。網站主機 Cloudflare 會在不使用 Cookie 的情況下計算造訪次數。複製的連結裡會包含名字。', wrong: '結果怪怪的?告訴我們,我們會修正清單。', secSound: '讀音', secMeaning: '意思', secChain: '這個名字在韓國會帶你去哪裡', lKo: '韓文', lJa: '日文', lZh: '中文(台灣)', conf: { h: '確定', m: '很可能', l: '不確定' }, word: '用各種語言說它的意思', idea: '同樣意思的名字', src: '出處:Behind the Name', chars: '逐字(韓國的訓與音、英文意思)', kanaApprox: '大約', noMeaning: '這個名字的意思我們還沒確認。告訴我們,我們會加上。' }
  };
  var UI = UI_ALL[LANG];

  /* ---------- Hangul helpers ---------- */
  var CHO = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ', JUNG = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ', JONG = ' ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ';
  function syl(c, v, f) { return String.fromCharCode(0xAC00 + (CHO.indexOf(c) * 21 + JUNG.indexOf(v)) * 28 + (f ? JONG.indexOf(f) : 0)); }
  function split(s) { var n = s.charCodeAt(0) - 0xAC00; return [CHO[Math.floor(n / 588)], JUNG[Math.floor(n % 588 / 28)], JONG[n % 28].trim()]; }
  function isHangul(ch) { var n = ch.charCodeAt(0); return n >= 0xAC00 && n <= 0xD7A3; }
  function addFinal(s, f) { var p = split(s); return p[2] ? null : syl(p[0], p[1], f); }

  /* ---------- Hangul -> Revised Romanization (names: syllable by syllable) ---------- */
  var RC = { 'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt', 'ㄹ': 'r', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h' };
  var RV = { 'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe', 'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui', 'ㅣ': 'i' };
  var RF = { 'ㄱ': 'k', 'ㄲ': 'k', 'ㅋ': 'k', 'ㄳ': 'k', 'ㄺ': 'k', 'ㄴ': 'n', 'ㄵ': 'n', 'ㄶ': 'n', 'ㄷ': 't', 'ㅅ': 't', 'ㅆ': 't', 'ㅈ': 't', 'ㅊ': 't', 'ㅌ': 't', 'ㅎ': 't', 'ㄹ': 'l', 'ㄼ': 'l', 'ㄽ': 'l', 'ㄾ': 'l', 'ㅀ': 'l', 'ㄻ': 'm', 'ㅁ': 'm', 'ㅂ': 'p', 'ㅄ': 'p', 'ㄿ': 'p', 'ㅍ': 'p', 'ㅇ': 'ng' };
  var SURNAME_RR = { '김': 'Kim', '이': 'Lee', '박': 'Park', '최': 'Choi', '정': 'Jung', '강': 'Kang', '조': 'Cho', '윤': 'Yoon', '장': 'Jang', '임': 'Lim', '한': 'Han', '오': 'Oh', '서': 'Seo', '신': 'Shin', '권': 'Kwon', '황': 'Hwang', '안': 'Ahn', '송': 'Song', '류': 'Ryu', '유': 'Yoo', '홍': 'Hong', '전': 'Jeon', '고': 'Ko', '문': 'Moon', '양': 'Yang', '손': 'Son', '배': 'Bae', '백': 'Baek', '허': 'Heo', '노': 'Noh', '남': 'Nam', '심': 'Shim', '하': 'Ha', '곽': 'Kwak', '성': 'Sung', '차': 'Cha', '주': 'Joo', '우': 'Woo', '구': 'Koo', '민': 'Min', '진': 'Jin', '나': 'Na', '지': 'Ji', '엄': 'Um', '채': 'Chae', '원': 'Won', '천': 'Cheon', '방': 'Bang', '공': 'Kong', '현': 'Hyun', '함': 'Ham', '변': 'Byun', '염': 'Yeom', '여': 'Yeo', '추': 'Choo', '도': 'Do', '소': 'So', '석': 'Seok', '선': 'Sun', '설': 'Seol', '마': 'Ma', '길': 'Gil', '연': 'Yeon', '위': 'Wi', '표': 'Pyo', '명': 'Myung', '기': 'Ki', '반': 'Ban', '왕': 'Wang', '금': 'Keum', '옥': 'Ok', '육': 'Yook', '인': 'In', '맹': 'Maeng', '제': 'Je', '모': 'Mo', '탁': 'Tak', '국': 'Kook', '어': 'Eo', '은': 'Eun', '편': 'Pyeon', '용': 'Yong' };
  function rrSyl(s) { var p = split(s); return RC[p[0]] + RV[p[1]] + (p[2] ? RF[p[2]] : ''); }
  function cap(w) { return w.charAt(0).toUpperCase() + w.slice(1); }
  function romanize(word) {
    var out = [];
    for (var i = 0; i < word.length; i++) if (isHangul(word[i])) out.push(rrSyl(word[i]));
    return out;
  }
  function hangulResult(words) {
    // "김민지" -> surname 김 + given 민지 ; "김 민지" also works
    var parts = words.length > 1 ? words : (words[0].length >= 2 && words[0].length <= 4 ? [words[0].slice(0, words[0].length === 4 ? 2 : 1), words[0].slice(words[0].length === 4 ? 2 : 1)] : words);
    var given = parts.slice(1).join('');
    var rr = cap(romanize(parts[0]).join('')) + (given ? ' ' + cap(romanize(given).join('-')) : '');
    var habit = SURNAME_RR[parts[0]];
    var extra = habit && given ? habit + ' ' + cap(romanize(given).join('')) : '';
    var ja = parts.map(toKatakana).join('・');
    var RS = window.KO_RU_SURNAME || {};
    var ru = parts.map(function (w, i) { return i === 0 && RS[w] ? RS[w] : toCyrillic(w); }).join(' ');
    return { hangul: parts.join(''), kind: 'hangul', sounds: [[UI.roman, rr + (extra && extra !== rr.replace('-', '') ? ' · ' + extra : '')], [UI.lJa + ' (' + UI.kanaApprox + ')', ja], [(T && T.lRu || 'Russian') + ' (' + UI.kanaApprox + ')', ru]], note: UI.rr, ko: { sur: parts.length > 1 ? parts[0] : '', given: parts.length > 1 ? given : parts[0] } };
  }



  /* ---------- Hangul -> Cyrillic (Kontsevich system, approximate) ---------- */
  var CYC = { 'ㄱ': ['к', 'г'], 'ㄲ': ['кк', 'кк'], 'ㄴ': ['н', 'н'], 'ㄷ': ['т', 'д'], 'ㄸ': ['тт', 'тт'], 'ㄹ': ['р', 'р'], 'ㅁ': ['м', 'м'], 'ㅂ': ['п', 'б'], 'ㅃ': ['пп', 'пп'], 'ㅅ': ['с', 'с'], 'ㅆ': ['сс', 'сс'], 'ㅇ': ['', ''], 'ㅈ': ['ч', 'дж'], 'ㅉ': ['чч', 'чч'], 'ㅊ': ['чх', 'чх'], 'ㅋ': ['кх', 'кх'], 'ㅌ': ['тх', 'тх'], 'ㅍ': ['пх', 'пх'], 'ㅎ': ['х', 'х'] };
  var CYV = { 'ㅏ': 'а', 'ㅐ': 'э', 'ㅑ': 'я', 'ㅒ': 'йе', 'ㅓ': 'о', 'ㅔ': 'е', 'ㅕ': 'ё', 'ㅖ': 'е', 'ㅗ': 'о', 'ㅘ': 'ва', 'ㅙ': 'вэ', 'ㅚ': 'ве', 'ㅛ': 'ё', 'ㅜ': 'у', 'ㅝ': 'во', 'ㅞ': 'ве', 'ㅟ': 'ви', 'ㅠ': 'ю', 'ㅡ': 'ы', 'ㅢ': 'ый', 'ㅣ': 'и' };
  var CYF = { 'ㄱ': 'к', 'ㄲ': 'к', 'ㅋ': 'к', 'ㄴ': 'н', 'ㅇ': 'н', 'ㅁ': 'м', 'ㄹ': 'ль', 'ㅂ': 'п', 'ㅍ': 'п', 'ㄷ': 'т', 'ㅅ': 'т', 'ㅆ': 'т', 'ㅈ': 'т', 'ㅊ': 'т', 'ㅌ': 'т', 'ㅎ': 'т' };
  function toCyrillic(word) {
    var out = '', prevFinal = '';
    for (var i = 0; i < word.length; i++) {
      if (!isHangul(word[i])) continue;
      var p = split(word[i]), c = CYC[p[0]][i === 0 || (prevFinal && prevFinal !== 'ㄴ' && prevFinal !== 'ㅁ' && prevFinal !== 'ㅇ' && prevFinal !== 'ㄹ') ? 0 : 1];
      var v = CYV[p[1]];
      if (!c && (v === 'э' || v === 'е') && i === 0) v = v === 'э' ? 'э' : 'е';
      out += c + v + (p[2] ? (CYF[p[2]] || '') : '');
      prevFinal = p[2];
    }
    return out.charAt(0).toUpperCase() + out.slice(1);
  }

  /* ---------- Hangul -> katakana (approximate, as Japanese media usually write Korean names) ---------- */
  var KROW = { '': 'アイウエオ', k: 'カキクケコ', g: 'ガギグゲゴ', s: 'サシスセソ', t: 'タチツテト', d: 'ダヂヅデド', n: 'ナニヌネノ', h: 'ハヒフヘホ', b: 'バビブベボ', p: 'パピプペポ', m: 'マミムメモ', r: 'ラリルレロ' };
  var KC = { 'ㄱ': ['k', 'g'], 'ㄲ': ['k', 'k'], 'ㄴ': ['n', 'n'], 'ㄷ': ['t', 'd'], 'ㄸ': ['t', 't'], 'ㄹ': ['r', 'r'], 'ㅁ': ['m', 'm'], 'ㅂ': ['p', 'b'], 'ㅃ': ['p', 'p'], 'ㅅ': ['s', 's'], 'ㅆ': ['s', 's'], 'ㅇ': ['', ''], 'ㅈ': ['ch', 'j'], 'ㅉ': ['ch', 'ch'], 'ㅊ': ['ch', 'ch'], 'ㅋ': ['k', 'k'], 'ㅌ': ['t', 't'], 'ㅍ': ['p', 'p'], 'ㅎ': ['h', 'h'] };
  var KV = { 'ㅏ': 'a', 'ㅐ': 'e', 'ㅑ': 'ya', 'ㅒ': 'ye', 'ㅓ': 'o', 'ㅔ': 'e', 'ㅕ': 'yo', 'ㅖ': 'ye', 'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'we', 'ㅚ': 'we', 'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'u', 'ㅢ': 'ui', 'ㅣ': 'i' };
  var KF = { 'ㄱ': 'ク', 'ㄲ': 'ク', 'ㅋ': 'ク', 'ㄴ': 'ン', 'ㅇ': 'ン', 'ㅁ': 'ム', 'ㄹ': 'ル', 'ㅂ': 'プ', 'ㅍ': 'プ', 'ㄷ': 'ッ', 'ㅅ': 'ッ', 'ㅆ': 'ッ', 'ㅈ': 'ッ', 'ㅊ': 'ッ', 'ㅌ': 'ッ', 'ㅎ': 'ッ' };
  function kmora(c, v) {
    var idx = 'aiueo'.indexOf(v);
    if (c === 'ch' || c === 'j') v = { wa: 'a', we: 'e', wi: 'i', wo: 'o', ui: 'i', ya: 'a', yu: 'u', yo: 'o', ye: 'e' }[v] || v;
    if (c === 'ch' || c === 'j') { var base = c === 'ch' ? 'チ' : 'ジ'; return v === 'i' ? base : base + { a: 'ャ', u: 'ュ', e: 'ェ', o: 'ョ' }[v]; }
    if (c === 's' && v === 'i') return 'シ';
    var td = { ti: 'ティ', tu: 'トゥ', di: 'ディ', du: 'ドゥ' }[c + v];
    if (td) return td;
    if (idx >= 0) return KROW[c][idx];
    var y = { ya: 'ャ', yu: 'ュ', yo: 'ョ' }[v];
    if (y) return c ? KROW[c][1] + y : { ya: 'ヤ', yu: 'ユ', yo: 'ヨ' }[v];
    if (v === 'ye') return c ? KROW[c][3] : 'イェ';
    var w = { wa: 'ァ', we: 'ェ', wi: 'ィ', wo: 'ォ', ui: 'ィ' }[v];
    if (!c) return { wa: 'ワ', we: 'ウェ', wi: 'ウィ', wo: 'ウォ', ui: 'ウィ' }[v];
    return KROW[c][2] + w;
  }
  function toKatakana(word) {
    var out = '';
    for (var i = 0; i < word.length; i++) {
      if (!isHangul(word[i])) continue;
      var p = split(word[i]), c = KC[p[0]][i === 0 ? 0 : 1];
      out += kmora(c, KV[p[1]]) + (p[2] ? (KF[p[2]] || '') : '');
    }
    return out;
  }

  /* ---------- Kana -> Hangul ---------- */
  function toHira(s) { return s.replace(/[ァ-ヶ]/g, function (c) { return String.fromCharCode(c.charCodeAt(0) - 0x60); }); }
  // [initial, medial] ; single value = same in both
  var K = {
    'あ': '아', 'い': '이', 'う': '우', 'え': '에', 'お': '오',
    'か': ['가', '카'], 'き': ['기', '키'], 'く': ['구', '쿠'], 'け': ['게', '케'], 'こ': ['고', '코'],
    'が': '가', 'ぎ': '기', 'ぐ': '구', 'げ': '게', 'ご': '고',
    'さ': '사', 'し': '시', 'す': '스', 'せ': '세', 'そ': '소',
    'ざ': '자', 'じ': '지', 'ず': '즈', 'ぜ': '제', 'ぞ': '조',
    'た': ['다', '타'], 'ち': ['지', '치'], 'つ': '쓰', 'て': ['데', '테'], 'と': ['도', '토'],
    'だ': '다', 'ぢ': '지', 'づ': '즈', 'で': '데', 'ど': '도',
    'な': '나', 'に': '니', 'ぬ': '누', 'ね': '네', 'の': '노',
    'は': '하', 'ひ': '히', 'ふ': '후', 'へ': '헤', 'ほ': '호',
    'ば': '바', 'び': '비', 'ぶ': '부', 'べ': '베', 'ぼ': '보',
    'ぱ': '파', 'ぴ': '피', 'ぷ': '푸', 'ぺ': '페', 'ぽ': '포',
    'ま': '마', 'み': '미', 'む': '무', 'め': '메', 'も': '모',
    'や': '야', 'ゆ': '유', 'よ': '요',
    'ら': '라', 'り': '리', 'る': '루', 'れ': '레', 'ろ': '로',
    'わ': '와', 'を': '오', 'ゔ': '부',
    'きゃ': ['갸', '캬'], 'きゅ': ['규', '큐'], 'きょ': ['교', '쿄'],
    'ぎゃ': '갸', 'ぎゅ': '규', 'ぎょ': '교',
    'しゃ': '샤', 'しゅ': '슈', 'しょ': '쇼', 'しぇ': '셰',
    'じゃ': '자', 'じゅ': '주', 'じょ': '조', 'じぇ': '제',
    'ちゃ': ['자', '차'], 'ちゅ': ['주', '추'], 'ちょ': ['조', '초'], 'ちぇ': ['제', '체'],
    'にゃ': '냐', 'にゅ': '뉴', 'にょ': '뇨',
    'ひゃ': '햐', 'ひゅ': '휴', 'ひょ': '효',
    'びゃ': '뱌', 'びゅ': '뷰', 'びょ': '뵤',
    'ぴゃ': '퍄', 'ぴゅ': '퓨', 'ぴょ': '표',
    'みゃ': '먀', 'みゅ': '뮤', 'みょ': '묘',
    'りゃ': '랴', 'りゅ': '류', 'りょ': '료',
    'ふぁ': '파', 'ふぃ': '피', 'ふぇ': '페', 'ふぉ': '포', 'てぃ': '티', 'でぃ': '디', 'とぅ': '투', 'どぅ': '두', 'うぃ': '위', 'うぇ': '웨', 'うぉ': '워'
  };
  function vowelOf(h) { return h ? split(h[h.length - 1])[1] : ''; }
  function kanaWord(w) {
    w = toHira(w);
    var out = '', i = 0, first = true, prevV = '';
    while (i < w.length) {
      var two = w.substr(i, 2), one = w[i], val = null, used = 1;
      if (K[two]) { val = K[two]; used = 2; } else if (K[one]) { val = K[one]; }
      if (one === 'ん') { var f = out && addFinal(out[out.length - 1], 'ㄴ'); if (f) out = out.slice(0, -1) + f; i++; continue; }
      if (one === 'っ') { var g = out && addFinal(out[out.length - 1], 'ㅅ'); if (g) out = out.slice(0, -1) + g; i++; continue; }
      if (one === 'ー') { i++; continue; }
      // long vowels are not written: ou, oo, uu
      if ((one === 'う' && (prevV === 'ㅗ' || prevV === 'ㅛ' || prevV === 'ㅜ' || prevV === 'ㅠ')) || (one === 'お' && (prevV === 'ㅗ' || prevV === 'ㅛ'))) { i++; continue; }
      if (val === null) return null;
      var h = typeof val === 'string' ? val : val[first ? 0 : 1];
      out += h; prevV = vowelOf(h); first = false; i += used;
    }
    return out;
  }


  /* ---------- Japanese romaji -> kana (used on the Japanese page) ---------- */
  var RK = {};
  (function () {
    var rows = { '': 'あいうえお', k: 'かきくけこ', g: 'がぎぐげご', s: 'さしすせそ', z: 'ざじずぜぞ', t: 'たちつてと', d: 'だぢづでど', n: 'なにぬねの', h: 'はひふへほ', b: 'ばびぶべぼ', p: 'ぱぴぷぺぽ', m: 'まみむめも', r: 'らりるれろ' };
    Object.keys(rows).forEach(function (c) { 'aiueo'.split('').forEach(function (v, i) { RK[c + v] = rows[c][i]; }); });
    RK.shi = 'し'; RK.chi = 'ち'; RK.tsu = 'つ'; RK.fu = 'ふ'; RK.ji = 'じ'; delete RK.si; delete RK.ti; delete RK.tu; delete RK.hu; delete RK.zi;
    RK.ya = 'や'; RK.yu = 'ゆ'; RK.yo = 'よ'; RK.wa = 'わ'; RK.wo = 'を';
    'k:き,g:ぎ,n:に,h:ひ,b:び,p:ぴ,m:み,r:り'.split(',').forEach(function (x) { var c = x.split(':'); RK[c[0] + 'ya'] = c[1] + 'ゃ'; RK[c[0] + 'yu'] = c[1] + 'ゅ'; RK[c[0] + 'yo'] = c[1] + 'ょ'; });
    RK.sha = 'しゃ'; RK.shu = 'しゅ'; RK.sho = 'しょ'; RK.ja = 'じゃ'; RK.ju = 'じゅ'; RK.jo = 'じょ'; RK.cha = 'ちゃ'; RK.chu = 'ちゅ'; RK.cho = 'ちょ';
  })();
  function romajiToKana(w) {
    w = w.toLowerCase().replace(/oh(?=[^aiueoy]|$)/g, 'ou').replace(/ō/g, 'ou').replace(/ū/g, 'uu').replace(/ā/g, 'a').replace(/ē/g, 'e').replace(/ī/g, 'i');
    var out = '', i = 0;
    while (i < w.length) {
      if (w[i] === 'n' && (i + 1 === w.length || !/[aiueoy]/.test(w[i + 1]))) { out += 'ん'; i++; if (w[i] === "'") i++; continue; }
      if (w[i] === w[i + 1] && /[kstpgdbcmj]/.test(w[i])) { out += 'っ'; i++; continue; }
      if (w.substr(i, 3) === 'tch') { out += 'っ'; i++; continue; }
      var hit = null;
      for (var l = 3; l >= 1 && !hit; l--) if (RK[w.substr(i, l)]) hit = [RK[w.substr(i, l)], l];
      if (!hit) return null;
      out += hit[0]; i += hit[1];
    }
    return out;
  }

  /* ---------- Kanji / Hanzi -> Korean reading ---------- */
  var DUEUM = { 'ㄹ': { 'ㅑ': 'ㅇ', 'ㅕ': 'ㅇ', 'ㅖ': 'ㅇ', 'ㅛ': 'ㅇ', 'ㅠ': 'ㅇ', 'ㅣ': 'ㅇ', '*': 'ㄴ' }, 'ㄴ': { 'ㅑ': 'ㅇ', 'ㅕ': 'ㅇ', 'ㅛ': 'ㅇ', 'ㅠ': 'ㅇ', 'ㅣ': 'ㅇ' } };
  function dueum(s) {
    var p = split(s), rule = DUEUM[p[0]];
    if (!rule) return s;
    var to = rule[p[1]] || rule['*'];
    return to ? syl(to, p[1], p[2]) : s;
  }
  function hanWord(w, isFirstWord) {
    var out = '';
    for (var i = 0; i < w.length; i++) {
      var c = w[i], n = c.charCodeAt(0);
      if (c === '々' && out) { out += out[out.length - 1]; continue; }
      if (n < 0x4E00 || n > 0x9FFF || !window.HANJA_KO) return null;
      var h = window.HANJA_KO[n - 0x4E00];
      if (h === '·') return null;
      if (isFirstWord && i === 0 && c === '金') h = '김';
      if (i === 0) h = dueum(h);
      out += h;
    }
    return out;
  }

  /* ---------- Latin -> Hangul ---------- */
  var LIST = ('aaron:에런,abigail:애비게일,adam:애덤,adrian:에이드리언,aiden:에이든,alex:알렉스,alexander:알렉산더,alexandra:알렉산드라,alice:앨리스,alicia:알리시아,amanda:어맨다,amber:앰버,amelia:아멜리아,amy:에이미,andrew:앤드루,andy:앤디,angela:앤절라,anna:안나,anne:앤,anthony:앤서니,aria:아리아,ashley:애슐리,audrey:오드리,ava:에이바,barbara:바버라,ben:벤,benjamin:벤저민,bella:벨라,brandon:브랜던,brian:브라이언,brittany:브리트니,brooke:브룩,caleb:케일럽,cameron:캐머런,camila:카밀라,carlos:카를로스,caroline:캐럴라인,catherine:캐서린,charles:찰스,charlie:찰리,charlotte:샬럿,chloe:클로이,chris:크리스,christian:크리스천,christina:크리스티나,christopher:크리스토퍼,claire:클레어,daniel:대니얼,david:데이비드,diana:다이애나,dylan:딜런,edward:에드워드,eleanor:엘리너,elena:엘레나,eli:일라이,elijah:일라이자,elizabeth:엘리자베스,ella:엘라,ellie:엘리,emily:에밀리,emma:에마,eric:에릭,ethan:이선,eva:에바,evelyn:에벌린,gabriel:가브리엘,george:조지,grace:그레이스,hannah:해나,harper:하퍼,harry:해리,hazel:헤이즐,henry:헨리,isaac:아이작,isabel:이저벨,isabella:이사벨라,jack:잭,jackson:잭슨,jacob:제이컵,james:제임스,jane:제인,jasmine:재스민,jason:제이슨,jennifer:제니퍼,jessica:제시카,john:존,jonathan:조너선,jordan:조던,joseph:조지프,joshua:조슈아,julia:줄리아,julian:줄리언,justin:저스틴,kate:케이트,katherine:캐서린,kevin:케빈,kyle:카일,laura:로라,lauren:로런,layla:레일라,leo:레오,liam:리엄,lily:릴리,lisa:리사,logan:로건,lucas:루카스,lucy:루시,luna:루나,madison:매디슨,maria:마리아,mark:마크,mary:메리,mason:메이슨,matthew:매슈,maya:마야,megan:메건,mia:미아,michael:마이클,michelle:미셸,mila:밀라,nathan:네이선,nicholas:니컬러스,nicole:니콜,noah:노아,nora:노라,oliver:올리버,olivia:올리비아,owen:오언,patrick:패트릭,paul:폴,peter:피터,rachel:레이철,rebecca:레베카,richard:리처드,robert:로버트,ryan:라이언,samantha:서맨사,samuel:새뮤얼,sarah:세라,scarlett:스칼릿,sebastian:세바스찬,sophia:소피아,sophie:소피,stella:스텔라,stephanie:스테퍼니,steven:스티븐,thomas:토머스,tyler:타일러,victoria:빅토리아,violet:바이올렛,william:윌리엄,zoe:조이,zoey:조이,' +
    // Spanish, French, German, Italian, Portuguese
    'alejandro:알레한드로,ana:아나,antonio:안토니오,carmen:카르멘,diego:디에고,francisco:프란시스코,javier:하비에르,jorge:호르헤,jose:호세,juan:후안,lucia:루시아,luis:루이스,manuel:마누엘,miguel:미겔,pablo:파블로,santiago:산티아고,sofia:소피아,valentina:발렌티나,camille:카미유,chloé:클로에,léa:레아,louis:루이,lucie:뤼시,manon:마농,pierre:피에르,jean:장,marie:마리,hugo:위고,anna-lena:안나레나,felix:펠릭스,lukas:루카스,leon:레온,giulia:줄리아,marco:마르코,matteo:마테오,francesca:프란체스카,alessandro:알레산드로,joão:주앙,ines:이네스,' +
    // Southeast Asia / others commonly seen
    'nguyen:응우옌,linh:린,minh:민,anh:아인,siti:시티,putri:뿌뜨리,ahmad:아흐마드,muhammad:무함마드,fatima:파티마,ali:알리,omar:오마르,aisha:아이샤,brooklyn:브루클린,grayson:그레이슨,zachary:재커리,mackenzie:매켄지,xavier:재비어,wyatt:와이엇,hudson:허드슨,lincoln:링컨,nolan:놀런,hunter:헌터,connor:코너,evan:에번,austin:오스틴,jayden:제이든,landon:랜던,carter:카터,ezra:에즈라,isaiah:아이제이아,levi:리바이,luke:루크,max:맥스,miles:마일스,nathaniel:너새니얼,ian:이언,josh:조시,matt:맷,mike:마이크,nick:닉,sam:샘,tom:톰,tim:팀,joe:조,rose:로즈,ruby:루비,penelope:퍼넬러피,riley:라일리,nova:노바,aurora:오로라,savannah:서배너,natalie:내털리,leah:리아,addison:애디슨,naomi:나오미,everly:에벌리,skylar:스카일러,quinn:퀸,sadie:세이디,ivy:아이비,jade:제이드,emilia:에밀리아,madeline:매덜린,kennedy:케네디,kylie:카일리,josephine:조지핀,bailey:베일리,taylor:테일러,morgan:모건,ariana:아리아나,hailey:헤일리,kayla:케일라,jenny:제니,jessie:제시,tiffany:티파니,wendy:웬디,vivian:비비언,irene:아이린,joy:조이,kelly:켈리,vicky:비키,cindy:신디,annie:애니,fiona:피오나,joanne:조앤,judy:주디,peggy:페기,sandy:샌디,tina:티나,winnie:위니,jerry:제리,vincent:빈센트,eason:이슨,jay:제이,allen:앨런,ray:레이,sean:숀,tony:토니,gary:게리,jimmy:지미,johnny:조니,steve:스티브,frank:프랭크,smith:스미스,johnson:존슨,williams:윌리엄스,brown:브라운,jones:존스,garcia:가르시아,miller:밀러,davis:데이비스,rodriguez:로드리게스,martinez:마르티네스,hernandez:에르난데스,lopez:로페스,gonzalez:곤살레스,wilson:윌슨,anderson:앤더슨,moore:무어,martin:마틴,lee:리,thompson:톰프슨,white:화이트,harris:해리스,clark:클라크,lewis:루이스,robinson:로빈슨,walker:워커,young:영,king:킹,wright:라이트,scott:스콧,green:그린,baker:베이커,adams:애덤스,nelson:넬슨,hill:힐,campbell:캠벨,mitchell:미첼,roberts:로버츠,phillips:필립스,evans:에번스,turner:터너,parker:파커,collins:콜린스,edwards:에드워즈,stewart:스튜어트,morris:모리스,murphy:머피,cook:쿡,rogers:로저스,cooper:쿠퍼,ward:워드,cox:콕스,wood:우드,kim:킴,wang:왕,chen:천,schmidt:슈미트,müller:뮐러,schneider:슈나이더,fischer:피셔,weber:베버,meyer:마이어,wagner:바그너,becker:베커,kowalski:코발스키,nowak:노바크,rossi:로시,russo:루소,silva:실바,santos:산투스,dubois:뒤부아,yusuf:유수프,sean:숀,juan:후안,ivan:이반,jaime:하이메,joe:조,matteo:마테오,matthias:마티아스,pedro:페드로,pierre:피에르,hannah:해나,ann:앤,anne:앤,mary:메리,marie:마리,isabel:이저벨,eliza:일라이자,elisa:엘리사,alexandra:알렉산드라,luca:루카,rosa:로사,pearl:펄,victor:빅터,eve:이브,estelle:에스텔,estrella:에스트레야,andre:앙드레,andrea:안드레아,jacques:자크,giovanni:조반니,johannes:요하네스,miguel:미겔,mikhail:미하일,sofiya:소피야,zofia:조피아,theodore:시어도어,margaret:마거릿,dominic:도미닉,gavin:개빈,garrett:개릿,jaxon:잭슨,arjun:아르준,freya:프레야,oscar:오스카,desmond:데즈먼드,priya:프리야,rahul:라훌,wei:웨이,mei:메이,aubrey:오브리,lillian:릴리언,delilah:딜라일라,kinsley:킨즐리,colton:콜턴,brayden:브레이든,bradley:브래들리,ingrid:잉그리드,spencer:스펜서,trevor:트레버').split(',');
  var NAMES = {};
  LIST.forEach(function (p) { var kv = p.split(':'); if (kv[1]) NAMES[kv[0]] = kv[1]; });

  // rough spelling-based reading for names not on the list
  // vowel spellings -> [vowel, extra syllable vowel] (diphthongs such as ay -> 에이)
  var VOW = [['igh', 'ㅏ', 'ㅣ'], ['eau', 'ㅗ'], ['ee', 'ㅣ'], ['ea', 'ㅣ'], ['oo', 'ㅜ'], ['ou', 'ㅏ', 'ㅜ'], ['ai', 'ㅔ', 'ㅣ'], ['ay', 'ㅔ', 'ㅣ'], ['ei', 'ㅔ', 'ㅣ'], ['ey', 'ㅔ', 'ㅣ'], ['ie', 'ㅣ'], ['oa', 'ㅗ'], ['oe', 'ㅗ'], ['au', 'ㅗ'], ['aw', 'ㅗ'], ['ow', 'ㅗ'], ['a', 'ㅏ'], ['e', 'ㅔ'], ['i', 'ㅣ'], ['o', 'ㅗ'], ['u', 'ㅜ'], ['y', 'ㅣ']];
  var CON = [['sch', 'ㅅ', 'ㅟ'], ['tch', 'ㅊ'], ['sh', 'ㅅ', 'ㅟ'], ['ch', 'ㅊ'], ['th', 'ㅅ'], ['ph', 'ㅍ'], ['ck', 'ㅋ'], ['qu', 'ㅋ', 'ㅜ'], ['b', 'ㅂ'], ['c', 'ㅋ'], ['d', 'ㄷ'], ['f', 'ㅍ'], ['g', 'ㄱ'], ['h', 'ㅎ'], ['j', 'ㅈ'], ['k', 'ㅋ'], ['l', 'ㄹ'], ['m', 'ㅁ'], ['n', 'ㄴ'], ['p', 'ㅍ'], ['q', 'ㅋ'], ['r', 'ㄹ'], ['s', 'ㅅ'], ['t', 'ㅌ'], ['v', 'ㅂ'], ['w', 'ㅇ', 'ㅜ'], ['x', 'ㅋ'], ['z', 'ㅈ']];
  var GLIDE = { 'ㅜ': { 'ㅏ': 'ㅘ', 'ㅔ': 'ㅞ', 'ㅣ': 'ㅟ', 'ㅗ': 'ㅝ', 'ㅓ': 'ㅝ' }, 'ㅣ': { 'ㅏ': 'ㅑ', 'ㅔ': 'ㅖ', 'ㅗ': 'ㅛ', 'ㅜ': 'ㅠ', 'ㅓ': 'ㅕ' }, 'ㅟ': { 'ㅏ': 'ㅑ', 'ㅔ': 'ㅖ', 'ㅗ': 'ㅛ', 'ㅜ': 'ㅠ', 'ㅓ': 'ㅕ' } };
  function roughWord(w) {
    w = w.replace(/^wr/, 'r').replace(/^kn/, 'n').replace(/^ps/, 's').replace(/(.)\1/g, '$1').replace(/([^aeiouy])e$/, '$1').replace(/([^aeiou])es$/, '$1s');
    var toks = [], i = 0;
    while (i < w.length) {
      var t = null;
      for (var a = 0; a < VOW.length && !t; a++) {
        var vs = VOW[a][0];
        if (w.substr(i, vs.length) !== vs) continue;
        if (vs[0] === 'y' && i === 0) continue;                  // initial y is a consonant
        if (vs.slice(-1) === 'y' && /[aeiou]/.test(w[i + vs.length] || '')) continue;
        t = { v: VOW[a][1], tail: VOW[a][2], n: vs.length };
        if ((vs === 'ey' || vs === 'y' || vs === 'ie') && i + vs.length === w.length) t = { v: 'ㅣ', n: vs.length };
      }
      for (var b = 0; b < CON.length && !t; b++) if (w.substr(i, CON[b][0].length) === CON[b][0]) t = { c: CON[b][1], g: CON[b][2], n: CON[b][0].length, raw: CON[b][0] };
      if (!t && w[i] === 'y') t = { c: 'ㅇ', g: 'ㅣ', n: 1, raw: 'y' };
      if (!t) return null;
      if (t.raw === 'c' && /[eiy]/.test(w[i + 1] || '')) t.c = 'ㅅ';
      if (t.raw === 'g' && /[eiy]/.test(w[i + 1] || '') && i > 0) t.c = 'ㅈ';
      toks.push(t); i += t.n;
    }
    // h is silent unless a vowel follows it
    toks = toks.filter(function (t, k) { return !(t.raw === 'h' && !(toks[k + 1] && toks[k + 1].v)); });
    var isC = function (t) { return t && !t.v; };
    toks.forEach(function (t, k) {
      var n1 = toks[k + 1], n2 = toks[k + 2];
      if (!t.v || t.tail) return;
      // er, ir, ur (and or after the first syllable) before a consonant or the end: 어 (Spencer 스펜서, Trevor 트레버)
      if (n1 && n1.raw === 'r' && (!n2 || isC(n2)) && (/[ㅔㅣㅜ]/.test(t.v) || (t.v === 'ㅗ' && k > 1))) t.v = 'ㅓ';
      // short a before two consonants (not r): Bradley 브래들리
      else if (t.v === 'ㅏ' && isC(n1) && n1.raw !== 'r' && isC(n2)) t.v = 'ㅐ';
    });
    var vowels = toks.filter(function (t) { return t.v; }).length;
    // unstressed endings: -son -> 슨, -on/-an/-en -> 언
    var L = toks.length;
    if (vowels > 1 && L >= 2 && toks[L - 1].raw === 'n' && toks[L - 2].v && !toks[L - 2].tail) {
      toks[L - 2].v = toks[L - 3] && toks[L - 3].raw === 's' ? 'ㅡ' : 'ㅓ';
    }
    var out = '';
    for (var k = 0; k < toks.length; k++) {
      var cur = toks[k], next = toks[k + 1], prev = toks[k - 1];
      if (cur.v) { out += syl('ㅇ', cur.v); if (cur.tail) out += syl('ㅇ', cur.tail); continue; }
      if (next && next.v) {
        var v = next.v;
        if (cur.g && GLIDE[cur.g] && GLIDE[cur.g][v]) v = GLIDE[cur.g][v];
        if (cur.raw === 'l' && prev && out && (prev.v || split(out[out.length - 1])[1] === 'ㅡ')) { var lf = addFinal(out[out.length - 1], 'ㄹ'); if (lf) out = out.slice(0, -1) + lf; }
        out += syl(cur.c, v); if (next.tail) out += syl('ㅇ', next.tail); k++; continue;
      }
      var last = out && out[out.length - 1];
      if (cur.raw === 'r' && prev && prev.v) continue;                 // r after a vowel is silent: Peter -> 피터
      var fin = { 'ㄴ': 'ㄴ', 'ㅁ': 'ㅁ', 'ㄹ': 'ㄹ' }[cur.c];
      if (cur.raw === 'n' && next && (next.raw === 'g' || next.raw === 'k' || next.raw === 'c') && !(toks[k + 2] && toks[k + 2].v)) fin = next.raw === 'g' ? 'ㅇ' : 'ㅇ';
      if (fin && last && prev && prev.v && !split(last)[2]) { out = out.slice(0, -1) + addFinal(last, fin); if (fin === 'ㅇ' && next.raw === 'g' && k + 2 === toks.length) k++; continue; }
      if (cur.raw === 'x') { out += '크스'; continue; }
      if (cur.raw === 'z') { out += '즈'; continue; }
      out += syl(cur.c, cur.c === 'ㅈ' || cur.c === 'ㅊ' || cur.raw === 'sh' || cur.raw === 'sch' ? 'ㅣ' : 'ㅡ');
    }
    return out;
  }

  /* ---------- run ---------- */
  function entryFor(key) {
    var D = window.NADRI_NAMES || {}, e = D[key], hops = 0;
    while (typeof e === 'string' && hops++ < 3) { key = e; e = D[e]; }
    return e ? { key: key, e: e } : null;
  }
  function convert(raw) {
    var s = raw.trim().replace(/\s+/g, ' ');
    if (!s) return null;
    var words = s.split(' ');
    var kind = /[가-힣]/.test(s) ? 'hangul' : /[぀-ヿ]/.test(s) ? 'kana' : /[一-鿿]/.test(s) ? 'han' : /[a-zA-ZÀ-ÿ]/.test(s) ? 'latin' : null;
    if (kind === 'hangul') return hangulResult(words.filter(function (w) { return /[가-힣]/.test(w); }));
    var out = [], approx = false, romajiUsed = false, infos = [], latinCount = 0, firstKey = null;
    for (var i = 0; i < words.length; i++) {
      var w = words[i], h = null;
      if (/[぀-ヿ]/.test(w)) h = kanaWord(w);
      else if (/[一-鿿々]/.test(w)) {
        // no space between Chinese surname and given name: read whole word, rule applies per name part
        if (words.length === 1 && w.length >= 2 && w.length <= 4 && kind === 'han') {
          var cut = w.length === 4 ? 2 : 1;
          var a = hanWord(w.slice(0, cut), true), b = hanWord(w.slice(cut), false);
          h = a && b ? a + ' ' + b : null;
        } else h = hanWord(w, i === 0);
      } else {
        latinCount++;
        var key = w.toLowerCase().replace(/[^a-zà-ÿ-]/g, '');
        var jk = LANG === 'ja' && !NAMES[key] && !entryFor(key) ? romajiToKana(key) : null;
        var hit = entryFor(key) || entryFor(key.normalize('NFD').replace(/[\u0300-\u036f]/g, ''));
        var typed = key.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
        if (hit && hit.key !== typed && hit.key !== key) {
          // a variant (Yusuf -> Joseph): meaning comes from the root name, but the sound is the name as typed
          hit = { key: hit.key, e: hit.e, alias: true };
          infos.push(hit); h = NAMES[key] || NAMES[typed] || roughWord(typed); if (!NAMES[key] && !NAMES[typed]) approx = true;
          if (!firstKey) firstKey = typed;
        } else if (hit) { infos.push(hit); h = hit.e.ko; if (!firstKey) firstKey = typed; }
        else if (NAMES[key]) h = NAMES[key];
        else if (jk) { h = kanaWord(jk); romajiUsed = true; }
        else { var plain = key.normalize('NFD').replace(/[̀-ͯ]/g, ''); h = NAMES[plain] || roughWord(plain); if (!NAMES[plain]) approx = true; }
      }
      if (!h) return { error: true };
      out.push(h);
    }
    var hangul = out.join(' ');
    var note = kind === 'kana' || romajiUsed ? UI.kana : kind === 'han' ? UI.hanja : approx ? UI.approx : UI.checked;
    var sounds = [[kind === 'han' ? UI.reading : UI.lKo, hangul]];
    var r = { hangul: hangul, kind: kind, note: note, approx: approx, sounds: sounds, firstKey: firstKey };
    if (kind === 'latin') {
      var all = infos.length === latinCount && infos.length && !infos.some(function (x) { return x.alias; });
      if (all) { sounds.push([UI.lJa, infos.map(function (x) { return x.e.ja; }).join('・')]); sounds.push([UI.lZh, infos.map(function (x) { return x.e.zh; }).join('·')]); }
      var main = infos.filter(function (x) { return x.e.m; })[0];
      if (main) { r.meaning = main; r.chain = main.e.ch; } else r.noMeaning = true;
    }
    if (kind === 'kana' || romajiUsed) sounds.push([UI.lJa, words.join(' ')]);
    if (kind === 'han') {
      var K = window.NADRI_KANJI || {}, KCH = window.NADRI_KANJI_CHAIN || {};
      r.chars = s.replace(/ /g, '').split('').map(function (c) {
        var n = c.charCodeAt(0), rd = n >= 0x4E00 && n <= 0x9FFF && window.HANJA_KO ? window.HANJA_KO[n - 0x4E00] : '';
        return { c: c, read: rd === '·' ? '' : rd, ko: K[c] && K[c].ko, en: K[c] && K[c].en };
      });
      r.chars.forEach(function (x) { if (!r.chain && KCH[x.c]) r.chain = KCH[x.c]; });
    }
    return r;
  }

  /* ---------- seal (dojang) as SVG ---------- */
  function sealSVG(name) {
    var chars = name.replace(/ /g, '').split('');
    var cols = chars.length <= 2 ? 1 : chars.length <= 4 ? 2 : 3;
    var rows = Math.ceil(chars.length / cols);
    // fill an empty cell with 인 (印, 'seal'), as Korean name seals do for three-letter names
    if (chars.length < cols * rows) chars.push('인');
    var n = chars.length, size = 240, pad = 22, inner = size - pad * 2;
    // traditional reading order: right column first, top to bottom
    var cw = inner / cols, ch = inner / rows, fs = Math.min(cw, ch) * 0.86, txt = '';
    for (var i = 0; i < n; i++) {
      var col = cols - 1 - Math.floor(i / rows), row = i % rows;
      var x = pad + cw * col + cw / 2, y = pad + ch * row + ch / 2 + fs * 0.34;
      txt += '<text x="' + x.toFixed(1) + '" y="' + y.toFixed(1) + '" font-size="' + fs.toFixed(1) + '" text-anchor="middle">' + chars[i] + '</text>';
    }
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + size + ' ' + size + '" width="' + size + '" height="' + size + '" role="img" aria-label="' + name + '">' +
      '<rect x="6" y="6" width="' + (size - 12) + '" height="' + (size - 12) + '" rx="14" fill="#b3261e"/>' +
      '<rect x="14" y="14" width="' + (size - 28) + '" height="' + (size - 28) + '" rx="8" fill="none" stroke="#f4f0e6" stroke-width="3"/>' +
      '<g fill="#f4f0e6" font-family="Song Myung, serif">' + txt + '</g></svg>';
  }

  /* ---------- UI (many languages) ---------- */
  var I18N = window.NADRI_I18N || {}, SITE2UI = { en: 'en', ko: 'ko', ja: 'ja', 'zh-tw': 'zh-TW' };
  var params = new URLSearchParams(location.search);
  var uiLang = params.get('hl');
  if (!uiLang || !I18N[uiLang]) {
    uiLang = SITE2UI[LANG];
    // a visitor whose browser speaks another language we support gets that language on the English page
    var nav = (navigator.language || '').toLowerCase();
    if (LANG === 'en') Object.keys(I18N).forEach(function (k) { if (k !== 'en' && nav.indexOf(k.toLowerCase().slice(0, 2)) === 0 && ['ko', 'ja', 'zh-TW', 'zh-CN'].indexOf(k) < 0) uiLang = k; });
  }
  var T;
  function applyLang(l) {
    uiLang = l;
    var base = I18N.en, t = I18N[l] || base;
    T = {}; Object.keys(base).forEach(function (k) { T[k] = t[k] !== undefined ? t[k] : base[k]; });
    var site = { ko: 'ko', ja: 'ja', 'zh-TW': 'zh-tw' }[l] || 'en';
    UI = Object.assign({}, UI_ALL[site], { lKo: T.ko, lJa: T.ja, lZh: T.zh, roman: T.roman + ' (RR)', approx: T.approx, empty: T.empty, none: T.none, privacy: T.privacy });
    root.setAttribute('dir', t._rtl ? 'rtl' : 'ltr');
  }
  applyLang(uiLang);
  var L3 = function () { return uiLang === 'ko' ? 'ko' : uiLang === 'ja' ? 'ja' : (uiLang === 'zh-TW' || uiLang === 'zh-CN') ? 'zh' : 'en'; };
  var esc = function (t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var MAIL = 'gibyeol.official@gmail.com';
  function mail(subject, label) { return '<a href="mailto:' + MAIL + '?subject=' + encodeURIComponent(subject) + '">' + label + '</a>'; }

  function shell() {
    var opts = Object.keys(I18N).map(function (k) { return '<option value="' + k + '"' + (k === uiLang ? ' selected' : '') + '>' + I18N[k]._n + '</option>'; }).join('');
    root.innerHTML =
      '<div class="namer-langbar"><label>' + T.lang + ' <select class="namer-lang">' + opts + '</select></label></div>' +
      '<form class="namer-form"><label class="vh" for="namer-in">' + T.ph + '</label>' +
      '<input id="namer-in" type="text" autocomplete="off" maxlength="40" placeholder="' + esc(T.ph) + '">' +
      '<button type="submit">' + T.go + '</button></form>' +
      '<p class="namer-privacy">' + T.privacy + '</p><div class="namer-out" aria-live="polite"></div>';
    input = root.querySelector('input'); out = root.querySelector('.namer-out');
    root.querySelector('form').addEventListener('submit', function (e) { e.preventDefault(); render(input.value); });
    root.querySelector('.namer-lang').addEventListener('change', function (e) {
      var v = input.value; applyLang(e.target.value); shell(); input.value = v; if (v) render(v);
    });
  }
  var input, out;

  function lname(en) { var m = window.NADRI_LNAMES && window.NADRI_LNAMES[en], k = L3(); return m && m[k] ? m[k] : en; }
  function rname(en) { var m = window.NADRI_RNAMES && window.NADRI_RNAMES[en], k = L3(); return m && m[k] ? m[k] : en; }
  var LANG_ORDER = ['Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Russian', 'Polish', 'Dutch', 'Greek', 'Arabic', 'Hebrew', 'Turkish', 'Persian', 'Hungarian', 'Finnish', 'Czech', 'Irish', 'Catalan', 'Croatian', 'Danish', 'Norwegian', 'Swedish', 'Icelandic', 'Ukrainian', 'Bulgarian', 'Romanian', 'Georgian', 'Armenian', 'Indonesian', 'Swahili', 'Hawaiian', 'Māori'];

  function render(name) {
    var r = convert(name);
    if (!r) { out.innerHTML = '<p>' + T.empty + '</p>'; return; }
    if (r.error) { out.innerHTML = '<p>' + T.none + '</p>'; return; }
    var k3 = L3(), pre = { ko: '/ko', ja: '/ja', zh: '/zh-tw' }[k3] || '';
    var key = r.meaning ? r.meaning.key : (r.firstKey || null);
    var B = (window.NADRI_BTN || {})[r.firstKey] || (key && (window.NADRI_BTN || {})[key]) || null;
    var h = '';
    // 1. sound
    h += '<h3 class="namer-h">' + T.sound + '</h3>' + r.sounds.map(function (l) {
      var back = '';
      if (L3() === 'ko' && r.kind !== 'kana') {
        if (/[\u30A0-\u30FF]/.test(l[1])) back = l[1].split(/[・\s]/).map(function (w) { return kanaWord(w) || ''; }).join(' ').trim();
        else if (/[\u0400-\u04FF]/.test(l[1])) back = cyrToHangul(l[1]);
      }
      return '<div class="namer-line"><span>' + l[0] + '</span><strong>' + esc(l[1]) + (back ? '<span class="namer-kr">' + esc(back) + '</span>' : '') + '</strong></div>'; }).join('');
    // 2. meaning
    if (r.meaning || B) {
      var e = r.meaning ? r.meaning.e : {}, conf = e.c || 'h';
      var local = e.m && e.m[k3] && k3 !== 'en' ? e.m[k3] : null;
      var root2 = r.meaning && r.meaning.alias ? ' · ' + esc(name.trim().split(' ')[0]) + ' → ' + esc(r.meaning.key.charAt(0).toUpperCase() + r.meaning.key.slice(1)) : '';
      h += '<h3 class="namer-h">' + T.meaning + root2 + ' <span class="namer-conf c-' + conf + '">' + T.conf[conf] + '</span></h3>';
      if (local) h += '<p class="namer-mean">' + esc(local) + '</p>';
      if (B) h += '<p class="' + (local ? 'namer-sub' : 'namer-mean') + '">' + esc(B.meaning) + ' <span class="namer-origin">(' + esc(B.origin) + ')</span></p>';
      else if (e.m) h += '<p class="namer-mean">' + esc(e.m.en) + '</p>';
      if (e.w) h += '<p class="namer-sub"><span>' + T.meaning + ' · 한국어 / 日本語 / 中文</span> ' + esc(e.w.ko) + ' / ' + esc(e.w.ja) + ' / ' + esc(e.w.zh) + '</p>';
      if (e.i) h += '<p class="namer-sub"><span>' + T.idea + '</span> <strong>' + esc(e.i.ko) + '</strong> · ' + esc(e.i.ja) + ' · ' + esc(e.i.zh) + '</p>';
      h += '<p class="namer-src">' + T.src + ': <a href="https://www.behindthename.com/name/' + encodeURIComponent(r.firstKey || key) + '" rel="noopener" target="_blank">Behind the Name</a></p>';
    } else if (r.kind === 'latin') {
      h += '<h3 class="namer-h">' + T.meaning + '</h3><p class="namer-sub">' + mail('Nadri name meaning: ' + name, T.native) + '</p>';
    }
    if (r.chars) {
      h += '<h3 class="namer-h">' + T.meaning + ' · ' + T.chars + '</h3><ul class="namer-chars">' + r.chars.map(function (x) {
        return '<li><b>' + esc(x.c) + '</b> ' + (x.ko ? esc(x.ko) + ' ' : '') + esc(x.read || '') + (x.en ? ' <i>' + esc(x.en) + '</i>' : '') + '</li>';
      }).join('') + '</ul>';
    }
    var seal = r.hangul.replace(/ /g, '').length <= 9 ? sealSVG(esc(r.hangul)) : '';
    var card = '<div class="namer-card"><div class="namer-seal">' + seal + '</div><div class="namer-text">' + h +
      (r.approx || !r.meaning ? '<p class="namer-note' + (r.approx ? ' approx' : '') + '">' + (r.approx ? T.approx : r.note) + '</p>' : '') +
      '<p class="namer-actions"><button type="button" class="namer-cardbtn">' + (SHARE_FILES ? T.cardShare : T.cardSave) + '</button> <button type="button" class="namer-share">' + T.share + '</button></p>' +
      '<p class="namer-wrong">' + mail('Nadri name: ' + name, T.wrong) + '</p></div></div>';
    // 3. your name in other countries
    var more = '';
    if (B && B.variants && Object.keys(B.variants).length) {
      var langs = Object.keys(B.variants).filter(function (lg) { return !/^(Biblical|Medieval|Ancient|Germanic|Late Roman|Old )/.test(lg) && lg.indexOf('(') < 0; }).sort(function (a, b) { var ia = LANG_ORDER.indexOf(a), ib = LANG_ORDER.indexOf(b); return (ia < 0 ? 99 : ia) - (ib < 0 ? 99 : ib); });
      more += '<section class="namer-sec"><h3 class="namer-h">' + T.variants + '</h3><ul class="namer-var">' + langs.map(function (lg) {
        return '<li><span>' + esc(lname(lg)) + '</span><b>' + B.variants[lg].slice(0, 3).map(function (f) { return esc(f) + kr(f, lg); }).join(' · ') + '</b></li>';
      }).slice(0, 18).join('') + '</ul><p class="namer-src">' + T.src + ': Behind the Name · ' + mail('Nadri name in my language: ' + name, T.native) + '</p></section>';
    }
    // 4. where it is most loved
    if (B && B.top && B.top.length) {
      more += '<section class="namer-sec"><h3 class="namer-h">' + T.popular + '</h3><ol class="namer-top">' + B.top.slice().sort(function (a, b) { return a[2] - b[2] || b[1] - a[1]; }).map(function (t) {
        return '<li><span>' + esc(rname(t[0])) + '</span><b>' + T.rank.replace('{r}', t[2]).replace('{y}', t[1]) + '</b></li>';
      }).join('') + '</ol><p class="namer-src">' + T.popularNote + '</p></section>';
    }
    var bornL = r.kind === 'latin' && key && ((window.NADRI_BORN_OF || {}).latin || {})[key];
    if (bornL) { r.born = { id: bornL }; more = bornBlock(r.born) + more; }
    if (r.chars) { r.born = bornFromHanja(r.chars.map(function (x) { return x.c; })); if (r.born) more = bornBlock(r.born) + more; }
    var latinConcept = r.kind === 'latin' && key && ((window.NADRI_CONCEPT_OF || {}).latin || {})[key];
    var WD = window.NADRI_WORLD || {};
    if (latinConcept) more += conceptBlock(latinConcept, { noChain: !!(r.chain) || !!WD[latinConcept] });
    // Korean names: surname count, baby-name rank, hanja picker, native meaning
    if (r.kind === 'hangul' && r.ko) more += koSections(r);
    var cids = r.chars ? conceptsForHanja(r.chars.map(function (x) { return x.c; })) : [];
    cids.forEach(function (id, i) { more += conceptBlock(id, { noChain: (i > 0 && !!r.chain) || !!WD[id] }); });
    // 5. where the meaning leads around the world: many regions, Korea one of them (its chain keeps the links to our guides)
    var wids = [];
    if (latinConcept && WD[latinConcept]) wids.push(latinConcept);
    cids.forEach(function (id) { if (WD[id] && wids.indexOf(id) < 0) wids.push(id); });
    if (!wids.length && r.chain && WD[r.chain]) wids.push(r.chain);
    var krChain = r.kind === 'latin' ? r.chain : null;
    r.typed = name; r.btn = B; r.krChain = krChain; r.cids = cids; r.concept = latinConcept || cids[0] || null;
    if (cids.length) r.chain = null;
    if (wids.length) {
      r.worldId = wids[0];
      if (!r.born) more = worldBornBlock(wids[0]) + more;
      wids.slice(0, 2).forEach(function (id, i) { more += worldBlock(id, i === 0 ? krChain : null, name); });
    }
    // Korea-only chain (meanings we have not mapped worldwide yet), with the slot for travellers' lines and the next name
    var steps = !wids.length && r.chain && window.NADRI_CHAINS && window.NADRI_CHAINS[r.chain];
    if (steps) {
      more += '<section class="namer-sec namer-chain"><h3 class="namer-h">' + T.chain + '</h3><ol>' + steps.map(function (st) {
        return '<li>' + esc(st[k3] || st.en) + (st.link ? ' <a href="' + pre + st.link + '">→</a>' : '') +
          '<span class="namer-step"><span class="namer-conf c-' + st.c + '">' + T.conf[st.c] + '</span> ' + T.src + ': ' + esc(st.s) + '</span></li>';
      }).join('') + '</ol><div class="namer-oneline"><b>' + T.oneLine + '</b><p>' + mail('Nadri one line: ' + r.chain, T.oneLineEmpty) + '</p></div></section>';
    }
    var rel = (window.NADRI_RELATED || {})[key] || (window.NADRI_RELATED || {})[r.firstKey];
    if (rel) more += '<p class="namer-next"><span>' + T.related + '</span> ' + rel.map(function (n) { return '<button type="button" data-n="' + n + '">' + n.charAt(0).toUpperCase() + n.slice(1) + '</button>'; }).join(' ') + '</p>';
    out.innerHTML = card + more;
    prepareCard(r);
    out.querySelector('.namer-cardbtn').onclick = cardClick;
    out.querySelector('.namer-share').onclick = function (ev) {
      var url = location.origin + location.pathname + '?n=' + encodeURIComponent(name) + (uiLang !== SITE2UI[LANG] ? '&hl=' + uiLang : '');
      (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { ev.target.textContent = T.copied; }, function () { prompt('', url); });
    };
    wireGo(); if (r.kind === 'hangul') wireHanja(r);
  }




  function kr(form, lang) {
    if (L3() !== 'ko' || !form || /[가-힣]/.test(form)) return '';
    var r = window.nadriKoRead ? window.nadriKoRead(form, lang) : '';
    return r ? '<span class="namer-kr">' + esc(r) + '</span>' : '';
  }
  /* Cyrillic back to Hangul, so Korean readers can say it */
  var CY2 = { 'б': 'ㅂ', 'в': 'ㅂ', 'г': 'ㄱ', 'д': 'ㄷ', 'ж': 'ㅈ', 'з': 'ㅈ', 'к': 'ㅋ', 'л': 'ㄹ', 'м': 'ㅁ', 'н': 'ㄴ', 'п': 'ㅍ', 'р': 'ㄹ', 'с': 'ㅅ', 'т': 'ㅌ', 'ф': 'ㅍ', 'х': 'ㅎ', 'ц': 'ㅊ', 'ч': 'ㅊ', 'ш': 'ㅅ', 'щ': 'ㅅ' };
  var CYV2 = { 'а': 'ㅏ', 'е': 'ㅔ', 'ё': 'ㅛ', 'и': 'ㅣ', 'о': 'ㅗ', 'у': 'ㅜ', 'ы': 'ㅡ', 'э': 'ㅔ', 'ю': 'ㅠ', 'я': 'ㅑ' };
  function cyrToHangul(w) {
    w = w.toLowerCase().replace(/ь/g, '').replace(/й/g, 'и');
    var out = '', i = 0;
    while (i < w.length) {
      var c = w[i], n = w[i + 1];
      if (c === ' ') { out += ' '; i++; continue; }
      if (CYV2[c]) { out += syl('ㅇ', CYV2[c]); i++; continue; }
      if (CY2[c] && n && CYV2[n]) { out += syl(CY2[c], CYV2[n]); i += 2; continue; }
      if (CY2[c]) {
        var last = out[out.length - 1], f = { 'ㄴ': 'ㄴ', 'ㅁ': 'ㅁ', 'ㄹ': 'ㄹ', 'ㅋ': 'ㄱ', 'ㅍ': 'ㅂ' }[CY2[c]];
        if (f && last && isHangul(last) && !split(last)[2] && !(n && CYV2[n])) out = out.slice(0, -1) + addFinal(last, f); else out += syl(CY2[c], 'ㅡ');
        i++; continue;
      }
      i++;
    }
    return out;
  }

  /* "If you were born in…": the localized name per country, why, and how sure we are */
  var BORN_PRI = ['dipper', 'star', 'wisdom', 'peace', 'light'];
  function bornFromHanja(chars) {
    var M = (window.NADRI_BORN_OF || {}).hanja || {}, found = {};
    chars.forEach(function (c) { if (M[c]) found[M[c]] = 1; });
    var id = BORN_PRI.filter(function (b) { return found[b]; })[0];
    return id ? { id: id, first: chars.some(function (c) { return '元一始初首'.indexOf(c) >= 0; }) } : null;
  }
  function bornBlock(b) {
    var B = (window.NADRI_BORN || {})[b.id]; if (!B) return '';
    var k3 = L3(), ph = (b.first && B.first ? B.first : B.phrase);
    var rows = B.c.map(function (c) {
      var country = c[1][k3] || c[1].en, why = c[4][k3 === 'ko' ? 'ko' : 'en'] || c[4].en;
      if (!c[2]) return '<li class="hold"><span class="namer-flag">' + c[0] + '</span><div><b>' + esc(country) + '</b> <small>' + esc(c[3]) + '</small><p>' + esc(why) + ' ' + mail('Nadri born-in: ' + b.id + ' / ' + country, T.native) + '</p></div></li>';
      return '<li><span class="namer-flag">' + c[0] + '</span><div><b>' + esc(country) + ' → ' + esc(c[2]) + kr(c[2]) + '</b>' + (c[3] ? ' <small>' + esc(c[3]) + '</small>' : '') + '<p>' + esc(why) + '</p><span class="namer-pct">' + T.sure + ' ' + c[5] + '%</span></div></li>';
    }).join('');
    return '<section class="namer-sec namer-born"><p class="namer-born-h">' + T.yourNameIs + ' <strong>“' + esc(ph[k3] || ph.en) + '”</strong></p><h3 class="namer-h">' + T.bornIn + '</h3><ul class="namer-born-list">' + rows + '</ul></section>';
  }

  /* one meaning, the names that carry it around the world, and its Korean story */
  function conceptBlock(cid, opts) {
    var C = (window.NADRI_CONCEPTS || {})[cid]; if (!C) return '';
    var k3 = L3(), lab = C[k3] || C.en, pre = { ko: '/ko', ja: '/ja', zh: '/zh-tw' }[k3] || '';
    var h = '<section class="namer-sec namer-concept"><h3 class="namer-h">' + T.koAbroad + ' · ' + esc(lab) + (k3 !== 'en' ? ' (' + esc(C.en) + ')' : '') + '</h3><ul class="namer-var">' +
      C.names.map(function (n) { return '<li><span>' + esc(langLabel(n[0])) + '</span><b>' + esc(n[1]) + (n[2] && /[\uAC00-\uD7A3]/.test(n[2]) ? '' : kr(n[1])) + (n[2] ? ' <small>' + esc(n[2]) + '</small>' : '') + '</b></li>'; }).join('') + '</ul>';
    var steps = C.chain && window.NADRI_CHAINS && window.NADRI_CHAINS[C.chain];
    if (steps && !(opts && opts.noChain)) h += '<h3 class="namer-h">' + T.chain + '</h3><ol class="namer-steps">' + steps.map(function (st) { return '<li>' + esc(st[k3] || st.en) + (st.link ? ' <a href="' + pre + st.link + '">→</a>' : '') + '<span class="namer-step"><span class="namer-conf c-' + st.c + '">' + T.conf[st.c] + '</span> ' + T.src + ': ' + esc(st.s) + '</span></li>'; }).join('') + '</ol>';
    return h + '</section>';
  }
  function conceptsForHanja(chars) {
    var CO = (window.NADRI_CONCEPT_OF || {}).hanja || {}, seen = {}, ids = [];
    chars.forEach(function (c) { var id = CO[c]; if (id && !seen[id]) { seen[id] = 1; ids.push(id); } });
    return ids;
  }

  /* the meaning around the world: one checked story or place per region, each with its source; Korea is one region */
  function regionOf(code) { var R = (window.NADRI_REGIONS || {})[code] || ['', { en: code }], k3 = L3(); return { flag: R[0], name: R[1][k3] || R[1].en }; }
  function worldName(e) {
    if (!e.n) return '';
    return ' → ' + esc(e.n) + (L3() === 'ko' && e.nk ? '<span class="namer-kr">' + esc(e.nk) + '</span>' : '');
  }
  function srcLine(e) {
    return '<span class="namer-step"><span class="namer-conf c-' + e.c + '">' + (T.conf[e.c] || e.c) + '</span> ' + T.src + ': ' +
      e.s.map(function (x) { return '<a href="' + esc(x[1]) + '" rel="noopener" target="_blank">' + esc(x[0]) + '</a>'; }).join(' · ') +
      ' · ' + esc(T.opened.replace('{d}', e.d)) + '</span>';
  }
  function chainSteps(id) {
    var steps = window.NADRI_CHAINS && window.NADRI_CHAINS[id]; if (!steps) return '';
    var k3 = L3(), pre = { ko: '/ko', ja: '/ja', zh: '/zh-tw' }[k3] || '';
    // inside the world list (flex rows), keep each step a plain list item
    return '<ol class="namer-steps">' + steps.map(function (st) { return '<li style="display:list-item;border:0;padding:4px 0">' + esc(st[k3] || st.en) + (st.link ? ' <a href="' + pre + st.link + '">→</a>' : '') + '<span class="namer-step"><span class="namer-conf c-' + st.c + '">' + T.conf[st.c] + '</span> ' + T.src + ': ' + esc(st.s) + '</span></li>'; }).join('') + '</ol>';
  }
  function worldBlock(wid, krChain, typed) {
    var W = (window.NADRI_WORLD || {})[wid]; if (!W) return '';
    var k3 = L3(), pre = { ko: '/ko', ja: '/ja', zh: '/zh-tw' }[k3] || '', C = (window.NADRI_CONCEPTS || {})[wid];
    var list = W.slice();
    if (krChain && !list.some(function (e) { return e.r === 'KR'; })) list.push({ r: 'KR', chain: krChain });
    // Korea first (owner 2026-11-26 11:14: "한국부분이 가장 먼저 눈에 보이게 위로 올려")
    list.sort(function (a, b) { return (a.r === 'KR' ? 0 : 1) - (b.r === 'KR' ? 0 : 1); });
    var rows = list.map(function (e) {
      var rg = regionOf(e.r), body;
      if (e.chain) body = chainSteps(e.r === 'KR' && krChain ? krChain : e.chain);
      else body = '<p>' + esc(e[k3] || e.en) + (e.link ? ' <a href="' + pre + e.link + '">→</a>' : '') + '</p>' + srcLine(e);
      return '<li data-r="' + e.r + '"><span class="namer-flag">' + rg.flag + '</span><div><b>' + esc(rg.name) + worldName(e) + '</b>' + (e.nn ? ' <small>' + esc(e.nn) + '</small>' : '') + body + '</div></li>';
    }).join('');
    var lab = C ? ' · ' + esc(C[k3] || C.en) : '';
    return '<section class="namer-sec namer-chain namer-world"><h3 class="namer-h">' + T.world + lab + '</h3><ul class="namer-born-list">' + rows + '</ul>' +
      '<p class="namer-src">' + mail('Nadri world chain: ' + wid + ' / ' + (typed || ''), T.native) + '</p>' +
      '<div class="namer-oneline"><b>' + T.oneLine + '</b><p>' + mail('Nadri one line: ' + wid, T.oneLineEmpty) + '</p></div></section>';
  }
  /* "If you were born in…" built from the world entries that carry a name (used where no older born-in list exists) */
  function worldBornBlock(wid) {
    var W = (window.NADRI_WORLD || {})[wid], C = (window.NADRI_CONCEPTS || {})[wid]; if (!W) return '';
    var named = W.filter(function (e) { return e.n; }); if (!named.length) return '';
    var k3 = L3(), lab = C ? (C[k3] || C.en) : (named[0].n);
    var rows = named.slice(0, 6).map(function (e) {
      var rg = regionOf(e.r);
      return '<li><span class="namer-flag">' + rg.flag + '</span><div><b>' + esc(rg.name) + worldName(e) + '</b>' + (e.nn ? ' <small>' + esc(e.nn) + '</small>' : '') + '<p>' + esc(e.g[k3] || e.g.en) + '</p><span class="namer-conf c-' + e.c + '">' + (T.conf[e.c] || e.c) + '</span></div></li>';
    }).join('');
    return '<section class="namer-sec namer-born"><p class="namer-born-h">' + T.yourNameIs + ' <strong>“' + esc(lab) + '”</strong></p><h3 class="namer-h">' + T.bornIn + '</h3><ul class="namer-born-list">' + rows + '</ul></section>';
  }

  function abroadFor(meanings) {
    var M = window.KO_MEANING_TO_NAME || {}, N = window.NADRI_NAMES || {}, seen = {}, out = [];
    meanings.forEach(function (m) { (M[(m || '').toLowerCase()] || []).forEach(function (k) { if (!seen[k] && N[k] && typeof N[k] === 'object') { seen[k] = 1; out.push(k); } }); });
    if (!out.length) return '';
    var k3 = L3();
    return '<ul class="namer-var">' + out.map(function (k) { var e = N[k]; return '<li><span>' + esc((e.m && (e.m[k3] || e.m.en)) || '') + '</span><b><button type="button" class="namer-go" data-n="' + k + '">' + k.charAt(0).toUpperCase() + k.slice(1) + '</button></b></li>'; }).join('') + '</ul>';
  }
  function koSections(r) {
    var K = r.ko, h = '', k3 = L3(), fmt = function (n) { return Number(n).toLocaleString(); };
    var POP = window.KO_SURNAME_POP || {}, TOT = window.KO_SURNAME_TOTAL || 5582;
    if (K.sur) {
      var sh = (window.KO_SURNAME_HANJA || {})[K.sur], hun = sh && (window.KO_SURNAME_HUN || {})[sh];
      h += '<section class="namer-sec"><h3 class="namer-h">' + T.koSurname + ' · ' + esc(K.sur) + (sh ? ' ' + sh : '') + '</h3>';
      if (hun) h += '<p class="namer-mean">' + sh + ' <span class="namer-origin">' + esc(hun[0]) + ' ' + esc(K.sur) + ' · ' + esc(hun[1]) + '</span></p>';
      h += '<p class="namer-sub">' + (POP[K.sur] ? T.koPop.replace('{n}', fmt(POP[K.sur])).replace('{p}', (POP[K.sur] / 510694).toFixed(1)).replace('{t}', fmt(TOT)) : T.koPopOther.replace('{t}', fmt(TOT))) + '</p></section>';
    }
    var B = window.KO_BABY_2025 || { boys: [], girls: [] }, bi = B.boys.indexOf(K.given), gi = B.girls.indexOf(K.given);
    h += '<section class="namer-sec"><h3 class="namer-h">' + T.koBaby + ' · ' + esc(K.given) + '</h3><p class="namer-sub">' +
      (bi >= 0 ? T.koBabyRank.replace('{r}', bi + 1).replace('{g}', T.boys) + ' ' : '') + (gi >= 0 ? T.koBabyRank.replace('{r}', gi + 1).replace('{g}', T.girls) : '') + (bi < 0 && gi < 0 ? T.koBabyNone : '') + '</p>';
    var nat = (window.KO_NATIVE || {})[K.given];
    if (nat) h += '<p class="namer-sub"><span>' + T.koNative + '</span> <strong>' + esc(k3 === 'ko' ? nat[0] : nat[1]) + '</strong></p>' + abroadFor([nat[1]]);
    var bornN = ((window.NADRI_BORN_OF || {}).native || {})[K.given]; if (bornN) { r.born = { id: bornN }; h = bornBlock(r.born) + h; }
    h += '<p class="namer-src">' + T.src + ': ' + T.srcKo + '</p></section>';
    // hanja picker for each syllable of the given name
    var H = window.KO_NAME_HANJA || {}, sy = K.given.split('');
    var rows = sy.map(function (c, i) {
      var opts = H[c] || [];
      if (!opts.length) return '<div class="namer-pick"><b>' + esc(c) + '</b> <span class="namer-origin">—</span></div>';
      return '<div class="namer-pick" data-i="' + i + '"><b>' + esc(c) + '</b> ' + opts.map(function (o) { return '<button type="button" data-h="' + o[0] + '" data-hun="' + esc(o[1]) + '" data-en="' + esc(o[2]) + '">' + o[0] + ' <small>' + esc(o[1]) + '</small></button>'; }).join('') + '</div>';
    }).join('');
    return '<section class="namer-sec namer-hanja"><h3 class="namer-h">' + T.koHanja + '</h3><p class="namer-sub">' + T.koHanjaHint + '</p>' + rows + '<div class="namer-hanja-out"></div></section>' + h;
  }
  function wireHanja(r) {
    var box = out.querySelector('.namer-hanja'); if (!box) return;
    var picked = {};
    Array.prototype.forEach.call(box.querySelectorAll('.namer-pick button'), function (b) {
      b.onclick = function () {
        var row = b.parentNode, i = row.getAttribute('data-i');
        Array.prototype.forEach.call(row.querySelectorAll('button'), function (x) { x.classList.remove('on'); });
        b.classList.add('on'); picked[i] = { h: b.getAttribute('data-h'), hun: b.getAttribute('data-hun'), en: b.getAttribute('data-en') };
        var list = Object.keys(picked).sort().map(function (k) { return picked[k]; });
        var sh = (window.KO_SURNAME_HANJA || {})[r.ko.sur] || '';
        var name = sh + list.map(function (x) { return x.h; }).join('');
        var o = '<p class="namer-mean">' + esc(name) + '</p><p class="namer-sub">' + list.map(function (x) { return '<b>' + x.h + '</b> ' + esc(x.hun) + ' · ' + esc(x.en); }).join(' / ') + '</p>';
        var ids = conceptsForHanja(list.map(function (x) { return x.h; })), CC = window.NADRI_CONCEPTS || {}, k3 = L3();
        r.born = bornFromHanja(list.map(function (x) { return x.h; })); r.pickedName = name; r.picked = list; r.pickedIds = ids;
        var WD = window.NADRI_WORLD || {}, wids = ids.filter(function (id) { return WD[id]; });
        r.worldId = wids[0] || null;
        if (r.born) o += bornBlock(r.born); else if (wids.length) o += worldBornBlock(wids[0]);
        if (ids.length) o += '<p class="namer-gloss">' + ids.map(function (id) { return esc(CC[id][k3] || CC[id].en); }).join(' + ') + (k3 !== 'en' ? ' <span class="namer-origin">(' + ids.map(function (id) { return esc(CC[id].en); }).join(' + ') + ')</span>' : '') + '</p>';
        ids.forEach(function (id) { o += conceptBlock(id, { noChain: !!WD[id] }); });
        wids.slice(0, 2).forEach(function (id) { o += worldBlock(id, null, name); });
        if (!ids.length) { var ab = abroadFor(list.map(function (x) { return x.en; })); if (ab) o += '<h3 class="namer-h">' + T.koAbroad + '</h3>' + ab; }
        box.querySelector('.namer-hanja-out').innerHTML = o;
        wireGo(); prepareCard(r);
      };
    });
  }
  function wireGo() {
    Array.prototype.forEach.call(out.querySelectorAll('.namer-go, .namer-next button'), function (b) { b.onclick = function () { input.value = b.getAttribute('data-n'); render(input.value); root.scrollIntoView({ behavior: 'smooth' }); }; });
  }

  /* ---------- share card ----------
     Owner 2026-11-26 [7eb4ec94#2276]: the card is built on the results below the stamp, compact and clean (replaces the stamp card in
     ops/name-tool.md appendix). One 1080x1350 PNG (Instagram feed/stories, Threads), drawn on this device; nothing is sent.
     Layout: [meaning photo band, optional] tag + small seal / name (hero) / "Your name means …" + confidence /
     Korean·Japanese·Chinese / same meaning in other countries / where it leads / sources / Nadri + address.
     Meaning photo (owner [7eb4ec94#2296]): window.NADRI_MEANING_IMG[conceptId] = { src, credit }; same-origin files only, so nothing
     leaves the site and the canvas can still be saved. No photo: the card starts with the tag line. Only sections with data are drawn. */
  var CW = 1080, CH = 1350, CM = 84, CIN = CW - CM * 2;
  var C_PAPER = '#f4f0e6', C_INK = '#16151a', C_MUTED = '#5f5b55', C_HAIR = '#ddd6c8', C_RED = '#b8392f';
  var F_HEAD = '"Song Myung", "Noto Serif KR", serif', F_TEXT = '"IBM Plex Sans KR", system-ui, -apple-system, "Segoe UI", "Noto Sans KR", sans-serif', F_MONO = '"IBM Plex Mono", ui-monospace, monospace';
  function cfont(kind, size, weight) { return (weight ? weight + ' ' : '') + Math.round(size) + 'px ' + (kind === 'head' ? F_HEAD : kind === 'mono' ? F_MONO : F_TEXT); }
  function langLabel(l) {
    var k3 = L3();
    return l.split(' / ').map(function (x) { var m = window.NADRI_LNAMES && window.NADRI_LNAMES[x]; var extra = { Latin: { ko: '라틴어', ja: 'ラテン語', zh: '拉丁文' }, Sanskrit: { ko: '산스크리트어', ja: 'サンスクリット語', zh: '梵文' }, Hindi: { ko: '힌디어', ja: 'ヒンディー語', zh: '印地文' }, Welsh: { ko: '웨일스어', ja: 'ウェールズ語', zh: '威爾斯文' }, Japanese: { ko: '일본어', ja: '日本語', zh: '日文' }, Chinese: { ko: '중국어', ja: '中国語', zh: '中文' }, Korean: { ko: '한국어', ja: '韓国語', zh: '韓文' }, Slavic: { ko: '슬라브어', ja: 'スラブ語', zh: '斯拉夫語' }, English: { ko: '영어', ja: '英語', zh: '英文' }, Germanic: { ko: '게르만어', ja: 'ゲルマン語', zh: '日耳曼語' } }[x]; return (m && m[k3]) || (extra && extra[k3]) || x; }).join(' · ');
  }

  /* what goes on the card: only what the page shows for this name, with the page's confidence labels */
  function cardModel(r) {
    var k3 = L3(), typed = String(r.typed || '').trim().replace(/\s+/g, ' ');
    var m = { hero: r.kind === 'hangul' ? r.hangul : typed, scripts: [], meaning: null, same: [], lead: null, facts: [], concept: null };
    var low = function (x) { return String(x || '').toLowerCase(); };
    // 1. the name in Korean / Japanese / Chinese (Taiwan), as the page shows it (Russian stays on the page)
    r.sounds.forEach(function (l) {
      if (!l[1] || l[1] === m.hero || /[Ѐ-ӿ]/.test(l[1])) return;
      // a Korean reading guessed from the spelling keeps the page's 'approximate' mark
      m.scripts.push({ label: l[0] + (r.approx && l[0] === UI.lKo ? ' (' + UI.kanaApprox + ')' : ''), lines: String(l[1]).split(' · ') });
    });
    if (r.pickedName) m.scripts.push({ label: T.koHanja, lines: [r.pickedName] });
    // 2. meaning
    var e = r.meaning && r.meaning.e, B = r.btn, CC = window.NADRI_CONCEPTS || {};
    var clabel = function (id) { return CC[id] ? (CC[id][k3] || CC[id].en) : ''; };
    if (e && e.m) {
      m.meaning = { word: (k3 !== 'en' && e.m[k3]) || e.m.en, conf: T.conf[e.c || 'h'], root: r.meaning.alias ? cap(r.meaning.key) : '', src: 'Behind the Name' };
    } else if (r.kind === 'latin' && B && B.meaning) {
      m.meaning = { word: B.meaning, conf: T.conf.h, long: true, src: 'Behind the Name' };
    } else if (r.kind === 'han' && r.chars) {
      var ids = (r.cids || []).filter(function (id) { return CC[id]; });
      var parts = r.chars.filter(function (x) { return x.ko || x.en; }).map(function (x) { return x.c + ' ' + (k3 === 'ko' && x.ko ? x.ko + ' ' + (x.read || '') : (x.en || x.ko)); });
      if (ids.length) m.meaning = { word: ids.map(clabel).join(' + '), detail: parts.join(' · ') };
      else if (parts.length) m.meaning = { word: parts.join(' · '), long: true };
    } else if (r.kind === 'hangul' && r.picked && r.picked.length) {
      var pids = (r.pickedIds || []).filter(function (id) { return CC[id]; });
      var pparts = r.picked.map(function (x) { return x.h + ' ' + (k3 === 'ko' ? x.hun : x.en); });
      m.meaning = pids.length ? { word: pids.map(clabel).join(' + '), detail: pparts.join(' · ') } : { word: pparts.join(' · '), long: true };
    } else if (r.kind === 'hangul' && r.ko) {
      var nat = (window.KO_NATIVE || {})[r.ko.given];
      if (nat) m.meaning = { word: k3 === 'ko' ? nat[0] : nat[1], label: T.koNative };
    }
    m.concept = r.concept || (r.pickedIds && r.pickedIds[0]) || r.worldId || (r.born && r.born.id) || null;
    // 3. the same meaning as a real name elsewhere: checked world entries first (they carry sources), then the older born-in list, then concept names
    var W = r.worldId && (window.NADRI_WORLD || {})[r.worldId];
    if (W) {
      var named = W.filter(function (x) { return x.n && low(x.n) !== low(m.hero) && low(x.n) !== low(typed); });
      named = named.filter(function (x) { return x.c === 'h'; }).concat(named.filter(function (x) { return x.c !== 'h'; }));
      named.slice(0, 4).forEach(function (x) {
        m.same.push({ place: regionOf(x.r).name, name: x.n, sub: [x.nn, k3 === 'ko' ? x.nk : ''].filter(Boolean).join(' · '), conf: T.conf[x.c] || x.c, src: x.s && x.s[0] && x.s[0][0] });
      });
    }
    var BB = !m.same.length && r.born && (window.NADRI_BORN || {})[r.born.id];
    if (BB) BB.c.filter(function (c) { return c[2] && low(c[2]) !== low(m.hero); }).slice(0, 4).forEach(function (c) {
      var rd = k3 === 'ko' && window.nadriKoRead && !/[가-힣]/.test(c[2]) ? window.nadriKoRead(c[2]) : '';
      m.same.push({ place: c[1][k3] || c[1].en, name: c[2], sub: [c[3], rd].filter(Boolean).join(' · '), conf: T.sure + ' ' + c[5] + '%' });
    });
    if (!m.same.length) {
      var cid = [r.concept].concat(r.cids || [], r.pickedIds || []).filter(function (id) { return id && CC[id]; })[0];
      if (cid) CC[cid].names.filter(function (n) { return low(n[1]) !== low(m.hero) && low(n[1]) !== low(typed); }).slice(0, 4).forEach(function (n) {
        m.same.push({ place: langLabel(n[0]), name: n[1], sub: n[2] || '', conf: '' });
        m.sameLabel = T.idea;   // these are languages, not countries
      });
    }
    // 4. where it leads: Korea first (owner 2026-11-26 11:14), one line; a step that leads to one of our guides if the chain has one
    var CHN = window.NADRI_CHAINS || {};
    var fromChain = function (id) {
      var st = CHN[id]; if (!st || !st.length) return null;
      var s0 = st.filter(function (x) { return x.link; })[0] || st[0];
      return { text: s0[k3] || s0.en, conf: T.conf[s0.c] || '', src: s0.s };
    };
    var korea = regionOf('KR').name, lead = null;
    if (W) {
      var KRe = W.filter(function (x) { return x.r === 'KR'; })[0];
      if (KRe) lead = KRe.chain ? fromChain(r.krChain || KRe.chain) : { text: (KRe.g && (KRe.g[k3] || KRe.g.en)) || KRe[k3] || KRe.en, conf: T.conf[KRe.c] || '', src: KRe.s && KRe.s[0] && KRe.s[0][0] };
      else if (r.krChain) lead = fromChain(r.krChain);
      if (lead) lead.place = korea;
      else {
        var g0 = W.filter(function (x) { return x.g; })[0];
        if (g0) lead = { place: regionOf(g0.r).name, text: g0.g[k3] || g0.g.en, conf: T.conf[g0.c] || '', src: g0.s && g0.s[0] && g0.s[0][0] };
      }
    } else if (r.chain) { lead = fromChain(r.chain); if (lead) lead.place = korea; }
    if (lead && lead.text) m.lead = lead;
    // 5. facts the page shows for Korean names (surname count, baby-name rank); for other names only when nothing else is known
    var srcKo = String(T.srcKo || '').split(/;|,(?![^(]*\))/).map(function (x) { return x.trim(); });
    if (r.kind === 'hangul' && r.ko) {
      var POP = window.KO_SURNAME_POP || {}, K = r.ko, fmt = function (n) { return Number(n).toLocaleString(); };
      if (K.sur && POP[K.sur]) { m.facts.push({ label: T.koSurname + ' · ' + K.sur, text: T.koPop.replace('{n}', fmt(POP[K.sur])).replace('{p}', (POP[K.sur] / 510694).toFixed(1)).replace('{t}', fmt(window.KO_SURNAME_TOTAL || 5582)), src: srcKo[0] }); }
      var KB = window.KO_BABY_2025 || { boys: [], girls: [] }, bi = KB.boys.indexOf(K.given), gi = KB.girls.indexOf(K.given);
      if (bi >= 0 || gi >= 0) { m.facts.push({ label: T.koBaby + ' · ' + K.given, text: [bi >= 0 ? T.koBabyRank.replace('{r}', bi + 1).replace('{g}', T.boys) : '', gi >= 0 ? T.koBabyRank.replace('{r}', gi + 1).replace('{g}', T.girls) : ''].filter(Boolean).join(' · '), src: srcKo.slice(1).join(', ') }); }
    } else if (!m.meaning && !m.same.length && B && B.top && B.top.length) {
      var t = B.top.slice().sort(function (a, b) { return a[2] - b[2] || b[1] - a[1]; })[0];
      m.facts.push({ label: T.popular, text: rname(t[0]) + ' · ' + T.rank.replace('{r}', t[2]).replace('{y}', t[1]), src: 'Behind the Name' });
    }
    return m;
  }

  /* text that fits: words (Hangul and Latin) or characters (kana, hanzi) per line */
  function wrapLines(g, text, maxW) {
    var toks = String(text).match(/[぀-ヿ㐀-鿿豈-﫿＀-￯][、。，．！？」』）)]*|\s+|[^\s぀-ヿ㐀-鿿豈-﫿＀-￯]+/g) || [];
    var out = [], line = '', fits = function (x) { return g.measureText(x).width <= maxW; };
    toks.forEach(function (t) {
      if (/^\s+$/.test(t)) { if (line) line += ' '; return; }
      if (fits(line + t)) { line += t; return; }
      if (line.trim()) { out.push(line.trim()); line = ''; }
      if (fits(t)) { line = t; return; }
      Array.from(t).forEach(function (ch) { if (line && !fits(line + ch)) { out.push(line); line = ch; } else line += ch; });
    });
    if (line.trim()) out.push(line.trim());
    return out;
  }
  // largest size (max..min) at which the text fits in maxLines lines; at min it returns all lines (never cut)
  function fitText(g, text, kind, weight, max, min, maxW, maxLines) {
    for (var s = max; s >= min; s -= 2) { g.font = cfont(kind, s, weight); var L = wrapLines(g, text, maxW); if (L.length <= maxLines) return { size: s, lines: L, kind: kind, weight: weight }; }
    g.font = cfont(kind, min, weight); return { size: min, lines: wrapLines(g, text, maxW), kind: kind, weight: weight };
  }
  function drawLines(g, f, x, y, lh, color, align) {
    g.font = cfont(f.kind, f.size, f.weight); g.fillStyle = color; g.textAlign = align || 'left';
    f.lines.forEach(function (l, i) { g.fillText(l, x, y + i * lh); });
    return f.lines.length * lh;
  }
  function chip(g, text, x, y) {   // small outlined label (confidence), baseline y
    g.font = cfont('text', 20, 600); var w = g.measureText(text).width + 18;
    g.strokeStyle = C_MUTED; g.lineWidth = 1.5; rrect(g, x, y - 22, w, 30, 6); g.stroke();
    g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(text, x + 9, y - 1);
    return w;
  }
  function rrect(g, x, y, w, h, r) { g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath(); }
  function smallSeal(g, name, x, y, size) {   // same layout as the page's seal, drawn small as an accent
    var chars = name.replace(/ /g, '').split(''); if (!chars.length || chars.length > 4) return false;
    var cols = chars.length <= 2 ? 1 : 2, rows = Math.ceil(chars.length / cols); if (chars.length < cols * rows) chars.push('인');
    var k = size / 240, pad = 22 * k, inner = size - pad * 2, cw = inner / cols, ch = inner / rows, fs = Math.min(cw, ch) * 0.86;
    g.fillStyle = C_RED; rrect(g, x + 6 * k, y + 6 * k, size - 12 * k, size - 12 * k, 14 * k); g.fill();
    g.strokeStyle = C_PAPER; g.lineWidth = 3 * k; rrect(g, x + 14 * k, y + 14 * k, size - 28 * k, size - 28 * k, 8 * k); g.stroke();
    g.fillStyle = C_PAPER; g.textAlign = 'center'; g.font = cfont('head', fs);
    chars.forEach(function (c, i) { var col = cols - 1 - Math.floor(i / rows), row = i % rows; g.fillText(c, x + pad + cw * col + cw / 2, y + pad + ch * row + ch / 2 + fs * 0.34); });
    return true;
  }
  function cardLabel(g, text, x, y, extra, maxW) {   // section label, baseline y
    var f = fitText(g, text, 'text', 600, 23, 17, maxW || CIN, 1);
    g.font = cfont('text', f.size, 600); g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(f.lines.join(' '), x, y);
    if (extra) chip(g, extra, x + g.measureText(f.lines.join(' ')).width + 14, y);
  }
  /* body sections: each measures itself first, then draws at y; each carries the sources of what it shows */
  function cardBlocks(g, m) {
    var blocks = [];
    if (m.scripts.length) {
      var n = m.scripts.length, gap = 32, colW = (CIN - gap * (n - 1)) / n;
      var fits = m.scripts.map(function (s) { return s.lines.map(function (l) { return fitText(g, l, 'head', 0, 46, 28, colW, 1); }); });
      var asRows = fits.some(function (f) { return f.some(function (x) { return x.lines.length > 1; }); });
      if (asRows) fits = m.scripts.map(function (s) { return s.lines.map(function (l) { return fitText(g, l, 'head', 0, 40, 26, CIN - 260, 2); }); });
      var valH = function (f) { return f.reduce(function (h, x) { return h + x.lines.length * x.size * 1.2; }, 0); };
      var h = asRows ? fits.reduce(function (h2, f) { return h2 + Math.max(36, valH(f)) + 14; }, 0) : 36 + Math.max.apply(null, fits.map(valH));
      blocks.push({ id: 'scripts', h: h, src: [], draw: function (y) {
        if (asRows) {
          m.scripts.forEach(function (s, i) {
            cardLabel(g, s.label, CM, y + 30, null, 250); var yy = y;
            fits[i].forEach(function (f) { yy += drawLines(g, f, CM + 260, yy + f.size, f.size * 1.2, C_INK); });
            y += Math.max(36, valH(fits[i])) + 14;
          });
          return;
        }
        m.scripts.forEach(function (s, i) {
          var x = CM + i * (colW + gap), yy = y + 36;
          cardLabel(g, s.label, x, y + 22, null, colW);
          fits[i].forEach(function (f) { yy += drawLines(g, f, x, yy + f.size, f.size * 1.2, C_INK); });
        });
      } });
    }
    if (m.same.length) {   // one row, three columns: the same grid as the scripts above
      var cols = 3, cw = (CIN - 32 * (cols - 1)) / cols, items = m.same.slice(0, cols);
      var cells = items.map(function (it) {
        g.font = cfont('text', 21, 600); var chipW = it.conf ? g.measureText(it.conf).width + 30 : 0;
        return { place: fitText(g, it.place, 'text', 0, 23, 18, cw - chipW, 2), name: fitText(g, it.name, 'head', 0, 46, 28, cw, 2), sub: it.sub ? fitText(g, it.sub, 'text', 0, 23, 18, cw, 1) : null, conf: it.conf, chipW: chipW };
      });
      var cellH = function (c) { return c.place.lines.length * 30 + 8 + c.name.lines.length * c.name.size * 1.15 + (c.sub ? 32 : 0); };
      var rowH = Math.max.apply(null, cells.map(cellH));
      blocks.push({ id: 'same', h: 40 + rowH, src: items.map(function (x) { return x.src; }), draw: function (y) {
        cardLabel(g, m.sameLabel || T.cardSame, CM, y + 22);
        cells.forEach(function (c, ci) {
          var x = CM + ci * (cw + 32), y2 = y + 40;
          drawLines(g, c.place, x, y2 + 22, 30, C_MUTED);
          if (c.conf) { g.font = cfont('text', c.place.size); chip(g, c.conf, x + g.measureText(c.place.lines[0]).width + 10, y2 + 24); }
          y2 += c.place.lines.length * 30 + 8;
          y2 += drawLines(g, c.name, x, y2 + c.name.size * 0.95, c.name.size * 1.15, C_INK);
          if (c.sub) drawLines(g, c.sub, x, y2 + 24, 26, C_MUTED);
        });
      } });
    }
    if (m.lead) {
      var lf = fitText(g, m.lead.place + ' — ' + m.lead.text, 'text', 0, 30, 24, CIN, 3);
      blocks.push({ id: 'lead', h: 40 + lf.lines.length * lf.size * 1.35, src: [m.lead.src], draw: function (y) {
        cardLabel(g, T.cardLeads, CM, y + 22, m.lead.conf);
        drawLines(g, lf, CM, y + 40 + lf.size, lf.size * 1.35, C_INK);
      } });
    }
    m.facts.forEach(function (fa) {
      var ff = fitText(g, fa.text, 'text', 0, 28, 22, CIN, 3);
      blocks.push({ id: 'fact', h: 40 + ff.lines.length * ff.size * 1.35, src: [fa.src], draw: function (y) {
        cardLabel(g, fa.label, CM, y + 22);
        drawLines(g, ff, CM, y + 40 + ff.size, ff.size * 1.35, C_INK);
      } });
    });
    return blocks;
  }

  function drawCard(m, img) {
    var c = document.createElement('canvas'); c.width = CW; c.height = CH;
    var g = c.getContext('2d'); g.textBaseline = 'alphabetic'; g.direction = 'ltr';
    g.fillStyle = C_PAPER; g.fillRect(0, 0, CW, CH);
    var BAND = 330, top;
    // optional meaning photo: a top band that fades into the paper; without one, a tag line
    if (img) {
      var sc = Math.max(CW / img.width, BAND / img.height), iw = img.width * sc, ih = img.height * sc;
      g.save(); g.beginPath(); g.rect(0, 0, CW, BAND); g.clip();
      g.drawImage(img, (CW - iw) / 2, (BAND - ih) / 2, iw, ih);
      g.restore();
      var grd = g.createLinearGradient(0, BAND - 140, 0, BAND); grd.addColorStop(0, 'rgba(244,240,230,0)'); grd.addColorStop(1, C_PAPER);
      g.fillStyle = grd; g.fillRect(0, BAND - 140, CW, 140);
      top = BAND - 4;
    } else {
      g.font = cfont('text', 24, 600); g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(T.cardTag, CM, CM + 6);
      top = CM + 64;
    }
    smallSeal(g, m.seal || '', CW - CM - 92, CM - 34, 92);   // the stamp, only as a small accent
    // footer: Nadri and the address
    var foot = CH - 152;
    g.fillStyle = C_INK; g.fillRect(CM, foot, CIN, 2);
    g.font = cfont('head', 56); g.textAlign = 'left'; g.fillText('Nadri', CM, CH - 70);
    g.textAlign = 'right'; g.font = cfont('text', 23); g.fillStyle = C_MUTED; g.fillText(T.cardTry, CW - CM, CH - 106);
    g.font = cfont('mono', 28, 600); g.fillStyle = C_RED; g.fillText('nadri-guide.pages.dev/name', CW - CM, CH - 70);
    // measure: hero, meaning, body sections
    var hero = fitText(g, m.hero, 'head', 0, img ? 116 : 132, 80, CIN, 1);
    if (hero.lines.length > 1) hero = fitText(g, m.hero, 'head', 0, 88, 52, CIN, 2);
    var heroH = hero.lines.length * hero.size * 1.08;
    var mean = null, meanH = 0;
    if (m.meaning) {
      mean = { lab: (m.meaning.label || T.yourNameIs) + (m.meaning.root ? ' (→ ' + m.meaning.root + ')' : '') };
      mean.word = m.meaning.long ? fitText(g, m.meaning.word, 'head', 0, 50, 32, CIN, 3) : fitText(g, '“' + m.meaning.word + '”', 'head', 0, 76, 40, CIN, 2);
      mean.det = m.meaning.detail ? fitText(g, m.meaning.detail, 'text', 0, 27, 22, CIN, 2) : null;
      meanH = 18 + 42 + mean.word.lines.length * mean.word.size * 1.18 + (mean.det ? 8 + mean.det.lines.length * mean.det.size * 1.35 : 0);
    }
    var blocks = cardBlocks(g, m), MINGAP = 34;
    var srcOf = function (bl) {
      var all = (m.meaning && m.meaning.src ? [m.meaning.src] : []);
      bl.forEach(function (b) { all = all.concat(b.src); });
      var out = []; all.forEach(function (x) { x = String(x || '').split(':')[0].trim(); if (x && out.indexOf(x) < 0) out.push(x); });
      var t = (m.credit ? m.credit : '') + (out.length ? (m.credit ? ' · ' : '') + T.src + ': ' + out.join(' · ') : '');
      return t ? fitText(g, t, 'text', 0, 20, 17, CIN, 2) : null;
    };
    var srcH = function (f) { return f ? 24 + f.lines.length * f.size * 1.35 : 0; };
    var sum = function () { return blocks.reduce(function (a, b) { return a + b.h + MINGAP; }, 0); };
    var room = function () { return foot - srcH(srcOf(blocks)) - 28 - top - heroH - meanH; };
    // when it does not fit: drop extra facts, then where-it-leads, then the same-meaning row; the name in Korean/Japanese/Chinese stays
    while (blocks.length && sum() > room()) {
      var drop = ['fact', 'lead', 'same', 'scripts'].filter(function (id) { return blocks.some(function (b) { return b.id === id; }); })[0];
      blocks.splice(blocks.map(function (b) { return b.id; }).lastIndexOf(drop), 1); m.dropped = (m.dropped || []).concat(drop);
    }
    var sf = srcOf(blocks), avail = foot - srcH(sf) - 28 - top - heroH - meanH;
    var used = blocks.reduce(function (a, b) { return a + b.h; }, 0);
    var gap = blocks.length ? Math.min(64, (avail - used) / blocks.length) : 0;
    var spare = avail - used - gap * blocks.length;
    var y = top + (img ? 0 : Math.max(0, spare * 0.42));   // short cards sit a little above the middle instead of leaving a hole
    // draw
    y += drawLines(g, hero, CM, y + hero.size * 0.9, hero.size * 1.08, C_INK);
    if (mean) {
      y += 18;
      g.font = cfont('text', 30); g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(mean.lab, CM, y + 28);
      if (m.meaning.conf) chip(g, m.meaning.conf, CM + g.measureText(mean.lab).width + 14, y + 28);
      y += 42;
      y += drawLines(g, mean.word, CM, y + mean.word.size * 0.95, mean.word.size * 1.18, C_RED);
      if (mean.det) { y += 8; y += drawLines(g, mean.det, CM, y + mean.det.size, mean.det.size * 1.35, C_MUTED); }
    }
    blocks.forEach(function (b) {
      y += gap / 2; g.fillStyle = C_HAIR; g.fillRect(CM, y, CIN, 2);
      y += gap / 2; b.draw(y); y += b.h;
    });
    if (sf) drawLines(g, sf, CM, foot - 24 - (sf.lines.length - 1) * sf.size * 1.35, sf.size * 1.35, C_MUTED);
    return c;
  }

  function cardImage(id) {
    var P = (window.NADRI_MEANING_IMG || {})[id];
    if (!P || !P.src) return Promise.resolve(null);
    return new Promise(function (res) {
      var im = new Image(), done = false, fin = function (v) { if (!done) { done = true; res(v); } };
      im.crossOrigin = 'anonymous'; im.onload = function () { fin(im); }; im.onerror = function () { fin(null); };
      setTimeout(function () { fin(null); }, 5000); im.src = P.src;
    });
  }
  function canvasBlob(c) { return new Promise(function (res, rej) { try { c.toBlob(function (b) { if (b) res(b); else rej(new Error('blob')); }, 'image/png'); } catch (err) { rej(err); } }); }
  var SHARE_FILES = (function () {   // phones with a share sheet that takes image files; computers save the PNG instead
    try { return !!(navigator.share && navigator.canShare && window.matchMedia && matchMedia('(pointer: coarse)').matches && navigator.canShare({ files: [new File([new Blob(['x'], { type: 'image/png' })], 'nadri.png', { type: 'image/png' })] })); } catch (err) { return false; }
  })();
  var cardJob = null;
  // drawn as soon as the result shows, so the share sheet can open straight from the tap
  function prepareCard(r) {
    var m = cardModel(r), job = { m: m };
    m.seal = r.hangul;
    var P = (window.NADRI_MEANING_IMG || {})[m.concept];
    var ready = document.fonts && document.fonts.load ? Promise.all([cfont('head', 60), cfont('text', 30), cfont('text', 30, 600), cfont('mono', 24, 600), cfont('mono', 24, 500)].map(function (f) {
      return document.fonts.load(f, JSON.stringify(m) + 'Nadri' + T.cardTag + T.cardSame + T.cardLeads + T.cardTry + T.yourNameIs + T.src);
    })).catch(function () {}) : Promise.resolve();
    job.p = ready.then(function () { return cardImage(m.concept); }).then(function (img) {
      m.credit = img && P.credit ? P.credit : '';
      return canvasBlob(drawCard(m, img)).catch(function () { m.credit = ''; return canvasBlob(drawCard(m, null)); });
    }).then(function (blob) {
      job.blob = blob;
      job.fname = 'nadri-name-' + (m.hero.replace(/[\s\/\\:*?"<>|]+/g, '') || 'card') + '.png';
      try { job.file = new File([blob], job.fname, { type: 'image/png' }); } catch (err) { job.file = null; }
      return job;
    });
    cardJob = job;
    return job;
  }
  function downloadCard(job) {
    var u = URL.createObjectURL(job.blob), a = document.createElement('a');
    a.download = job.fname; a.href = u; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(u); }, 4000);
  }
  function cardClick() {
    var job = cardJob; if (!job) return;
    var page = location.origin + location.pathname;   // the link in the share text carries no name
    var share = function (j) {
      return navigator.share({ files: [j.file], title: 'Nadri', text: T.cardTry + ' ' + page }).catch(function (err) { if (!err || err.name !== 'AbortError') downloadCard(j); });
    };
    if (SHARE_FILES && job.file) { share(job); return; }
    job.p.then(function (j) { if (SHARE_FILES && j.file) share(j); else downloadCard(j); });
  }

  shell();
  var q = params.get('n');
  if (q) { input.value = q; render(q); }

  window.NadriName = { convert: convert, setLang: function (l) { applyLang(l); shell(); }, card: function () { return cardJob && cardJob.p; } }; // for tests
})();
