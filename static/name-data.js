/* Nadri name tool data, v2 (2026-11-25).
   NAMES: checked common names. Each: sound in Korean (ko), Japanese katakana (ja), Taiwanese Mandarin characters (zh),
   origin, meaning in 4 UI languages, confidence (h = well documented, m = likely, l = uncertain),
   the meaning as a word in ko/ja/zh, a name built from the same meaning where one exists naturally, and a chain id.
   Meanings follow standard etymologies as summarised by Behind the Name (behindthename.com); add a name only after checking it there.
   KANJI: characters common in names, with the Korean way of teaching them (meaning + sound, 훈음) and an English gloss.
   CHAINS: meaning -> story -> place -> our guide. Every step must be a checked fact; sources are listed on the page. */
window.NADRI_NAMES = {
  sophia: { ko: '소피아', ja: 'ソフィア', zh: '蘇菲亞', o: 'Greek', c: 'h', m: { en: 'wisdom', ko: '지혜', ja: '知恵', zh: '智慧' }, w: { ko: '지혜', ja: '知恵(ちえ)', zh: '智慧' }, i: { ko: '지혜 · 슬기', ja: '智恵(ちえ)', zh: '慧' }, ch: 'wisdom' },
  sofia: 'sophia', sophie: 'sophia',
  olivia: { ko: '올리비아', ja: 'オリビア', zh: '奧莉維亞', o: 'Latin', c: 'h', m: { en: 'olive tree (made popular by Shakespeare)', ko: '올리브나무 (셰익스피어 작품으로 널리 쓰임)', ja: 'オリーブの木(シェイクスピア作品で広まった)', zh: '橄欖樹(因莎士比亞作品而流行)' }, w: { ko: '올리브', ja: 'オリーブ', zh: '橄欖' }, ch: 'peace' },
  emma: { ko: '에마', ja: 'エマ', zh: '艾瑪', o: 'Germanic', c: 'h', m: { en: 'whole, universal', ko: '온전한, 온 세상의', ja: 'すべての、完全な', zh: '完整的、普世的' }, w: { ko: '온전함', ja: '完全', zh: '完整' }, i: { ko: '온', ja: '円(まどか)', zh: '全' } },
  liam: { ko: '리엄', ja: 'リアム', zh: '連恩', o: 'Irish, from William', c: 'h', m: { en: 'will + helmet: a resolute protector', ko: '의지 + 투구: 굳센 수호자', ja: '意志+兜:揺るがない守り手', zh: '意志+頭盔:堅定的守護者' }, w: { ko: '수호', ja: '守護', zh: '守護' }, i: { ko: '수호', ja: '守(まもる)', zh: '守' }, ch: 'guard' },
  william: 'liam',
  noah: { ko: '노아', ja: 'ノア', zh: '諾亞', o: 'Hebrew', c: 'h', m: { en: 'rest, comfort', ko: '쉼, 위로', ja: '休息、慰め', zh: '安息、安慰' }, w: { ko: '쉼', ja: '安らぎ', zh: '安息' }, i: { ko: '안식 · 쉼', ja: '安(やす)', zh: '安' }, ch: 'rest' },
  james: { ko: '제임스', ja: 'ジェームズ', zh: '詹姆士', o: 'Hebrew, via Latin Iacomus (Jacob)', c: 'h', m: { en: 'the same name as Jacob; in Spanish, Saint James became Santiago', ko: '야곱과 같은 이름. 스페인어로 성 야고보(Saint James)가 산티아고가 됐어요', ja: 'ヤコブと同じ名前。スペイン語で聖ヤコブ(Saint James)がサンティアゴに', zh: '與雅各同源。西班牙文的聖雅各(Saint James)就是 Santiago' }, ch: 'santiago' },
  jacob: 'james', jaime: 'james',
  santiago: { ko: '산티아고', ja: 'サンティアゴ', zh: '聖地牙哥', o: 'Spanish', c: 'h', m: { en: 'Saint James (Sant Iago)', ko: '성 야고보 (Sant Iago)', ja: '聖ヤコブ(Sant Iago)', zh: '聖雅各(Sant Iago)' }, ch: 'santiago' },
  grace: { ko: '그레이스', ja: 'グレース', zh: '葛瑞絲', o: 'English, from Latin gratia', c: 'h', m: { en: 'grace, favour', ko: '은혜, 우아함', ja: '恵み、優雅さ', zh: '恩典、優雅' }, w: { ko: '은혜', ja: '恵み', zh: '恩典' }, i: { ko: '은혜', ja: '恵(めぐみ)', zh: '恩惠' } },
  anna: { ko: '안나', ja: 'アンナ', zh: '安娜', o: 'Hebrew', c: 'h', m: { en: 'favour, grace', ko: '은혜', ja: '恵み', zh: '恩典' }, w: { ko: '은혜', ja: '恵み', zh: '恩典' }, i: { ko: '은혜', ja: '恵(めぐみ)', zh: '恩惠' } },
  hannah: 'anna', ann: 'anna', anne: 'anna',
  john: { ko: '존', ja: 'ジョン', zh: '約翰', o: 'Hebrew', c: 'h', m: { en: 'God is gracious', ko: '신은 자비롭다', ja: '神は恵み深い', zh: '神是恩慈的' }, w: { ko: '자비', ja: '恵み', zh: '恩慈' }, i: { ko: '은혜', ja: '恵(めぐみ)', zh: '恩' } },
  jack: 'john', juan: 'john', ivan: 'john', jean: 'john', sean: 'john',
  david: { ko: '데이비드', ja: 'デイビッド', zh: '大衛', o: 'Hebrew', c: 'h', m: { en: 'beloved', ko: '사랑받는 사람', ja: '愛される人', zh: '被愛的人' }, w: { ko: '사랑', ja: '愛', zh: '愛' }, i: { ko: '사랑', ja: '愛(あい)', zh: '愛' } },
  michael: { ko: '마이클', ja: 'マイケル', zh: '麥可', o: 'Hebrew', c: 'h', m: { en: 'who is like God?', ko: '누가 신과 같은가?', ja: '誰が神のようであろうか', zh: '誰能像神?' } },
  daniel: { ko: '대니얼', ja: 'ダニエル', zh: '丹尼爾', o: 'Hebrew', c: 'h', m: { en: 'God is my judge', ko: '신이 나의 재판관', ja: '神はわが裁き主', zh: '神是我的審判者' } },
  ethan: { ko: '이선', ja: 'イーサン', zh: '伊森', o: 'Hebrew', c: 'h', m: { en: 'solid, enduring', ko: '굳건한, 오래가는', ja: '揺るがない、長く続く', zh: '堅定、持久' }, w: { ko: '굳건함', ja: '堅固', zh: '堅定' }, i: { ko: '굳건', ja: '堅(けん)', zh: '堅' } },
  elizabeth: { ko: '엘리자베스', ja: 'エリザベス', zh: '伊莉莎白', o: 'Hebrew', c: 'h', m: { en: 'my God is an oath', ko: '나의 신은 맹세', ja: 'わが神は誓い', zh: '我的神是誓約' } },
  isabella: { ko: '이사벨라', ja: 'イザベラ', zh: '伊莎貝拉', o: 'Hebrew, via Elisabeth', c: 'h', m: { en: 'a form of Elizabeth: my God is an oath', ko: '엘리자베스의 다른 형태: 나의 신은 맹세', ja: 'エリザベスの別形:わが神は誓い', zh: '伊莉莎白的變體:我的神是誓約' } },
  isabel: 'isabella', elisa: 'elizabeth', eliza: 'elizabeth',
  charlotte: { ko: '샬럿', ja: 'シャーロット', zh: '夏洛特', o: 'French, from Charles', c: 'h', m: { en: 'a feminine form of Charles: man', ko: '찰스의 여성형: 사람(남자)', ja: 'チャールズの女性形:人(男)', zh: '查爾斯的女性形:人(男子)' } },
  amelia: { ko: '아멜리아', ja: 'アメリア', zh: '艾蜜莉亞', o: 'Germanic', c: 'h', m: { en: 'work', ko: '일, 노력', ja: '働き、努力', zh: '勞動、努力' }, w: { ko: '노력', ja: '努力', zh: '努力' } },
  emily: { ko: '에밀리', ja: 'エミリー', zh: '艾蜜莉', o: 'Latin', c: 'h', m: { en: 'rival (from the Roman family name Aemilius)', ko: '맞수 (로마 가문 이름 아이밀리우스에서)', ja: '好敵手(ローマの氏族名アエミリウスから)', zh: '對手(源自羅馬家族名 Aemilius)' } },
  henry: { ko: '헨리', ja: 'ヘンリー', zh: '亨利', o: 'Germanic', c: 'h', m: { en: 'home + ruler: ruler of the home', ko: '집 + 다스리는 이: 집의 주인', ja: '家+支配者:家のあるじ', zh: '家+統治者:一家之主' }, ch: 'king' },
  alexander: { ko: '알렉산더', ja: 'アレクサンダー', zh: '亞歷山大', o: 'Greek', c: 'h', m: { en: 'defender of people', ko: '사람들을 지키는 이', ja: '人々を守る者', zh: '保護人們的人' }, w: { ko: '수호', ja: '守護', zh: '守護' }, ch: 'guard' },
  alex: 'alexander', alexandra: 'alexander',
  benjamin: { ko: '벤저민', ja: 'ベンジャミン', zh: '班傑明', o: 'Hebrew', c: 'h', m: { en: 'son of the south (or of the right hand)', ko: '남쪽의 아들 (또는 오른손의 아들)', ja: '南の息子(または右手の息子)', zh: '南方之子(或右手之子)' } },
  lucas: { ko: '루카스', ja: 'ルーカス', zh: '盧卡斯', o: 'Greek, via Latin', c: 'h', m: { en: 'from Lucania, a region of Italy (often linked to "light", but that is folk etymology)', ko: '이탈리아 루카니아 지방 사람 ("빛"이라는 풀이는 민간 어원이에요)', ja: 'イタリアのルカニア地方の人(「光」という解釈は俗説)', zh: '來自義大利盧卡尼亞地區(「光」的解釋是民間說法)' } },
  luke: 'lucas', luca: 'lucas',
  lily: { ko: '릴리', ja: 'リリー', zh: '莉莉', o: 'English', c: 'h', m: { en: 'lily (the flower)', ko: '백합(꽃)', ja: '百合(花)', zh: '百合(花)' }, w: { ko: '백합 · 나리', ja: '百合', zh: '百合' }, i: { ko: '나리', ja: '百合(ゆり)', zh: '百合' } },
  chloe: { ko: '클로이', ja: 'クロエ', zh: '克蘿伊', o: 'Greek', c: 'h', m: { en: 'green shoot', ko: '푸른 새싹', ja: '若芽', zh: '嫩芽' }, w: { ko: '새싹', ja: '若葉', zh: '嫩芽' }, i: { ko: '새싹', ja: '若葉(わかば)', zh: '芽' } },
  zoe: { ko: '조이', ja: 'ゾーイ', zh: '柔伊', o: 'Greek', c: 'h', m: { en: 'life', ko: '생명', ja: '命', zh: '生命' }, w: { ko: '생명', ja: '命', zh: '生命' }, i: { ko: '생', ja: '命(いのち)', zh: '生' } },
  zoey: 'zoe',
  peter: { ko: '피터', ja: 'ピーター', zh: '彼得', o: 'Greek', c: 'h', m: { en: 'stone', ko: '돌, 반석', ja: '石、岩', zh: '石頭、磐石' }, w: { ko: '반석', ja: '岩', zh: '磐石' }, i: { ko: '석', ja: '岩(いわお)', zh: '磐' } },
  pedro: 'peter', pierre: 'peter',
  paul: { ko: '폴', ja: 'ポール', zh: '保羅', o: 'Latin', c: 'h', m: { en: 'small, humble', ko: '작은, 겸손한', ja: '小さな、謙虚な', zh: '小的、謙卑的' } },
  stella: { ko: '스텔라', ja: 'ステラ', zh: '史黛拉', o: 'Latin', c: 'h', m: { en: 'star', ko: '별', ja: '星', zh: '星' }, w: { ko: '별', ja: '星', zh: '星' }, i: { ko: '별 · 성(星)', ja: '星(ほし)', zh: '星' }, ch: 'star' },
  estelle: 'stella', estrella: 'stella',
  mia: { ko: '미아', ja: 'ミア', zh: '米婭', o: 'from Maria', c: 'm', m: { en: 'a short form of Maria (whose original meaning is uncertain)', ko: '마리아의 짧은 형태 (마리아의 본래 뜻은 확실하지 않아요)', ja: 'マリアの短縮形(マリアの元の意味ははっきりしません)', zh: '瑪麗亞的簡稱(瑪麗亞的原意並不確定)' } },
  maria: { ko: '마리아', ja: 'マリア', zh: '瑪麗亞', o: 'Hebrew, via Latin', c: 'l', m: { en: 'uncertain; many meanings have been suggested', ko: '확실하지 않아요. 여러 풀이가 있어요', ja: 'はっきりしません。いくつもの説があります', zh: '不確定,有多種說法' } },
  mary: 'maria', marie: 'maria',
  ava: { ko: '에이바', ja: 'エヴァ', zh: '艾娃', o: 'uncertain', c: 'l', m: { en: 'uncertain; possibly a form of Eve (life)', ko: '확실하지 않아요. 이브(생명)의 다른 형태라는 풀이가 있어요', ja: 'はっきりしません。イブ(命)の別形という説があります', zh: '不確定,可能是夏娃(生命)的變體' } },
  eva: { ko: '에바', ja: 'エヴァ', zh: '伊娃', o: 'Hebrew', c: 'h', m: { en: 'life', ko: '생명', ja: '命', zh: '生命' }, w: { ko: '생명', ja: '命', zh: '生命' }, i: { ko: '생', ja: '命(いのち)', zh: '生' } },
  eve: 'eva',
  victoria: { ko: '빅토리아', ja: 'ヴィクトリア', zh: '維多利亞', o: 'Latin', c: 'h', m: { en: 'victory', ko: '승리', ja: '勝利', zh: '勝利' }, w: { ko: '승리', ja: '勝利', zh: '勝利' }, i: { ko: '승리', ja: '勝(まさる)', zh: '勝' } },
  victor: 'victoria',
  leo: { ko: '레오', ja: 'レオ', zh: '里歐', o: 'Latin', c: 'h', m: { en: 'lion', ko: '사자', ja: '獅子', zh: '獅子' }, w: { ko: '사자', ja: '獅子', zh: '獅子' } },
  felix: { ko: '펠릭스', ja: 'フェリックス', zh: '菲利克斯', o: 'Latin', c: 'h', m: { en: 'lucky, happy', ko: '운 좋은, 행복한', ja: '幸運な、幸せな', zh: '幸運、快樂' }, w: { ko: '행복', ja: '幸せ', zh: '幸福' }, i: { ko: '행복 · 복', ja: '幸(さち)', zh: '福' } },
  irene: { ko: '아이린', ja: 'アイリーン', zh: '艾琳', o: 'Greek', c: 'h', m: { en: 'peace', ko: '평화', ja: '平和', zh: '和平' }, w: { ko: '평화', ja: '平和', zh: '和平' }, i: { ko: '평화', ja: '和(なごみ)', zh: '和平' }, ch: 'peace' },
  rose: { ko: '로즈', ja: 'ローズ', zh: '蘿絲', o: 'Latin', c: 'h', m: { en: 'rose (the flower)', ko: '장미', ja: 'バラ', zh: '玫瑰' }, w: { ko: '장미', ja: '薔薇', zh: '玫瑰' } },
  rosa: 'rose',
  margaret: { ko: '마거릿', ja: 'マーガレット', zh: '瑪格麗特', o: 'Greek', c: 'h', m: { en: 'pearl', ko: '진주', ja: '真珠', zh: '珍珠' }, w: { ko: '진주', ja: '真珠', zh: '珍珠' }, i: { ko: '진주', ja: '珠(たま)', zh: '珍珠' } },
  pearl: 'margaret',
  joy: { ko: '조이', ja: 'ジョイ', zh: '喬伊', o: 'English', c: 'h', m: { en: 'joy', ko: '기쁨', ja: '喜び', zh: '喜悅' }, w: { ko: '기쁨', ja: '喜び', zh: '喜悅' }, i: { ko: '기쁨 · 희(喜)', ja: '喜(よし)', zh: '欣' } },
  hope: { ko: '호프', ja: 'ホープ', zh: '霍普', o: 'English', c: 'h', m: { en: 'hope', ko: '희망', ja: '希望', zh: '希望' }, w: { ko: '희망', ja: '希望', zh: '希望' }, i: { ko: '소망', ja: '望(のぞみ)', zh: '希' } },
  andrew: { ko: '앤드루', ja: 'アンドリュー', zh: '安德魯', o: 'Greek', c: 'h', m: { en: 'manly, brave', ko: '용감한', ja: '勇敢な', zh: '勇敢' }, w: { ko: '용기', ja: '勇気', zh: '勇氣' }, i: { ko: '용(勇)', ja: '勇(いさむ)', zh: '勇' } },
  andy: 'andrew', andre: 'andrew', andrea: 'andrew',
  thomas: { ko: '토머스', ja: 'トーマス', zh: '湯瑪斯', o: 'Aramaic', c: 'h', m: { en: 'twin', ko: '쌍둥이', ja: '双子', zh: '雙胞胎' } },
  tom: 'thomas'
};


