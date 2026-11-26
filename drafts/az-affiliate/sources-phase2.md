# 제휴 A to Z 2단계: 열어 본 출처와 인용 (2026-11-27 02:29~ KST 열람, Claude)

원문 저장: wondu-archive `staging/az-affiliate-2026-11-27/raw/` (브랜치 claude/determined-euler-xsz86i, MANIFEST.md에 주소·결과). 아래 인용은 그 파일의 글자 그대로(태그만 뺀 .txt). 페이지에 넣은 문장은 이 인용을 줄인 것.

## 차단·실패 (우회 안 함)
| 호스트 | 결과 | 막힌 것 |
|---|---|---|
| www.klook.com | 403, DataDome 캡차 "Please enable JS and disable any ad blocker" (`curl -A 'Mozilla/5.0'` 1회) | 티머니 공항 수령·와우패스·공항철도 직통·SKT eSIM 2개 상품의 받는 곳·사용 방법·값·환불 → **확인 못 함** |
| yesim.app | 202 본문 0, `x-amzn-waf-action: challenge` | Yesim 요금제·설치 안내·환불 → **확인 못 함** |
| eng.tmoney.co.kr | 이 환경 프록시가 CONNECT 403 | 티머니 영문 안내 → 확인 못 함 |
| www.tmoney.co.kr (본문 주소) | 연결 재설정 | 확인 못 함 |
| www.samsungsvc.co.kr | 502 "홈페이지 시스템 점검 안내" 2회 | abroad-esim의 기존 출처 2개 재확인 못 함 |
| tpx.li | 열지 않음(클릭 기록 위험) | — |

## 공항철도 (airportrailroad.com) — raw/arex-*.txt
- 직통열차 이용안내 `/train/express/guide`: "자동발매기 이용 / 서울역 : 공항철도 서울역 지하 2층 / 인천공항1터미널역 : 인천공항 제1여객터미널 지하1층 교통센터 / 인천공항2터미널역 : 인천공항 제2여객터미널 지하1층 교통센터"; "해외발행 신용카드 비자카드 마스터카드 JCB카드 다이너스클럽카드 아메리칸익스프레스카드 유니온페이카드(은련카드)"; "결제된 승차권에는 QR코드가 생성됩니다. QR코드가 표시된 승차권을 확인하셔서 게이트에서 QR코드를 스캔하시면 통과 후 열차에 탑승할 수 있습니다."; "1층에 도착하여 엘리베이터나 에스컬레이터를 이용하여 지하1층에 도착 후 승차표를 구입. 게이트를 지나서 다시 엘리베이터나 에스컬레이터를 이용하여 지하4층에 있는 타는 곳으로 이동"; 승차권 문구 "열차 출발시각 3분 전 까지 승강장에 도착하셔야 합니다."; "승차권 변경은 3회까지 가능하며, 2회 이상 변경 시 수수료가 발생합니다. (변경 수수료는 열차 출발 당일 2회 이상 변경하는 경우에 한하여 발생)"; 할인 선택 "체크박스&교환번호 - 교환번호 13자리 입력 칸과 인증버튼", "쿠폰 또는 바우처 번호가 있거나 제휴할인 카드가 있을 경우 할인을 선택하실 수 있습니다."
- 제휴사 `/train/express/partners`: "제휴사 여행사 코네스트 한유망 KKDAY 서울패스 한차오 KLOOK 노랑풍선 하나투어 Creatrip"
- 도심공항터미널 이용안내 `/train/express/city/info`: "이용대상 직통열차 승차권 구매 고객 / 이용방법 직통열차 승차권의 QR코드를 도심공항터미널 게이트에 스캔하여 입장 및 이용"; "탑승수속 : 05:20 ~ 19:00 (접수마감 18:50)"; "인천공항1터미널 : 항공기 출발 3시간 전 수속완료 / 인천공항2터미널 : 항공기 출발 3시간 20분 전 수속완료"
- FAQ(목록 40건): "탑승수속은 직통열차 승차권을 소지한 본인에 한해 가능하며 대리수속은 불가합니다."; "현재 출발 당일 8개 항공사 [아시아나항공, 제주항공, 티웨이, 에어서울, 에어부산, 대한항공, 진에어, 이스타]"
- **확인 못 한 것:** 클룩에서 산 직통열차 표가 공항철도 QR 승차권으로 바로 오는지, 교환번호로 바꾸는 방식인지(공항철도 페이지에 클룩 표 처리 방법 문장 없음). → 도심공항 수속에 클룩 표가 되는지도 직접 근거 없음.

