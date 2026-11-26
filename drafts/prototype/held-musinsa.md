# Held: facts read from musinsa.com through a headless browser (2026-11-26)

Status: HELD, not shown on the page, pending the owner's decision on whether reading musinsa.com this way is acceptable (coordinator instruction 2026-11-26).
How they were read: headless Chromium (Playwright) through the session proxy, 2026-11-26 about 15:20 KST. Plain curl got a Cloudflare 403. Later a Musinsa search-page fetch was refused by the permission system; musinsa.com/llms.txt asks automated tools to avoid search/filter URLs. Since then musinsa.com has not been accessed.
Pages: (A) https://www.musinsa.com/content/1566699932019111639 "오프라인에서 즐기는 무진장 쇼핑 가이드" (dated 2026.11.23 on the page); (B) https://www.musinsa.com/app/product/real_size "사이즈 측정법".
Some of the same facts also sit in data/deals.json (entries musinsa-offline-codes and musinsa-archive, source = page A, checked 2026-11-24 by the deals board; that check's method isn't recorded here).

## Page text removed from drafts/prototype/winter-light-puffer.md (verbatim, with original line numbers)

### Line 70: offline 무진장 sale row (page A)
<tr data-start="2026-11-20" data-end="2026-12-02"><td><b>무신사 무진장(오프라인 매장)</b><br><small>11월 20일~12월 2일, 전국 무신사 매장</small><br><small><b>확인:</b> 매장의 MD’s Pick 코너에 11월 11일부터 경량 패딩. ‘아우터 대전’ 다운은 일부 상품 매장 추가 최대 40%</small></td><td><span class="dday" data-today="오늘 마감">D-6</span></td></tr>

### Line 71: archive sale row (dates from deals.json musinsa-archive = 12/03–12/17 online, max 70%; page A says offline archive sale 11.20(금)–12.17(목) at 5 stores; the conflict is unresolved, see below)
<tr data-start="2026-12-03" data-end="2026-12-17"><td>무신사 아카이브 세일<br><small>12월 3~17일, 최대 70%, 지난 시즌·이월 상품</small><br><small>확인: 무신사 세일. 이번 시즌 신상품이 아니라 이월 상품이에요</small></td><td><span class="dday">12/3 시작</span></td></tr>

### Line 74: sentence about the archive sale
**고르는 순서:** 마감이 가까운 추론 세일(유니클로·스파오·탑텐·백화점)은 매장이나 앱에서 경량 패딩이 할인 대상인지 먼저 보고, 아니면 12월 2일까지인 무신사 쪽으로 가요. 블프에서 놓친 건 12월 3일부터 아카이브 세일이 2차 기회예요.

### Lines 78–89: keyword coupon codes and the note (page A; codes also in deals.json musinsa-offline-codes)
<h3 class="tr-step"><span class="n">1</span><i class="ic ic-ticket" aria-hidden="true"></i>무신사 매장 키워드 쿠폰 15%</h3>

<div class="table"><table class="codes"><thead><tr><th>코드</th><th>어디서</th><th>마감</th><th></th></tr></thead><tbody>
<tr data-start="2026-11-20" data-end="2026-12-02"><td><code>퍼재킷다퍼줄게</code></td><td>무신사 오프라인 매장 전용</td><td class="mono">12/02</td><td><button type="button" class="copy" data-code="퍼재킷다퍼줄게" data-done="복사됨">복사</button></td></tr>
<tr data-start="2026-11-20" data-end="2026-12-02"><td><code>어그도무신사랑해</code></td><td>무신사 오프라인 매장 전용</td><td class="mono">12/02</td><td><button type="button" class="copy" data-code="어그도무신사랑해" data-done="복사됨">복사</button></td></tr>
</tbody></table></div>

1. **무신사 앱에 로그인해요.** 쿠폰은 무신사 회원 계정으로 받아요. 가입에 무엇이 필요한지는 오늘 확인하지 못했어요.
2. **앱의 쿠폰함을 열고 위 코드를 그대로 입력해요.** 복사 버튼을 누르면 붙여 넣기만 하면 돼요.
3. **매장 계산대에서 앱 쿠폰을 써 달라고 말해요.** 온라인 주문에는 안 되는 매장 전용 쿠폰이에요.

<aside class="tr-note"><i class="ic ic-triangle-alert" aria-hidden="true"></i><span><b>경량 패딩에 되는지 꼭 물어보세요.</b> 무신사 안내에는 MD’s Pick 코너가 퍼 재킷·경량 패딩·퍼/패딩 슬라이드·퍼 부츠를 모았고, 키워드 쿠폰은 ‘해당 기획의 적용 대상 상품’에 쓴다고만 적혀 있어요. 코드 이름은 퍼 재킷과 어그(퍼 부츠)를 가리키고, 일부 품목은 빠질 수 있다고 해요. 계산 전에 직원에게 확인하세요.</span></aside>

### Lines 91–93: offline cart coupon (page A)
<h3 class="tr-step"><span class="n">2</span><i class="ic ic-receipt" aria-hidden="true"></i>무신사 매장 장바구니 쿠폰 10%</h3>