/* sound-only entries (common surnames and names without a checked meaning yet): ko | ja | zh */
('smith|스미스|スミス|史密斯,johnson|존슨|ジョンソン|強森,williams|윌리엄스|ウィリアムズ|威廉斯,brown|브라운|ブラウン|布朗,jones|존스|ジョーンズ|瓊斯,garcia|가르시아|ガルシア|加西亞,miller|밀러|ミラー|米勒,davis|데이비스|デイビス|戴維斯,rodriguez|로드리게스|ロドリゲス|羅德里格斯,martinez|마르티네스|マルティネス|馬丁尼茲,wilson|윌슨|ウィルソン|威爾森,anderson|앤더슨|アンダーソン|安德森,taylor|테일러|テイラー|泰勒,thomas|토머스|トーマス|湯瑪斯,moore|무어|ムーア|摩爾,martin|마틴|マーティン|馬丁,lee|리|リー|李,white|화이트|ホワイト|懷特,harris|해리스|ハリス|哈里斯,clark|클라크|クラーク|克拉克,lewis|루이스|ルイス|路易斯,walker|워커|ウォーカー|沃克,young|영|ヤング|楊,allen|앨런|アレン|艾倫,king|킹|キング|金恩,wright|라이트|ライト|萊特,scott|스콧|スコット|史考特,green|그린|グリーン|格林,baker|베이커|ベイカー|貝克,adams|애덤스|アダムス|亞當斯,nelson|넬슨|ネルソン|尼爾森,campbell|캠벨|キャンベル|坎貝爾,mitchell|미첼|ミッチェル|米契爾,roberts|로버츠|ロバーツ|羅伯茲,parker|파커|パーカー|帕克,evans|에번스|エヴァンス|伊凡斯,turner|터너|ターナー|透納,collins|콜린스|コリンズ|柯林斯,murphy|머피|マーフィー|墨菲,cooper|쿠퍼|クーパー|庫柏,kim|킴|キム|金,wang|왕|ワン|王,chen|천|チェン|陳,schmidt|슈미트|シュミット|施密特,muller|뮐러|ミュラー|穆勒,rossi|로시|ロッシ|羅西,silva|실바|シルヴァ|席爾瓦,nguyen|응우옌|グエン|阮').split(',').forEach(function (r) {
  var a = r.split('|'); if (!window.NADRI_NAMES[a[0]]) window.NADRI_NAMES[a[0]] = { ko: a[1], ja: a[2], zh: a[3] };
});

