# 이름 도구 독립 검토 — 일본·대만 한자 뜻, 성씨 판정, 새 뜻 묶음 (2026-11-28 01:30 KST)

- 검토자: 독립 검토(작성자 아님). 코드는 고치지 않았고 판정만 함.
- 대상: 브랜치 `claude/determined-euler-xsz86i`
  - 1912c04 — `static/name-data.js` NADRI_KANJI 8자 + NADRI_KANJI_L, `static/name.js` 일본어·중국어 화면 뜻 우선, 두 글자 성씨 판정
  - 093912c — `static/name-concepts.js` 새 뜻 묶음 harbour·green·jasmine·silk, lotus에 Nalini·Liên·Ubon, `name-data.js` NADRI_KANJI_L에 結 翔 生 白 琉 紬 茉 凛, `name.js` 언어 이름 Vietnamese·Thai·Tamil
- 대조한 원 출처: wondu-archive `raw-from-scratchpad/names-2026-11-28/` 의 kp/(漢字ペディア), moe/(教育部 重編國語辭典修訂本, 家=ID 5502, 碩=ID 9151), unihan/, wikt/(41KB 내외 같은 크기 파일 = 문서 없음), btn/(Behind the Name 뜻 검색 목록). 인터넷은 다시 열지 않음.
- 화면 확인: `python3 build.py` → dist를 8766(새), 1912c04^ 워크트리 dist를 8767(이전)으로 띄우고 Playwright(chromium)로 `/ko|ja|zh-tw/name/?n=…`의 `.namer-out` 글을 비교. 093912c 반영 뒤 다시 빌드해 새 묶음도 확인. 페이지 오류(pageerror) 0건.

## 반드시 고칠 것 (보이기 전에)

1. **기존 한국 이름이 망가짐(1912c04 성씨 판정).** `KO_SURNAME_HANJA`는 소리마다 한자 1개뿐이라(양=梁, 배=裵, 조=趙, 유=柳 …) 다른 한자를 쓰는 한국 성은 성으로 안 잡힌다. 두 글자 입력에서 그 성이 이름으로 풀린다.
   - 裴勇: 이전 “날랠” → 지금 “裴 + 날랠” (ko·ja·zh 모두, ja/zh는 “裴 + brave”)
   - 宣明: 이전 “밝을” → 지금 “宣 + 밝을”
   - 曺·兪·慎으로 시작하는 두 글자도 같은 경로를 탄다(曺敏·兪敏·慎敏은 敏에 뜻 자료가 없어 화면 차이가 안 보였을 뿐).
   - 중국 간체 성(张·刘·陈·杨)도 목록에 없어 같은 경로(张伟·刘洋·陈静·杨帆은 지금은 뜻 자료가 없어 차이가 안 보임).
   - 고칠 방향(선택은 작성자·원두): 한국 성 한자 목록을 소리당 여러 한자로 넓히기(출처 있는 성씨 한자 목록), 간체 성 추가, 또는 성이 아니라고 판정할 때만 쓰는 '흔한 일본·대만 이름 첫 글자' 목록으로 반대로 좁히기.
2. **한국어 화면 공유 카드에 “물건 + 妍”.** 品 ko=‘물건’(위키 훈 맞음), 妍은 위키낱말 문서가 없어 ko가 빈 값 → 전체 풀이가 「당신의 이름은 “물건 + 妍”」으로 카드 맨 위에 크게 나옴(카드 PNG 직접 확인). 이름 뜻으로 ‘물건’ + 한자 그대로는 이용자에게 불쾌·오해. 같은 이름이 중국어 화면에서는 “人品(人的德性) + 美好”, 영어 쪽은 “article; rank”로 언어마다 다른 뜻을 고름. 같은 문제가 093912c의 琉·紬·茉·凛(ko 빈 값)에도 있음: ko 凛花 → “凛 + 꽃”.
   - 방향: 글자 하나라도 그 언어 뜻이 없으면 전체 풀이를 띄우지 않기, 또는 출처 있는 ko 뜻을 채우기. 品은 세 언어에서 같은 뜻을 고르거나 여러 뜻을 함께.
