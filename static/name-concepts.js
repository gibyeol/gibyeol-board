/* Meaning concepts: one meaning, the real given names that carry it around the world, and the Korean story it leads to.
   names: [language, name, native script or note]. Only names whose meaning is standard in name dictionaries (Behind the Name and the like).
   hanja: characters (used in Korean, Japanese and Chinese names) that carry the concept. latin: name keys in NADRI_NAMES with this meaning.
   chain: id in NADRI_CHAINS. Added 2026-11-25; extend nightly. */
window.NADRI_CONCEPTS = {
  star: { ko: '별', en: 'star', ja: '星', zh: '星', hanja: '星辰奎斗', latin: ['stella'], chain: 'dipper',
    names: [['Latin / Italian', 'Stella'], ['Spanish', 'Estrella'], ['Greek', 'Aster', 'Αστήρ'], ['Sanskrit / Hindi', 'Tara', 'तारा'], ['Arabic', 'Najma', 'نجمة'], ['Persian', 'Setareh', 'ستاره'], ['Turkish', 'Yıldız'], ['Welsh', 'Seren'], ['Serbian', 'Zvezdana', 'Звездана'], ['Japanese', 'Hoshiko', '星子'], ['Chinese', 'Xing', '星'], ['Korean', 'Hanbyeol', '한별']] },
  first: { ko: '으뜸·처음', en: 'first, origin', ja: '始まり', zh: '首、元', hanja: '元一始初', latin: [],
    names: [['Italian', 'Primo / Prima'], ['Japanese', 'Hajime', '元・一'], ['Chinese', 'Yuan', '元']] },
  wisdom: { ko: '지혜', en: 'wisdom', ja: '知恵', zh: '智慧', hanja: '智慧叡哲賢知', latin: ['sophia'], chain: 'wisdom',
    names: [['Greek', 'Sophia', 'Σοφία'], ['Spanish', 'Sofía'], ['French', 'Sophie'], ['Polish', 'Zofia'], ['Russian', 'Sofiya', 'София'], ['Arabic', 'Hikmat', 'حكمت'], ['Turkish', 'Bilge'], ['Japanese', 'Chie', '智恵'], ['Chinese', 'Hui', '慧'], ['Korean', 'Seulgi', '슬기']] },
  light: { ko: '빛·밝음', en: 'light, bright', ja: '光', zh: '光明', hanja: '光明昭炫晟炯輝煥熙燦赫亮耀晃炳', latin: [],
    names: [['Latin / Italian', 'Lucia'], ['English', 'Lucy'], ['Arabic', 'Nur', 'نور'], ['Russian', 'Svetlana', 'Светлана'], ['Sanskrit / Hindi', 'Jyoti', 'ज्योति'], ['Turkish', 'Aydın'], ['Japanese', 'Hikari', '光'], ['Chinese', 'Guang', '光'], ['Korean', 'Bitna', '빛나']] },
  sky: { ko: '하늘', en: 'sky, heaven', ja: '空', zh: '天', hanja: '天昊旻空乾', latin: [],
    names: [['Latin / Spanish / Italian', 'Celeste'], ['Greek', 'Ourania', 'Ουρανία'], ['Sanskrit / Hindi', 'Akash', 'आकाश'], ['Arabic', 'Samaa', 'سماء'], ['Japanese', 'Sora', '空'], ['Chinese', 'Tian', '天'], ['Korean', 'Haneul', '하늘']] },
  sea: { ko: '바다·물', en: 'sea, water', ja: '海', zh: '海', hanja: '海洋洙浩河淵潭湖', latin: [],
    names: [['Latin / Italian / Spanish', 'Marina'], ['Hawaiian', 'Kai'], ['Hawaiian / Māori', 'Moana'], ['Turkish', 'Derya'], ['Spanish / Portuguese', 'Rio (river)'], ['Japanese', 'Umi', '海'], ['Chinese', 'Hai', '海'], ['Korean', 'Bada', '바다']] },
  flower: { ko: '꽃', en: 'flower', ja: '花', zh: '花', hanja: '花華英芳菊蘭梅蕙薇', latin: ['lily', 'rose'],
    names: [['Latin', 'Flora'], ['Greek', 'Anthea', 'Ἄνθεια'], ['Hawaiian', 'Pua'], ['Turkish', 'Çiçek'], ['Arabic', 'Zahra', 'زهراء'], ['English', 'Blossom'], ['Japanese', 'Hana', '花'], ['Chinese', 'Hua', '華']] },
  lotus: { ko: '연꽃', en: 'lotus', ja: '蓮', zh: '蓮', hanja: '蓮荷', latin: [],
    names: [['Sanskrit / Hindi', 'Padma', 'पद्म'], ['Sanskrit / Hindi', 'Kamala', 'कमला'], ['Persian', 'Nilufar', 'نیلوفر'], ['Japanese', 'Ren', '蓮'], ['Chinese', 'Lian', '蓮'], ['Hindi', 'Nalini', 'नलिनी'], ['Vietnamese', 'Liên', '蓮'], ['Thai', 'Ubon']] },
  /* 2026-11-28: concepts for common Japanese given names (明治安田 2025). Names and meanings read on Behind the Name 'meaning' searches
     (behindthename.com/names/meaning/harbour, green, jasmine, silk), saved in wondu-archive raw-from-scratchpad/names-2026-11-28/btn/. */
  harbour: { ko: '항구', en: 'harbour', ja: '港(みなと)', zh: '港口', hanja: '湊港', latin: [],
    names: [['Japanese', 'Minato', '湊・港'], ['Arabic', 'Bandar']] },
  green: { ko: '초록', en: 'green', ja: '緑', zh: '綠', hanja: '翠緑碧青', latin: [],
    names: [['Greek', 'Chloe'], ['Greek', 'Chloris'], ['Arabic', 'Khadra'], ['Albanian', 'Blerta'], ['Japanese', 'Midori', '緑'], ['Japanese', 'Sui', '翠'], ['Chinese', 'Qing', '青'], ['Vietnamese', 'Bích', '碧']] },
  jasmine: { ko: '재스민', en: 'jasmine', ja: '茉莉(ジャスミン)', zh: '茉莉', hanja: '茉莉', latin: [],
    names: [['Arabic', 'Yasmin'], ['English', 'Jasmine'], ['Turkish', 'Yasemin'], ['Spanish', 'Jazmín'], ['Italian', 'Gelsomina'], ['Armenian', 'Hasmik'], ['Tamil', 'Mallika'], ['Indonesian', 'Melati']] },
  silk: { ko: '비단', en: 'silk', ja: '絹・紬', zh: '絲綢', hanja: '紬紗', latin: [],
    names: [['Turkish', 'İpek'], ['Hindi', 'Reshma'], ['Japanese', 'Tsumugi', '紬']] },
  spring: { ko: '봄', en: 'spring', ja: '春', zh: '春', hanja: '春', latin: [],
    names: [['Persian / Turkish', 'Bahar'], ['Slavic', 'Vesna', 'Весна'], ['Japanese', 'Haru', '春'], ['Chinese', 'Chun', '春'], ['Korean', 'Bom', '봄']] },
  summer: { ko: '여름', en: 'summer', ja: '夏', zh: '夏', hanja: '夏昰', latin: [], names: [['English', 'Summer'], ['Japanese', 'Natsu', '夏'], ['Chinese', 'Xia', '夏']] },
  autumn: { ko: '가을', en: 'autumn', ja: '秋', zh: '秋', hanja: '秋', latin: [], names: [['English', 'Autumn'], ['Japanese', 'Aki', '秋'], ['Chinese', 'Qiu', '秋']] },
  snow: { ko: '눈', en: 'snow', ja: '雪', zh: '雪', hanja: '雪', latin: [], chain: 'snow',
    names: [['Italian', 'Neve'], ['Spanish', 'Nieves'], ['Japanese', 'Yuki', '雪'], ['Chinese', 'Xue', '雪']] },
  moon: { ko: '달', en: 'moon', ja: '月', zh: '月', hanja: '月', latin: [],
    names: [['Latin / Spanish / Italian', 'Luna'], ['Greek', 'Selene', 'Σελήνη'], ['Sanskrit / Hindi', 'Chandra', 'चन्द्र'], ['Arabic', 'Qamar', 'قمر'], ['Turkish', 'Aylin'], ['Chinese', 'Yue', '月']] },
  sun: { ko: '해·볕', en: 'sun', ja: '陽', zh: '陽', hanja: '陽日暉曦', latin: [],
    names: [['Spanish', 'Sol'], ['Greek', 'Helios', 'Ἥλιος'], ['Sanskrit / Hindi', 'Surya', 'सूर्य'], ['Arabic', 'Shams', 'شمس'], ['Turkish', 'Güneş'], ['Japanese', 'Hinata', '陽向'], ['Chinese', 'Yang', '陽']] },
  dawn: { ko: '새벽', en: 'dawn', ja: '暁', zh: '曉', hanja: '曉晨', latin: [],
    names: [['Latin', 'Aurora'], ['English', 'Dawn'], ['Greek', 'Eos', 'Ἠώς'], ['Sanskrit / Hindi', 'Usha', 'उषा'], ['Arabic', 'Fajr', 'فجر'], ['Turkish', 'Şafak'], ['Chinese', 'Xiao', '曉']] },
  peace: { ko: '평화', en: 'peace', ja: '平和', zh: '和平', hanja: '平和安康靜', latin: ['irene', 'olivia'], chain: 'peace',
    names: [['Greek', 'Irene', 'Ειρήνη'], ['Spanish', 'Paz'], ['Germanic', 'Frida'], ['Hebrew', 'Shalom', 'שָׁלוֹם'], ['Sanskrit / Hindi', 'Shanti', 'शान्ति'], ['Turkish', 'Barış'], ['Japanese', 'Kazu', '和'], ['Chinese', 'Ping', '平']] },
  joy: { ko: '기쁨', en: 'joy', ja: '喜び', zh: '喜悅', hanja: '喜怡欣樂楽熙', latin: ['joy', 'felix'],
    names: [['English', 'Joy'], ['Latin', 'Felicity'], ['Italian', 'Gioia'], ['Sanskrit / Hindi', 'Ananda', 'आनन्द'], ['Arabic', 'Farah', 'فرح'], ['Turkish', 'Sevinç'], ['Chinese', 'Xin', '欣']] },
  love: { ko: '사랑', en: 'love', ja: '愛', zh: '愛', hanja: '愛慈', latin: ['david'],
    names: [['Latin / English', 'Amanda'], ['Hebrew', 'David', 'דָּוִד'], ['Sanskrit / Hindi', 'Priya', 'प्रिया'], ['Arabic', 'Habiba', 'حبيبة'], ['Turkish', 'Sevgi'], ['Russian', 'Lyubov', 'Любовь'], ['Japanese', 'Ai', '愛'], ['Korean', 'Sarang', '사랑']] },
  hope: { ko: '희망', en: 'hope', ja: '希望', zh: '希望', hanja: '希望願', latin: ['hope'],
    names: [['English', 'Hope'], ['Spanish', 'Esperanza'], ['Greek', 'Elpida', 'Ελπίδα'], ['Russian', 'Nadezhda', 'Надежда'], ['Arabic', 'Amal', 'أمل'], ['Turkish', 'Umut'], ['Sanskrit / Hindi', 'Asha', 'आशा'], ['Japanese', 'Nozomi', '望']] },
  grace: { ko: '은혜', en: 'grace, blessing', ja: '恵み', zh: '恩典', hanja: '恩惠恵祐祥瑞', latin: ['grace', 'anna', 'john'],
    names: [['English', 'Grace'], ['Hebrew', 'Hannah', 'חַנָּה'], ['Spanish', 'Gracia'], ['Sanskrit / Hindi', 'Kripa', 'कृपा'], ['Japanese', 'Megumi', '恵'], ['Korean', 'Eunhye', '은혜']] },
  beauty: { ko: '아름다움', en: 'beauty', ja: '美', zh: '美', hanja: '美佳娥妍媛娜婷嘉', latin: [],
    names: [['Italian', 'Bella'], ['Greek', 'Callista', 'Καλλίστη'], ['Arabic', 'Jamila', 'جميلة'], ['Sanskrit / Hindi', 'Sundari', 'सुन्दरी'], ['Japanese', 'Mika', '美香'], ['Chinese', 'Mei', '美'], ['Korean', 'Areum', '아름']] },
  brave: { ko: '용기·굳셈', en: 'brave, strong', ja: '勇', zh: '勇', hanja: '勇健雄豪桓', latin: ['andrew'],
    names: [['Greek', 'Andreas', 'Ανδρέας'], ['Latin', 'Valentin'], ['Japanese', 'Isamu', '勇'], ['Chinese', 'Yong', '勇']] },
  kind: { ko: '어짊', en: 'kind, benevolent', ja: '仁', zh: '仁', hanja: '仁善順淳', latin: [],
    names: [['Latin', 'Clement'], ['Arabic', 'Karim', 'كريم'], ['Sanskrit / Hindi', 'Daya', 'दया'], ['Japanese', 'Hitoshi', '仁'], ['Chinese', 'Ren', '仁']] },
  truth: { ko: '참·정성', en: 'true, sincere', ja: '誠', zh: '真', hanja: '眞真誠貞信', latin: [],
    names: [['Greek', 'Alethea', 'Ἀλήθεια'], ['Russian', 'Vera', 'Вера'], ['Sanskrit / Hindi', 'Satya', 'सत्य'], ['Arabic', 'Sadiq', 'صادق'], ['English', 'Faith'], ['Japanese', 'Makoto', '誠'], ['Chinese', 'Zhen', '真']] },
  gold: { ko: '금', en: 'gold', ja: '金', zh: '金', hanja: '金', latin: [],
    names: [['Latin', 'Aurelia / Aurelio'], ['Armenian / Hindi', 'Sona'], ['Chinese', 'Jin', '金']] },
  jewel: { ko: '옥·보배', en: 'jade, jewel', ja: '玉', zh: '玉', hanja: '玉珠瑛珉玟琪瓊寶珍琳瑜圭珪', latin: ['margaret'],
    names: [['English / French', 'Jade'], ['Italian', 'Gemma'], ['Greek', 'Margarita (pearl)', 'Μαργαρίτα'], ['Arabic', 'Lulu (pearl)', 'لؤلؤ'], ['Indonesian', 'Mutiara (pearl)'], ['Sanskrit / Hindi', 'Ratna', 'रत्न'], ['Japanese', 'Tama', '玉'], ['Chinese', 'Yu', '玉']] },
  forest: { ko: '나무·숲', en: 'tree, forest', ja: '森', zh: '林', hanja: '林森樹松柏栗杜', latin: [],
    names: [['Latin', 'Silvia'], ['Hebrew', 'Oren (pine)', 'אורן'], ['Japanese', 'Shin', '森'], ['Chinese', 'Lin', '林']] },
  dragon: { ko: '용', en: 'dragon', ja: '龍', zh: '龍', hanja: '龍竜', latin: [], chain: 'king',
    names: [['Greek / Latin', 'Draco'], ['English', 'Drake'], ['Japanese', 'Ryu', '龍'], ['Chinese', 'Long', '龍']] },
  tiger: { ko: '범', en: 'tiger', ja: '虎', zh: '虎', hanja: '虎寅', latin: [],
    names: [['Persian / Hindi', 'Sher'], ['Persian', 'Babur'], ['Japanese', 'Tora', '虎'], ['Chinese', 'Hu', '虎']] },
  king: { ko: '임금·다스림', en: 'king, ruler', ja: '王', zh: '王', hanja: '王君尹宰', latin: ['henry'], chain: 'king',
    names: [['Latin', 'Rex'], ['Greek', 'Basil', 'Βασίλειος'], ['French', 'Leroy'], ['Arabic', 'Malik', 'مالك'], ['Sanskrit / Hindi', 'Raja', 'राजा'], ['Chinese', 'Wang', '王']] },
  life: { ko: '생명·장수', en: 'life, long life', ja: '命', zh: '生命', hanja: '壽命生久', latin: ['zoe', 'eva'],
    names: [['Greek', 'Zoe', 'Ζωή'], ['Latin', 'Vita'], ['Hebrew', 'Chaim', 'חיים'], ['Arabic / Turkish', 'Hayat'], ['Japanese', 'Hisashi', '久'], ['Chinese', 'Shou', '壽']] },
  victory: { ko: '승리', en: 'victory', ja: '勝利', zh: '勝利', hanja: '勝', latin: ['victoria'],
    names: [['Latin', 'Victoria / Victor'], ['Greek', 'Nicole / Nicholas'], ['Arabic / Persian', 'Zafar', 'ظفر'], ['Turkish', 'Zafer'], ['Sanskrit / Hindi', 'Vijay', 'विजय'], ['Japanese', 'Masaru', '勝'], ['Chinese', 'Sheng', '勝']] },
  pure: { ko: '맑음·깨끗함', en: 'pure, clear', ja: '清', zh: '潔', hanja: '潔淸清晶雅淡素', latin: [],
    names: [['Arabic', 'Tahira', 'طاهرة'], ['Arabic', 'Safiya', 'صفية'], ['Japanese', 'Kiyoshi', '清'], ['Chinese', 'Jie', '潔']] },
  eternal: { ko: '영원', en: 'eternal', ja: '永遠', zh: '永恆', hanja: '永久長遠', latin: [],
    names: [['Latin', 'Perpetua'], ['Persian', 'Sarmad', 'سرمد'], ['Sanskrit / Hindi', 'Anant', 'अनन्त'], ['Japanese', 'Hisashi', '永'], ['Chinese', 'Yong', '永']] },
  east: { ko: '동녘', en: 'east, sunrise', ja: '東', zh: '東', hanja: '東', latin: [], names: [['Greek', 'Anatole', 'Ἀνατολή'], ['Japanese', 'Azuma', '東'], ['Chinese', 'Dong', '東']] },
  great: { ko: '큼', en: 'great', ja: '大', zh: '大', hanja: '大太泰偉碩宏浩', latin: [], names: [['Latin', 'Magnus'], ['Arabic', 'Akbar', 'أكبر'], ['Japanese', 'Futoshi', '太'], ['Chinese', 'Da', '大']] },
  universe: { ko: '우주', en: 'universe', ja: '宇宙', zh: '宇宙', hanja: '宇宙', latin: [], names: [['Greek', 'Cosmo', 'Κόσμος'], ['Japanese', 'Sora', '宙'], ['Chinese', 'Yu', '宇']] },
  song: { ko: '노래·소리', en: 'song, music', ja: '音', zh: '音', hanja: '音詩韶', latin: [], names: [['English', 'Melody'], ['Hebrew', 'Shira', 'שירה'], ['Sanskrit / Hindi', 'Gita', 'गीता'], ['Chinese', 'Yin', '音']] },
  writing: { ko: '글', en: 'writing, letters', ja: '文', zh: '文', hanja: '文書', latin: [], names: [['Japanese', 'Fumi', '文'], ['Chinese', 'Wen', '文']] },
  guard: { ko: '지킴', en: 'guard, protect', ja: '守', zh: '守', hanja: '守護佑', latin: ['liam', 'william', 'alexander'], chain: 'guard',
    names: [['Germanic / English', 'William'], ['Irish', 'Liam'], ['Greek', 'Alexander', 'Ἀλέξανδρος'], ['Japanese', 'Mamoru', '守'], ['Chinese', 'Shou', '守']] },
  rest: { ko: '쉼', en: 'rest, comfort', ja: '安らぎ', zh: '安息', hanja: '安', latin: ['noah'], chain: 'rest',
    names: [['Hebrew', 'Noah', 'נֹחַ'], ['Arabic', 'Nuh', 'نوح'], ['Japanese', 'Yasushi', '安']] }
};
window.NADRI_CONCEPT_OF = (function () {
  var o = { hanja: {}, latin: {} }, C = window.NADRI_CONCEPTS;
  Object.keys(C).forEach(function (k) {
    (C[k].hanja || '').split('').forEach(function (h) { if (!o.hanja[h]) o.hanja[h] = k; });
    (C[k].latin || []).forEach(function (n) { if (!o.latin[n]) o.latin[n] = k; });
  });
  o.hanja['斗'] = 'star';
  return o;
})();