window.NADRI_KANJI = ('花:꽃:flower,子:아들(아이):child,美:아름다울:beautiful,愛:사랑:love,翔:날:soar,太:클:great,郎:사내:man,陽:볕:sun,菜:나물:greens,結:맺을:tie,衣:옷:robe,大:큰:big,和:화할:harmony,優:넉넉할:gentle,真:참:true,心:마음:heart,春:봄:spring,夏:여름:summer,秋:가을:autumn,冬:겨울:winter,雪:눈:snow,桜:앵두(벚꽃):cherry blossom,櫻:앵두(벚꽃):cherry blossom,月:달:moon,星:별:star,光:빛:light,海:바다:sea,空:빌(하늘):sky,山:메:mountain,川:내:river,田:밭:field,中:가운데:middle,木:나무:tree,林:수풀:forest,森:수풀:forest,石:돌:stone,金:쇠:gold,王:임금:king,明:밝을:bright,智:슬기:wisdom,慧:슬기로울:wisdom,怡:기쁠:joyful,婷:예쁠:graceful,雅:맑을(우아할):elegant,佳:아름다울:fine,文:글월:writing,英:꽃부리:outstanding,志:뜻:will,玲:옥소리:jade sound,偉:클:great,宇:집:universe,豪:호걸:heroic,傑:뛰어날:outstanding,龍:용:dragon,竜:용:dragon,華:빛날:splendid,国:나라:country,國:나라:country,平:평평할:peace,安:편안:calm,康:편안:healthy,健:굳셀:strong,楽:즐길:enjoy,樂:즐길:enjoy,欣:기쁠:glad,雨:비:rain,晴:갤:clear sky,恵:은혜:blessing,惠:은혜:blessing,希:바랄:hope,望:바랄:hope,勇:날랠:brave,誠:정성:sincere,信:믿을:trust,仁:어질:kind,義:옳을:right,礼:예도:courtesy,禮:예도:courtesy,孝:효도:devotion,忠:충성:loyal,永:길:eternal,久:오랠:long,長:길:long,一:한:one,二:두:two,三:석:three,千:일천:thousand,万:일만:ten thousand,萬:일만:ten thousand,子:아들:child,代:대신할:generation,奈:어찌:(sound),香:향기:fragrance,紀:벼리:era,里:마을:village,沙:모래:sand,彩:채색:colour,音:소리:sound,詩:시:poem,菊:국화:chrysanthemum,蘭:난초:orchid,梅:매화:plum blossom,竹:대:bamboo,松:소나무:pine,葉:잎:leaf,芽:싹:sprout,蓮:연꽃:lotus,玉:구슬:jade,珠:구슬:pearl,琳:아름다운 옥:jade,瑜:아름다운 옥:jade,婉:순할:gentle,娟:예쁠:lovely,芳:꽃다울:fragrant,秀:빼어날:excellent,俊:준걸:talented,浩:넓을:vast,宏:클:grand,博:넓을:broad,明:밝을:bright,亮:밝을:bright,輝:빛날:shine,耀:빛날:radiant,晨:새벽:dawn,曦:햇빛:sunlight,嘉:아름다울:fine,欣:기쁠:glad,宜:마땅할:fitting,庭:뜰:garden,君:임금:lord,德:큰:virtue,徳:큰:virtue,正:바를:right,哲:밝을:wise,賢:어질:wise,聖:성인:holy,天:하늘:heaven,地:땅:earth,東:동녘:east,西:서녘:west,南:남녘:south,北:북녘:north,藤:등나무:wisteria,野:들:field,原:언덕:plain,井:우물:well,村:마을:village,島:섬:island,橋:다리:bridge,本:근본:origin,佐:도울:help,伊:저:(sound),加:더할:add,吉:길할:lucky,高:높을:high,小:작을:small,上:위:above,下:아래:below,口:입:mouth,川:내:river,谷:골:valley,池:못:pond,岡:언덕:hill,宮:집:palace,陳:베풀:display,李:오얏:plum,張:베풀:stretch,黃:누를:yellow,吳:나라 이름:(name),蔡:거북:(name),楊:버들:willow,劉:죽일:(name),周:두루:all around,許:허락할:allow,鄭:나라 이름:(name),謝:사례할:thank,郭:둘레:outer wall,洪:넓을:flood,曾:일찍:once,蕭:쓸쓸할:(name),羅:벌릴:net,葉:잎:leaf,呂:법칙:(name),蘇:되살아날:revive,莊:씩씩할:solemn,江:강:river').split(',').reduce(function (o, p) { var a = p.split(':'); if (!o[a[0]]) o[a[0]] = { ko: a[1], en: a[2] }; return o; }, {});