3. **새 외국 이름 24개에 한글 읽기가 없음(093912c).** 설계서 3절 “한국어 화면에서 모든 외국 이름 옆에 한글 읽기”. 기존 이름은 모두 있음(Padma파드마, Ren렌). 새로 넣은 Nalini·Liên·Ubon, Minato·Bandar, Chloe·Chloris·Khadra·Blerta·Midori·Sui·Qing·Bích, Yasmin·Jasmine·Yasemin·Jazmín·Gelsomina·Hasmik·Mallika·Melati, İpek·Reshma·Tsumugi는 `NADRI_KOREAD`에 없어 한국어 화면에 읽기 없이 나옴(화면 확인: ko 蓮·紬·莉子). 기계 점검: 모든 묶음 이름 중 읽기 없는 것은 이 24개뿐.
4. **출처에 없는 말(검수 데이터셋에서만 원칙, 설계서 3절).** 뜻이 틀린 것은 아니지만 기록한 출처와 글자가 다름. 출처를 바꾸거나 값을 출처대로:
   - 恩 zh ‘恩惠’ — 教育部 釋義는 “他人給我或我給他人的幫助”, ‘恩惠’라는 말이 없음(위키낱말 한국어 항목에 ‘은혜(恩惠)’로만 있음).
   - 品 en ‘article; rank’ — Unihan은 “article, product, commodity”. ‘rank’는 없음(教育部 3.等級을 옮긴 것으로 보임).
   - 湊 en ‘harbour (Japanese minato); gather’ — Unihan은 “piece together, assemble”. ‘harbour’는 漢字ペディア みなと를 옮긴 것. 湊 ko ‘(일본 이름에선 항구)’ — 漢字ペディア는 ①みなと를 일반 뜻으로 쓰고 ‘이름에서’라는 말은 없음(근거 없는 한정).
   - 葵 en ‘mallow’ — Unihan은 “sunflower; measure”. 漢字ペディア アオイ科를 옮긴 것(Behind the Name Aoi는 “hollyhock, althea”).
   - 琉 en ‘(lapis)’, 紬 en ‘(pongee)’, 凛 en ‘stern’ — Unihan(琉 “sparkling stone; glazed, opaque”, 紬 “kind of thin silk”, 凛 “to shiver with cold or fear”)에 없음. pongee는 Behind the Name Tsumugi에 있음, stern은 漢字ペディア きびしい를 옮긴 것, lapis는 보관 출처 어디에도 없음.
   - 093912c 묶음 green의 Chloe ‘Χλόη’ — 보관한 Behind the Name 목록에 그리스 문자 표기가 없음(근거 미보관). 이름 개별 문서를 보관하거나 표기를 빼기.

## 권고 (고치면 좋음)

- **일본어·중국어 화면의 언어 섞임.** 그 언어 뜻이 없는 글자는 영어로 돌아감: ja 恩碩 “kindness, mercy + great, eminent”, ja 結衣 “むすぶ + robe”, ja 陽翔(1912c04 시점) “日の光 + soar”, ja 莉子 “莉 + child”, zh 陽葵 “sun + sunflower; mallow (Japanese aoi)”, zh 湊 “harbour (Japanese minato); gather”. 이전에도 있던 영어 대체 방식이지만 이번에 일부만 현지어가 되어 한 문장 안에서 섞임.
- **괄호 설명이 전체 풀이에 그대로 들어감.** 「あなたの名前は “日の光 + あおい(アオイ科の植物)”」, 「“宝石「琉璃(ルリ)」の字 + いきる・うまれる”」, 「你的名字是 “人品(人的德性) + 美好”」. 글자 목록에는 괄호를 두고 전체 풀이에는 앞말만 쓰면 자연스러움.
- **莉에 글자 뜻이 없음.** 093912c가 莉를 jasmine 묶음에 넣었지만 NADRI_KANJI에 莉가 없어 “莉 + 아들(아이)”로 나옴. Behind the Name 목록에 莉 “white jasmine”(Airi·Riko·Rina·Rio)이 있으니 그걸로 채울 수 있음.
- **코드 주석과 실제가 다름.** 주석 “ja: first sense”인데 翠 ‘みどり’는 ②(①은 かわせみ), 凛 ‘りりしい’는 ②(①さむい), 生 ‘いきる・うまれる’는 ②③(①はえる). 고른 뜻은 이름에 맞지만 주석을 “이름에 맞는 뜻 골라 줄임”으로.
- **教育部 예시어를 뜻처럼 씀.** 家 zh ‘家庭’, 品 zh ‘人品’은 釋義 본문이 아니라 ‘如：’ 뒤 예시어. 豪 ‘才德出眾’은 “才德智能出眾的人”(사람)을 줄여 형용으로 바꿈. 뜻이 뒤집히지는 않음.
- **언어 표시.** Mallika를 ‘Sanskrit’로 표시 — Behind the Name 쓰임은 Tamil·Malayalam·Kannada·Telugu·Bengali(“Means jasmine in Sanskrit”). 093912c가 Tamil 언어 이름을 더했는데 데이터에서 쓰는 곳이 없음 → Mallika를 Tamil로 쓰려던 것으로 보임(추론). Chloris는 Behind the Name 쓰임이 Greek Mythology.
- **green 묶음 hanja에 青 없음.** 이름 목록에 Qing 青을 넣었으나 hanja는 ‘翠緑綠碧’ → 青 입력은 green으로 안 이어짐. 綠은 緑의 번체로 맞지만 보관 출처(Behind the Name)에는 없음.
- **일본 성 두 글자만 입력.** 佐藤 이전 “등나무” → 지금 “도울 + 등나무”, 鈴木 → “鈴 + 나무”. 둘 다 틀린 풀이(성)라 나빠진 것은 아니지만, 두 글자 일본 성은 성으로 보는 처리가 없음.

