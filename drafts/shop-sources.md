# 쇼핑 데이터 출처 목록 (1차) — 2026-11-26 확인

작성: Claude(하위 작업). 확인 방법: 이 세션 환경에서 `curl`로 robots.txt와 첫 페이지를 열었다. User-Agent는 정직하게 `NadriResearchBot/0.1 (manual research)`를 썼다. 차단을 우회하려고 가짜 헤더나 헤드리스 브라우저를 쓰지 않았다.
원본: robots.txt 원문은 wondu-archive `staging/shop-trends-2026-11-26/robots/`, 기사 원문 발췌는 같은 폴더(비공개)에 있다.

## 읽는 법
- **접근(오늘)**: open = 열림. site-403 = 사이트 자체 봇 차단(Cloudflare 등 확인 화면). proxy-403 = 이 작업 환경의 네트워크 정책이 막음. 사이트 문제가 아니므로 GitHub Actions에서는 열릴 수 있다(확인 안 됨). reset = 연결 끊김.
- **판정**: auto = robots가 허용하고 공개 페이지라 자동 수집 후보. manual = 사람이 보고 옮김. no = 쓰지 않음. ? = 확인 못 함.
- **약관**: robots.txt 말고 이용약관의 자동 수집 조항은 **오늘 어느 곳도 읽지 않았다.** 그래서 auto 판정은 모두 "robots 기준, 약관 확인 전"이다. 다음 단계에서 읽는다.
- **분류**: 출처가 스스로 나눠 발표하는 분류(예: '외국인 구매')와 그 주기. 원두 원칙: 우리가 분류를 만들지 않는다 [7eb4ec94#1605].

## 1. 공식 보도자료·뉴스룸

| 출처 | URL | 주는 것 | 출처가 발표하는 분류·주기 | 접근 | robots.txt (원문 인용) | 판정 |
|---|---|---|---|---|---|---|
| CJ 뉴스룸 (올리브영·CJ ONE·CJ제일제당·CJ온스타일) | https://cjnews.cj.net/ | 올영세일 검색·구매 분석(세일마다), 올리브영 어워즈(매년 11월 말~12월), 외국인 구매 통계, CJ ONE 쿠폰·혜택, 비비고 판매 | 전체(세일 분석), '외국인 구매'(2025-12-03, 2026-08-31 등 비정기, 대략 반기 간격), 어워즈 부문 40개(연 1회) | open | `User-agent: *` / `Disallow: /wp-admin/` / `Disallow: /?s=` / `Disallow: /search/` / `Sitemap: https://cjnews.cj.net/sitemap.xml` | auto (sitemap·글 페이지) |
| 다이소 공식(다이소소식) | https://www.daiso.co.kr/brand/daiso_news?btype=product | 다이소몰 기획전(크리스마스 마켓, 겨울나기), 카드 혜택 | 기획전 단위(월 2~4건) | open | `User-agent: *` / `Disallow: /common/` … `Allow: /` | auto |
| 무신사 뉴스룸 | https://newsroom.musinsa.com/ | 무신사 판매 데이터 보도자료 | ? | proxy-403 | 확인 못 함 | ? |
| 면세점(신라) | https://www.shilladfs.com/ | 행사·쿠폰 | ? | open (첫 페이지 660KB) | `User-agent: *` / `Crawl-delay: 5` / `Disallow: /files/` … | auto 후보(행사 페이지 구조 미확인) |
| 면세점(신세계) | https://www.ssgdfs.com/ | 행사·쿠폰 | ? | robots open, 첫 페이지 406 | `User-agent: *` / `Allow: /` | ? (406 = 사이트가 요청 거부) |
| 면세점(현대) | https://www.hddfs.com/ | 행사 | ? | open | 검색엔진·AI 봇 목록만 `Allow: /`, 그 밖은 `User-agent: *` / `Disallow: /` | no(자동) / manual |
| 면세점(롯데) | https://www.lottedfs.com/ | 행사 | ? | robots open, 첫 페이지 연결 실패 | `User-Agent:ClaudeBot` … `Claude-User` `Disallow:` (빈 값 = 허용) / `User-Agent:*` / `Disallow: /` | no(자체 봇), manual |
| 편의점 CU | https://cu.bgfretail.com/ | 행사 상품(1+1 등) | ? | open, robots.txt 404(규칙 없음) | 없음 | auto 후보(약관 확인 전) |
| 편의점 GS25 | https://gs25.gsretail.com/ | 행사 | ? | 301 후 proxy-403 | 확인 못 함 | ? |
| 세븐일레븐 / 이마트24 | www.7-eleven.co.kr / www.emart24.co.kr | 행사 | ? | proxy-403 | 확인 못 함 | ? |
| BGF리테일·GS리테일 본사 | www.bgfretail.com / www.gsretail.com | 보도자료 | ? | proxy-403 | 확인 못 함 | ? |

## 2. 플랫폼 공개 랭킹

| 출처 | URL | 주는 것 | 접근 | robots / 차단 내용 | 판정 |
|---|---|---|---|---|---|
| 올리브영(국내) | https://www.oliveyoung.co.kr/ | 실시간 랭킹, 어워즈 수상 목록 | site-403 (제목 "잠시만 기다려 주세요 - 올리브영", Cloudflare 확인) | robots.txt도 확인 화면으로 응답 | no(자동). 원두 휴대폰 화면 또는 사람이 브라우저로 |
| 올리브영 글로벌 | https://global.oliveyoung.com/ | 해외 판매 랭킹 | site-403 ("Access restricted") | 같음 | no(자동) |
| 무신사 / 무신사 글로벌 | www.musinsa.com / global.musinsa.com | 랭킹, 쿠폰 공지 | site-403 ("Attention Required! \| Cloudflare") | 같음 | no(자동) |
| 다이소몰 | https://www.daisomall.co.kr/ds/rank/C105 등 | 랭킹(전체·신상·리뷰·픽업·박스) | open이지만 내용은 자바스크립트로 그림. 데이터 서버 cdn.daisomall.co.kr은 proxy-403 | `User-agent: *` / `Allow: /ds/` … `Disallow: /or/` … `Crawl-delay: 30` | auto 후보: robots는 /ds/ 허용. 단 랭킹 데이터는 비공개 내부 API → 약관 확인 전까지 manual |
| YesStyle | https://www.yesstyle.com/ | 해외 K뷰티 베스트 | site-403(challenge) | robots.txt도 403 | no |
| Stylevana | https://www.stylevana.com/ | 해외 K뷰티 베스트 | 첫 페이지 site-403(captcha) | `User-agent: *` / `Content-Signal: search=yes,ai-train=no,use=reference` / `Allow: /`, 그리고 `User-agent: ClaudeBot` / `Disallow: /` | no |
| 지그재그·W컨셉·에이블리·29CM | — | 검색·색상 트렌드 | proxy-403 | 확인 못 함 | ? (언론 인용으로만 사용: kh-black-puffer) |
| 쿠팡 | www.coupang.com | 판매 순위 | proxy-403 | 확인 못 함 | ? |

## 3. 정부·관광 통계

| 출처 | URL | 주는 것 | 접근 | robots | 판정 |
|---|---|---|---|---|---|
| 관광지식정보시스템(외래관광객조사) | https://know.tour.go.kr/ | 외래관광객 쇼핑 품목(조사·연·분기). 출처 분류: 외래관광객 | open. 단 조사 메뉴가 POST 양식+자바스크립트라 내용 추출 실패 | `User-agent: Googlebot` / `Disallow: /customer/qna/` (그 밖 규칙 없음) | manual(보고서 PDF 내려받기) |
| 한국관광 데이터랩 | https://datalab.visitkorea.or.kr/ | 외래객 카드 소비(업종별) | open(302 → 메인) | `User-agent: *` / `DisAllow: /search/` | auto 후보, 화면 구조 미확인 |
| 비짓코리아(영문) | https://english.visitkorea.or.kr/ | 쇼핑·면세·택스리펀드 안내 | open | `User-agent: *` / `Disallow: /totalSearch/search.do` | auto |
| 비짓코리아(한·일·중) | korean./japanese./chinese.visitkorea.or.kr | 같음 | proxy-403 | 확인 못 함 | ? |
| 비짓서울 | www.visitseoul.net | 쿠폰·혜택 | proxy-403 | 확인 못 함 | ? |
| 정책브리핑 | https://www.korea.kr/ | 정부 보도자료(택스리펀드 등) | robots open, 검색 요청은 reset | `User-Agent: *` / `Allow: /` | auto 후보 |
| 서울시 뉴스 | https://news.seoul.go.kr/ | 서울시 행사·혜택 | open | `User-agent: *` / `Allow: /` / `Disallow: /*?s=` | auto |
| 공공데이터포털·KOSIS·문체부·한국관광공사 본사 | data.go.kr, kosis.kr, mcst.go.kr, knto.or.kr | 통계 API | proxy-403 | 확인 못 함 | ? (공식 API 키 방식이면 auto 후보) |
| 한국소비자원 | kca.go.kr | 품질 비교 시험(선크림·패딩 등) | proxy-403 | 확인 못 함 | ? — '알려진 이유' 근거로 꼭 필요한 출처 |

## 4. 공식 할인·관광객 혜택

| 출처 | 주는 것 | 접근 | 판정 |
|---|---|---|---|
| CJ ONE 글로벌 쿠폰팩 (cjnews 보도) | 방한 외국인 회원 쿠폰 10종, ~12/31 | open | auto(뉴스룸 경유) |
| WOWPASS https://wowpass.io/ | 결제 카드 혜택 | open. 첫 페이지엔 후기 위주, 현재 혜택 목록은 못 뽑음 | robots `User-Agent: *` / `Allow: /` → auto 후보 |
| 코리아그랜드세일 www.koreagrandsale.co.kr | 외국인 대상 세일 | proxy-403 | ? |
| 카드사(신한·현대 등)·Visa·Mastercard·알리페이·위챗 | 관광객 프로모션 | proxy-403 | ? |
| 면세점 외국인 쿠폰 | — | 위 1번 표 참조 | 신라만 auto 후보 |

## 5. 언론 (수치 보도 = '경향')

| 출처 | 접근 | robots | 판정 |
|---|---|---|---|
| The Korea Herald https://www.koreaherald.com/ | open | `User-agent: *` / `Allow: /` / `Disallow: /_TP/` … `Sitemap: …/sitemap/latest-articles` (제목 포함 최근 기사 사이트맵) | auto(최신 사이트맵으로 키워드 감지) |
| The Korea Times https://www.koreatimes.co.kr/ | open | `User-agent:*` / `Disallow:/preview` | auto |
| 국내 언론 대부분(연합·매경·한경·조선·중앙·동아·뉴시스·zdnet·인사이트 등), 네이버·구글 뉴스·구글 트렌드 | proxy-403 | 확인 못 함 | ? — 이 환경에서는 못 씀. 상황판(deals.json) 출처 중 zdnet·segye 등은 오늘 재확인 불가 |

## 6. 제휴 네트워크

| 출처 | 접근 | 내용 |
|---|---|---|
| Klook 제휴 https://affiliate.klook.com/ | open | 페이지 제목 "Join Klook’s Affiliate Program…" 확인. robots `user-agent: *` / `Allow: /$` |
| Awin https://www.awin.com/ | open | 제휴 네트워크 첫 페이지만. 쿠폰 피드는 가입자 전용(공개 피드 확인 못 함) |
| Amazon Associates, Involve Asia, Impact, Rakuten, CJ Affiliate, 링크프라이스, 쿠팡 파트너스 | proxy-403 | 확인 못 함 |

## 요약 (Claude 판단)
- 오늘 자동 수집이 되는 경로는 **공식 보도자료(CJ 뉴스룸·다이소)와 영문 언론(Korea Herald·Korea Times)** 뿐이다. 실시간 랭킹을 주는 곳(올리브영·무신사·YesStyle·Stylevana)은 사이트가 봇을 막는다. 그래서 자동 수집 대상이 아니고, 원두 휴대폰 화면이나 사람의 브라우저 확인이 필요하다.
- proxy-403은 이 작업 환경의 정책이고 사이트의 차단이 아니다. GitHub Actions에서는 열릴 수 있다(추론). 그때도 사이트의 robots와 약관을 먼저 읽는다.
- 다음 단계: 각 auto 후보의 이용약관 자동 수집 조항 원문 읽기, know.tour.go.kr 보고서 PDF 수동 확인, 소비자원 시험 결과 확보.