## 와우패스 (wowpass.io, robots `Allow: /`) — raw/wowpass-*.txt, wowpass-ko-guide-strings.txt
- 사용 안내(/ko/guide 화면 문구): "티머니 잔액은 WOWPASS 잔액과 별도로 충전해야해요."; "WOWPASS는 전국에 설치된 WOWPASS 무인환전기를 통해 외화 현찰, 원화 현찰은 물론 신용카드를 사용해 간편하게 충전할 수 있고, 모바일 앱을 통해서도 해외신용카드나 모바일 페이로 잔액을 충전할 수 있어요."; "무인환전기에서 16종 화폐 현금 또는 신용카드로 충전해요."; "WOWPASS 결제 잔액은 WOWPASS 기기에서 원화로 출금이 가능해요. 한번에 10만원씩 여러 번 출금할 수 있고, 1회당 출금 수수료는 1,000원이에요."; "WOWPASS 카드에 내장된 티머니 잔액은 별도로 충전해야 이용할 수 있어요. 일반 교통카드와 동일하게 지하철역/편의점 등에서 충전하거나, 모바일앱에서 WOWPASS 잔액으로 충전 가능해요."; "앱 NFC 기능을 이용해 WOWPASS 잔액을 티머니 잔액으로 전환할 수 있어요."; "티머니 잔액은 남은 금액에 따라 환불방법이 달라요. … 환불 수수료는 500원이에요."; "티머니타운 방문 (서울역 10번 출구 티머니 본사 1층, 평일 9시-18시)"; "50,000KRW이상의 잔액은 티머니 본사에서만 환불이 가능하니"; "잔액 출금은 원화 현금으로만 가능하며, 1,000원 미만 동전은 출금할 수 없습니다."; "단, 티머니 잔액의 경우 실물카드를 잃어버리면 WOWPASS를 재발급해도 되찾을 수 없어요."
- 와우패스 자체 예약(기기 수령) 안내 문구: "키오스크에서 '카드 발급'을 선택한 후, '예약 코드로 발급' 버튼을 눌러주세요. / 여권을 스캔하고, 발급받은 코드를 입력해주세요. / WOWPASS 카드가 기기에서 나오면 한번 기계에 꽂아 활성화해주면 발급 완료! / 앱에 카드를 등록해주세요."; "바우처를 사용하지 않았다면, 바우처 유효기간 내 취소가 가능합니다. 바우처를 사용한 후에는 환불이 불가능합니다."
- 와우패스 자체 예약(CU 수령) 문구: "T1: CU편의점 2·3·4호점(영업시간 : 24시간) / T2: 입국장 A 바로 왼편에 있는 CU편의점 2호점(영업시간 : 24시간)", "구매 후 취소 / 환불이 불가능합니다." — **와우패스 공식 예약 경로의 것. 클룩 상품에 같은지 모름 → 페이지에 수령 장소로 쓰지 않음.**
- 와우패스 eSIM 안내 문구: "eSIM QR코드를 설치한 뒤에는 환불이 불가능해요" — essentials의 "설치한 뒤에는 환불이 안 되는 곳이 있어요"의 근거(와우패스 eSIM 한 곳의 예).
- 예약 화면(/ko/purchase): "전국 약 446대의 무인 키오스크". 카드 값(5,500원 등)은 화면 HTML에 없음(스크립트로 불러옴) → **값 재확인 못 함.**

## 인천국제공항공사 (airport.kr 1008) — raw/airport-kr-ap_ko-1008.txt
- "공용 ATM 24H … 제1여객터미널 지하1층 공항철도 일반열차 승차권 발매기 인근"; 같은 이름 1층: "1층 일반지역 4번 / 6번 / 9번 / 11번 출입구 부근".
- 로밍센터: "SKT 로밍센터 06:00 ~ 22:00 … 제1여객터미널 1층 동편 A 입국장 부근", "SKT 로밍센터(24H) … 제1여객터미널 1층 서편 F 입국장 부근" (페이지에는 안 넣음 — 클룩 SKT eSIM 수령과 관계가 확인되지 않음).

## 코리아헤럴드 10947683 — raw/koreaherald-10947683.txt
"The card costs 15,000 won ($11.20), including 5,000 won for the card itself and 10,000 won in transit credit. It is available from T-money vending machines at the airport railroad stations serving Terminals 1 and 2. The machines accept cash and credit cards issued in South Korea or overseas."; "AREX's announcement did not specify whether passengers can reload the new card with a credit card after purchase."