## A. 넣은 뜻 ↔ 출처 (글자마다)

| 글자 | 넣은 값 | 출처 원문(요지) | 판정 |
|---|---|---|---|
| 湊 | ja みなと | kp ①みなと。ふなつきば ②あつまる | 맞음 |
| 湊 | ko 모일(일본 이름에선 항구) | wikt 훈 ‘모이다’ / kp ①みなと | ‘모일’ 맞음, ‘일본 이름에선’ 근거 없음 |
| 湊 | en harbour (Japanese minato); gather | Unihan “piece together, assemble” | harbour는 Unihan에 없음(kp 옮김) |
| 翠 | ja みどり | kp ①かわせみ ②みどり | 맞음(②) |
| 翠 | ko 물총새(푸른빛) / en green; kingfisher | wikt ‘물총새’ / Unihan “color green; kingfisher” | 맞음 |
| 陽 | ja 日の光 | kp ①ひ。日の光 | 맞음 |
| 葵 | ja あおい(アオイ科の植物) | kp あおい。アオイ科の植物の総称 | 맞음 |
| 葵 | ko 해바라기·아욱 / en sunflower; mallow (Japanese aoi) | wikt ‘해바라기, 아욱’ / Unihan “sunflower; measure” | ko 맞음, mallow는 kp 옮김 |
| 蓮 | ja はす(スイレン科の多年草) | kp はす。はちす。スイレン科の多年草 | 맞음 |
| 家 | ko 집 / en home; family / zh 家庭 | wikt ‘집’ / Unihan “house, home, residence; family” / moe ID5502 1.眷屬共同生活的場所。如：「家庭」 | ko·en 맞음, zh는 예시어 |
| 淑 | ko 맑을·착할 / en pure; virtuous / zh 善良美好 | wikt ‘맑다, 착하다’ / Unihan “good, pure, virtuous, charming” / moe 2.善良、美好 | 맞음 |
| 芬 | ko 향기로울 / en fragrance / zh 香氣 | wikt ‘향기롭다’ / Unihan “fragrance, aroma; perfume” / moe 1.香氣 | 맞음 |
| 承 | ko 이을 / en inherit; receive | wikt ‘잇다, 성’ / Unihan “inherit, receive; succeed” | 맞음 |
| 宥 | ko 너그러울 / en forgive | wikt ‘너그러울’ / Unihan “forgive, pardon, indulge” | 맞음 |
| 豪 | zh 才德出眾 | moe [名]2.才德智能出眾的人 | 줄임(뜻 유지) |
| 品 | ko 물건 | wikt ‘물건’ | 맞음(훈) — 단 이름 풀이로 부적절(반드시 고칠 것 2) |
| 品 | en article; rank | Unihan “article, product, commodity” | rank 출처 없음 |
| 品 | zh 人品(人的德性) | moe [名]5.人的德性。如：「人品」 | 출처에 있음. 첫 뜻(眾多/物品)이 아닌 5번을 고름 → ko·en과 다른 뜻 |
| 妍 | en beautiful / zh 美好 / ko 없음 | Unihan “beautiful, handsome; seductive” / moe 豔麗、美好 / wikt 문서 없음 | en·zh 맞음, ko 비어 화면 문제 |
| 恩 | ko 은혜 / en kindness, mercy | wikt ‘은혜’ / Unihan “kindness, mercy, charity” | 맞음 |
| 恩 | zh 恩惠 | moe 1.他人給我或我給他人的幫助 | ‘恩惠’ 출처에 없음 |
| 碩 | ko 클 / en great, eminent / zh 大、學識淵博 | wikt ‘크다’ / Unihan “great, eminent; large, big” / moe ID9151 1.大的 2.學識淵博的 | 맞음 |
| 結 | ja むすぶ | kp ①むすびつける… (訓 むすぶ) | 맞음 |
| 翔 | ja かける・とぶ | kp かける。とぶ | 맞음 |
| 生 | ja いきる・うまれる | kp ②うむ。うまれる ③いきる | 맞음(①はえる 아님) |
| 白 | ja しろ | kp ①しろ。しろい | 맞음 |
| 琉 | ja 宝石「琉璃(ルリ)」の字 / en sparkling stone (lapis) | kp 宝石の名「琉璃(ルリ)」に用いられる字 / Unihan “sparkling stone; glazed, opaque” | ja 맞음, lapis 출처 없음 |
| 紬 | ja つむぎ(絹織物) / en thin silk (pongee) | kp ①つむぎ…絹織物の一つ / Unihan “kind of thin silk” / BtN Tsumugi “pongee, silk cloth” | 맞음(pongee는 BtN) |
| 茉 | ja 「茉莉(マツリ)」の字 / en white jasmine | kp 「茉莉(マツリ)」に用いられる字 / Unihan “white jasmine” | 맞음 |
| 凛 | ja りりしい / en cold; stern | kp ①さむい ②きびしい。りりしい / Unihan “to shiver with cold or fear” | ja 맞음, stern은 kp 옮김 |