11월 20일~12월 2일, 10만 원 이상 사면 10%, 최대 1만 원. 무신사 ID 하나에 한 번. 상품 쿠폰과 함께 쓸 수 있어요(그 밖의 쿠폰과는 중복 안 돼요).

### Line 107: "입어 봐야 안다" (page A)
코트 안에 입을 옷이라면 직접 입어 보는 게 제일 확실해요. 무신사 안내도 겨울 아우터는 무게와 착용감, 이너 위에 걸쳤을 때의 여유와 실루엣을 입어 봐야 안다고 적었어요.

### Line 114: MD's Pick / 아우터 대전 step (page A)
4. **MD’s Pick 코너와 ‘아우터 대전’에서 경량 패딩·다운을 입어 보고**, 키워드 쿠폰이 되는지 물은 뒤 계산해요.

### Line 118: event store list (page A)
**다른 무신사 매장:** 무신사 안내에 무진장 행사 매장으로 메가스토어 용산, 스토어 성수·홍대·명동·강남 등이 나와요. 출구는 지도 앱에 매장 이름을 넣으면 나와요. 홍대·명동 가는 길은 [명동·성수·홍대 고르는 법](/ko/shopping-streets/)에 있어요.

### Line 129: size note ~2cm (page B)
2. **상품 페이지의 ‘실측’ 표와 비교해요.** 무신사는 상품마다 같은 측정 기준으로 실측을 재서 올리고, 측정 방법에 따라 약 2cm 차이가 날 수 있다고 안내해요. 1~2cm 차이는 측정 차이일 수 있어요.

### Sources sentence for pages A and B
무신사 <a href="https://www.musinsa.com/content/1566699932019111639" rel="noopener" target="_blank">「오프라인에서 즐기는 무진장 쇼핑 가이드」</a>(2026년 11월 23일: 매장 행사 11월 20일~12월 2일, 장바구니 쿠폰, 아우터 대전 추가 최대 40%, MD’s Pick 11월 11일부터 경량 패딩, 키워드 쿠폰 두 개 15%, 아카이브 세일, 행사 매장 목록)·<a href="https://www.musinsa.com/app/product/real_size" rel="noopener" target="_blank">사이즈 측정법</a>(실측 기준, 약 2cm 오차)

## Raw facts from page A as read (for restoring; quoted in Korean as on the page)
- 기간 11.20(금)–12.02(수), 전국 무신사 오프라인 스토어. "[오프라인] 무신사 무진장 장바구니 10% 쿠폰" 10만원 이상 구매 시 최대 1만원, 상품 쿠폰과 중복 가능, 그 외 쿠폰과 중복 불가, 무신사 ID 1개당 1회.
- 아우터 대전 11.20–12.02: "일부 상품 오프라인 추가 최대 40% 할인", 추가 할인 여부와 할인율은 브랜드·상품별로 다름, 매장별 입고 상품 다름.
- 아카이브 세일 11.20(금)–12.17(목), 5개 매장(메가스토어 성수 노티카 최대 67%, 메가스토어 용산 넌블랭크 최대 70%, 스토어 성수 이우가마카라스 최대 60%, 스토어 홍대 오헤시오 최대 55%, 스토어 롯데백화점 잠실점 디스커스 애슬레틱 최대 60%), "무진장 종료 후에도 12월 17일까지 이어진다".
- MD's Pick: "11월 11일부터 퍼 재킷과 경량 패딩, 퍼·패딩 슬라이드를 선보이고 있으며, 25일에는 퍼 부츠도 추가된다." 키워드 쿠폰: "무신사 App 쿠폰함에 '퍼재킷다퍼줄게', '어그도무신사랑해'를 입력하면 해당 기획의 적용 대상 상품에 사용할 수 있는 오프라인 전용 15% 할인 쿠폰", "키워드 쿠폰은 일부 품목에는 적용되지 않습니다."
- "겨울 아우터는 입어 봐야 알 수 있는 부분이 많다. 무게와 착용감은 물론, 이너 위에 걸쳤을 때의 여유와 전체적인 실루엣도 중요하다."
- Stores named on page A for 후드·니트 zones and brand focus include: 메가스토어 성수·용산, 스토어 성수·홍대·명동·강남·대구, 트리플스트리트 송도점, AK플라자 수원점, 롯데백화점 잠실점, 무신사 걸즈 타임스퀘어 영등포점; 킥스 홍대·성수·스타필드 고양; 아울렛 & 유즈드 롯데몰 은평; 런 서울숲; 엠프티 성수.
- Page B: "무신사 스토어에서는 아래의 사이즈 측정 기준에 따라 각 제품의 실측을 측정하고 있습니다." "측정 방법에 따라 약 2cm 정도의 오차가 있을 수 있습니다."

## Archive sale date conflict (review item 2)
- data/deals.json musinsa-archive: 2026-12-03 to 2026-12-17, "최대 70%. 블프에서 놓친 거 2차 기회", source page A.
- Page A as I read it: offline archive sale 11.20–12.17 at five stores (list above). I did not see a separate 12/03 start on page A.
- Not resolved: no other source I can open today states the dates. Row removed from the visible page until checked.