## Apple (support.apple.com, ko-kr/en-us/ja-jp/zh-tw) — raw/apple-*.txt
- 118669(ko): "카메라 앱을 열고 QR 코드를 스캔합니다. '셀룰러 요금제가 감지됨' 알림이 표시되면 이 알림을 탭합니다. / iOS 17.4 및 이후 버전이 설치된 iPhone을 사용 중이고 … QR 코드를 길게 탭합니다. 그런 다음 'eSIM 추가'를 탭합니다. / 화면 하단에 있는 '계속'을 탭합니다. / '셀룰러 요금제 추가'를 탭합니다."; 링크: "링크를 탭하여 eSIM을 설정합니다. / 새 eSIM 활성화 알림이 나타나면 '허용'을 탭합니다."
- 118227(ko): "설정 앱을 엽니다. '일반'을 탭합니다. '정보'를 탭합니다. iPhone이 해제되어 있는 경우 이동통신사 잠금 항목에 'SIM 제한 없음'이라는 메시지가 표시됩니다."; "'여행용 eSIM 켜기'를 탭합니다. '여행용 eSIM 전용'과 '여행용 SIM 및 현재 eSIM' 중 무엇을 사용할지 선택합니다. 두 회선을 모두 사용하기로 선택하면 여행용 eSIM이 데이터용으로 사용됩니다. 거주지 eSIM에서 여전히 로밍 요금이 부과될 수도 있습니다."; "'셀룰러'를 탭한 다음 '셀룰러 데이터'를 탭합니다. 사용할 회선을 선택합니다."; 귀국: "사용하려는 기본 eSIM 옆에 '이 회선 켜기'가 활성화되어 있는지 확인합니다. 더 이상 사용하지 않는 다른 여행용 eSIM 회선을 모두 끕니다." (iPhone XS·XS Max·XR 이후)
- 109317(ko): "한 번에 한 번호만 셀룰러 데이터를 사용할 수 있습니다."; "각 요금제의 셀룰러 설정을 변경하려면 … '셀룰러' 또는 '모바일 데이터'를 탭합니다. 변경하려는 전화번호를 탭합니다. 각 옵션을 탭하고 평상시와 같이 설정합니다."; "셀룰러 데이터를 사용하는 번호에 데이터 로밍이 켜져 있으면 …" — **'데이터 로밍' 스위치 이름은 이 문장에서 가져옴. 번호별 메뉴 목록에 이름이 직접 나열되지는 않음(원두 폰 화면으로 확인 필요).**
- 102478(ko): "에어플레인 모드를 켰다가 끕니다. / 설정 앱을 열고 '셀룰러'를 탭합니다. … 회선을 껐다가 다시 켭니다. / 기기를 재시동합니다."; "iPhone의 IMEI 또는 EID. … '일반'을 탭한 다음 '정보'를 탭합니다."
- ja-jp·zh-tw·en-us 같은 문서에서 메뉴 이름 확인: ja「モバイル通信プランが検出されました」「続ける」「モバイル通信プランを追加」「eSIMを追加」「許可」「旅行用のeSIMをオンにする」「旅行用eSIMのみ」「旅行用eSIMと現在のeSIM」「モバイル通信」→「モバイルデータ通信」「SIMロック」「SIMロックなし」「この回線をオンにする」データローミング・機内モード / zh-tw「偵測到行動方案」「繼續」「加入行動方案」「加入 eSIM」「開啟旅遊 eSIM」「僅旅遊 eSIM」「旅遊 eSIM 和目前的 eSIM」「行動服務」→「行動數據」「電信業者鎖定」「沒有 SIM 卡限制」「開啟此號碼」數據漫遊・飛航模式 / en "Cellular Plan Detected", "Add Cellular Plan", "Turn On Travel eSIM", "Cellular → Cellular Data", "No SIM Restrictions", "Turn On this Line".

## Samsung (samsung.com)
- sec/support/newsalert/3184 (2023-02-20): "1단계) 설정 에서 연결 을 선택 후, SIM 관리자 를 눌러주세요. 2단계) eSIM 추가 를 누른 후 QR 코드 스캔 을 선택하세요. 3단계) 이동통신사에서 제공한 QR 코드를 스캔합니다."; 수동: "QR 코드 스캔 을 선택하고 활성화 코드 입력 을 눌러주세요."
- jp galaxy-esim…: "「設定」 > 「接続」 > 「SIM マネージャー」 「eSIM を追加」 > 「QR コードをスキャン」"
- tw galaxy-esim… (2026-09-21 갱신): "前往 設定 > 連接 > SIM 卡管理工具 輕觸 新增 eSIM ，然後輕觸 掃描 QR 碼"; "輕觸 輸入啟用碼"
- us ANS10001619: "Tap SIM manager. From here, you can tap the switch next to your physical SIM or activated eSIM to enable or disable their connections. You can also tap Primary SIM to change the default connection for making calls, sending texts, and using data."; "Restart the device to apply the eSIM profile."
- uk data roaming (2026-06-05): "Open the Settings app / Tap Connections / Tap Mobile Networks / Tap the switch to activate or deactivate Data Roaming / If the Data Roaming switch is greyed out, check that Mobile data is activated."
- uk dual SIM (2026-10-08): "Open the Settings app, then tap Connections / Tap SIM Card Manager / Tap Calls, Text Messages or Mobile data / Tap the SIM card you would like to switch to"
- ie eSIM (2022-01-14): "You can find the EID on the box of your smartphone or in Settings > About phone > Status."
- **번역한 메뉴 이름(삼성 원문에 해당 언어 표기 없음):** ko '모바일 데이터'·'모바일 네트워크 → 데이터 로밍'·'휴대전화 정보 → 상태 정보'(마지막은 기존 abroad-esim에 있던 것), ja「モバイルデータ」「モバイルネットワーク → データローミング」「端末情報 → ステータス情報」, zh-tw「行動數據」「行動網路 → 數據漫遊」「關於手機 → 狀態資訊」. 실제 화면 글자와 다를 수 있음 → 원두 폰 화면 또는 각국 삼성 문서로 확인 필요.