/* which characters lead into a chain */
window.NADRI_KANJI_CHAIN = { '智': 'wisdom', '慧': 'wisdom', '賢': 'wisdom', '哲': 'wisdom', '雪': 'snow', '冬': 'snow', '桜': 'blossom', '櫻': 'blossom', '平': 'peace', '和': 'peace', '星': 'star', '王': 'king', '君': 'king', '宮': 'king', '安': 'rest', '守': 'guard' };

window.NADRI_CHAINS = {
  wisdom: [
    { ko: '세종대왕은 집현전에 학자들을 모았고, 그 시대에 한글이 만들어졌어요.', en: 'King Sejong gathered scholars at the Jiphyeonjeon, the Hall of Worthies, and Hangul was created in his reign.', ja: '世宗大王は集賢殿に学者を集め、その時代にハングルが生まれました。', zh: '世宗大王在集賢殿聚集學者,韓文就在他的時代誕生。' },
    { ko: '경복궁 수정전은 집현전이 있던 자리에 서 있어요.', en: 'Sujeongjeon hall in Gyeongbokgung stands where the Jiphyeonjeon used to be.', ja: '景福宮の修政殿は、集賢殿があった場所に建っています。', zh: '景福宮的修政殿,就建在集賢殿的舊址上。', link: '/palaces/' },
    { ko: '광화문광장 세종대왕 동상 아래에는 세종의 업적을 보여 주는 무료 전시 \'세종이야기\'가 있어요.', en: 'Under the King Sejong statue in Gwanghwamun Square, the free "Story of King Sejong" exhibition shows his work.', ja: '光化門広場の世宗大王像の下に、無料の展示「世宗物語」があります。', zh: '光化門廣場世宗大王銅像下方,有免費展覽「世宗故事」。' }
  ],
  santiago: [
    { ko: '스페인의 산티아고 순례길(Camino de Santiago)은 성 야고보에게 가는 길이에요.', en: 'Spain\'s Camino de Santiago is the pilgrims\' way to Saint James.', ja: 'スペインのサンティアゴ巡礼路は、聖ヤコブへ向かう道です。', zh: '西班牙的聖雅各朝聖之路(Camino de Santiago),是走向聖雅各的路。' },
    { ko: '그 길을 걸은 서명숙이 2007년 제주에 만든 걷기 길이 제주 올레예요.', en: 'Suh Myung-sook walked it, came home and opened the first Jeju Olle walking trail in 2007.', ja: 'その道を歩いたソ・ミョンスクが、2007年に済州に作った道が済州オルレです。', zh: '走過這條路的徐明淑,2007 年在濟州開了第一條「濟州偶來」步道。' },
    { ko: '산티아고의 이름을 가진 사람에게 한국에서 가장 어울리는 길이에요.', en: 'If your name is James or Santiago, this is your walk in Korea.', ja: 'ジェームズやサンティアゴという名前なら、韓国ではこの道がいちばん似合います。', zh: '如果你叫 James 或 Santiago,這就是你在韓國最該走的路。', link: '/jeju/' }
  ],
  guard: [
    { ko: '조선의 궁궐 문은 수문장이 지켰어요.', en: 'In the Joseon dynasty, palace gates were kept by gate guards, the sumunjang.', ja: '朝鮮王朝の宮殿の門は、守門将が守っていました。', zh: '朝鮮王朝的宮門,由守門將看守。' },
    { ko: '경복궁 광화문 앞에서 수문장 교대식을 재현해요. 무료로 볼 수 있어요.', en: 'The guard-changing ceremony is re-enacted in front of Gyeongbokgung\'s Gwanghwamun gate, free to watch.', ja: '景福宮・光化門の前で守門将交代式が再現され、無料で見られます。', zh: '景福宮光化門前會重現守門將交接儀式,免費觀看。', link: '/palaces/' }
  ],
  peace: [
    { ko: '올리브 가지와 평화를 뜻하는 이름은 한국에서 가장 무거운 질문과 이어져요.', en: 'A name that carries the olive branch, or peace itself, leads to Korea\'s heaviest question.', ja: 'オリーブの枝や平和を意味する名前は、韓国でいちばん重い問いにつながります。', zh: '帶著橄欖枝或「和平」意義的名字,會連到韓國最沉重的問題。' },
    { ko: '파주 임진각 평화누리공원은 분단선 가까이에서 평화를 생각하는 곳이에요.', en: 'Imjingak Pyeonghwa-Nuri Park in Paju is where Koreans come to think about peace, close to the dividing line.', ja: '坡州の臨津閣・平和ヌリ公園は、分断線の近くで平和を考える場所です。', zh: '坡州臨津閣和平樂園,是在分斷線附近思考和平的地方。' }
  ],
  rest: [
    { ko: '쉼을 뜻하는 이름에는 절에서 하룻밤 머무는 템플스테이가 어울려요.', en: 'A name that means rest suits a templestay: a night at a Buddhist temple.', ja: '休息を意味する名前には、お寺に一晩泊まるテンプルステイが似合います。', zh: '意思是「安息」的名字,很適合去寺廟住一晚的寺院寄宿(Templestay)。' }
  ],
  snow: [
    { ko: '눈을 뜻하는 이름이라면 한국의 겨울이 제철이에요.', en: 'If your name means snow, Korea\'s winter is your season.', ja: '雪を意味する名前なら、韓国の冬が旬です。', zh: '名字有「雪」,韓國的冬天就是你的季節。', link: '/winter/' }
  ],
  blossom: [
    { ko: '벚꽃 이름에는 매년 봄 창원 진해에서 열리는 진해군항제가 어울려요. 도시 전체가 벚꽃으로 덮여요.', en: 'A cherry-blossom name belongs at the Jinhae Gunhangje festival in Changwon each spring, when the whole town turns pink.', ja: '桜の名前には、毎年春に昌原・鎮海で開かれる鎮海軍港祭が似合います。町じゅうが桜に包まれます。', zh: '櫻花的名字,適合每年春天在昌原鎮海舉辦的鎮海軍港節,整座城都被櫻花覆蓋。' }
  ],
  star: [
    { ko: '경주의 첨성대는 신라 때 세운 별을 보던 대로 알려져 있어요. 동아시아에 남은 가장 오래된 천문 시설 가운데 하나예요.', en: 'Cheomseongdae in Gyeongju, built in the Silla kingdom, is known as a star-watching tower and is one of the oldest surviving observatories in East Asia.', ja: '慶州の瞻星台は新羅時代に建てられた星を観る台とされ、東アジアに残る最古級の天文施設のひとつです。', zh: '慶州的瞻星臺建於新羅時代,被認為是觀星臺,是東亞現存最古老的天文設施之一。' }
  ],
  king: [
    { ko: '집과 나라를 다스리는 이의 이름이라면, 조선 임금이 살던 경복궁부터.', en: 'For a name about ruling a home or a land, start where Joseon\'s kings lived: Gyeongbokgung.', ja: '家や国を治める人の名前なら、朝鮮の王が暮らした景福宮から。', zh: '名字有「統治一家、一國」的意思,就從朝鮮國王住過的景福宮開始。', link: '/palaces/' }
  ]
};