## A-2. 093912c 뜻 묶음 ↔ Behind the Name 목록

| 묶음 | 이름(표시 언어, 원어 표기) | BtN 목록 원문 | 판정 |
|---|---|---|---|
| harbour | Minato (Japanese, 湊・港) | “港 (minato) or 湊 (minato) both meaning "harbour"” | 맞음, 표기 출처 있음 |
| harbour | Bandar (Arabic) | “Means "harbour, port" in Arabic (of Persian origin)” | 맞음 |
| harbour hanja | 湊港 | 위 Minato | 맞음 |
| green | Chloe (Greek, Χλόη) | “Means "green shoot" in Greek” — Χλόη 표기 없음, 쓰임 English·Ancient Greek 등 | 뜻 맞음, 표기 근거 미보관 |
| green | Chloris (Greek) | “χλωρός (chloros) meaning "pale green"”, 쓰임 Greek Mythology | 맞음(표시는 Greek Mythology가 정확) |
| green | Khadra (Arabic) | “Feminine form of Arabic أخْضر … "green"” | 맞음 |
| green | Blerta (Albanian) | “Albanian blertë meaning "green"” | 맞음 |
| green | Midori (Japanese, 緑) | “緑 (midori) meaning "green"” | 맞음 |
| green | Sui (Japanese, 翠) | “翠 (sui) meaning "green, blue"” | 맞음 |
| green | Qing (Chinese, 青) | “青 (qīng) meaning "blue, green, young"” | 맞음 |
| green | Bích (Vietnamese, 碧) | “碧 (bích) meaning "bluish green, cyan"” | 맞음 |
| green hanja | 翠緑綠碧 | 翠(Sui)·緑(Midori)·碧(Bích, Ao) 있음, 綠은 없음(緑의 번체) | 대체로 맞음, 青 빠짐 |
| jasmine | Yasmin·Jasmine·Yasemin·Jazmín·Gelsomina·Hasmik·Melati | 목록에 모두 있음(Gelsomina “Italian form of Jasmine”, Melati “jasmine flower”) | 맞음 |
| jasmine | Mallika (Sanskrit) | “Means "jasmine" in Sanskrit”, 쓰임 Tamil·Malayalam·Kannada·Telugu·Bengali | 뜻 맞음, 언어 표시는 Tamil 등이 정확 |
| jasmine hanja | 茉莉 | 莉 “white jasmine”(Airi·Riko·Rina·Rio·Xiaoli), 茉 kp·Unihan | 맞음 |
| silk | İpek (Turkish), Reshma (Hindi), Tsumugi (Japanese, 紬) | 목록에 모두 있음 | 맞음 |
| silk hanja | 紬紗 | 紬(Tsumugi), 紗 “thread, silk”(Risa·Sana·Sayaka) | 맞음 |
| lotus 추가 | Nalini (Hindi, नलिनी) | “From Sanskrit नलिनी (nalinī) meaning "lotus"”, 쓰임에 Hindi 있음 | 맞음, 표기 출처 있음 |
| lotus 추가 | Liên (Vietnamese, 蓮) | “Sino-Vietnamese 蓮 (liên) meaning "lotus, water lily"” | 맞음 |
| lotus 추가 | Ubon (Thai) | “Means "lotus" in Thai” | 맞음 |

- 묶음 이름표(ko 항구·초록·재스민·비단, ja 港(みなと)·緑·茉莉(ジャスミン)·絹・紬, zh 港口·綠·茉莉·絲綢)는 출처 문장이 아니라 일반 낱말 번역. 틀린 곳은 없음. 絹은 보관 출처에 없음.
- **기존 한자 묶음 바뀜 없음**: 1912c04와 093912c의 `NADRI_CONCEPT_OF.hanja`를 node로 비교 → 바뀐 것은 새 글자 10개(湊港翠緑綠碧茉莉紬紗)가 새로 생긴 것뿐, 기존 글자가 다른 묶음으로 옮겨진 것 0건. 여러 묶음에 겹친 글자는 이전부터 있던 熙(light/joy)·浩(sea/great)·安(peace/rest)·久(life/eternal)뿐.

## B. 성씨 판정 변경 — 이전(1912c04^) ↔ 지금 화면 비교

