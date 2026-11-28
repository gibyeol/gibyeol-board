# 이름 4개 언어 자료 수집 지시 (공통) — 보고는 한국어

목적(운영자 원두 원문): "영어, 한국어, 일본어, 중국어 간에 번역이 원활하게 되는걸 우선목표로 수집하자" / "매튜/매슈 둘다 띄우는 방식으로 해"
Nadri 이름 도구(https://nadri-guide.pages.dev/name/)에서 사람이 영어 이름을 치면 한국어·일본어·중국어(대만) 표기와 뜻이 나와야 하고, 일본어·중국어 표기로 쳐도 같은 이름을 찾아야 한다.

## 절대 규칙
- 출처에서 확인한 것만 쓴다. 확인 못 한 칸은 비워 두고(null) 이유를 note에 쓴다. 지어내지 않는다.
- 사이트가 막히면(403 등) 우회하지 않는다(User-Agent 바꾸기, 헤드리스 브라우저, 미러·캐시 금지). 그냥 '못 엶'으로 적는다.
- 허용된 사이트만: en/ko/ja/zh.wikipedia.org(API 포함), korean.go.kr, www.behindthename.com, www.census.gov. 그 밖은 열지 않는다.
- 파일만 쓴다. git 커밋·push 하지 않는다. 결과 파일 경로는 지시에 적힌 곳.

## 이름마다 모을 것 (JSON 배열의 객체 하나)
{
 "key": "matthew",                 // 소문자 영어 철자
 "type": "given" | "surname" | "nick",
 "of": null | "james",             // nick일 때 본 이름 key
 "sex": "m" | "f" | "u" | null,    // given/nick만
 "rank_src": "어느 목록에서 몇 위였는지 + 주소",
 "ko_std": "매슈",                  // 국립국어원 외래어 표기 용례의 한글 표기(그 이름 단독 또는 그 이름을 가진 인물 표기에서 이름 부분)
 "ko_std_src": "https://korean.go.kr/front/search/searchAllList.do?searchQuery=Matthew (용례 'OOO, 매슈 Matthew OOO')",
 "ko_alt": ["매튜"],                 // 실제로 쓰이는 다른 한글 표기. 근거가 있는 것만
 "ko_alt_src": "근거: 예) 한국어 위키백과 본문 검색 '매튜' totalhits 2229, 문서 예: '…'(제목/첫 문장)",
 "ja": "マシュー", "ja_src": "ja.wikipedia 문서 제목·주소(이름 문서 또는 그 이름 유명 인물 문서의 이름 부분)",
 "zh": "馬修", "zh_src": "zh.wikipedia 대만 표기(zh-tw 변환) 주소",
 "origin": "Hebrew, via Greek",
 "meaning": {"en": "gift of God", "ko": "신의 선물", "ja": "神の贈り物", "zh": "神的禮物"},  // en은 Behind the Name 문장에서 짧게, ko/ja/zh는 그 번역
 "meaning_src": "https://www.behindthename.com/name/matthew",
 "c": "h" | "m",                   // 뜻 확신: Behind the Name에 분명하면 h, 여러 설이면 m
 "nicks": ["matt"],                 // given만: Behind the Name 'Diminutives'에 있는 영어권 애칭 중 흔한 것(최대 3)
 "note": "막힌 것·애매한 것"
}

## 효율적으로 찾는 법 (권장)
- 일본어·중국어·한국어 위키 제목: en.wikipedia API langlinks
  https://en.wikipedia.org/w/api.php?action=query&titles=Matthew_(given_name)&prop=langlinks&lllang=ja&format=json (lllang=ko, zh도)
  이름 문서가 없으면 '<Name> (name)', '<Name> (surname)' 등을 시도. zh 제목은 간체일 수 있으니
  https://zh.wikipedia.org/w/api.php?action=parse&page=<제목>&prop=displaytitle&variant=zh-tw&format=json 로 대만 표기를 확인.
  위키 제목이 인물 목록 문서(예: 'マシュー')라도 이름 부분의 표기를 쓴다. 괄호 설명은 뺀다.
- 국립국어원: https://korean.go.kr/front/search/searchAllList.do?searchQuery=<영문> 결과의 '한글표기' 열. 같은 이름의 용례가 여럿이면 가장 많은 표기, 갈리면 둘 다 note에.
- 실제로 쓰이는 다른 표기(ko_alt): 표준과 다른 흔한 표기 후보(예: 매튜, 데이빗, 스티브 잡스의 '스티브')를 한국어 위키백과 API 본문 검색으로 '쓰인다'는 근거만 확인:
  https://ko.wikipedia.org/w/api.php?action=query&list=search&srsearch=<표기>&format=json&srlimit=3
  totalhits와 예시 문서 제목을 근거로 적는다. 근거가 약하면(예: totalhits 20 미만) 넣지 않는다. '가장 많이 쓰인다'고 주장하지 않는다.
- 뜻: https://www.behindthename.com/name/<key> (성은 https://surnames.behindthename.com 이 막혀 있으면 www.behindthename.com 쪽 성 페이지가 있는지 확인, 없으면 null)
- 요청 사이 0.3초쯤 쉬고, 같은 주소를 반복해서 열지 않는다.

## 보고(한국어, 짧게)
몇 개 모았는지, 칸별 빈칸 수, 막힌 사이트, 판단이 애매했던 이름 목록.
