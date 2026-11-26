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
    ko: { ph: '이름을 입력하세요 (김민지, Sophia, 田中…)', go: '도장 찍기', sound: '한글로 쓰면', reading: '한국 한자음으로 읽으면', roman: '로마자로 쓰면 (국어의 로마자 표기법)', approx: '대략적인 소리예요. 아직 확인한 이름 목록에 없어서 철자로 추정했어요.', checked: '확인한 흔한 이름 목록에서 가져왔어요.', kana: '일본어 소리를 외래어 표기법대로 한글로 썼어요.', hanja: '글자마다 한국 한자음으로 읽고, 첫소리는 두음법칙을 따랐어요 (예: 李 → 이).', rr: '이름은 음절마다 따로 적는 공식 표기예요. 여권에는 Lee, Park, Kim처럼 관습 표기를 쓰는 경우가 많아요.', save: '도장 저장', share: '링크 복사', copied: '복사했어요', empty: '먼저 이름을 입력하세요.', none: '읽을 수 없는 글자예요. 로마자, 가나, 한글, 한자로 입력해 보세요.', privacy: '입력한 이름은 이 기기 밖으로 보내지 않고, 공유 카드도 이 기기에서 그려요. 이 페이지에는 제휴·광고 스크립트가 없어요. 사이트를 호스팅하는 Cloudflare가 쿠키 없이 방문 수를 세요. 링크를 복사하면 그 링크에는 이름이 들어가요.', wrong: '이상하게 나왔나요? 알려 주시면 목록을 고칠게요.', secSound: '소리', secMeaning: '뜻', secChain: '이 이름이 한국에서 이어지는 곳', lKo: '한국어', lJa: '일본어', lZh: '중국어(대만)', conf: { h: '확실', m: '유력', l: '불확실' }, word: '뜻을 각 언어로', idea: '같은 뜻의 이름', src: '출처: Behind the Name', chars: '글자마다 (훈과 음, 영어 뜻)', kanaApprox: '대략', btnKo: 'Behind the Name 영어 설명을 우리말로 옮겼어요. 원문', noMeaning: '아직 뜻을 확인하지 않은 이름이에요. 알려 주시면 추가할게요.' },
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
      var w0 = words[0], gv = words.length > 1 ? words.slice(1).join('') : (w0.length >= 2 && w0.length <= 4 ? w0.slice(w0.length === 4 ? 2 : 1) : w0);
      r.givenChars = gv.split('');
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
    var bkey = (window.NADRI_BTN || {})[r.firstKey] ? r.firstKey : key;
    var B = (window.NADRI_BTN || {})[r.firstKey] || (key && (window.NADRI_BTN || {})[key]) || null;
    r.btnKo = k3 === 'ko' && B ? (window.NADRI_BTN_KO || {})[bkey] || '' : '';
    var h = '';
    // 1. sound
    h += '<h3 class="namer-h">' + T.sound + '</h3>' + r.sounds.map(function (l) {
      var back = readBack(l[1], r.kind);
      return '<div class="namer-line"><span>' + l[0] + '</span><strong>' + esc(l[1]) + (back ? '<span class="namer-kr">' + esc(back) + '</span>' : '') + '</strong></div>'; }).join('');
    // 2. meaning
    if (r.meaning || B) {
      var e = r.meaning ? r.meaning.e : {}, conf = e.c || 'h';
      var local = e.m && e.m[k3] && k3 !== 'en' ? e.m[k3] : null;
      var root2 = r.meaning && r.meaning.alias ? ' · ' + esc(name.trim().split(' ')[0]) + ' → ' + esc(r.meaning.key.charAt(0).toUpperCase() + r.meaning.key.slice(1)) : '';
      h += '<h3 class="namer-h">' + T.meaning + root2 + ' <span class="namer-conf c-' + conf + '">' + T.conf[conf] + '</span></h3>';
      if (local) h += '<p class="namer-mean">' + esc(local) + '</p>';
      // Korean interface: our Korean translation first, Behind the Name's English sentence under it (owner: "영어를 없애라는 말이 아니야")
      if (B && r.btnKo) h += '<p class="' + (local ? 'namer-sub' : 'namer-mean') + '">' + esc(r.btnKo) + ' <span class="namer-origin">(' + esc(B.origin) + ')</span></p><p class="namer-src">' + UI.btnKo + ': “' + esc(B.meaning) + '”</p>';
      else if (B) h += '<p class="' + (local ? 'namer-sub' : 'namer-mean') + '">' + esc(B.meaning) + ' <span class="namer-origin">(' + esc(B.origin) + ')</span></p>';
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
      }).join('') + '</ul>%%WHOLE%%';
    }
    var seal = r.hangul.replace(/ /g, '').length <= 9 ? sealSVG(esc(r.hangul)) : '';
    var card = '<div class="namer-card"><div class="namer-seal">' + seal + '</div><div class="namer-text">' + h +
      (r.approx || !r.meaning ? '<p class="namer-note' + (r.approx ? ' approx' : '') + '">' + (r.approx ? T.approx : r.note) + '</p>' : '') +
      '<p class="namer-actions"><button type="button" class="namer-open">' + T.cardShare + '</button> <button type="button" class="namer-share">' + T.share + '</button></p>' +
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
    if (r.chars) {
      r.born = bornFromHanja(r.chars.map(function (x) { return x.c; }));
      var KJ = window.NADRI_KANJI || {}, gl = function (c) { return KJ[c] ? (k3 === 'ko' ? KJ[c].ko : KJ[c].en) : ''; };
      r.whole = (r.givenChars || []).some(gl) ? wholeMeaning(r.givenChars, gl, r.born) : '';
      if (r.born) more = bornBlock(r.born, r.whole) + more;
    }
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
      if (!r.born) more = worldBornBlock(wids[0], r.whole) + more;
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
    // the whole-name meaning appears once: in the born-in heading if there is one, else under the characters
    card = card.replace('%%WHOLE%%', r.whole && more.indexOf('namer-born-h') < 0 ? '<p class="namer-gloss">' + T.yourNameIs + ' <strong>“' + esc(r.whole) + '”</strong></p>' : '');
    // the same 'Share card' button at the very top of the result, seen without scrolling
    out.innerHTML = '<p class="namer-actions namer-top"><button type="button" class="namer-open">' + T.cardShare + '</button></p>' + card + more;
    prepareCard(r);
    Array.prototype.forEach.call(out.querySelectorAll('.namer-open'), function (b) { b.onclick = function () { openShare(b); }; });
    out.querySelector('.namer-share').onclick = function (ev) {
      var url = location.origin + location.pathname + '?n=' + encodeURIComponent(name) + (uiLang !== SITE2UI[LANG] ? '&hl=' + uiLang : '');
      (navigator.clipboard ? navigator.clipboard.writeText(url) : Promise.reject()).then(function () { ev.target.textContent = T.copied; }, function () { prompt('', url); });
    };
    wireGo(); if (r.kind === 'hangul') wireHanja(r);
  }




  /* the Hangul reading the page shows after a sound line (Korean interface): kana and Cyrillic read back (as before),
     Chinese characters by their Mandarin reading (외래어 표기법 Chinese table; data name-zhko.js, built by tools/build_zhko.py) */
  function zhRead(v) {
    var Z = window.NADRI_ZHKO, M = window.NADRI_ZHKO_MULTI || '', out = '', approx = false, ok = true;
    if (!Z || L3() !== 'ko') return '';
    Array.from(v).forEach(function (ch) {
      if (/[\s·・]/.test(ch)) out += ' ';
      else if (Z[ch]) { out += Z[ch]; if (M.indexOf(ch) >= 0) approx = true; }
      else ok = false;
    });
    return ok && out.trim() ? out.trim().replace(/\s+/g, ' ') + (approx ? ' · ' + UI.kanaApprox : '') : '';
  }
  function readBack(v, kind) {
    if (L3() !== 'ko' || kind === 'kana' || !v) return '';
    if (/[\u30A0-\u30FF]/.test(v)) return v.split(/[・\s]/).map(function (w) { return kanaWord(w) || ''; }).join(' ').trim();
    if (/[\u0400-\u04FF]/.test(v)) return cyrToHangul(v);
    if (/[\u4E00-\u9FFF]/.test(v) && kind !== 'han') return zhRead(v);
    return '';
  }
  /* the whole given name's meaning, every character joined (元斗 = 으뜸 + 별, owner's design); a natural phrase only where the
     data has one that covers every character (the born-in 'first star' phrase for 元/一/始/初/首 + the star character) */
  function wholeMeaning(chars, gloss, born) {
    var BB = born && (window.NADRI_BORN || {})[born.id], M = (window.NADRI_BORN_OF || {}).hanja || {}, k3 = L3();
    if (BB && born.first && BB.first && chars.length > 1 && chars.every(function (c) { return '元一始初首'.indexOf(c) >= 0 || M[c] === born.id; })) return BB.first[k3] || BB.first.en;
    return chars.map(function (c) { return gloss(c) || c; }).join(' + ');
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
  function bornBlock(b, whole) {
    var B = (window.NADRI_BORN || {})[b.id]; if (!B) return '';
    var k3 = L3(), ph = (b.first && B.first ? B.first : B.phrase);
    var rows = B.c.map(function (c) {
      var country = c[1][k3] || c[1].en, why = c[4][k3 === 'ko' ? 'ko' : 'en'] || c[4].en;
      if (!c[2]) return '<li class="hold"><span class="namer-flag">' + c[0] + '</span><div><b>' + esc(country) + '</b> <small>' + esc(c[3]) + '</small><p>' + esc(why) + ' ' + mail('Nadri born-in: ' + b.id + ' / ' + country, T.native) + '</p></div></li>';
      return '<li><span class="namer-flag">' + c[0] + '</span><div><b>' + esc(country) + ' → ' + esc(c[2]) + kr(c[2]) + '</b>' + (c[3] ? ' <small>' + esc(c[3]) + '</small>' : '') + '<p>' + esc(why) + '</p><span class="namer-pct">' + T.sure + ' ' + c[5] + '%</span></div></li>';
    }).join('');
    var p0 = ph[k3] || ph.en, top = whole || p0;
    return '<section class="namer-sec namer-born"><p class="namer-born-h">' + T.yourNameIs + ' <strong>“' + esc(top) + '”</strong></p><h3 class="namer-h">' + T.bornIn + (top !== p0 ? ' · ' + esc(p0) : '') + '</h3><ul class="namer-born-list">' + rows + '</ul></section>';
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
  function worldBornBlock(wid, whole) {
    var W = (window.NADRI_WORLD || {})[wid], C = (window.NADRI_CONCEPTS || {})[wid]; if (!W) return '';
    var named = W.filter(function (e) { return e.n; }); if (!named.length) return '';
    var k3 = L3(), lab = C ? (C[k3] || C.en) : (named[0].n);
    var rows = named.slice(0, 6).map(function (e) {
      var rg = regionOf(e.r);
      return '<li><span class="namer-flag">' + rg.flag + '</span><div><b>' + esc(rg.name) + worldName(e) + '</b>' + (e.nn ? ' <small>' + esc(e.nn) + '</small>' : '') + '<p>' + esc(e.g[k3] || e.g.en) + '</p><span class="namer-conf c-' + e.c + '">' + (T.conf[e.c] || e.c) + '</span></div></li>';
    }).join('');
    var top = whole || lab;
    return '<section class="namer-sec namer-born"><p class="namer-born-h">' + T.yourNameIs + ' <strong>“' + esc(top) + '”</strong></p><h3 class="namer-h">' + T.bornIn + (top !== lab ? ' · ' + esc(lab) : '') + '</h3><ul class="namer-born-list">' + rows + '</ul></section>';
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
    if (nat) r.whole = k3 === 'ko' ? nat[0] : nat[1];
    var bornN = ((window.NADRI_BORN_OF || {}).native || {})[K.given]; if (bornN) { r.born = { id: bornN }; h = bornBlock(r.born, r.whole) + h; }
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
        var zr = zhRead(name);
        var o = '<p class="namer-mean">' + esc(name) + (zr ? '<span class="namer-kr">' + esc(T.zh + ' ' + zr) + '</span>' : '') + '</p><p class="namer-sub">' + list.map(function (x) { return '<b>' + x.h + '</b> ' + esc(x.hun) + ' · ' + esc(x.en); }).join(' / ') + '</p>';
        var ids = conceptsForHanja(list.map(function (x) { return x.h; })), CC = window.NADRI_CONCEPTS || {}, k3 = L3();
        r.born = bornFromHanja(list.map(function (x) { return x.h; })); r.pickedName = name; r.picked = list; r.pickedIds = ids;
        var WD = window.NADRI_WORLD || {}, wids = ids.filter(function (id) { return WD[id]; });
        r.worldId = wids[0] || null;
        var bySyl = r.ko.given.split('').map(function (c, j) { return picked[j] || null; });
        var hun = {}; list.forEach(function (x) { hun[x.h] = k3 === 'ko' ? x.hun : x.en; });
        r.whole = wholeMeaning(bySyl.map(function (x) { return x ? x.h : '?'; }), function (c) { return hun[c] || ''; }, r.born);
        var bb = r.born ? bornBlock(r.born, r.whole) : wids.length ? worldBornBlock(wids[0], r.whole) : '';
        o += bb || '<p class="namer-gloss">' + T.yourNameIs + ' <strong>“' + esc(r.whole) + '”</strong></p>';
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
     Owner 2026-11-26 [7eb4ec94#2276]: built on the results below the stamp, compact and clean; [7eb4ec94#2341]: every result section
     must be on it (a representative part of each, plus a "see the full result" link), and every name with its reading as the page shows it.
     One 1080x1920 PNG (9:16; Instagram stories/feed, Threads), drawn on this device; nothing is sent.
     Layout: [meaning photo band, optional] tag + small seal / name / "Your name means …" + confidence / sound (with readings) /
     If you were born in… (3) / names with the same meaning (6, 3x2) / where it leads around the world (Korea first, 3) /
     Korean surname facts / "See the full result → address" / sources / Nadri. When space is short, sections keep fewer items; none is dropped.
     Meaning photo (owner [7eb4ec94#2296]): window.NADRI_MEANING_IMG[conceptId] = { src, credit }; same-origin files only, so nothing
     leaves the site and the canvas can still be saved. No photo: the card starts with the tag line. */
  var CW = 1080, CH = 1920, CM = 84, CIN = CW - CM * 2;   // CH: 1920 for the 9:16 story, 1350 for the 4:5 card (set per drawing)
  var C_PAPER = '#f4f0e6', C_INK = '#16151a', C_MUTED = '#5f5b55', C_HAIR = '#ddd6c8', C_RED = '#b8392f';
  var F_HEAD = '"Song Myung", "Noto Serif KR", serif', F_TEXT = '"IBM Plex Sans KR", system-ui, -apple-system, "Segoe UI", "Noto Sans KR", sans-serif', F_MONO = '"IBM Plex Mono", ui-monospace, monospace';
  function cfont(kind, size, weight) { return (weight ? weight + ' ' : '') + Math.round(size) + 'px ' + (kind === 'head' ? F_HEAD : kind === 'mono' ? F_MONO : F_TEXT); }
  function langLabel(l) {
    var k3 = L3();
    return l.split(' / ').map(function (x) { var m = window.NADRI_LNAMES && window.NADRI_LNAMES[x]; var extra = { Latin: { ko: '라틴어', ja: 'ラテン語', zh: '拉丁文' }, Sanskrit: { ko: '산스크리트어', ja: 'サンスクリット語', zh: '梵文' }, Hindi: { ko: '힌디어', ja: 'ヒンディー語', zh: '印地文' }, Welsh: { ko: '웨일스어', ja: 'ウェールズ語', zh: '威爾斯文' }, Japanese: { ko: '일본어', ja: '日本語', zh: '日文' }, Chinese: { ko: '중국어', ja: '中国語', zh: '中文' }, Korean: { ko: '한국어', ja: '韓国語', zh: '韓文' }, Slavic: { ko: '슬라브어', ja: 'スラブ語', zh: '斯拉夫語' }, English: { ko: '영어', ja: '英語', zh: '英文' }, Germanic: { ko: '게르만어', ja: 'ゲルマン語', zh: '日耳曼語' } }[x]; return (m && m[k3]) || (extra && extra[k3]) || x; }).join(' · ');
  }

  /* what goes on the card: every result section the page shows for this name (owner [7eb4ec94#2341]), each cut to its representative
     items, with the readings and confidence marks exactly as the page shows them. Nothing the page does not show. */
  function cardModel(r) {
    var k3 = L3(), ko = k3 === 'ko', typed = String(r.typed || '').trim().replace(/\s+/g, ' ');
    var CC = window.NADRI_CONCEPTS || {}, WD = window.NADRI_WORLD || {}, CHN = window.NADRI_CHAINS || {};
    var m = { hero: r.kind === 'hangul' ? r.hangul : typed, sounds: [], phrase: null, born: null, same: null, world: null, facts: [], concept: null, src: {} };
    var low = function (x) { return String(x || '').toLowerCase(); };
    var dup = function (x) { return low(x) === low(m.hero) || low(x) === low(typed); };
    var clabel = function (id) { return CC[id] ? (CC[id][k3] || CC[id].en) : ''; };
    var rd = function (form, lang) {   // the page's kr(): Hangul reading of a foreign name, Korean interface only
      if (!ko || !form || /[가-힣]/.test(form) || !window.nadriKoRead) return '';
      return window.nadriKoRead(form, lang) || '';
    };
    // 1. sound: every line of the page's sound section, with the page's Hangul read-back of kana and Cyrillic (Korean interface)
    r.sounds.forEach(function (l) {
      if (!l[1] || l[1] === m.hero) return;
      var back = readBack(l[1], r.kind);
      m.sounds.push({ label: l[0] + (r.approx && l[0] === UI.lKo ? ' (' + UI.kanaApprox + ')' : ''), lines: String(l[1]).split(' · '), read: back });
    });
    if (r.pickedName) { var zr = zhRead(r.pickedName); m.sounds.push({ label: T.koHanja, lines: [r.pickedName], read: zr ? T.zh + ' ' + zr : '' }); }
    // 2. the whole-name meaning ("Your name means …")
    var e = r.meaning && r.meaning.e, B = r.btn, BB = r.born && (window.NADRI_BORN || {})[r.born.id];
    var ids = (r.kind === 'hangul' ? r.pickedIds : r.kind === 'han' ? r.cids : (r.concept ? [r.concept] : [])) || [];
    ids = ids.filter(function (id) { return CC[id]; });
    var ph = null, btnLine = r.btnKo || (B && B.meaning) || '';
    if (r.kind === 'latin' && e && e.m) ph = { word: (k3 !== 'en' && e.m[k3]) || e.m.en, conf: T.conf[e.c || 'h'], detail: btnLine };
    else if (r.kind === 'latin' && B && B.meaning) ph = { word: btnLine, conf: T.conf.h, long: true };
    else if (r.whole) ph = { word: r.whole };   // every character of the given name (or the native word's meaning), as the page shows it
    else if (BB) ph = { word: (r.born.first && BB.first ? BB.first : BB.phrase)[k3] || BB.phrase.en };
    else if (r.worldId && CC[r.worldId]) ph = { word: clabel(r.worldId) };
    else if (ids.length) ph = { word: clabel(ids[0]) };
    var nat = r.kind === 'hangul' && r.ko && !(r.picked && r.picked.length) ? (window.KO_NATIVE || {})[r.ko.given] : null;
    if (nat) ph = { word: ko ? nat[0] : nat[1], detail: T.koNative };
    if (ph) {
      if (r.kind === 'han' && r.chars) ph.detail = r.chars.filter(function (x) { return x.ko || x.en; }).map(function (x) { return x.c + ' ' + (ko && x.ko ? x.ko + ' ' + (x.read || '') : (x.en || x.ko)); }).join(' · ');
      if (r.kind === 'hangul' && r.picked && r.picked.length) ph.detail = r.picked.map(function (x) { return x.h + ' ' + (ko ? x.hun : x.en); }).join(' · ');
      if (r.meaning && r.meaning.alias) ph.root = cap(r.meaning.key);
      if (r.kind === 'latin') m.src.phrase = [r.btnKo ? 'Behind the Name (우리말 옮김)' : 'Behind the Name'];
      m.phrase = ph;
    }
    m.concept = r.concept || ids[0] || r.worldId || (r.born && r.born.id) || null;
    // 3. "If you were born in…": the page's list (older born-in list, or world entries that carry a name)
    var rows = [];
    if (BB) BB.c.filter(function (c) { return c[2] && !dup(c[2]); }).forEach(function (c) {
      rows.push({ place: c[1][k3] || c[1].en, name: c[2], read: rd(c[2]), orig: c[3] || '', why: c[4][ko ? 'ko' : 'en'] || c[4].en, conf: T.sure + ' ' + c[5] + '%' });
    });
    else if (r.worldId && WD[r.worldId]) WD[r.worldId].filter(function (x) { return x.n && !dup(x.n); }).forEach(function (x) {
      rows.push({ place: regionOf(x.r).name, name: x.n, read: ko && x.nk ? x.nk : '', orig: x.nn || '', why: x.g[k3] || x.g.en, conf: T.conf[x.c] || x.c, src: x.s && x.s[0] && x.s[0][0] });
    });
    if (rows.length) {
      m.born = rows;
      var bp = BB ? ((r.born.first && BB.first ? BB.first : BB.phrase)[k3] || BB.phrase.en) : clabel(r.worldId);
      m.bornLabel = T.bornIn + (bp && (!m.phrase || m.phrase.word !== bp) ? ' · ' + bp : '');
    }
    // 4. names with the same meaning in other languages (the page's concept grid; for native Korean words, its list of names abroad)
    var cid = ids.filter(function (id) { return CC[id].names && CC[id].names.length; })[0];
    if (cid) {
      m.same = { label: T.koAbroad + ' · ' + clabel(cid), items: CC[cid].names.filter(function (n) { return !dup(n[1]); }).map(function (n) {
        return { lang: langLabel(n[0]), name: n[1], read: n[2] && /[가-힣]/.test(n[2]) ? '' : rd(n[1]), orig: n[2] || '' };
      }) };
    } else if (nat) {
      var MN = window.KO_MEANING_TO_NAME || {}, NN = window.NADRI_NAMES || {}, seen = {}, ab = [];
      (MN[low(nat[1])] || []).forEach(function (k) { if (!seen[k] && NN[k] && typeof NN[k] === 'object') { seen[k] = 1; ab.push({ lang: (NN[k].m && (NN[k].m[k3] || NN[k].m.en)) || '', name: cap(k), read: '', orig: '' }); } });
      if (ab.length) m.same = { label: T.koAbroad, items: ab };
    }
    if (m.same && !m.same.items.length) m.same = null;
    // 5. where it leads around the world: Korea first, then the next regions, one line each
    var W = r.worldId && WD[r.worldId], step = function (id) {
      var st = CHN[id]; if (!st || !st.length) return null;
      var s0 = st.filter(function (x) { return x.link; })[0] || st[0];
      return { text: s0[k3] || s0.en, conf: T.conf[s0.c] || '', src: s0.s };
    };
    var lines = [];
    if (W) {
      var list = W.slice();
      if (r.krChain && !list.some(function (x) { return x.r === 'KR'; })) list.push({ r: 'KR', chain: r.krChain });
      list.sort(function (a, b) { return (a.r === 'KR' ? 0 : 1) - (b.r === 'KR' ? 0 : 1); });
      list.forEach(function (x) {
        var L = x.chain ? step(x.r === 'KR' && r.krChain ? r.krChain : x.chain)
          : { text: (x.g && (x.g[k3] || x.g.en)) || (String(x[k3] || x.en || '').match(/^[\s\S]*?[.。](?=\s|$)/) || [String(x[k3] || x.en || '')])[0], conf: T.conf[x.c] || x.c, src: x.s && x.s[0] && x.s[0][0] };
        if (L && L.text) { L.place = regionOf(x.r).name; lines.push(L); }
      });
      if (lines.length) m.world = { label: T.world + (CC[r.worldId] ? ' · ' + clabel(r.worldId) : ''), lines: lines };
    } else if (r.chain && CHN[r.chain]) {   // Korea-only chain: the page lists its steps
      CHN[r.chain].forEach(function (s0) { lines.push({ place: regionOf('KR').name, text: s0[k3] || s0.en, conf: T.conf[s0.c] || '', src: s0.s }); });
      if (lines.length) m.world = { label: T.chain, lines: lines };
    }
    // 6. Korean names: surname count and baby-name rank, as the page shows them
    var srcKo = String(T.srcKo || '').split(/;|,(?![^(]*\))/).map(function (x) { return x.trim(); });
    if (r.kind === 'hangul' && r.ko) {
      var POP = window.KO_SURNAME_POP || {}, K = r.ko, fmt = function (n) { return Number(n).toLocaleString(); };
      if (K.sur) m.facts.push({ label: T.koSurname + ' · ' + K.sur, text: POP[K.sur] ? T.koPop.replace('{n}', fmt(POP[K.sur])).replace('{p}', (POP[K.sur] / 510694).toFixed(1)).replace('{t}', fmt(window.KO_SURNAME_TOTAL || 5582)) : T.koPopOther.replace('{t}', fmt(window.KO_SURNAME_TOTAL || 5582)), src: srcKo[0] });
      var KB = window.KO_BABY_2025 || { boys: [], girls: [] }, bi = KB.boys.indexOf(K.given), gi = KB.girls.indexOf(K.given);
      m.facts.push({ label: T.koBaby + ' · ' + K.given, text: (bi >= 0 ? T.koBabyRank.replace('{r}', bi + 1).replace('{g}', T.boys) + ' ' : '') + (gi >= 0 ? T.koBabyRank.replace('{r}', gi + 1).replace('{g}', T.girls) : '') + (bi < 0 && gi < 0 ? T.koBabyNone : ''), src: srcKo.slice(1).join(', ') });
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
  /* body sections at one trim level p: each measures itself first, then draws at y, and carries the sources of what it shows */
  function cardBlocks(g, m, p) {
    var blocks = [], small = function (t, max, min, w, n) { return fitText(g, t, 'text', 0, max, min, w, n || 1); };
    if (m.sounds.length) {   // a grid: up to 3 across (4 lines: 2 x 2); a line that will not fit goes to label-left rows
      var n = m.sounds.length, gap = 32, across = n <= 3 ? n : 2, grid = true, colW, S;
      var build = function () {
        colW = grid ? (CIN - gap * (across - 1)) / across : CIN - 250;
        S = m.sounds.map(function (s) {
          return { vals: s.lines.map(function (l) { return fitText(g, l, 'head', 0, grid ? 44 : 40, 26, colW, grid ? 1 : 2); }), read: s.read ? small('(' + s.read + ')', 24, 18, colW) : null };
        });
      };
      build();
      if (S.some(function (s) { return s.vals.some(function (v) { return v.lines.length > 1; }); })) { grid = false; build(); }
      var hOf = function (s) { return s.vals.reduce(function (a, v) { return a + v.lines.length * v.size * 1.2; }, 0) + (s.read ? 32 : 0); };
      var rowHs = [];
      if (grid) for (var r0 = 0; r0 < n; r0 += across) rowHs.push(34 + Math.max.apply(null, S.slice(r0, r0 + across).map(hOf)));
      else S.forEach(function (x) { rowHs.push(Math.max(36, hOf(x))); });
      blocks.push({ id: 'sounds', h: rowHs.reduce(function (a, h) { return a + h + 14; }, 0) - 14, src: [], draw: function (y) {
        var yRow = y;
        m.sounds.forEach(function (s, i) {
          var row = grid ? Math.floor(i / across) : i, col = grid ? i % across : 0;
          if (i && (!grid || col === 0)) yRow += rowHs[row - 1] + 14;
          var x = grid ? CM + col * (colW + gap) : CM + 250, yy = grid ? yRow + 34 : yRow;
          cardLabel(g, s.label, grid ? x : CM, grid ? yRow + 22 : yRow + 30, null, grid ? colW : 240);
          S[i].vals.forEach(function (v) { yy += drawLines(g, v, x, yy + v.size, v.size * 1.2, C_INK); });
          if (S[i].read) drawLines(g, S[i].read, x, yy + 26, 30, C_MUTED);
        });
      } });
    }
    if (m.born) {
      var R = m.born.slice(0, p.b).map(function (it) {
        g.font = cfont('text', 21, 600); var chipW = g.measureText(it.conf).width + 30;
        var name = fitText(g, it.name, 'head', 0, 42, 30, CIN * 0.6, 1);
        g.font = cfont('head', name.size); var nameW = g.measureText(name.lines[0]).width;
        var extra = [it.read ? '(' + it.read + ')' : '', it.orig].filter(Boolean).join(' ');
        g.font = cfont('text', 25); var inline = extra && nameW + 14 + g.measureText(extra).width <= CIN;
        return { it: it, chipW: chipW, place: small(it.place, 23, 18, CIN - chipW), name: name, nameW: nameW, extra: extra ? small(extra, 25, 19, inline ? CIN - nameW - 14 : CIN) : null, inline: inline,
          why: p.why ? fitText(g, it.why, 'text', 0, 25, 20, CIN, p.why) : null };
      });
      var rowH = function (x) { return 30 + x.name.size * 1.2 + (x.extra && !x.inline ? 30 : 0) + (x.why ? x.why.lines.length * x.why.size * 1.35 + 4 : 0); };
      blocks.push({ id: 'born', h: 40 + R.reduce(function (a, x) { return a + rowH(x) + 16; }, 0) - 16, src: R.map(function (x) { return x.it.src; }), draw: function (y) {
        cardLabel(g, m.bornLabel || T.bornIn, CM, y + 22); y += 40;
        R.forEach(function (x) {
          drawLines(g, x.place, CM, y + 22, 30, C_MUTED);
          g.font = cfont('text', x.place.size); chip(g, x.it.conf, CM + g.measureText(x.place.lines[0]).width + 10, y + 24);
          var yy = y + 30 + x.name.size * 0.95;
          drawLines(g, x.name, CM, yy, x.name.size * 1.2, C_INK);
          if (x.extra) { if (x.inline) drawLines(g, x.extra, CM + x.nameW + 14, yy, 30, C_MUTED); else drawLines(g, x.extra, CM, yy + 32, 30, C_MUTED); }
          yy = y + 30 + x.name.size * 1.2 + (x.extra && !x.inline ? 30 : 0);
          if (x.why) drawLines(g, x.why, CM, yy + x.why.size + 2, x.why.size * 1.35, C_INK);
          y += rowH(x) + 16;
        });
      } });
    }
    if (m.same) {
      var cols3 = 3, cw = (CIN - 32 * 2) / cols3, items = m.same.items.slice(0, p.c);
      var cells = items.map(function (it) {
        var sub = [it.read ? '(' + it.read + ')' : '', it.orig].filter(Boolean).join(' ');
        return { lang: small(it.lang, 21, 16, cw), name: fitText(g, it.name, 'head', 0, 36, 24, cw, 1), sub: sub ? small(sub, 22, 16, cw) : null };
      });
      var cellH = function (c) { return 28 + c.name.size * 1.2 + (c.sub ? 28 : 0); };
      var rowsH = [];
      for (var i = 0; i < cells.length; i += cols3) rowsH.push(Math.max.apply(null, cells.slice(i, i + cols3).map(cellH)));
      blocks.push({ id: 'same', h: 40 + rowsH.reduce(function (a, b) { return a + b + 16; }, 0) - 16, src: [], draw: function (y) {
        cardLabel(g, m.same.label, CM, y + 22); var yy = y + 40;
        rowsH.forEach(function (rh, ri) {
          cells.slice(ri * cols3, ri * cols3 + cols3).forEach(function (c, ci) {
            var x = CM + ci * (cw + 32);
            drawLines(g, c.lang, x, yy + 20, 26, C_MUTED);
            drawLines(g, c.name, x, yy + 28 + c.name.size * 0.95, c.name.size * 1.2, C_INK);
            if (c.sub) drawLines(g, c.sub, x, yy + 28 + c.name.size * 1.2 + 22, 26, C_MUTED);
          });
          yy += rh + 16;
        });
      } });
    }
    if (m.world) {
      var Ls = m.world.lines.slice(0, p.d);
      g.font = cfont('text', 20, 600);
      var chipCol = Math.max.apply(null, Ls.map(function (l) { return l.conf ? g.measureText(l.conf).width + 30 : 0; }));
      var F = Ls.map(function (l) { return fitText(g, l.place + ' — ' + l.text, 'text', 0, 27, 21, CIN - chipCol, 2); });
      var lh = function (f) { return f.lines.length * f.size * 1.35; };
      blocks.push({ id: 'world', h: 40 + F.reduce(function (a, f) { return a + lh(f) + 10; }, 0) - 10, src: Ls.map(function (l) { return l.src; }), draw: function (y) {
        cardLabel(g, m.world.label, CM, y + 22); y += 40;
        F.forEach(function (f, i) {
          if (Ls[i].conf) chip(g, Ls[i].conf, CM, y + f.size + 2);
          drawLines(g, f, CM + chipCol, y + f.size, f.size * 1.35, C_INK);
          y += lh(f) + 10;
        });
      } });
    }
    if (m.facts.length) {
      var FA = m.facts.slice(0, p.f).map(function (fa) { return { fa: fa, f: fitText(g, fa.text, 'text', 0, 26, 21, CIN, 2) }; });
      blocks.push({ id: 'facts', h: FA.reduce(function (a, x) { return a + 34 + x.f.lines.length * x.f.size * 1.35 + 12; }, 0) - 12, src: FA.map(function (x) { return x.fa.src; }), draw: function (y) {
        FA.forEach(function (x) {
          cardLabel(g, x.fa.label, CM, y + 22);
          drawLines(g, x.f, CM, y + 34 + x.f.size, x.f.size * 1.35, C_INK);
          y += 34 + x.f.lines.length * x.f.size * 1.35 + 12;
        });
      } });
    }
    return blocks;
  }
  // trim levels: every section stays; only the number of items in it (and the length of the reasons) goes down
  var CARD_LEVELS = [
    { b: 3, c: 6, d: 3, why: 2, f: 2 }, { b: 3, c: 6, d: 3, why: 1, f: 2 }, { b: 3, c: 6, d: 2, why: 1, f: 2 }, { b: 3, c: 6, d: 2, why: 1, f: 1 },
    { b: 3, c: 3, d: 2, why: 1, f: 1 }, { b: 2, c: 3, d: 2, why: 1, f: 1 }, { b: 2, c: 3, d: 1, why: 1, f: 1 }, { b: 1, c: 3, d: 1, why: 1, f: 1 }];

  function drawCard(m, img, fmt) {
    CH = fmt === '45' ? 1350 : 1920;
    var tight = CH < 1500;   // 4:5: same sections, fewer items and a smaller head
    var c = document.createElement('canvas'); c.width = CW; c.height = CH;
    var g = c.getContext('2d'); g.textBaseline = 'alphabetic'; g.direction = 'ltr';
    g.fillStyle = C_PAPER; g.fillRect(0, 0, CW, CH);
    var BAND = tight ? 260 : 380, top;
    // optional meaning photo: a top band that fades into the paper; without one, a tag line
    if (img) {
      var sc = Math.max(CW / img.width, BAND / img.height), iw = img.width * sc, ih = img.height * sc;
      g.save(); g.beginPath(); g.rect(0, 0, CW, BAND); g.clip();
      g.drawImage(img, (CW - iw) / 2, (BAND - ih) / 2, iw, ih);
      g.restore();
      var grd = g.createLinearGradient(0, BAND - 150, 0, BAND); grd.addColorStop(0, 'rgba(244,240,230,0)'); grd.addColorStop(1, C_PAPER);
      g.fillStyle = grd; g.fillRect(0, BAND - 150, CW, 150);
      top = BAND - 4;
    } else {
      g.font = cfont('text', 24, 600); g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(T.cardTag, CM, CM + 6);
      top = CM + 64;
    }
    smallSeal(g, m.seal || '', CW - CM - 92, CM - 34, 92);   // the stamp, only as a small accent
    // footer: Nadri
    var foot = CH - 130;
    g.fillStyle = C_INK; g.fillRect(CM, foot, CIN, 2);
    g.font = cfont('head', 52); g.textAlign = 'left'; g.fillText('Nadri', CM, CH - 58);
    g.textAlign = 'right'; g.font = cfont('text', 23); g.fillStyle = C_MUTED; g.fillText(T.cardTry, CW - CM, CH - 64);
    // sources (full width, under the content) depend on which sections are shown
    var srcOf = function (bl) {
      var all = (m.src.phrase || []).slice();
      bl.forEach(function (b) { all = all.concat(b.src); });
      var out = [], seenK = []; all.forEach(function (x) { x = String(x || '').split(':')[0].trim(); var k = x.replace(/\s*\([^)]*\)$/, ''); if (x && seenK.indexOf(k) < 0) { seenK.push(k); out.push(x); } });
      var t = (m.credit || '') + (out.length ? (m.credit ? ' · ' : '') + T.src + ': ' + out.join(' · ') : '');
      var w0 = CIN; CIN = CIN0; var f = t ? fitText(g, t, 'text', 0, 19, 16, CIN0, 2) : null; CIN = w0; return f;
    };
    var srcH = function (f) { return f ? 18 + f.lines.length * f.size * 1.35 : 0; };
    var MINGAP = tight ? 16 : 22, CIN0 = CIN;
    // lay out the content at scale s: the name, the whole-name meaning, the sections at the first trim level that fits, the "see all" line.
    // If even the last trim level does not fit, the whole content is drawn a little smaller (never below 76%) instead of overlapping.
    var layout = function (s) {
      CIN = CIN0 / s;
      var L = { s: s };
      L.hero = fitText(g, m.hero, 'head', 0, tight ? (img ? 88 : 100) : (img ? 112 : 128), tight ? 64 : 76, CIN, 1);
      if (L.hero.lines.length > 1) L.hero = fitText(g, m.hero, 'head', 0, tight ? 64 : 84, 44, CIN, 2);
      L.heroH = L.hero.lines.length * L.hero.size * 1.08; L.meanH = 0; L.mean = null;
      if (m.phrase) {
        var mean = { lab: T.yourNameIs + (m.phrase.root ? ' (→ ' + m.phrase.root + ')' : '') };
        mean.word = m.phrase.long ? fitText(g, m.phrase.word, 'head', 0, tight ? 42 : 48, 30, CIN, 3) : fitText(g, '“' + m.phrase.word + '”', 'head', 0, tight ? 58 : 72, 36, CIN, 2);
        mean.det = m.phrase.detail ? fitText(g, m.phrase.detail, 'text', 0, 26, 20, CIN, 2) : null;
        L.mean = mean; L.meanH = 16 + 42 + mean.word.lines.length * mean.word.size * 1.18 + (mean.det ? 6 + mean.det.lines.length * mean.det.size * 1.35 : 0);
      }
      g.font = cfont('text', 27, 600); L.moreLab = T.cardMore + ' →';
      L.moreW = g.measureText(L.moreLab + ' ').width; g.font = cfont('mono', 27, 600);
      L.moreOne = L.moreW + g.measureText('nadri-guide.pages.dev/name').width <= CIN; L.moreH = L.moreOne ? 40 : 76;
      for (L.level = 0; L.level < CARD_LEVELS.length; L.level++) {
        L.blocks = cardBlocks(g, m, CARD_LEVELS[L.level]);
        L.sf = srcOf(L.blocks);
        L.avail = (foot - 24 - srcH(L.sf) - top) / s - L.heroH - L.meanH;
        L.need = L.blocks.reduce(function (a, b) { return a + b.h + MINGAP; }, 0) + MINGAP + L.moreH;
        if (L.need <= L.avail) { L.fits = true; break; }
      }
      if (L.level === CARD_LEVELS.length) L.level--;
      return L;
    };
    var L = layout(1);
    for (var s = 0.96; !L.fits && s >= 0.76; s -= 0.04) L = layout(s);
    m.level = L.level; m.scale = L.s;
    m.shown = {}; L.blocks.forEach(function (b) { m.shown[b.id] = 1; });
    var used = L.blocks.reduce(function (a, b) { return a + b.h; }, 0) + L.moreH;
    var gap = Math.max(MINGAP, Math.min(60, (L.avail - used) / (L.blocks.length + 1)));
    var spare = L.avail - used - gap * (L.blocks.length + 1);
    var y = top + (img ? 0 : Math.max(0, spare * 0.42));   // short cards sit a little above the middle
    g.save(); g.setTransform(L.s, 0, 0, L.s, CM * (1 - L.s), top * (1 - L.s));   // scale about the content's top-left corner
    y += drawLines(g, L.hero, CM, y + L.hero.size * 0.9, L.hero.size * 1.08, C_INK);
    if (L.mean) {
      y += 16;
      g.font = cfont('text', 30); g.fillStyle = C_MUTED; g.textAlign = 'left'; g.fillText(L.mean.lab, CM, y + 28);
      if (m.phrase.conf) chip(g, m.phrase.conf, CM + g.measureText(L.mean.lab).width + 14, y + 28);
      y += 42;
      y += drawLines(g, L.mean.word, CM, y + L.mean.word.size * 0.95, L.mean.word.size * 1.18, C_RED);
      if (L.mean.det) { y += 6; y += drawLines(g, L.mean.det, CM, y + L.mean.det.size, L.mean.det.size * 1.35, C_MUTED); }
    }
    L.blocks.forEach(function (b) {
      y += gap / 2; g.fillStyle = C_HAIR; g.fillRect(CM, y, CIN, 2);
      y += gap / 2; b.draw(y); y += b.h;
    });
    // "See the full result → nadri-guide.pages.dev/name"
    y += gap / 2; g.fillStyle = C_HAIR; g.fillRect(CM, y, CIN, 2); y += gap / 2;
    g.textAlign = 'left'; g.font = cfont('text', 27, 600); g.fillStyle = C_INK; g.fillText(L.moreLab, CM, y + 30);
    g.font = cfont('mono', 27, 600); g.fillStyle = C_RED;
    if (L.moreOne) g.fillText('nadri-guide.pages.dev/name', CM + L.moreW, y + 30); else g.fillText('nadri-guide.pages.dev/name', CM, y + 66);
    g.restore();
    CIN = CIN0;
    m.contentBottom = top + (y + (L.moreOne ? 40 : 76) - top) * L.s;   // for tests: must stay above the sources line
    if (L.sf) drawLines(g, L.sf, CM, foot - 22 - (L.sf.lines.length - 1) * L.sf.size * 1.35, L.sf.size * 1.35, C_MUTED);
    m.srcTop = L.sf ? foot - 22 - (L.sf.lines.length - 1) * L.sf.size * 1.35 - L.sf.size : foot;
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
  var SHARE_FILES = (function () {   // any browser whose share sheet takes image files (phones, Windows/macOS Chrome·Edge·Safari); owner [7eb4ec94#2569]
    try { return !!(navigator.share && navigator.canShare && navigator.canShare({ files: [new File([new Blob(['x'], { type: 'image/png' })], 'nadri.png', { type: 'image/png' })] })); } catch (err) { return false; }
  })();
  var cardJob = null;
  // both formats are drawn as soon as the result shows, so the preview opens at once and the share sheet opens straight from the tap
  function prepareCard(r) {
    var m = cardModel(r), job = { m: m, f: {}, done: {} };
    m.seal = r.hangul;
    var P = (window.NADRI_MEANING_IMG || {})[m.concept];
    var ready = document.fonts && document.fonts.load ? Promise.all([cfont('head', 60), cfont('text', 30), cfont('text', 30, 600), cfont('mono', 24, 600), cfont('mono', 24, 500)].map(function (f) {
      return document.fonts.load(f, JSON.stringify(m) + 'Nadri' + T.cardTag + T.cardMore + T.cardTry + T.yourNameIs + T.bornIn + T.world + T.koAbroad + T.chain + T.src + T.sure);
    })).catch(function () {}) : Promise.resolve();
    var base = ready.then(function () { return cardImage(m.concept); });
    var stem = 'nadri-name-' + (m.hero.replace(/[\s\/\\:*?"<>|]+/g, '') || 'card');
    ['45', '916'].forEach(function (fmt) {
      job.f[fmt] = base.then(function (img) {
        var o = { fmt: fmt };
        var draw = function (im) { m.credit = im && P && P.credit ? P.credit : ''; var cv = drawCard(m, im, fmt); o.level = m.level; o.shown = m.shown; o.scale = m.scale; o.contentBottom = m.contentBottom; o.srcTop = m.srcTop; return canvasBlob(cv); };
        return draw(img).catch(function () { return draw(null); }).then(function (blob) {
          o.blob = blob; o.fname = stem + (fmt === '45' ? '-4x5' : '-9x16') + '.png';
          try { o.file = new File([blob], o.fname, { type: 'image/png' }); } catch (err) { o.file = null; }
          job.done[fmt] = o;
          return o;
        });
      });
    });
    job.p = job.f['916'];
    cardJob = job;
    return job;
  }
  function downloadCard(o) {
    var u = URL.createObjectURL(o.blob), a = document.createElement('a');
    a.download = o.fname; a.href = u; document.body.appendChild(a); a.click(); a.remove();
    setTimeout(function () { URL.revokeObjectURL(u); }, 4000);
  }

  /* ---------- share panel (owner [7eb4ec94#2580] [7eb4ec94#2584] [7eb4ec94#2587]): the image first, large, then the ways to share it ---------- */
  var ICON = {
    phone: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18 16a3 3 0 0 0-2.4 1.2l-6.7-3.4a3 3 0 0 0 0-1.6l6.7-3.4A3 3 0 1 0 15 7a3 3 0 0 0 .1.8L8.4 11.2a3 3 0 1 0 0 1.6l6.7 3.4A3 3 0 1 0 18 16z"/></svg>',
    threads: '<svg viewBox="0 0 24 24" aria-hidden="true"><text x="12" y="18" text-anchor="middle" font-size="19" font-weight="700" font-family="Arial, Helvetica, sans-serif" fill="currentColor">@</text></svg>',
    x: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M18.9 1.2h3.7l-8 9.2L24 22.8h-7.4l-5.8-7.6-6.6 7.6H.5l8.6-9.8L0 1.2h7.6l5.2 6.9zm-1.3 19.5h2L6.5 3.2H4.3z"/></svg>',
    facebook: '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 22v-8.2h2.8l.4-3.2h-3.2V8.5c0-.9.3-1.6 1.6-1.6h1.7V4.1c-.3 0-1.3-.1-2.5-.1-2.5 0-4.2 1.5-4.2 4.3v2.4H7.3v3.2h2.8V22z"/></svg>',
    line: '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 3C6.5 3 2 6.6 2 11c0 3.9 3.5 7.2 8.3 7.9.3.1.8.2.9.5.1.3.1.7 0 1l-.1.9c0 .3-.2 1 .9.6 1.1-.5 6-3.5 8.2-6.1C21.7 14.2 22 12.7 22 11c0-4.4-4.5-8-10-8z"/><text x="12" y="13.6" text-anchor="middle" font-size="5.6" font-weight="700" font-family="Arial, Helvetica, sans-serif" fill="#fff">LINE</text></svg>',
    instagram: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.3" cy="6.7" r="1" fill="currentColor" stroke="none"/></svg>',
    link: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
    save: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M7 10l5 5 5-5"/><path d="M12 15V3"/></svg>'
  };
  var panel = null;
  function shareLinks() {
    var page = location.origin + location.pathname, text = T.cardTry, e = encodeURIComponent;   // no name in any of these (privacy line)
    return {
      page: page,
      threads: 'https://www.threads.net/intent/post?text=' + e(text + ' ' + page),
      x: 'https://twitter.com/intent/tweet?text=' + e(text) + '&url=' + e(page),
      facebook: 'https://www.facebook.com/sharer/sharer.php?u=' + e(page),
      line: 'https://social-plugins.line.me/lineit/share?url=' + e(page)
    };
  }
  function openShare(opener) {
    if (!cardJob) return;
    if (panel) closeShare();
    var job = cardJob, L = shareLinks(), fmt = '45', urls = {};
    var item = function (cls, icon, label, href) {
      return href ? '<a class="' + cls + '" href="' + esc(href) + '" target="_blank" rel="noopener"><span class="nshare-ic">' + ICON[icon] + '</span>' + esc(label) + '</a>'
        : '<button type="button" class="' + cls + '"><span class="nshare-ic">' + ICON[icon] + '</span><span class="nshare-lab">' + esc(label) + '</span></button>';
    };
    var el = document.createElement('div');
    el.className = 'nshare'; el.setAttribute('dir', root.getAttribute('dir') || 'ltr');
    el.innerHTML = '<div class="nshare-box" role="dialog" aria-modal="true" aria-labelledby="nshare-t">' +
      '<div class="nshare-head"><h2 id="nshare-t">' + esc(T.cardShare) + '</h2><button type="button" class="nshare-x" aria-label="' + esc(T.close) + '">✕</button></div>' +
      '<div class="nshare-tabs" role="tablist"><button type="button" role="tab" data-f="45" aria-selected="true">' + esc(T.fmtCard) + '</button><button type="button" role="tab" data-f="916" aria-selected="false">' + esc(T.fmtStory) + '</button></div>' +
      '<div class="nshare-img"><img alt="" hidden><span class="nshare-wait">…</span></div>' +
      '<div class="nshare-row">' +
        (SHARE_FILES ? item('nshare-phone', 'phone', T.phoneShare) : '') +
        item('nshare-ig', 'instagram', 'Instagram') +
        item('nshare-threads', 'threads', 'Threads', L.threads) + item('nshare-xx', 'x', 'X', L.x) +
        item('nshare-fb', 'facebook', 'Facebook', L.facebook) + item('nshare-line', 'line', 'LINE', L.line) +
        item('nshare-copy', 'link', T.share) + item('nshare-save', 'save', T.saveImg) +
      '</div><p class="nshare-note">' + esc(SHARE_FILES ? T.shareNote : T.shareNoteSave) + '</p></div>';   // no app-share button: the note only points to saving
    document.body.appendChild(el);
    var img = el.querySelector('.nshare-img img'), wait = el.querySelector('.nshare-wait');
    var show = function () {
      job.f[fmt].then(function (o) {
        if (!panel || panel.el !== el) return;
        if (!urls[fmt]) urls[fmt] = URL.createObjectURL(o.blob);
        if (o.fmt !== fmt) return;
        img.src = urls[fmt]; img.hidden = false; wait.hidden = true;
        img.alt = (fmt === '45' ? T.fmtCard : T.fmtStory) + ' · ' + job.m.hero;
        img.setAttribute('data-f', fmt);
      });
    };
    Array.prototype.forEach.call(el.querySelectorAll('[role=tab]'), function (t) {
      t.onclick = function () {
        fmt = t.getAttribute('data-f');
        Array.prototype.forEach.call(el.querySelectorAll('[role=tab]'), function (x) { x.setAttribute('aria-selected', x === t ? 'true' : 'false'); });
        show();
      };
    });
    var now = function (f) { var o = job.done[fmt]; if (o) f(o); else job.f[fmt].then(f); };
    var ph = el.querySelector('.nshare-phone');
    if (ph) ph.onclick = function () {
      now(function (o) {
        if (!o.file) { downloadCard(o); return; }
        navigator.share({ files: [o.file], title: 'Nadri', text: T.cardTry + ' ' + L.page }).catch(function (err) { if (!err || err.name !== 'AbortError') downloadCard(o); });
      });
    };
    // Instagram has no web share link (owner [7eb4ec94#2626]): with an app share sheet, send the image there (pick Instagram);
    // otherwise save the image and open Instagram, with a one-line hint
    el.querySelector('.nshare-ig').onclick = function () {
      now(function (o) {
        if (SHARE_FILES && o.file) {
          navigator.share({ files: [o.file], title: 'Nadri', text: T.cardTry + ' ' + L.page }).catch(function (err) { if (!err || err.name !== 'AbortError') downloadCard(o); });
          return;
        }
        downloadCard(o);
        window.open('https://www.instagram.com/', '_blank', 'noopener');
        var IG = { ko: '이미지를 저장했어요. 인스타그램에서 + 를 눌러 올려 주세요.', ja: '画像を保存しました。Instagramの「+」から投稿してください。', 'zh-tw': '圖片已儲存。到 Instagram 按「+」上傳。' };
        el.querySelector('.nshare-note').textContent = IG[LANG] || 'Image saved. Open Instagram and tap + to post it.';
      });
    };
    el.querySelector('.nshare-save').onclick = function () { now(downloadCard); };
    el.querySelector('.nshare-copy').onclick = function (ev) {
      var lab = el.querySelector('.nshare-copy .nshare-lab');
      (navigator.clipboard ? navigator.clipboard.writeText(L.page) : Promise.reject()).then(function () { lab.textContent = T.copied; }, function () { prompt('', L.page); });
    };
    el.querySelector('.nshare-x').onclick = closeShare;
    // outside click: close on 'click' (after the browser's own focus change), only if the press also started on the backdrop
    var downOut = false;
    el.addEventListener('mousedown', function (ev) { downOut = ev.target === el; });
    el.addEventListener('click', function (ev) { if (ev.target === el && downOut) closeShare(); });
    var keys = function (ev) {
      if (ev.key === 'Escape') { ev.preventDefault(); closeShare(); return; }
      if (ev.key !== 'Tab') return;
      var f = Array.prototype.filter.call(el.querySelectorAll('button, a[href]'), function (x) { return x.offsetParent !== null; });
      if (!f.length) return;
      if (ev.shiftKey && document.activeElement === f[0]) { ev.preventDefault(); f[f.length - 1].focus(); }
      else if (!ev.shiftKey && document.activeElement === f[f.length - 1]) { ev.preventDefault(); f[0].focus(); }
    };
    document.addEventListener('keydown', keys);
    panel = { el: el, opener: opener, keys: keys, urls: urls, overflow: document.body.style.overflow };
    document.body.style.overflow = 'hidden';
    el.querySelector('[role=tab][aria-selected=true]').focus();
    show();
  }
  function closeShare() {
    if (!panel) return;
    var p0 = panel; panel = null;
    document.removeEventListener('keydown', p0.keys);
    document.body.style.overflow = p0.overflow;
    p0.el.remove();
    Object.keys(p0.urls).forEach(function (k) { URL.revokeObjectURL(p0.urls[k]); });
    if (p0.opener && p0.opener.focus) p0.opener.focus();
  }

  shell();
  var q = params.get('n');
  if (q) { input.value = q; render(q); }

  window.NadriName = { convert: convert, setLang: function (l) { applyLang(l); shell(); }, card: function (fmt) { return cardJob && cardJob.f[fmt || '916'].then(function (o) { return Object.assign({ m: cardJob.m }, o); }); } }; // for tests
})();