입력 12개 × 3개 화면(ko·ja·zh-tw). 같은 방법으로 빌드한 두 사이트의 `.namer-out` 글 비교. 아래 ‘풀이’는 “당신의 이름은 …” 문장.

| 입력 | 화면 | 이전 | 지금 | 판정 |
|---|---|---|---|---|
| 李元斗 | 3개 | 같음 | 같음 | 변화 없음 |
| 王明 | 3개 | 같음(王 성 + 明) | 같음 | 변화 없음 |
| 金敏 | 3개 | 같음(金 성 + 敏) | 같음 | 성+이름 유지 |
| 김민준 / Olivia | 3개 | 같음 | 같음 | 변화 없음 |
| 陳淑芬 | ko | 풀이 없음(淑·芬 뜻 없음) | “맑을·착할 + 향기로울” | 데이터 추가로 좋아짐 |
| 陳淑芬 | ja | 풀이 없음 | “pure; virtuous + fragrance” | 영어 섞임(권고) |
| 陳淑芬 | zh | 풀이 없음 | “善良美好 + 香氣” | 좋아짐 |
| 淑芬 | 3개 | 풀이 없음(淑 성으로 봄) | 陳淑芬과 같은 풀이 | 의도대로(이름 전체) |
| 陽葵 | ko | “해·볕”(陽 성으로 봄) | “볕 + 해바라기·아욱” | 의도대로 |
| 陽葵 | ja | “陽” | “日の光 + あおい(アオイ科の植物)” | 의도대로, 괄호 권고 |
| 陽葵 | zh | “陽” | “sun + sunflower; mallow (Japanese aoi)” | 영어 섞임 |
| 湊 | ko / ja / zh | 풀이 없음 | “모일(일본 이름에선 항구)” / “みなと” / “harbour (Japanese minato); gather” | 데이터 추가. ko 한정어·zh 영어 |
| 品妍 | ko | 풀이 없음 | “물건 + 妍” | **반드시 고칠 것 2** |
| 品妍 | ja / zh | 풀이 없음 | “article; rank + beautiful” / “人品(人的德性) + 美好” | 언어마다 다른 뜻 |
| 恩碩 | ko / ja / zh | 풀이 없음 | “은혜 + 클” / “kindness, mercy + great, eminent” / “恩惠 + 大、學識淵博” | ja 영어, zh 恩惠 출처 |
| 家豪 | ko | “호걸”(家를 성으로 봄, 잘못) | “집 + 호걸” | 좋아짐 |
| 家豪 | ja / zh | “heroic” | “home; family + heroic” / “家庭 + 才德出眾” | 좋아짐 |

추가로 확인한 입력(같은 방법):

| 입력 | 이전 | 지금 | 판정 |
|---|---|---|---|
| 裴勇 (ko) | “날랠” | “裴 + 날랠” | **나빠짐** (반드시 고칠 것 1) |
| 宣明 (ko) | “밝을” | “宣 + 밝을” | **나빠짐** |
| 曺敏·兪敏·慎敏 | 풀이 없음 | 풀이 없음 | 화면 같음, 내부 판정은 이름 전체로 바뀜 |
| 张伟·刘洋·陈静·杨帆 | — | 같음 | 화면 같음, 내부 판정은 이름 전체로 바뀜(간체 성 없음) |
| 陽翔·結衣 (ko) | “날” / “옷” | “볕 + 날” / “맺을 + 옷” | 좋아짐(일본 이름) |
| 佐藤·鈴木 (ko) | “등나무” / “나무” | “도울 + 등나무” / “鈴 + 나무” | 둘 다 틀림(성), 권고 |
| 高橋·明美·文雄 | 같음 | 같음 | 변화 없음 |

- 2글자 한국식 이름(金敏 = 성 金 + 이름 敏, 王明)은 그대로 성+이름으로 풀림. 단 성 한자가 `KO_SURNAME_HANJA`(소리당 1자)와 대만 성 목록 둘 다에 없으면 이름 전체로 풀림.

## C. 일본어·중국어 문장, 카드 이미지

- 카드 PNG: ja 陽葵, ja 湊, zh-tw 家豪, zh-tw 品妍, zh-tw 陳淑芬, ko 品妍, ko 恩碩 — 모두 1080×1350으로 생성, 글자 넘침·깨짐 없음(ja 陽葵·zh 品妍·ko 品妍·ja 湊는 이미지 열어 직접 봄). 가장 긴 「“日の光 + あおい(アオイ科の植物)”」도 한 줄 안에 들어감.
- 어색한 문장(지적만): 「“日の光 + あおい(アオイ科の植物)”」(사전 분류명이 이름 풀이에 들어감), 「“宝石「琉璃(ルリ)」の字 + いきる・うまれる”」, 「“むすぶ + robe”」, 「你的名字是 “家庭 + 才德出眾”」(家庭은 ‘가정·가구’로 읽혀 이름 뜻으로 어색), 「“人品(人的德性) + 美好”」. 한국어 카드 「“물건 + 妍”」은 반드시 고칠 것 2.
- 언어 이름 Vietnamese·Thai: ko 베트남어·태국어, ja ベトナム語・タイ語, zh 越南文·泰文으로 화면에 나옴(확인). Tamil은 데이터에서 쓰이지 않음.

