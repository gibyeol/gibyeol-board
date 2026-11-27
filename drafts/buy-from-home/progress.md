# 진행 기록 — 집에서 사는 법 초안 (drafts/buy-from-home)

공개하지 않는 초안. build.py는 drafts/를 읽지 않음. 원두가 아침에 검토.

## 한 일
- 2026-11-26 밤: 명세·원칙(CLAUDE.md 콘텐츠 제작 원칙, ops/shop-spec.md, ops/affiliate-signup-list.md), 공개된 olive-young.md·kbeauty-how-to-choose.md 읽음.
- 접속 시험(curl, 한 번씩): YesStyle·Stylevana·올리브영 글로벌·올리브영 글로벌 고객센터·무신사 글로벌 = 사이트가 자동 접속 차단(봇 확인 화면·Captcha·Access restricted·Cloudflare). 우회하지 않음.
  iHerb·올리브영 US·각국 세관(미국 CBP 제외) = 이 세션 네트워크 설정이 막음. CBP = 사이트 차단(Access Denied).
  일본 세관(customs.go.jp) = 열림.

- 공식으로 확인한 것: CJ뉴스룸 보도자료 2건(올리브영 US US$35·글로벌 US$60·블루밍턴 물류센터·배송 5~7영업일의 절반, 글로벌몰 시즌세일 연 4회), 일본 세관 FAQ 7건.
- buy-from-home.md(한국어 초안), sources.md(출처·못 연 것), review.md(자체 점검, 종합 FAIL: 데이터 빈칸) 작성.
- 스크래치 빌드 미리보기 390·1280: /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/buy-from-home/

- 2026-11-27 01:30~02:20 KST (원두 네트워크 허용 [7eb4ec94#2712] 뒤 2차):
  - 다시 접속 시험(curl -A 'Mozilla/5.0', 주소당 1회): iHerb 배송·반품 페이지, 올리브영 회사 사이트, 영국·캐나다·호주·싱가포르·대만·홍콩 세관, EU 뉴스 = 열림. 올리브영 US·글로벌(고객센터 포함)·iHerb 고객센터 = Cloudflare/Access restricted, CBP = Access Denied, EU 소비자 안내 = 429, YesStyle 고객센터 = 프록시 502. 우회 안 함.
  - 원자료 저장: wondu-archive staging/overnight-2026-11-27/raw/buy-from-home/ (커밋 27105d0, aa67484).
  - buy-from-home.md: 비교 표 9/24칸(1차 5칸), 나머지 '확인 못 함' 표시와 이유. iHerb 카드·반품 3단계, 세금 '내 나라 한 줄' 표 8개 나라 + 나라별 접기, 출처 ①~㉑ 접기. (gibyeol-board 41d0ae8 외)
  - sources.md: ⑩~㉑ 원문 인용·주소·날짜, 2차 '열지 못한 것'. 인용 66개 원자료와 기계 대조 일치.
  - review.md: 2차 자체 점검(부분 PASS, 공개 불가), 남은 빈칸·원두 결정 6개.
  - 미리보기: /tmp/claude-0/-home-user/7eb4ec94-764c-5989-af23-6a2e9e40b53c/scratchpad/buy-from-home/v2_*.png, seg2/

## 남은 일 (원두 결정 뒤)
- 남은 빈칸: review.md 2차 '원두가 정할 것' 1·3·6.
- 독립 검토, 분류 결정, en·ja·zh-tw판, 올리브영 내용 원두 직접 승인.

## 2026-11-27 22:2x~22:4x KST — 공개 판 4개 언어로 완성 (원두 [7eb4ec94#3538] "그렇게 해", [7eb4ec94#3526] "(나)로 진행해")
- 3차 접속(주소당 1회, `curl -sL -A 'Mozilla/5.0'`, 우회 없음): Stylevana = 403 "Enable JavaScript and cookies"(사이트 봇 확인) → 칸 못 채움. YesStyle 고객센터 = 프록시 502. 올리브영 US·글로벌·두 고객센터 = 403(Access restricted / Cloudflare). CBP = Access Denied. iHerb 배송·반품 = 200(인용 다시 일치), iHerb K-Beauty 분류 페이지(새 출처 ㉒) = 200. EU 소비자 안내 주소 = 404, 통계 페이지만 열림(VAT 규칙 없음 → 안 씀). 원자료: wondu-archive staging/overnight-2026-11-27/raw/buy-from-home/round3-2026-11-27/.
- content/{ko,en,ja,zh-tw}/buy-from-home.md 새로 씀(브랜치 커밋 7e44674에 메인 세션이 함께 담음). 초안에서 바꾼 것:
  - '확인 못 함' 칸 전부 삭제 → "그 쇼핑몰 안내에서 확인" 또는 행 삭제. YesStyle·무신사 글로벌 행 삭제(공식 정보 0). Stylevana는 표에서 빼고 '다른 쇼핑몰(예: Stylevana)' 카드 + 일반 링크만(원두 [#3538]).
  - 세금 표 미국 행·미국 접기 삭제, 대만 우편 줄 삭제, EU 'VAT 확인 못 함' → "부가세는 내 나라 세관 안내". '표에 없는 나라는 그 나라 세관 안내' 한 줄.
  - 제목 '한국에서 뜨는' 삭제(독립 검토 필수 3). 올리브영 글로벌 US$60은 "2026년 5월 회사 발표" 표시(원문 과거형).
  - `disclosure: yes` 삭제: 제휴 링크 0개라 사이트 공통 '일부 제휴 링크' 문구·Skimlinks/Travelpayouts 스크립트가 붙지 않게 함 → 본문 "지금은 모두 일반 링크"가 사실과 맞음. disclosure.md(Stylevana 승인·링크 없음, 올리브영 Rakuten 신청)와 일치.
  - `section` 삭제: main build.py는 이 쪽을 'Guides › 한국 여행 가이드'로 표시(틀림, 독립 검토 필수 6). build.py는 안 고침 → 경로 표시 없음.
  - iHerb K-Beauty 분류(㉒) 추가, 실수 목록에 iHerb 반품 확인 메일 1줄.
  - 언어별 세금 표 순서: ko 초안 그대로 / en 영국·캐나다·호주·싱가포르·홍콩 먼저 / ja 일본 먼저 / zh-tw 대만·홍콩·싱가포르 먼저.
- 링크 1줄씩: content/*/olive-young.md '#home' 절, content/*/shopping.md 끝.
- 빌드: origin/main 스냅숏(scratchpad/mainbuild2)에 바꾼 12개 파일 복사 → `python3 build.py` built 160 pages, 내부 링크 깨짐 0, '확인 못'·마크다운 잔여 0. 390·1280 화면 확인(scratchpad/bfh3/shot_*.png).

## 남은 일
- 독립 검토(작성자 아님) → 통과 시 main 공개(메인 세션).
- 사진·공식 화면 0장(독립 검토 '실사 우선' 미반영 그대로). Stylevana 배송·반품 칸은 사이트 차단으로 비어 있음 → 원두가 화면을 주거나 Awin 링크 받을 때 다시.
- 분류: build.py GUIDE_GROUPS '쇼핑과 할인'에 buy-from-home을 넣으면 쇼핑 경로가 맞게 나옴 — build.py 변경이라 별도 결정.
