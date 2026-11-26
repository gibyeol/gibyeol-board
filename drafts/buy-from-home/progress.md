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
