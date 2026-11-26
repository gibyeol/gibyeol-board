# 크리스마스 키워드 페이지 — 출처 기록 (초안, 공개 안 함)

작성: Claude(밤 하위 작업), 2026-11-27 00:3x KST. 확인 시각은 모두 2026-11-27 00:00~01:30 KST(서버 date 기준).
방법: 이 세션 네트워크에서 열리는 곳만 `curl`로 원문 HTML을 받아 글자 그대로 읽음(스크린숏·헤드리스 브라우저 안 씀). 페이지 숫자는 아래 인용과 글자 대조로 확인.
원문 텍스트 보관: 비공개 저장소 wondu-archive `staging/overnight-2026-11-27/raw/christmas/`(파일 이름은 아래 표 '원문' 칸). 공개 저장소에는 넣지 않음(기사 저작권).
2차(2026-11-27 01:31~01:36 KST): 원두 허용 [7eb4ec94#2712] 뒤 새로 열린 호스트에서 받은 것 = 아래 A2. 이때 koreatimes·koreaherald·mediahub.seoul.go.kr·english.visitseoul.net·daiso.co.kr은 이 세션에서 다시 안 열렸다(어젯밤 1차 때는 열림, 1차 원문은 보관소에 있음).

## A. 연 출처 (페이지에 쓴 것)

| # | 출처 | 날짜 | 가져온 것 (원문 그대로 / 페이지에 쓴 꼴) | 페이지 위치 |
|---|---|---|---|---|
| S1 | 아성다이소 공식 '시즌/시리즈상품 > 2026 크리스마스 마켓' https://www.daiso.co.kr/brand/product/season/180 | 페이지에 게시일 없음 · 11/27 확인 | 상품 카드 47장, 품번(7자리) **76개**, 가격은 전부 **1,000원·2,000원·3,000원·5,000원** 중 하나(기계적으로 셈: 원문 줄에서 `_가격원` 62개 = 1,000원 21 / 2,000원 18 / 5,000원 15 / 3,000원 8). 페이지에 쓴 상품: 집모양 어드벤트 캘린더(24칸)_1081347_5,000원, 어드벤트 캘린더(24칸)_1082356_3,000원, 책모양 어드벤트 캘린더(14칸)_1081348_3,000원, 퍼즐 어드벤트 캘린더(24칸)_1081501_5,000원, LED 트리_1081011_5,000원, 트리 오르골_1081487_5,000원, 별장식 리스_1084209_2,000원, 고깔 가랜드_1080575_1,000원, 워터볼 미니_1081499_1,000원/소형_1081497_2,000원/중형_1081880_3,000원/LED_1083194_5,000원, 대형 산타 장식(40cm)_1081351_5,000원, 입체 팝업 카드_1081878_1,000원, 포장지_1080955_1,000원 | 트렌드 칸 큰 숫자, '다이소 크리스마스 마켓' 목록, 코어 칸 용어 |
| S2 | 아성다이소 공식 다이소소식 '다이소몰, 크리스마스 신상을 한자리에! ‘다이소 득템 대전 크리스마스 마켓’ 행사 진행' https://www.daiso.co.kr/brand/daiso_news/126062?btype=product | 2026-11-16 | "11 월 16 일 오전 9 시부터 20 일 오후 6 시까지 … 시즌 신상 500 여 종" / "어드벤트 캘린더부터 장식 소품 , 완구까지" / 집 모양 어드벤트 캘린더 "24 개의 서랍장 … 초콜릿이나 쪽지로 직접 채워 넣는 DIY" / 퍼즐 "총 1,008 조각의 퍼즐을 24 일간 나누어 맞추는" "24 개의 상자에 42 개씩". 결제 이벤트는 "신한 슈퍼 SOL’ 또는 ‘SOL 페이 ’ 로 5 천 원 이상 결제 시 마이신한포인트 500P"(11/16~20, 끝남) | '더 보기'(왜 뜨나요), 어드벤트 캘린더 용어 |
| S3 | 다이소몰 홈 https://www.daisomall.co.kr/ (robots.txt: `User-agent: *` → `Allow: /ds/`, ClaudeBot `Allow: /`) | 11/27 확인 | 메뉴에 '크리스마스 마켓'(링크 `/ds/diy/C109`)과 '랭킹'(`/ds/rank/C105`)이 있다. 배너 글: "크리스마스 마켓\n2026년 신상 득템". 두 페이지 본문은 브라우저에서 스크립트로 그려져서 HTML에는 상품·순위가 없음 → **순위 숫자는 못 읽음**(헤드리스·내부 API 호출 안 함). 링크만 씀. 매장 재고: 다이소 공식 홈의 '재고 조회' 버튼 → https://prdm.daisomall.co.kr/ms/msb/SCR_MSB_0011?tab=tab2 (이 주소는 이 세션에서 안 열려 화면 단계 미확인) | '사러 가기' 링크, 재고 확인 줄 |
| S4 | The Korea Herald 'Seoul is beginning to look like Christmas' https://www.koreaherald.com/article/10929679 | 2026-11-08 15:31 | "around 50 days before Christmas"(크리스마스 약 50일 전부터 매장 장식) / 롯데 본점(명동) "20,000 light bulbs"(전구 2만 개) + "Christmas market" / 롯데 잠실점 "Christmas market from Nov. 19 to Jan. 3", "2,645-square-meter outdoor plaza", "17-meter-tall clock tower" / 신세계 명동 미디어 파사드 "through Jan. 31, every day from 5 p.m. to midnight" / 더현대 서울 H빌리지 뉴욕 테마 마켓 "Walk-in access will also be available for international visitors"(해외 방문객은 예약 없이 입장 가능) / 갤러리아 압구정 로로피아나 트리 "through Dec. 31"(12/31까지). 롯데 잠실 "Christmas market from Nov. 19 to Jan. 3"(11/19~1/3 크리스마스 마켓), "2,645-square-meter outdoor plaza"(야외 광장 2,645㎡), "17-meter-tall clock tower"(17m 시계탑), 신세계 "through Jan. 31, every day from 5 p.m. to midnight"(1/31까지 매일 17~24시) | 띠(D-day), 큰 숫자, '구경하며 사는 곳' |
| S5 | 서울시 내 손안에 서울 '누가 돌아왔게? 52일간의 설렘, 서울윈터페스티벌' https://mediahub.seoul.go.kr/archives/2020167 | 2026-11-25 17:20 | "광화문 마켓 (12.11.~'27.1.10.)은 ‘시간이 멈춘 산타마을’을 주제로 … 크리스마스 소품과 먹거리 판매 부스" / "로맨틱 한강 크리스마스마켓 (12.24.~12.27.)" 뚝섬한강공원 / 스탬프 투어 5곳 중 3곳 → 인근 상권 바우처 / 종로구·중구 야간(17~24시) 서울사랑상품권 5% 페이백 "계획" | 띠, '구경하며 사는 곳' |
| S6 | 서울관광재단 VISIT SEOUL '2026 Gwanghwamun Market' https://english.visitseoul.net/eventsx/2026GwanghwamunMarket/ENP0rc1ic | 11/27 확인 | "Dec 11, 2026 ~ Jan 10, 2027"(2026-12-11~2027-01-10) / "Sunday - Thursday 17:30~22:00, Friday - Saturday 17:30~22:30"(일~목 17:30~22:00, 금·토 17:30~22:30) / "Free admission"(무료 입장) / "Subway Line 5 Gwanghwamun Station Exit 9, 181m"(5호선 광화문역 9번 출구 181m) / "+82-2-3788-8168" | '구경하며 사는 곳' 광화문 줄 |
| S7 | The Korea Times 'Sejong Center's outdoor garden transforms into winter market' https://www.koreatimes.co.kr/lifestyle/people-events/20261117/sejong-centers-outdoor-garden-transforms-into-winter-market | 2026-11-17 | 세종문화회관 예술의정원 커튼콜 가든 겨울 마켓 "through Jan. 3", "daily from 11 a.m. to 9 p.m.", "holiday decorations", "10 to 20 businesses each week", "spend at least 10,000 won … prize drawing", "Admission … free … do not need reservations"(무료, 예약 필요 없음). 뜻: 1/3까지, 매일 11~21시, 연말 장식 판매, 주마다 10~20팀, 1만 원 이상 사면 추첨 응모 | 띠, '구경하며 사는 곳' |
| S8 | The Korea Times 'Korean heritage souvenirs fuel 41% sales surge at Seoul design landmark' https://www.koreatimes.co.kr/lifestyle/people-events/20261116/korean-heritage-souvenirs-fuel-41-sales-surge-at-seoul-design-landmark | 2026-11-16 | DDP 디자인스토어 1~10월 매출 "2.734 billion won"(27억 3,400만 원) "up 41.2 percent"(41.2% 증가) / 크리스마스 선물 기획전 "from Monday to Dec. 25"(월요일~12/25, 기사 월요일 = 11/16) / "about 30 new products developed with Seoul Museum of History"(서울역사박물관과 만든 신상 약 30종) / 많이 팔린 것(순위 없이 나열): 서울 스티커 모음, 사대문·4대궁 엽서, 복 물고기 자석, 대한제국 트럼프 카드 / 온라인: "Naver Smart Store, KakaoTalk Gift and Ohouse"(네이버 스마트스토어·카카오톡 선물하기·오늘의집) | 큰 숫자, 띠, '선물' 목록 |
| S9 | The Korea Times 'From jade rings to flowers: What young Koreans are buying at Namdaemun' https://www.koreatimes.co.kr/lifestyle/trends/20261118/from-jade-rings-to-flowers-what-young-koreans-are-buying-at-namdaemun | 2026-11-18 | "the artificial flower section is brimming with affordable Christmas decorations, from tree ornaments and festive dolls to twinkling lights" / 꽃시장은 "Building E’s third-floor", "Vendors begin closing around 3 or 4 p.m." , "Bring cash or arrange a bank transfer"(현금이나 계좌이체 준비 — 꽃시장 손님 조언). 첫 인용 뜻: 조화 상가에 트리 장식·인형·반짝이 전구 등 싼 크리스마스 장식이 가득. 꽃시장은 E동 3층, 상인들은 오후 3~4시부터 문을 닫기 시작 | '구경하며 사는 곳' 남대문 줄 |
| S10 | The Korea Herald 'Christmas cake wars heat up' https://www.koreaherald.com/article/10942858 | 2026-11-21 (수정 11/22) | 콘래드 서울 "25,000 won to 135,000 won" / 포시즌스 78,000·99,000·150,000원 / 반얀트리 80,000~85,000원 "Reservations begin Dec. 1"(12/1부터 예약) / 풀만 앰배서더 이스트폴 89,000~120,000원 "promotional benefits … reservations made by Nov. 30"(11/30까지 예약하면 혜택) / 안다즈 강남 "200,000 won … through Dec. 27"(20만 원, 12/27까지) / 르메르디앙 명동 "available through Dec. 28"(12/28까지) | 띠, '케이크' 줄 |
| S11 | CJ뉴스룸(CJ푸드빌 보도자료) '뚜레쥬르, 이도현과 함께한 홀리데이 캠페인 영상 공개…케이크 사전예약도' https://cjnews.cj.net/%eb%9a%9c%eb%a0%88%ec%a5%ac%eb%a5%b4-%ec%9d%b4%eb%8f%84%ed%98%84%ea%b3%bc-%ed%95%a8%ea%bb%98%ed%95%9c-%ed%99%80%eb%a6%ac%eb%8d%b0%ec%9d%b4-%ec%ba%a0%ed%8e%98%ec%9d%b8-%ec%98%81%ec%83%81-%ea%b3%b5/ | 2026-11-11 | "오는 12월22일까지 뚜레쥬르 앱에서 홀리데이 제품 35종에 대해 사전예약 시 최대 30% 할인" / "사전예약한 제품은 오는 12월18일부터 25일까지 매장에서 픽업" | 띠, '케이크' 줄 |
| S12 | The Korea Times 'Starfield Library decorates Christmas with goblin Santa, palace-inspired tree' https://www.koreatimes.co.kr/lifestyle/people-events/20261116/starfield-library-decorates-christmas-with-goblin-santa-palace-inspired-tree | 2026-11-16 | 코엑스 별마당도서관 캠페인 "through Jan. 31, 2027"(2027-01-31까지), 일월오봉도 모양 트리, 민화 오너먼트 만들기 "Wednesdays from Nov. 18 to Dec. 30"(11/18~12/30 매주 수요일), 한정 굿즈(책갈피·키링) "through Dec. 31"(12/31까지) | '구경하며 사는 곳' |
| S13 | 인천국제공항 '제한물품' https://www.airport.kr/ap_ko/906/subview.do | 11/27 확인 | 액체류 기내휴대 "개별 용기당 100ml 이하로 1인당 1L 비닐 지퍼백 … 1개 한해 반입 가능하며, 국내선은 제한없음", 위탁수하물 "가능". **스노우볼·워터볼은 이 페이지에 따로 적혀 있지 않음**(검색어 스노우·스노볼·워터볼 0건) | 코어 칸 '비행기 탈 거면' |
| S14 | 위키백과(영어) 'Advent calendar' https://en.wikipedia.org/wiki/Advent_calendar | 11/27 확인 | "many reusable Advent calendars … begin on December 1"(다시 쓰는 어드벤트 캘린더는 대부분 12월 1일에 시작) | 코어 칸 용어 |
| S15 | 위키백과(영어) 'Christmas market' https://en.wikipedia.org/wiki/Christmas_market | 11/27 확인 | "a street market associated with the celebration of Christmas during the four weeks of Advent. These markets originated in Germany"(크리스마스 전 대림절 4주 동안 여는 거리 시장, 독일에서 시작) | 코어 칸 용어 |
| S16 | 위키백과(영어) 'Music box' https://en.wikipedia.org/wiki/Music_box | 11/27 확인 | 오르골 = 핀이 박힌 원통이 돌며 쇠빗살을 튕겨 소리를 내는 상자 | 코어 칸 용어 |
| S17 | 위키백과(영어) 'Garland' https://en.wikipedia.org/wiki/Garland | 11/27 확인 | "A garland is a decorative braid, knot or wreath of flowers, leaves, or other material … hung on an inanimate object … used to decorate, especially around holidays"(꽃·잎 등을 엮은 장식, 물건에 걸기도 하고, 특히 명절·휴일 장식에 씀) | 코어 칸 용어 '가랜드' |
| S18 | 위키백과(영어) 'Snow globe' https://en.wikipedia.org/wiki/Snow_globe | 11/27 확인(재시도 끝에 받음) | "a transparent sphere … The sphere also encloses the water … the globe is shaken to churn up the white particles … the flakes fall down slowly through the water"(투명한 공 안에 물, 흔들면 흰 가루가 일었다가 천천히 내려옴). 다이소 '워터볼' = 스노볼이라는 연결은 Claude 추론(다이소 페이지에 설명 없음) | 코어 칸 '워터볼(스노볼)' |
| S19 | 위키백과(영어) 'Wreath' https://en.wikipedia.org/wiki/Wreath | 11/27 확인 | "an assortment of flowers, leaves, fruits, twigs, or various materials that is constructed to form a ring shape"(꽃·잎·열매·가지 등을 고리 모양으로 만든 것) | 코어 칸 '리스' |

## A2. 2차에 연 출처 (2026-11-27 01:31~01:36 KST, 페이지·데이터 파일에 쓴 것)

데이터 파일 `christmas-data.json`의 `sources` id와 같은 이름을 괄호에 적음. 인용은 원문 그대로, 뜻은 괄호.

| # | 출처 (id) | 날짜 | 가져온 것 (원문 그대로) | 원문 파일 | 페이지 위치 |
|---|---|---|---|---|---|
| S20 | 신세계그룹 뉴스룸 이마트 보도자료 '미리 크리스마스! 이마트 트리∙장식용품 최대 30% 할인' https://www.shinsegaegroupnewsroom.com/e-mart-sale-on-trees-and-decorations/ (ssg-emart) | 2026-11-26 | "11월 26일부터 12월 2일까지 일주일간 크리스마스 대표 트리상품을 신세계포인트 적립 시 최대 30% 할인" / "대표상품인 '원터치 팝업트리(150cm)'를 9만9,000원에서 20% 할인한 7만9,200원" / "단 5초만에 설치" / "오너먼트, 조명, 리본 등이 모두 포함된 '올인원(All-in-One)'세트" / "60cm는 7,900원에서 6,320원에, 120cm는 9,900원에서 7,920원에, 150 cm는 11,900원에서 9,520원" / "실속형 상품" / 트레이더스 "오는 29일(일)까지 삼성카드 결제 고객 대상" / "매년 베스트셀러 상품 'LED 와이어전구(1000구)'세트도 5만5,800원에서 6천원 할인된 4만9,800원" | ssg-emart-xmas.txt | 띠, '가게가 앞세운 상품', 값 카드, 트리 4가지, 할인 조건 팁 |
| S21 | 신세계그룹 뉴스룸 신세계까사 보도자료(까사미아) https://www.shinsegaegroupnewsroom.com/casamia-unveils-christmas-home-decor-picks/ (ssg-casamia) | 2026-11-23 | "까사미아 온라인몰에서는 11월(11/1~11/20) 크리스마스 관련 상품 매출이 전월 동기 대비 3.7배 증가했다" / "12월 31일까지 … 크리스마스 장식 소품을 온 · 오프라인 채널에서 30% 할인" / "11월 23일부터 12월 24일까지 크리스마스 홈데코 기획전 'HAPPY HOLIDAY'를 열고 관련 상품을 최대 50% 할인할 예정" | ssg-casamia.txt | 큰 숫자 1, 띠, '왜 뜨나요' |
| S22 | 브릿지경제 '트리 만들고 장식 달고… 11번가, 크리스마스 집 꾸미기 기획전' https://www.viva100.com/article/20261125500124 (viva-11st) | 2026-11-25 09:58 | "11번가는 오는 29일까지 '미리 만나는 크리스마스' 기획전을 열고 … 최대 20% 할인" / "이달 13~22일 '크리스마스 소품' 검색량은 직전 열흘보다 102% 늘었다. '크리스마스 리스 …'(49%)와 '크리스마스 장식'(48%), '크리스마스 트리'(32%) 검색량도 증가" / "벽에 걸 수 있는 트리" | viva100-11st.txt | 큰 숫자 2, 막대, 띠 |
| S23 | 테크M '1만원으로 연말 분위기 낸다...' https://www.techm.kr/news/articleView.html?idxno=157824 | 2026-11-26 11:36 | S20·S22와 같은 숫자(이마트 7만9200원·6320/7920/9520원, 11번가 검색 102%·49%·48%·32%)를 다시 보도 — 교차 확인용 | techm-157824.txt | (출처 목록) |
| S24 | 뉴스투데이 '이마트·11번가·신세계푸드, 트리부터 케이크까지' https://www.news2day.co.kr/article/20261126500087 (n2d-emart) | 2026-11-26 10:13 | "무장식 트리와 오너먼트·LED 전구·트리 스커트 등을 갖춘 풀세트, 잡아당기기만 하면 설치할 수 있는 접이식 원터치 트리" / "공간 활용도를 높인 벽 트리" / 신세계푸드 "26일부터 이마트 내 베이커리 매장에서 크리스마스 케이크 판매" "대표 상품은 … '딸무크'… 가격은 2만 7980원이다. 지난해 크리스마스 직전 10일 동안 하루 평균 1000개가량 판매" | news2day-emart.txt | 트리 4가지, '딸무크' 줄, 케이크 표 |
| S25 | 뉴스투데이 '지그재그·다이소몰·갤러리아몰, 연말 쇼핑 대전' https://www.news2day.co.kr/article/20261116500099 (n2d-daiso) | 2026-11-16 10:51 | "대표 상품인 '집 모양 어드벤트 캘린더'" (다이소몰 행사 설명). 같은 기사의 '장바구니 쿠폰 12%·8%'는 갤러리아몰 행사(11/16~22, 끝남, 크리스마스 품목 아님) → 안 씀 | news2day-zigzag.txt | '집모양 어드벤트 캘린더' 줄의 '대표 상품' |
| S26 | 헤럴드경제 '롯데타운 잠실에 영국 크리스마스 마켓…첫 주말 4만명' https://biz.heraldcorp.com/article/10942206 (herald-lotte) · 같은 글 재게재 https://biz.heraldcorp.com/article/10943937 (11/20) | 2026-11-19 09:17 | "지난 9일 오후 2시 롯데백화점몰 등에서 시작한 국내 사전 예약에는 동시접속자가 1만6000명 넘게" / "이달 말까지 이용할 수 있는 주말 패스트패스 입장권은 30분 만에 매진" / "첫 주말인 22일까지 방문객이 4만명을 넘을 것으로 추산" / "내년 1월 3일까지 46일간, 매일 오전 11시 30분부터 오후 10시까지" / "40여개 입점 상점" / "매일 오전 11시 30분부터 오후 9시 30분까지 2층 회전목마" / 장소 "잠실 월드파크 야외 잔디광장" | herald-lotte-jamsil.txt, herald-lotte-jamsil2.txt | 큰 숫자 3, 띠, 마켓 표 롯데 줄 |
| S27 | 서울경제 '잠실 롯데타운에 영국의 크리스마스 떴다' https://www.sedaily.com/article/20116554 (sedaily-lotte) | 2026-11-19 16:46 | "운영 시간은 매일 오전 11시 30분부터 오후 10시까지" / "40개 부스 가운데 절반인 20개를 F&B 매장" / "'클룩'을 통해 외국인을 대상으로 사전 예약을 진행한 결과, 약 1만 건 … 전체 사전 예약의 약 20%" | sedaily-lotte-jamsil.txt | 마켓 표, '왜 뜨나요' |
| S28 | 테크M '백화점 3사 크리스마스 전쟁' https://www.techm.kr/news/articleView.html?idxno=157526 (techm-dept3) | 2026-11-19 09:53 | 신세계 홀리데이 마켓 "강남점은 지난달 30일, 대전점은 이달 13일 문을 열었으며 본점은 오는 24일, 센텀시티점은 27일부터" / "크리스마스 소품과 선물 브랜드 … 캐리커처와 타로" / H빌리지 "네이버 예약을 통해 진행된 1차 예약도 마감" "사전 예약 외에 현장 대기 방식도 운영" | techm-157526-dept3.txt | 마켓 표 신세계 줄, '사지 않아도 볼 것' |
| S29 | 서울경제 '11월부터 불붙은 크리스마스 경쟁…백화점 3사' https://www.sedaily.com/article/20111414 | 2026-11-07 09:58 | H빌리지 "오는 10일부터 5층" "최대 10m 높이의 붉은 벽돌 건물 13개 동" "누적 관람객은 지난해까지 150만 명을 넘어섰다" "외국인 전용 예약과 현장 대기 접수 창구도 별도로" | sedaily-dept3.txt | '사지 않아도 볼 것', '왜 뜨나요' |
| S30 | 세계일보 '더현대 서울에 크리스마스 인 뉴욕 시티' https://www.segye.com/newsView/20261109515475 | 2026-11-09 23:00 | "12월31일까지 더현대 서울 5층 사운즈 포레스트에 크리스마스 마을 'H빌리지'" "1980∼1990년대 미국 뉴욕" | segye-hyundai.txt | '사지 않아도 볼 것' |
| S31 | 브릿지경제 '[비바100] 유통가 크리스마스 특수 잡아라' https://www.viva100.com/article/20261113500760 | 2026-11-18 07:00 | 롯데타운 크리스마스 마켓 "올해로 4회째" "2023년 첫 개최 이후 지난해까지 누적 방문객 수는 110만 명을 돌파" | viva100-xmas.txt | '왜 뜨나요' |
| S32 | 세계일보 '크리스마스 앞두고 벨리곰·헬로키티·미키마우스 총출동' https://www.segye.com/newsView/20261123502199 | 2026-11-23 08:10 | "롯데홈쇼핑은 지난 13일 아성다이소와 크리스마스 굿즈 20종을 출시했다. 산타 복장을 한 인형과 아크릴 키링, 파우치 등을 다이소 직영 매장에서 판매" / 스타벅스 "지난 19일부터 12월 31일까지 … 머그와 텀블러, 토트백 등 협업 굿즈 22종을 두 차례에 걸쳐" | segye-character.txt | '선물' 더 보기 |
| S33 | 세계일보 '벌써 크리스마스?…다이소 500종·스타벅스 헬로키티·해태 한정판까지' https://www.segye.com/newsView/20261116513915 | 2026-11-16 16:11 | 해태제과 어드벤트 캘린더 "12월 10일부터 크리스마스이브인 24일까지 15일간 하루에 한 칸씩" | segye-daiso500.txt | '선물' 더 보기 |
| S34 | 아시아경제 '루돌프·산타 입은 과자·라면…' https://view.asiae.co.kr/article/2026112410414025650 | 2026-11-24 10:58 | "오리온은 … 어드벤트 캘린더까지 크리스마스 한정판 과자세트 8종" / "'산타마을 어드벤트 캘린더' … 14일 동안 매일 하나씩" | asiae-snack.txt | '선물' 더 보기 |
| S35 | 아주경제 '1000만명 찾은 서울윈터페스티벌, 한강까지 넓힌다' https://www.ajunews.com/view/20261125131022252 (ajunews-winterfest) | 2026-11-25 | "뚝섬한강공원에서는 12월 24일부터 31일까지 '한강 나이트 사우나' … '로맨틱 한강 크리스마스마켓'과 연계". **마켓 운영 시간은 이 기사에도 없음** | ajunews-winterfest.txt (+ajunews-winterfest2, asiae-winterfest 같은 내용) | 마켓 표 한강 줄 |
| S36 | 이데일리 '기프티콘, 언제 보내야 좋을까' https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=02312406645317720 | 2026-01-14 07:46 | KT알파 '기프티쇼 비즈'(기업 전용 모바일 상품권 대량발송) 지난해 데이터: "크리스마스 이브부터 당일에는 평소 판매 1위인 스타벅스를 제치고 '파리바게뜨 크리스마스 케이크'가 최다 판매 … 전체 판매금액의 약 20% … 스타벅스보다 발송량도 20% 이상" | edaily-gifticon.txt | 케이크 더 보기 |
| S37 | 서울경제 '불황에도 뜨겁다…크리스마스 케이크 예약 전쟁' https://www.sedaily.com/article/14161949 | **2025**-12-23 16:18 | "이마트에 따르면 이달 1일부터 22일까지 장식 및 소품 카테고리 매출은 전년 동기 대비 9% 늘었다"(= 2025년 12/1~22) | sedaily-cake.txt (sedaily-8x.txt는 같은 기사 다른 판) | '지난해 참고' |
| S38 | 다이소몰 매장 재고 화면 https://prdm.daisomall.co.kr/ms/msb/SCR_MSB_0011?tab=tab2 | 11/27 01:34 확인 | HTTP 200이지만 HTML에는 메뉴 글자('다이소몰 - 매장', 홈·카테고리·검색…)뿐, 본문은 스크립트로 그려짐 → **재고 조회 단계 확인 못 함**(스크립트 실행·내부 API 호출 안 함). etnews(2026-10-20 기사, etnews-daiso-app.txt)는 앱 '매장 서비스' 메뉴의 '상품인증정보'(QR·품번 입력)만 설명 — 재고 조회 아님 | prdm-stock-page.txt | 코어 칸 재고 팁(문구 그대로 둠) |

2차에 받았지만 쓰지 않은 것: 신세계그룹 뉴스룸 '이마트, 크리스마스 장식용품 최대 60% 할인'(**2020-12-13** 글, ssg-emart-60.txt) — 올해 것이 아님. 아시아경제 2026-11-06 백화점 기사(asiae-dept-foreign.txt)의 롯데 본점 지난 5년 행사 매출 증가율 — 크리스마스 품목 매출이 아니라 점포 매출이라 안 씀. 아주경제 2026-11-24 다이소 연 매출 5조 기사(ajunews-daiso.txt) — 크리스마스 품목 숫자 없음.

## B. 못 연 출처 · 확인 결과 (2차 반영, 2026-11-27 01:4x KST)

우회하지 않았다(프록시 거부 = curl HTTP 000, 사이트 자체 거부 = 403 등). 검색 결과 요약에 보인 숫자는 원문을 열기 전에는 쓰지 않는다.

### B1. 1차에 막혔다가 2차에 열린 것 — 결과
| 출처 | 1차 때 검색 요약에 보인 것 | 2차에 원문을 연 결과 |
|---|---|---|
| 브릿지경제 viva100 20261125500124 | 11번가 '크리스마스 트리' 결제거래액 +24%, 결제고객 +68%, 소품 검색 +102%, 리스 +49%·장식 +48%·트리 +32% | 검색 증가율 4개는 원문에 있음 → 씀(S22). **'결제거래액 +24%·결제고객 +68%'는 이 기사 원문에 없음** → 안 씀(검색 요약이 다른 글과 섞였을 수 있음, 출처 미확인) |
| 테크M 157824 | 유통가 크리스마스 기획전 | 열림 → 교차 확인용(S23) |
| 신세계그룹 뉴스룸 까사미아 | 3.7배 | 원문 그대로 있음 → 씀(S21) |
| 뉴스투데이 20261126500087 | 이마트 11/26~12/2 | 원문 있음 → 씀(S24). 이마트 공식 보도자료(S20)로도 확인 |
| 다이소 매장 재고 prdm.daisomall.co.kr | 화면 단계 | 열리지만 빈 껍데기(S38) → 단계 미확인 |

### B2. 지금도 못 연 것 / 못 찾은 것
| 무엇 | 상태 | 어떻게 하면 |
|---|---|---|
| 올해 크리스마스 상품 **판매 순위**(몇 위) | 연 출처 중 순위를 낸 곳 없음. 다이소몰 랭킹 `/ds/rank/C105`·크리스마스 마켓 `/ds/diy/C109`는 스크립트로만 그려짐(1차 확인) | 원두 휴대폰 화면(경량 패딩 때처럼) — 원두 결정 필요 |
| 크리스마스 **할인 코드** | 연 공식 발표·기사 0개. 있는 건 조건부 할인(이마트 신세계포인트 적립, 트레이더스 삼성카드) | 각 앱 쿠폰함은 로그인 화면이라 이 세션에서 확인 불가 |
| 롯데 잠실 마켓 가장 가까운 역·출구 | 연 기사(S26·S27·S28·S31)에 역·출구 없음. 롯데 공식(lotteshopping.com)은 이 세션에서 안 열림(000) | 롯데 공식 안내 또는 VISIT SEOUL 롯데월드타워 페이지(english.visitseoul.net, 이번엔 안 열림) |
| 한강 크리스마스마켓 시간·출구 | 서울시 11/25(S5)·아주경제·아시아경제 모두 시간 없음 | 서울시 후속 발표 |
| 남대문 조화 상가 동·층 | 코리아타임스(S9) "꽃시장(E동 3층)에서 몇 블록" 뿐. 이데일리 사진 기사 4건 열어 봄 → 상가 이름 없음(보관 안 함) | 남대문시장 공식 안내도(미확인) |
| 호텔 케이크 예약 링크 | 호텔 사이트(포시즌스·힐튼·반얀트리·아코르·하얏트·메리어트, 첫 화면 주소로 시험) 모두 000 | 원두 허용 또는 그대로 '각 호텔 앱' 안내 |
| 이마트·11번가·까사미아·더현대·롯데 공식 상품 페이지 | 모두 000 → 상품 링크는 보도자료·기사로 연결함 | 허용 시 공식 판매 페이지로 교체 |
| 편의점(CU·GS25·세븐일레븐) 올해 크리스마스 케이크 | 검색에 2026년 기사 없음(2025년 것만) → 안 씀 | 발표 나오면 추가 |
| 올리브영 홀리데이 | global.oliveyoung.com은 사이트가 403 'Access restricted'(봇 차단). CJ뉴스룸 검색에 2026 크리스마스 글 없음. Rakuten 광고주라 원두 직접 검토 대상 | 이번엔 안 씀 |
| 코리아타임스·코리아헤럴드·서울시 미디어허브·VISIT SEOUL·다이소 공식 | 2차 때 이 세션에서 다시 000(1차 원문은 보관소에 있음) | 1차 숫자는 그대로 둠 |
| m.sedaily.com, view.asiae.co.kr 일부 | m.sedaily는 000 → www.sedaily.com 같은 글로 받음. asiae 2026111915522557930은 두 번 000 → 안 씀(같은 내용은 S26·S27) | — |
| 위키미디어 공용 사진 추가 | 이번엔 시도 안 함(사진 범위 밖) | — |

## C. 상황판(data/deals.json)과 어긋나는 점 — 고치지 않음(라이브 데이터라서), 원두 확인 필요

- `seoul-winter-market-2026`: 상황판은 2026-12-12~12-31 `expected`(작년 기준). 서울시 11/25 발표(S5)·VISIT SEOUL(S6)은 **12/11~2027-01-10**. → 확정으로 바꿀 근거 있음.
- `ttukseom-xmas`: 상황판은 블로그 한 곳 근거 `expected`. 서울시 11/25 발표(S5)에 "로맨틱 한강 크리스마스마켓 (12.24.~12.27.)" → 확정 근거 있음.
- 스토리 판(drafts/shop-storyboard.md)의 다이소 "신한 SOL페이 3만 원 이상 1,000P ~11/30"은 S2의 "5천 원 이상 500P(11/16~20)"와 다른 이벤트다(S2 하단 '다음 글: 신한 SOL페이 프로모션'). 1,000P 건은 이번에 원문을 다시 열지 않아 페이지에 안 씀.

## D. 사진 (위키미디어 공용만, 라이선스 확인, 핫링크 안 함)

- 쓴 것: `photos/xmas-ornaments.webp` ← [Christmas ornaments in Seoul, South Korea - DSC00723.JPG](https://commons.wikimedia.org/wiki/File:Christmas_ornaments_in_Seoul,_South_Korea_-_DSC00723.JPG), Daderot, **CC0**(공용 API 라이선스 값 'CC0', 'Own work'), 2011-12-03 촬영. 위쪽 장식 부분만 잘라 씀(지나가는 사람 얼굴 빠짐), 780×452 WebP. 기록: `photos.json`. 공개할 때 `static/photo/`로 복사해야 화면에 나옴(지금은 초안 폴더에만 있음).
- 안 쓴 것: [Christmas impression Seoul, Korea (11266996415).jpg](https://commons.wikimedia.org/wiki/File:Christmas_impression_Seoul,_Korea_(11266996415).jpg)(CC BY-SA 2.0) — 사진 앱 필터로 뭉개져 '불편한 이미지'[7eb4ec94#1776]라서 뺌. [Myeongdong Crowd at Christmas, Seoul.jpg](https://commons.wikimedia.org/wiki/File:Myeongdong_Crowd_at_Christmas,_Seoul.jpg)(CC BY-SA 4.0, 2017) — 사람 얼굴이 주인공인 군중 사진이라 안 받음. 'Nightview of the Gwanghwamun Square 2024.jpg'는 공공누리 1유형이라 이번 지시(CC0/PD/CC BY/BY-SA만)에 맞지 않아 뺌.
- 위키미디어가 요청 과다(429)로 자주 막혀서 후보를 넓게 보지 못했다. 어드벤트 캘린더·워터볼 같은 품목 예시 사진은 찾지 못함.