## D. 원두 원칙

| 원칙 | 판정 | 근거 |
|---|---|---|
| 불확실한 정보를 확실하게 말하지 않음(“근거를들어서 예상한다고 해” [7eb4ec94#2931]) | 일부 불합격 | 湊 ‘일본 이름에선 항구’(출처에 없는 한정), 琉 ‘lapis’(출처 없음). 品은 5번째 뜻을 이름 뜻으로 단정. |
| 실명 예시 금지(설계서 3절) | 통과 | 새로 넣은 것은 한자 뜻·성씨 한자 목록·BtN 이름(일반 이름)뿐, 사람 실명 없음. 李元斗는 검토 지시의 시험 입력으로만 씀. |
| 뜻은 AI 생성이 아니라 검수한 데이터셋에서만(설계서 3절) | 대체로 통과, 일부 불합격 | 대부분 출처 원문과 맞음(A표). 恩 恩惠, 品 rank, 湊 harbour, 葵 mallow, 凛 stern, 琉 lapis, Chloe Χλόη는 기록한 출처에 그 말이 없음(반드시 고칠 것 4). |
| 외국 이름에 한글 읽기(설계서 3절) | 불합격(093912c) | 새 이름 24개 읽기 없음(반드시 고칠 것 3). |
| 출처·확신도 표시 | 해당 일부 | 글자 뜻·뜻 묶음 이름에는 화면 출처 표시가 없음(코드 주석에만). 기존 방식과 같음. |

## E. 이번 변경이 아닌, 이미 있던 문제

1. **‘꽃’ 묶음의 한국 사슬이 벚꽃 전용.** flower 묶음 hanja ‘花華英芳菊蘭梅蕙薇’의 한국 항목이 `chain: 'blossom'`(“벚꽃 이름에는 매년 봄 … 진해군항제가 어울려요”). 화면 확인: 菊·梅·蘭 한 글자, 金英(英 = 꽃부리)에도 이 문장이 나옴. 국화·난초·매화 이름에 벚꽃 축제를 붙이는 셈.
2. **성 글자의 뜻 묶음이 이름 뜻처럼 나옴.** 金敏 → “같은 뜻의 다른 나라 이름 · 금(GOLD)”(Aurelia 등), 王明 → ‘임금·다스림’ 묶음과 세계 사슬, 金英 → GOLD. `conceptsForHanja`가 성을 빼지 않고 모든 글자를 봄.
3. **일본어·중국어 화면 글자 목록에 한국어 훈이 한글로 나옴**(예: ja 陽葵 「陽 볕 양 日の光」). 한국 한자음 소개 목적이면 의도일 수 있으나 일본·대만 이용자에게는 설명 없는 한글.
4. **언어 뜻이 없으면 영어로 대체**하는 방식 자체(ja·zh 화면). 이번 변경으로 더 눈에 띔(권고 1).
5. **두 글자 일본 성(佐藤·鈴木 등)** 을 한 글자 성 + 이름으로 풀던 문제(이전부터, 지금은 이름 전체로 풀어 여전히 틀림).

## 누가 판정했나

- 전부 독립 검토(작성자 아님)가 원 출처 파일과 빌드한 화면으로 판정. 카드 이미지는 4장을 열어 직접 봄, 나머지 3장은 생성·크기만 확인.
- 못 한 것: 일본어·중국어 문장의 원어민 자연스러움 판정(지적은 검토자 판단), Χλόη·綠·絹의 원 출처 확인(보관 파일에 없어 판정 보류 — 맞을 수 있으나 근거 미보관).

## 재검토(d755d38) — 2026-11-28 01:40 KST

- 검토자: 독립 검토(작성자 아님). 고치지 않고 판정만.
- 방법: `git diff cf620ff d755d38 -- static/name*.js` 읽기 → 빌드 → Playwright로 24개 입력 × ko·ja·zh-tw 화면, 이전 결과(1912c04^ 빌드, 1차 검토 때 저장)와 비교. 뜻 묶음 한자 배정은 node로 1912c04 대비 비교, 한글 읽기는 `nadriKoRead`로 모든 묶음 이름 점검. 카드 8장은 PNG를 직접 열어 봄. 페이지 오류 0건.

### 1. 반드시 고칠 것 4건 — 해결 여부

| # | 지적 | 판정 | 근거(화면·파일) |
|---|---|---|---|
| 1 | 성씨 판정 회귀(裴勇·宣明) | **해결** | 裴勇 ko “날랠” / ja·zh “brave”, 宣明 “밝을” — 1912c04^와 글자까지 같음. 曺明 “밝을”(성+이름). 李元斗·金敏·王明·김민준·Olivia 이전과 같음. 淑芬·陳淑芬·陽葵·家豪·品妍·恩碩·湊·翠는 이름 전체 풀이 유지. |
| 2 | 한국어 카드 “물건 + 妍” | **부분 해결** | 빈 뜻은 영어로 대체되어 ko 品妍 → 「당신의 이름은 “물건 + beautiful”」. 한자 그대로 나오던 문제는 없어짐. 그러나 ‘물건’이 이름 뜻으로 카드 맨 위에 나오는 문제와 언어마다 다른 뜻(ko 물건 / en article, product / zh 人的德性)은 그대로. 한국어 문장 안에 영어가 섞임(“white jasmine + 아들(아이)”, “cold + 꽃”). |
| 3 | 새 외국 이름 24개 한글 읽기 | **해결**(1개 권고) | 모든 묶음 이름 중 읽기 없는 이름 0개(node 점검). 외래어 표기법 대조: Bandar 반다르, Minato 미나토, Chloris 클로리스, Khadra 하드라, Blerta 블레르타, Midori 미도리, Sui 스이, Qing 칭, Bích 빅, Nalini 날리니, Liên 리엔, Ubon 우본, Yasmin 야스민, Jasmine 재스민, Yasemin 야세민, Jazmín 하스민, Gelsomina 젤소미나, Hasmik 하스미크, Mallika 말리카, Melati 믈라티(인도네시아어 약한 e→으), İpek 이페크, Reshma 레시마, Tsumugi 쓰무기 — 이상 없음. **Chloe 클로에**는 프랑스어식. 영어 Chloe는 ‘클로이’가 표기법·관용 모두에 맞고, 표시 언어가 Greek이면 더더욱 ‘클로에’가 아님. |
| 4 | 출처에 없던 말 | **해결**(경미 1) | 湊 ko ‘모일·항구’(위키 ‘모이다’ + 漢字ペディア みなと), en ‘harbour; gather’(BtN Minato “harbour” + Unihan assemble) — 주석에 출처 적음. 翠 ko ‘물총새·초록’(위키 + Unihan “color green”). 葵 en ‘sunflower; hollyhock’(Unihan + BtN Aoi “hollyhock, althea”). 恩 zh ‘幫助、情愛’(教育部 1.…的幫助 / 2.情愛). 品 zh ‘人的德性’(5번 원문 그대로), en ‘article, product’(Unihan 그대로). 琉 ‘sparkling stone’, 紬 ‘kind of thin silk’, 凛 ‘cold’(Unihan 줄임), 莉 ‘white jasmine’(BtN). Χλόη 삭제, hanja에서 綠 삭제. 경미: **家 zh ‘家人’**은 釋義 2 “一門之內共同生活的人”을 바꿔 말한 것이고, ‘家人’이라는 낱말은 출처에서 [形]2 “家中的。如：「家人」”의 예시어로만 나옴. 뜻은 맞음. |

- 그 밖에 1차 권고 반영: 괄호 설명 줄임(葵 あおい, 蓮 はす, 琉璃(ルリ)の字), Mallika Tamil, green hanja에 青 추가(‘翠緑碧青’). 뜻 묶음 한자 배정은 1912c04 대비 새 글자 11개(湊港翠緑碧青茉莉紬紗)만 새로 생겼고 기존 글자 이동 0건.

### 2. 새 문제

1. **성씨 목록을 넓히며 일본·대만 이름 첫 글자 일부가 다시 성으로 잡힘.** 새로 성으로 판정되는 글자: 裴宣曺兪愼慎邊魯陶奉夫太景甄葛晉晋皮宗龐慶柴睦殷芮 + 간체 성 46자(武·向·常·易·万·付 등 포함). 화면 확인: 太郎 → 太 성 + 郎 “사내”(ko) / “man”(ja·zh). 宗翰(대만 흔한 이름) → 宗 성 + 翰(지금은 뜻 자료가 없어 풀이 없음). 1912c04^와 같은 동작이라 ‘회귀’는 아니지만 1912c04의 목적(두 글자 일본·대만 이름은 이름 전체)과 어긋나는 경우. 권고: 太·宗처럼 이름 첫 글자로 흔한 글자는 화면 언어(ja·zh)에 따라 다르게 보거나 목록에서 빼는 것을 원두·작성자가 정함.
2. **같은 뜻 반복·혼합 문장.** ko·zh 茉莉 → “white jasmine + white jasmine”, ja 茉莉 → “茉莉(マツリ)の字 + white jasmine”, ko 凛花 “cold + 꽃”, ko 紬 “kind of thin silk”(한국어 화면 전체 풀이가 영어만).
3. **이름 풀이로 부정적이거나 오해될 낱말.** 凛 en ‘cold’(Unihan “to shiver with cold or fear”, 일본 이름 凛은 りりしい 쪽), 恩 zh ‘情愛’(현대 중국어에서 남녀의 애정으로 읽힐 수 있음), 品 ko ‘물건’. 출처에는 맞지만 ‘당신의 이름은 “…”’ 자리에 그대로 쓰기에는 맞지 않음. 이름에 쓰는 뜻을 고르는 기준(출처 안에서)을 정하면 해결됨.

### 3. 카드 8장 (static/cards/names/2026-11-28/, 모두 직접 열어 봄)

| 카드 | 깨짐 | 내용 판정 |
|---|---|---|
| ja-himari (陽葵) | 없음 | “日の光 + あおい” 화면과 일치. 그 나라에서 태어났다면·같은 뜻 이름은 陽(sun) 묶음 — 이상 없음. |
| ja-minato (湊) | 없음 | “みなと”, 묶음 港(みなと): Minato 湊・港 / Bandar — 출처와 맞음. |
| ja-sui (翠) | 없음 | “みどり”, 묶음 緑: Chloe·Chloris(ギリシャ語)·Khadra·Blerta·Midori 緑·Sui 翠. Chloe 쓰임은 BtN상 English·Ancient Greek(표시 ‘ギリシャ語’는 어원 기준이면 맞음). |
| tw-enshuo (恩碩) | 없음(가장 긴 줄 “幫助、情愛 + 大、學識淵博”도 폭 안) | ‘情愛’ 어감 권고(새 문제 3). 묶음 恩典: Grace·Hannah·Gracia·Kripa·Megumi 恵·Eunhye 은혜. |
| tw-jiahao (家豪) | 없음 | “家人 + 才德出眾”. 묶음 勇: Andreas·Valentin·Isamu·Yong — 豪가 brave 묶음으로 이어짐(기존 배정). |
| tw-pinyan (品妍) | 없음 | “人的德性 + 美好”, 묶음 美 — 이상 없음. 단 같은 이름의 한국어 화면은 “물건 + beautiful”(위 2번). |
| en-liam | 없음 | “will + helmet: a resolute protector”(well documented), 連恩, 근위병 — 기존 자료 그대로, 이상 없음. |
| en-olivia | 없음 | **반드시 고칠 것(공개 전)**: ① “If you were born in… · peace / Japan Kazuko 和子 **confidence 80%**” — 이 %는 설계서 5절 ‘원두 결정 대기 ② 기존 NADRI_BORN의 %(출처 없는 추정)’인 값. 불확실한 정보를 수치로 확실하게 보이는 것이라 원두 결정 전에는 스레드에 쓰지 않는 것이 원칙(“불확실한 정보를 올리면 안돼는건 모든 곳에 적용이야” [7eb4ec94#2954])에 맞음. ② 뜻은 “olive tree”(likely)인데 아래가 모두 ‘peace’ 묶음 — 올리브=평화는 상징에서 이은 것이고 Behind the Name 뜻 문장에는 없음(name-concepts.js peace latin: ['irene', 'olivia']). 이름 뜻처럼 이어 보임. |

- 8장 모두 1080×1350, 글자 넘침·겹침·빈 칸 깨짐 없음. 도장(Olivia 비올/아리)은 오른쪽 세로줄부터 읽는 전통 순서라 ‘올리비아’로 맞음.

### 기준별 판정 (재검토)

| 기준 | 판정 | 근거 |
|---|---|---|
| 기존 동작 회귀 | 통과 | 1차 지적 입력 전부 1912c04^와 같거나 의도대로 |
| 출처 대조(검수 데이터셋에서만) | 통과(경미 1) | 家 ‘家人’ 바꿔 말함 |
| 외국 이름 한글 읽기 | 통과(권고 1) | Chloe 클로에 → 클로이 권고 |
| 불확실한 정보 금지 | **불합격(카드 1장)** | en-olivia 카드의 출처 없는 ‘confidence 80%’, olive→peace 연결 |
| 실명 예시 금지 | 통과 | 카드 8장 모두 일반 이름 |
| 화면 문장 자연스러움 | 권고 | 영어 섞임, 같은 뜻 반복, 이름 뜻으로 어색한 낱말(물건·cold·情愛) |

- 판정: 전부 독립 검토. 못 한 것: 일본어·중국어 원어민 판정, Olivia·Liam 카드의 기존 자료(連恩, 근위병 문장) 원 출처 재대조(이번 변경 아님).
