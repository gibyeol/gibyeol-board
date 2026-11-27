# 할인판 공식 링크 — 독립 검토 (2026-11-28 KST, 검토자: 작성자 아님)

- 대상: 브랜치 claude/determined-euler-xsz86i 커밋 f786c38 (data/deals.json 항목별 `go`, build.py 버튼).
- 운영자 원문: "쇼핑할인판 보니까 각 페이지 연결루트가 없던데 달아야하지 않겠어? 할인정보만 있고 관련 링크가 없으면 신뢰도가 떨어질거 같은데." [7eb4ec94#4073]
- 방법: (1) 커밋 전후 deals.json을 항목 단위로 비교 (2) 저장본 `wondu-archive/raw-from-scratchpad/deals-2026-11-28/*.html` 본문 확인 (3) 이 세션에서 go 주소 29개를 curl로 다시 열기(우회 없음) (4) `python3 build.py` 후 4개 언어 할인판 HTML 확인.
- 판정은 고치지 않고 적기만 했다.

## 0. 데이터 손실 여부
- 확실: 36개 항목 모두 유지, `go` 외 필드 변경 0건(파이썬으로 항목별 비교). 위에 빈 `"notes": {}` 키 하나 추가.
- diff가 2246줄인 이유: 들여쓰기가 1칸→2칸으로 바뀜(내용 변경 아님). 다음 변경 검토가 어려워지므로 권고 R1.

## 1. 공식 도메인인가 (29개 고유 주소)
- 제3자·블로그·단축 링크: **0건**. 모두 그 회사·기관 도메인.
- 판정 통과: musinsa.com, oliveyoung.co.kr, klook.com, shinsegae.com, lotteshopping.com, ehyundai.com, koreagrandsale.co.kr(한국방문의해위원회), visitseoul.net(서울관광재단), shilladfs.com, samsung.com, coupang.com, a-bly.com, zigzag.kr, trinityairways.com, topten10mall.com, amazon.com, spao.com, zara.com, hm.com, cathaypacific.com, jejuair.net, eastarjet.com, festival.seoul.go.kr(서울시), 11st.co.kr, eapp.emart.com(이마트·트레이더스 전단), tlj.co.kr, guud.com.
- 주의: guud.com은 '까사미아' 이름이 아닌 신세계까사 운영 몰(조사 문서 근거: 검색 결과의 회사 소개). 공식이지만 버튼만 보면 다른 회사처럼 보일 수 있음 → 권고 R4.
- 행사 페이지를 못 찾아 첫 화면(kind=site)으로 둔 것이 22개 중 대부분 — 조사 문서의 "확인 못 한 행사 주소는 쓰지 않음" 원칙대로임(통과). 단, 첫 화면만으로는 원두 원문의 "연결루트"를 절반만 채움(약함, 숨기지 않음).

## 2. kind=event 8개 — 실제 그 행사 페이지인가 (저장본 본문 기준)
| 항목 | 주소 | 저장본 확인 | 판정 |
|---|---|---|---|
| samsung-week | samsung.com/sec/event/samsung-week/ | 제목 "Samsung Week", 본문 "2026.11.01 - 2026.11.30", 카드 7% 할인 11/1~11/30 | 통과 |
| cathay-bf | flights.cathaypacific.com/ko_KR/offers/black-friday-2026.html | 제목 "블랙프라이데이 특별 혜택", 예약 2026-11-30까지 | 통과 |
| seoul-winter-market-2026 | english.visitseoul.net/events/2026GwanghwamunMarket/… | "2026 Gwanghwamun Market", "Dec 11, 2026 ~ Jan 10, 2027" — 항목 날짜와 일치 | 통과 |
| ttukseom-xmas | festival.seoul.go.kr …festacode=415 | "2026 로맨틱한강 크리스마스 마켓 기간 2026-12-24 ~ 2026-12-27" — 항목과 일치(조사 문서의 12/18 의문은 이 페이지 기준 해소) | 통과 |
| traders-xmas-2026 | eapp.emart.com/tradersclub/flyerImgView.do | 전단 행사기간 11/23~11/29, "LED와이어전구 1000구 삼성카드 55800 6000", "LED 크리스마스 리스 35800 5000" — 카드 문구 가격과 일치 | 통과(주마다 바뀌는 주소, 11/29 이후 다른 전단) |
| emart-xmas-2026 | eapp.emart.com/leaflet/leafletView_EL.do | "[미리 준비하는 크리스마스] 행사기간 11.26(목)-12.2(수)", 팝업트리 99,000→79,200 | 통과(주마다 바뀌는 주소) |
| shilla-dfs-bf | shilladfs.com/estore/kr/ko/event | 행사 전용이 아니라 **이벤트 목록**. 다만 "2026 신라블프", "2026 SHILLA BLACK FRIDAY" 배너가 있음. 기간 표기는 본문에 없음 | 약하게 통과(버튼 '행사 페이지'는 다소 과함) |
| lotte-jamsil-xmas-2026 | lotteshopping.com/contents/christmas-market | 저장본·이번 curl 본문 모두 **2025 일정만**("2025 CHRISTMAS MARKET 일정 25.11.20 - 26.01.04"). 2026 정보 없음 | **불합격 후보** — 카드(2026-11-19~2027-01-03) 옆 '행사 페이지'를 누르면 작년 일정이 보임. 브라우저에서 스크립트로 2026이 뜨는지는 확인 못 함 |

### checked가 있는데 근거가 약한 것
- **zara-bf (www.zara.com/kr/ko/, checked 2026-11-28)**: 저장본 없음. 이 세션 curl은 사이트가 **403 "Access Denied"**(프록시는 통과, Akamai 쪽 거부). "열어 확인함"을 지금 재현 못 함.
- 저장본 없이 checked만 있는 것 6개: shinsegae, lotteshopping/main, ehyundai, zigzag, zara, tlj. 이번 재확인: lotteshopping/main 200(본문 "[WINTER SALE] 최대 40-50%"), zigzag 200("지그재그 스토어"), tlj 200("뚜레쥬르"), shinsegae·ehyundai 200이지만 본문은 메타 리다이렉트(`/index.do`, `gate.do`)만 — 공식 사이트 존재 확인 수준. zara는 위.
- checked가 없는 것(저장본이 Access Denied·오류): casamia(guud 이벤트 경로 Access Denied), trinity(Access Denied), jejuair(오류 페이지), amazon(500 리다이렉트) → 첫 화면 + checked 없음으로 둔 처리는 **맞음**.

## 3. 이 세션 curl 재확인 (`curl -sL -m 25`, 2026-11-28 02시대 KST)
- 200: shinsegae, lotteshopping/main, ehyundai, visitseoul, shilladfs/event, samsung-week, zigzag, cathay, jejuair(단 본문은 "JEJUAIR ERROR OCCURED"), festival.seoul.go.kr, eapp 전단 2개, tlj, lotte christmas-market
- 사이트 403(우회 안 함): musinsa, oliveyoung, klook, coupang, a-bly, trinityairways, zara, hm, eastarjet, guud
- 503: amazon.com
- 못 엶: en.koreagrandsale.co.kr(TLS "unable to get local issuer certificate"), www.11st.co.kr(시간 초과), spao.com(301 → www.spao.com 프록시 거부), **www.topten10mall.com(인증서 CN=topten10mall.com, www 이름 불일치)**
  - topten: 인증서가 www를 포함하지 않아 브라우저에서 경고가 뜰 수 있음(추론 — 이 세션 프록시 경유 관찰 1회, 실제 브라우저 확인 아님). topten10mall.com(www 없음)은 프록시가 막아 비교 못 함.

## 4. 빌드·언어
- `python3 build.py` → "built 160 pages", 오류 없음.
- 버튼 글(공식 링크만 집계):
  - ko 30장 카드 / 링크 30: 공식 사이트 22, 행사 페이지 8
  - en 7장 / 9: Event page 4, Official site 2, Shinsegae·Lotte·Hyundai Official site 각 1
  - ja 7장 / 9: イベントページ 4, 公式サイト 2, 新世界·ロッテ·現代 公式サイト 각 1
  - zh-tw 7장 / 9: 活動頁面 4, 官方網站 2, 新世界·樂天·現代 官方網站 각 1
- 각 언어 보이는 카드 중 공식 링크 없는 카드: 0.
- 태그 짝 검사(파서): 4개 파일 모두 열림·닫힘 오류 0.
- 약함: en/ja/zh-tw 카드의 링크 다수가 한국어 페이지(shilladfs kr/ko, lotteshopping, oliveyoung.co.kr, festival.seoul.go.kr). 외국어 사용자가 눌렀을 때 바로 못 읽음 → 권고 R3.

## 반드시 고칠 것
1. **lotte-jamsil-xmas-2026**: '행사 페이지'가 2025 일정만 보여 줌(저장본·재확인 둘 다). 카드 날짜와 어긋나 원두 원문의 "신뢰도"를 오히려 떨어뜨림. kind를 site로 낮추거나, 2026 공식 안내 주소를 찾기 전까지 checked 의미를 "열림"이 아니라 "내용 일치"로 쓸지 정해야 함.
2. **zara-bf checked 2026-11-28**: 저장본 없고 지금 403 Access Denied. 근거를 남길 수 없으면 checked를 빼야 "checked=열어 확인한 날짜" 규칙과 맞음.

## 권고
- R1. deals.json 들여쓰기를 원래(1칸)로 되돌려 diff를 실제 변경만 보이게. 빈 `notes: {}`는 쓰임 없으면 제거.
- R2. checked를 단 6개(shinsegae, lotteshopping/main, ehyundai, zigzag, zara, tlj)도 저장본을 같은 폴더에 남길 것 — 지금은 이 6개의 '열어 봄'을 기계로 대조할 방법이 없음.
- R3. 외국어판: 언어별 공식 주소가 있는 곳은 그것으로(예: koreagrandsale은 조사 문서에 jp./tw. 하위 도메인 있음). 없으면 버튼 옆에 "(한국어)" 표시 검토.
- R4. dept-shinsegae 등 첫 화면 링크와 guud.com처럼 이름이 다른 도메인은 ko판에도 회사 이름을 붙이면(예: "신세계까사 공식 몰") 덜 헷갈림.
- R5. topten10mall.com: www 인증서 불일치 관찰 — 브라우저에서 한 번 열어 경고 여부 확인.
- R6. 전단 2개(traders, emart)는 주마다 내용이 바뀌는 고정 주소. 카드 종료일(11/29, 12/2) 뒤에도 카드가 남는 화면이 있으면 링크를 내려야 함.
- R7. shilla-dfs-bf는 이벤트 목록이라 '행사 페이지'보다 '공식 이벤트 목록' 성격. 버튼 종류를 하나 더 둘지 판단.