/* "If you were born in…": the name a child with this meaning would be given in each country, why, and how sure we are (%).
   Base: the earlier name-tool conversation (trendmin-threads ops/name-tool.md, appendix). Native-speaker review pending; low confidence = on hold. */
window.NADRI_BORN = {
  dipper: { phrase: { ko: '길을 알려주는 별', en: 'the star that shows the way', ja: '道を示す星', zh: '指引方向的星' }, first: { ko: '길을 알려주는 첫 번째 별', en: 'the first star that shows the way', ja: '道を示す一番の星', zh: '指引方向的第一顆星' },
    c: [
      ['🇯🇵', { ko: '일본', en: 'Japan', ja: '日本', zh: '日本' }, 'Hokuto', '北斗 (ホクト)', { ko: '북두칠성이라는 뜻 그대로 쓰는 실제 일본 남자 이름. 일본에서 "호쿠토"라고 하면 바로 별을 떠올려요.', en: 'The Big Dipper itself: a real Japanese boy\'s name that makes people think of the stars.' }, 85],
      ['🇹🇼', { ko: '대만·중화권', en: 'Taiwan', ja: '台湾・中華圏', zh: '台灣・華人圈' }, 'Beichen', '北辰', { ko: '北辰은 북극성. 《논어》에서 덕으로 다스리는 사람을 북극성에 빗댔어요(為政以德, 譬如北辰). 사람들이 따르는 리더라는 뜻이 더해져요.', en: 'The North Star. In the Analects, a ruler of virtue is compared to it (為政以德，譬如北辰): the star everyone follows.' }, 75],
      ['🇬🇧', { ko: '영국·영어권', en: 'UK', ja: 'イギリス・英語圏', zh: '英國・英語圈' }, 'Arthur', '', { ko: '북두칠성을 포함한 큰곰자리를 영국 민간에서 "Arthur\'s Wain(아서왕의 수레)"이라고 불렀어요. 어원이 \'곰\'이라는 설도 있어요(학설이 갈림).', en: 'The Plough was called "Arthur\'s Wain" in English folk tradition, the king whose chariot crosses the sky. The name may come from a word for bear (disputed).' }, 60],
      ['🇪🇸', { ko: '스페인어권', en: 'Spain', ja: 'スペイン語圏', zh: '西語圈' }, 'Santiago', '', { ko: '은하수를 "산티아고의 길"이라 부르고 순례자들이 그 별길을 따라 걸었다는 전승. 북두칠성은 아니지만 \'밤하늘이 길을 알려준다\'는 뜻이 같아요.', en: 'The Milky Way was called the Way of Saint James, and pilgrims followed it: the road of stars. Not the Dipper, but the same idea of a sky that shows the way.' }, 65],
      ['🇹🇭', { ko: '태국', en: 'Thailand', ja: 'タイ', zh: '泰國' }, 'Dao', 'ดาว (ดาวเหนือ)', { ko: '태국은 본명 외에 짧은 별명(츠렌)을 써요. ดาวเหนือ는 \'북쪽 별\', ดาว(다오)는 \'별\'. 태국 친구들은 당신을 Dao라고 부를 거예요.', en: 'Thais use a short nickname besides their full name. ดาวเหนือ is the North Star and ดาว (Dao) means star: your Thai friends would call you Dao.' }, 70],
      ['🇻🇳', { ko: '베트남', en: 'Vietnam', ja: 'ベトナム', zh: '越南' }, null, 'Lý Nguyên Đẩu', { ko: '한자 독음은 정확하지만, 같은 뜻의 자연스러운 베트남 이름은 원어민 검수 전까지 보류해요.', en: 'The Sino-Vietnamese reading is exact, but a natural Vietnamese name with the same meaning waits for a native speaker.' }, 0]
    ] },
  star: { phrase: { ko: '별', en: 'a star', ja: '星', zh: '星' }, first: { ko: '첫 번째 별', en: 'the first star', ja: '一番星', zh: '第一顆星' },
    c: [
      ['🇯🇵', { ko: '일본', en: 'Japan' }, 'Hoshiko', '星子', { ko: '별(星)을 넣은 일본 여자 이름.', en: 'A Japanese girl\'s name built on 星, star.' }, 75],
      ['🇹🇼', { ko: '대만', en: 'Taiwan' }, 'Xing', '星', { ko: '이름에 자주 쓰는 \'별\' 글자.', en: 'The character for star, common in Taiwanese names.' }, 70],
      ['🇬🇧', { ko: '영국', en: 'UK' }, 'Stella', '', { ko: '라틴어로 \'별\'.', en: 'Latin for star.' }, 95],
      ['🇪🇸', { ko: '스페인', en: 'Spain' }, 'Estrella', '', { ko: '스페인어로 \'별\'.', en: 'Spanish for star.' }, 90],
      ['🇹🇭', { ko: '태국', en: 'Thailand' }, 'Dao', 'ดาว', { ko: '\'별\'이라는 뜻의 태국 별명.', en: 'Thai nickname meaning star.' }, 80],
      ['🇹🇷', { ko: '튀르키예', en: 'Türkiye' }, 'Yıldız', '', { ko: '튀르키예어로 \'별\'.', en: 'Turkish for star.' }, 90],
      ['🇮🇳', { ko: '인도', en: 'India' }, 'Tara', 'तारा', { ko: '산스크리트어로 \'별\'.', en: 'Sanskrit for star.' }, 90],
      ['🇸🇦', { ko: '아랍권', en: 'Arab world' }, 'Najma', 'نجمة', { ko: '아랍어로 \'별\'.', en: 'Arabic for star.' }, 85]
    ] },
  wisdom: { phrase: { ko: '지혜', en: 'wisdom', ja: '知恵', zh: '智慧' },
    c: [
      ['🇯🇵', { ko: '일본', en: 'Japan' }, 'Chie', '智恵 (ちえ)', { ko: '\'지혜\'를 그대로 이름으로 쓴 일본 여자 이름.', en: 'A Japanese girl\'s name that is the word for wisdom.' }, 85],
      ['🇹🇼', { ko: '대만', en: 'Taiwan' }, 'Hui', '慧', { ko: '대만 이름에 흔한 \'슬기로울 혜\'.', en: 'The character for wisdom, common in Taiwanese names.' }, 80],
      ['🇬🇧', { ko: '영국', en: 'UK' }, 'Sophia', '', { ko: '그리스어로 \'지혜\'.', en: 'Greek for wisdom.' }, 95],
      ['🇪🇸', { ko: '스페인', en: 'Spain' }, 'Sofía', '', { ko: 'Sophia의 스페인어 형태.', en: 'The Spanish form of Sophia.' }, 95],
      ['🇹🇭', { ko: '태국', en: 'Thailand' }, 'Panya', 'ปัญญา', { ko: '\'지혜\'라는 뜻의 태국 이름.', en: 'A Thai name meaning wisdom.' }, 75],
      ['🇹🇷', { ko: '튀르키예', en: 'Türkiye' }, 'Bilge', '', { ko: '\'지혜로운\'이라는 뜻.', en: 'Means wise.' }, 80],
      ['🇸🇦', { ko: '아랍권', en: 'Arab world' }, 'Hikmat', 'حكمت', { ko: '\'지혜\'라는 뜻.', en: 'Means wisdom.' }, 75]
    ] },
  peace: { phrase: { ko: '평화', en: 'peace', ja: '平和', zh: '和平' },
    c: [
      ['🇯🇵', { ko: '일본', en: 'Japan' }, 'Kazuko', '和子', { ko: '\'화할 화(和)\'를 쓴 일본 이름.', en: 'A Japanese name built on 和, harmony and peace.' }, 80],
      ['🇹🇼', { ko: '중화권', en: 'Chinese-speaking world' }, 'Heping', '和平', { ko: '\'평화\'를 그대로 쓴 이름.', en: 'The word for peace, used as a name.' }, 70],
      ['🇬🇧', { ko: '영국', en: 'UK' }, 'Irene', '', { ko: '그리스어로 \'평화\'.', en: 'Greek for peace.' }, 90],
      ['🇪🇸', { ko: '스페인', en: 'Spain' }, 'Paz', '', { ko: '스페인어로 \'평화\'.', en: 'Spanish for peace.' }, 90],
      ['🇹🇭', { ko: '태국', en: 'Thailand' }, 'Santi', 'สันติ', { ko: '\'평화\'라는 뜻의 태국 이름.', en: 'A Thai name meaning peace.' }, 80],
      ['🇹🇷', { ko: '튀르키예', en: 'Türkiye' }, 'Barış', '', { ko: '튀르키예어로 \'평화\'.', en: 'Turkish for peace.' }, 90],
      ['🇮🇳', { ko: '인도', en: 'India' }, 'Shanti', 'शान्ति', { ko: '산스크리트어로 \'평화\'.', en: 'Sanskrit for peace.' }, 85]
    ] },
  light: { phrase: { ko: '빛', en: 'light', ja: '光', zh: '光' },
    c: [
      ['🇯🇵', { ko: '일본', en: 'Japan' }, 'Hikari', '光 (ひかり)', { ko: '\'빛\'을 그대로 쓴 일본 이름.', en: 'The Japanese word for light, used as a name.' }, 90],
      ['🇹🇼', { ko: '대만', en: 'Taiwan' }, 'Guang', '光', { ko: '이름에 쓰는 \'빛 광\'.', en: 'The character for light, used in names.' }, 70],
      ['🇬🇧', { ko: '영국', en: 'UK' }, 'Lucy', '', { ko: '라틴어 lux(빛)에서 온 이름.', en: 'From Latin lux, light.' }, 85],
      ['🇪🇸', { ko: '스페인', en: 'Spain' }, 'Lucía', '', { ko: 'Lucy의 스페인어 형태.', en: 'The Spanish form of Lucy.' }, 85],
      ['🇹🇭', { ko: '태국', en: 'Thailand' }, 'Saeng', 'แสง', { ko: '\'빛\'이라는 뜻의 태국 이름·별명.', en: 'Thai for light, used as a name.' }, 70],
      ['🇸🇦', { ko: '아랍권', en: 'Arab world' }, 'Nur', 'نور', { ko: '아랍어로 \'빛\'.', en: 'Arabic for light.' }, 90],
      ['🇷🇺', { ko: '러시아', en: 'Russia' }, 'Svetlana', 'Светлана', { ko: '\'빛\'에서 온 슬라브 이름.', en: 'A Slavic name from the word for light.' }, 85]
    ] }
};
window.NADRI_BORN_OF = { hanja: { '斗': 'dipper', '北': 'dipper', '辰': 'dipper', '星': 'star', '奎': 'star', '智': 'wisdom', '慧': 'wisdom', '叡': 'wisdom', '哲': 'wisdom', '賢': 'wisdom', '知': 'wisdom', '平': 'peace', '和': 'peace', '光': 'light', '明': 'light', '昭': 'light', '炫': 'light', '輝': 'light', '晟': 'light', '炯': 'light' }, latin: { sophia: 'wisdom', stella: 'star', irene: 'peace', olivia: 'peace' }, native: { '별': 'star', '한별': 'star', '슬기': 'wisdom', '빛나': 'light' } };
