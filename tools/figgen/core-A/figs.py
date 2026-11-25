import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from svglib import *
OUT = "/home/user/gibyeol-board/static/fig"
LANGS = ["en", "ko", "ja", "zh-tw"]

def pill(lang): return {"en": ("Yes", "No", 52), "ko": ("예", "아니요", 44), "ja": ("はい", "いいえ", 56), "zh-tw": ("是", "否", 44)}[lang]

# ---------- e-arrival-card-1: decision ----------
EA1 = {
 "en": dict(t=["Do you need the e-Arrival Card?"], q=[
    (["Korean citizen, or a registered", "resident of Korea?"], ["No card needed"]),
    (["Holding a valid K-ETA?"], ["No card", "Update your stay on k-eta.go.kr"]),
    (["Changing planes within 24 hours,", "never leaving the transit area?"], ["No card needed"])],
    f=("File the free e-Arrival Card", ["e-arrivalcard.go.kr", "In the 3 days before you land"])),
 "ko": dict(t=["전자입국신고서, 내야 할까?"], q=[
    (["대한민국 국민이거나", "등록외국인인가요?"], ["낼 필요 없음"]),
    (["유효한 K-ETA가 있나요?"], ["낼 필요 없음", "k-eta.go.kr에서 체류지 현행화"]),
    (["24시간 안에 환승하고", "환승 구역을 안 나가나요?"], ["낼 필요 없음"])],
    f=("무료 전자입국신고서 제출", ["e-arrivalcard.go.kr", "도착 전 3일 안에"])),
 "ja": dict(t=["電子入国申告書は必要?"], q=[
    (["韓国籍、または", "韓国の外国人登録者?"], ["不要"]),
    (["有効なK-ETAがある?"], ["不要", "k-eta.go.krで滞在先を更新"]),
    (["24時間以内の乗り継ぎで", "空港の外に出ない?"], ["不要"])],
    f=("無料の電子入国申告書を提出", ["e-arrivalcard.go.kr", "到着前3日以内に"])),
 "zh-tw": dict(t=["需要填電子入境卡嗎?"], q=[
    (["韓國籍,或已登錄的", "在韓外國人?"], ["不用填"]),
    (["持有效 K-ETA?"], ["不用填", "到 k-eta.go.kr 更新住宿"]),
    (["24 小時內轉機、", "不出轉機區?"], ["不用填"])],
    f=("填免費的電子入境卡", ["e-arrivalcard.go.kr", "抵達前 3 天內"])),
}
def ea1(lang):
    d = EA1[lang]; y, n, pw = pill(lang)
    f = Fig(d["t"][0]); f.title(d["t"])
    for q, o in d["q"]:
        f.question(q, y, o, pw); f.arrow(n)
    f.card(d["f"][0], d["f"][1], stroke=RED, sw=2, head_fill=RED, line_fill=INK)
    return f

# ---------- e-arrival-card-2: filing window ----------
EA2 = {
 "en": dict(t=["Landing on the 31st?"], s=["Days counted in Korea time"], cw=56, rows=[
    ("28th", "Too early", ["Filing has not opened yet"], "off"),
    ("29th", "Filing opens", ["3 days before arrival"], "on"),
    ("30th", "Still fine", [], "ok"),
    ("31st", "You land", ["Still possible before the", "immigration desk"], "ok")],
    e=("A card expires", ["72 hours after you submit,", "or once you pass immigration"]),
    n=["Flight moved after you filed? Submit again."]),
 "ko": dict(t=["31일에 도착한다면?"], s=["날짜는 한국 시간 기준"], cw=56, rows=[
    ("28일", "아직 일러요", ["제출이 열리지 않았어요"], "off"),
    ("29일", "제출 시작", ["도착 3일 전부터"], "on"),
    ("30일", "제출 가능", [], "ok"),
    ("31일", "도착", ["입국심사 전까지는", "제출할 수 있어요"], "ok")],
    e=("신고서 효력이 끝나는 때", ["제출 후 72시간, 또는", "입국심사를 마친 때"]),
    n=["비행기가 바뀌었다면 다시 제출하세요."]),
 "ja": dict(t=["31日に到着するなら"], s=["日付は韓国時間"], cw=56, rows=[
    ("28日", "まだ早い", ["受付が始まっていません"], "off"),
    ("29日", "受付開始", ["到着の3日前から"], "on"),
    ("30日", "提出できます", [], "ok"),
    ("31日", "到着", ["入国審査の前までなら", "提出できます"], "ok")],
    e=("申告書が使えなくなる時", ["提出から72時間、または", "入国審査を通った時点"]),
    n=["便が変わったら出し直しましょう。"]),
 "zh-tw": dict(t=["31 日抵達的話"], s=["日期以韓國時間計算"], cw=56, rows=[
    ("28 日", "太早", ["還不能填"], "off"),
    ("29 日", "開放填寫", ["抵達前 3 天開始"], "on"),
    ("30 日", "可以填", [], "ok"),
    ("31 日", "抵達", ["走到入境審查前", "都還能補填"], "ok")],
    e=("入境卡失效", ["送出後滿 72 小時,", "或通過入境審查後"]),
    n=["班機改了?重新填一次。"]),
}
def ea2(lang):
    d = EA2[lang]; f = Fig(d["t"][0]); f.title(d["t"], d["s"])
    for chip, h, ls, st in d["rows"]:
        if st == "off":
            f.card(h, ls, chip=chip, chip_w=d["cw"], fill=SOFT, stroke=SOFT, head_fill=MUTED, chip_fill=WHITE, chip_ink=MUTED)
        elif st == "on":
            f.card(h, ls, chip=chip, chip_w=d["cw"], stroke=RED, sw=2, chip_fill=RED, chip_ink=WHITE, head_fill=RED)
        else:
            f.card(h, ls, chip=chip, chip_w=d["cw"], chip_fill=INK, chip_ink=WHITE)
    f.y += 6
    f.card(d["e"][0], d["e"][1], fill=SOFT, stroke=SOFT)
    f.note(d["n"], INK, 700)
    return f

# ---------- e-arrival-card-3: real vs look-alike ----------
EA3 = {
 "en": dict(t=["Real site or look-alike?"], real="e-arrivalcard.go.kr", rl=["Ends in go.kr", "Free: no payment step"],
            fake="look-alike address", card="Card number", fl="Asks for a fee → close it",
            n=["Type the address yourself.", "Don't click a search ad."]),
 "ko": dict(t=["진짜 사이트일까?"], real="e-arrivalcard.go.kr", rl=["끝이 go.kr", "무료: 결제 단계 없음"],
            fake="이름이 비슷한 주소", card="카드 번호", fl="수수료 요구 → 바로 닫기",
            n=["주소는 직접 입력하세요.", "검색 광고는 누르지 마세요."]),
 "ja": dict(t=["本物のサイト?"], real="e-arrivalcard.go.kr", rl=["末尾が go.kr", "無料:支払い画面なし"],
            fake="よく似た名前のアドレス", card="カード番号", fl="手数料を請求 → すぐ閉じる",
            n=["アドレスは直接入力。", "検索広告は押さない。"]),
 "zh-tw": dict(t=["是官網嗎?"], real="e-arrivalcard.go.kr", rl=["結尾是 go.kr", "免費:沒有付款步驟"],
            fake="名稱很像的網址", card="信用卡號碼", fl="要收手續費 → 馬上關掉",
            n=["網址請自己輸入,", "不要點搜尋廣告。"]),
}
def browser(f, addr, addr_fill, body_h, stroke, sw):
    top = f.y
    f.raw(f'<rect x="{M}" y="{top}" width="{W-2*M}" height="{44+body_h}" rx="10" fill="{WHITE}" stroke="{stroke}" stroke-width="{sw}"/>')
    f.raw(f'<path d="M{M} {top+44} H{W-M}" stroke="{RULE}"/>')
    for i in range(3):
        f.raw(f'<circle cx="{M+16+i*12}" cy="{top+22}" r="4" fill="{RULE}"/>')
    f.raw(f'<rect x="{M+56}" y="{top+8}" width="{W-2*M-68}" height="28" rx="14" fill="{SOFT}"/>')
    f.raw(T(M + 70, top + 28, addr, 16, 700, addr_fill))
    return top + 44
def ea3(lang):
    d = EA3[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    b = browser(f, d["real"], INK, 76, INK, 2)
    for i, l in enumerate(d["rl"]):
        yy = b + 30 + i * 28
        f.raw(f'<circle cx="{M+24}" cy="{yy-5}" r="9" fill="{INK}"/><path d="M{M+19} {yy-5} l4 4 l7 -8" fill="none" stroke="{WHITE}" stroke-width="2"/>')
        f.raw(T(M + 42, yy, l, 16, 700))
    f.y = b + 76 + 14
    b = browser(f, d["fake"], MUTED, 96, RED, 2)
    f.raw(f'<rect x="{M+14}" y="{b+14}" width="{W-2*M-28}" height="34" rx="6" fill="{WHITE}" stroke="{RULE}"/>')
    f.raw(T(M + 26, b + 37, d["card"] + "  ____ ____ ____", 16, 400, MUTED))
    f.raw(f'<circle cx="{M+24}" cy="{b+71}" r="9" fill="{RED}"/><path d="M{M+19} {b+66} l10 10 M{M+29} {b+66} l-10 10" stroke="{WHITE}" stroke-width="2"/>')
    f.raw(T(M + 42, b + 77, d["fl"], 16, 700, RED))
    f.y = b + 96 + 6
    f.note(d["n"], INK, 700)
    return f

# ---------- money-1: where to change ----------
MO1 = {
 "en": dict(t=["Where to change money"], s=["Usually best to worst"], r=[
    ("City money changer", ["Usually the best rate"]), ("City bank", ["Usually in between"]),
    ("Airport counter", ["Only enough to reach your hotel"])],
    atm=("Global ATM", ["Machine fee often ₩2,000+", "plus your own bank's fee"]), n=["Ask for ₩10,000 notes."]),
 "ko": dict(t=["환전은 어디서"], s=["보통 유리한 순서"], r=[
    ("시내 사설 환전소", ["보통 가장 유리"]), ("시중은행", ["보통 중간"]), ("공항", ["숙소까지 갈 만큼만"])],
    atm=("Global ATM", ["기계 수수료 보통 2,000원 이상", "+ 카드사 수수료 따로"]), n=["만 원권으로 받으세요."]),
 "ja": dict(t=["両替はどこで"], s=["ふつう有利な順"], r=[
    ("市内の両替所", ["ふつういちばん有利"]), ("市内の銀行", ["ふつう中間"]), ("空港", ["ホテルまでの交通費だけ"])],
    atm=("Global ATM", ["ATM手数料 約2,000ウォン〜", "+ カード会社所定の利息"]), n=["1万ウォン札で受け取りましょう。"]),
 "zh-tw": dict(t=["到了韓國,在哪裡換"], s=["通常由好到差"], r=[
    ("市區換錢所", ["通常匯率最好"]), ("銀行", ["通常居中"]), ("機場", ["只換到飯店的交通費"])],
    atm=("Global ATM", ["機器手續費常見 2,000 韓元以上", "+ 發卡銀行另收費用"]), n=["請對方給萬元鈔。"]),
}
def mo1(lang):
    d = MO1[lang]; f = Fig(d["t"][0]); f.title(d["t"], d["s"])
    for i, (h, ls) in enumerate(d["r"]):
        if i == 0: f.card(h, ls, chip=str(i+1), chip_fill=RED, chip_ink=WHITE, stroke=RED, sw=2)
        else: f.card(h, ls, chip=str(i+1), chip_fill=INK, chip_ink=WHITE)
    f.y += 6
    f.card(d["atm"][0], d["atm"][1], chip="ATM", chip_w=52, fill=SOFT, stroke=SOFT, chip_fill=WHITE)
    f.note(d["n"], INK, 700)
    return f

# ---------- money-2: card rejected ----------
MO2 = {
 "en": dict(t=["Card turned down?"], s=["Find your situation"], r=[
    ("Taxi", ["k.ride app takes overseas cards"]),
    ("Food delivery (Baemin)", ["Foreign card, no Korean number", "needed (since July 2026)"]),
    ("Naver Map booking or ordering", ["Verify with your passport", "(since June 2026)"]),
    ("Subway: Climate Card", ["New machines at 273 stations,", "Lines 1–8 (3.7% fee)"])],
    e=("Anywhere else", ["Your second card, then cash"])),
 "ko": dict(t=["카드가 막혔다면?"], s=["상황부터 찾으세요"], r=[
    ("택시", ["k.ride 앱은 해외 카드 결제 가능"]),
    ("배달 (배달의민족)", ["해외 카드로, 한국 번호 없이", "주문 가능 (2026년 7월부터)"]),
    ("네이버 지도 예약·주문", ["여권 인증으로 이용", "(2026년 6월부터)"]),
    ("지하철 기후동행카드", ["1~8호선 273개 역 새 발매기", "(해외 카드 수수료 3.7%)"])],
    e=("그 밖의 곳", ["다른 브랜드 카드, 그다음 현금"])),
 "ja": dict(t=["カードが通らない?"], s=["場面から探す"], r=[
    ("タクシー", ["k.ride アプリは海外カードOK"]),
    ("出前(配達の民族)", ["海外カードで注文、韓国の", "電話番号は不要(2026年7月〜)"]),
    ("NAVERマップの予約・注文", ["パスポート認証で利用", "(2026年6月〜)"]),
    ("地下鉄:気候同行カード", ["1〜8号線273駅の新しい券売機", "(海外カード手数料3.7%)"])],
    e=("それ以外", ["別ブランドのカード、次に現金"])),
 "zh-tw": dict(t=["卡刷不過?"], s=["先找你的情況"], r=[
    ("計程車", ["k.ride App 可用海外卡"]),
    ("外送(外送民族)", ["海外卡點餐,不需韓國號碼", "(2026 年 7 月起)"]),
    ("Naver Map 訂位、點餐", ["用護照驗證就能用", "(2026 年 6 月起)"]),
    ("地鐵:氣候同行卡", ["1~8 號線 273 站新售票機", "(海外卡手續費 3.7%)"])],
    e=("其他地方", ["換另一個卡組織的卡,", "再不行用現金"])),
}
def mo2(lang):
    d = MO2[lang]; f = Fig(d["t"][0]); f.title(d["t"], d["s"])
    for h, ls in d["r"]:
        f.card(h, ls)
    f.card(d["e"][0], d["e"][1], fill=SOFT, stroke=SOFT)
    return f

# ---------- money-3: WOWPASS costs ----------
MO3 = {
 "en": dict(t=["WOWPASS: what it costs"], r=[("Card", "₩5,000"), ("Card reserved in the app", "₩4,500"),
    ("Loading foreign cash", "No fee"), ("Paying in shops", "No fee"), ("Withdrawing won, per time", "₩1,000")],
    lim=("Withdrawal limit, per time", "₩100,000"), back=("Leftover balance", "Won cash only"), n=["Official guide, 4 November 2025"]),
 "ko": dict(t=["와우패스 비용 한눈에"], r=[("카드 발급비", "5,000원"), ("앱 예약 시", "4,500원"),
    ("외화 현금 충전", "수수료 없음"), ("결제", "수수료 없음"), ("원화 인출 1회", "1,000원")],
    lim=("1회 인출 한도", "10만 원"), back=("남은 잔액", "원화 현금으로"), n=["공식 이용 안내(2025년 11월 4일) 기준"]),
 "ja": dict(t=["WOWPASSの費用"], r=[("カード発行費", "5,000ウォン"), ("アプリで予約", "4,500ウォン"),
    ("外貨現金のチャージ", "手数料なし"), ("支払い", "手数料なし"), ("ウォン引き出し1回", "1,000ウォン")],
    lim=("1回の引き出し上限", "10万ウォン"), back=("残高の払い戻し", "ウォン現金のみ"), n=["公式利用案内(2025年11月4日)より"]),
 "zh-tw": dict(t=["WOWPASS 費用一覽"], r=[("發卡費", "5,000 韓元"), ("App 預約", "4,500 韓元"),
    ("儲值外幣現金", "免手續費"), ("消費", "免手續費"), ("領韓元,每次", "1,000 韓元")],
    lim=("每次領取上限", "10 萬韓元"), back=("餘額退還", "只退韓元現金"), n=["依官方使用說明(2025 年 11 月 4 日)"]),
}
def mo3(lang):
    d = MO3[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    f.box_start()
    for i, (a, b) in enumerate(d["r"]):
        f.row(a, b, value_fill=RED if i >= 2 and i <= 3 else INK, top_rule=i > 0)
    f.row(*d["lim"], bold_value=False)
    f.row(*d["back"], bold_value=False)
    f.box_end()
    f.note(d["n"])
    return f

# ---------- tax-refund-1: receipt ----------
TR1 = {
 "en": dict(t=["Read the total on your receipt"], tot="Total (tax incl.)", c=[
    ("₩15,000 or more", ["One receipt, one shop:", "it can be refunded"]),
    ("Under ₩1,000,000", ["Instant refund at the till"]),
    ("Up to ₩5,000,000", ["All instant-refund buys", "on one visit, added up"])]),
 "ko": dict(t=["영수증 합계를 보세요"], tot="합계(세금 포함)", c=[
    ("15,000원 이상", ["한 매장, 영수증 한 장 기준", "환급 대상"]),
    ("100만 원 미만", ["계산대에서 즉시 환급"]),
    ("500만 원까지", ["한 번 입국해 즉시 환급받은", "구매를 모두 더한 금액"])]),
 "ja": dict(t=["レシートの合計を見る"], tot="合計(税込)", c=[
    ("15,000ウォン以上", ["1店舗・1レシートで", "還付の対象"]),
    ("100万ウォン未満", ["レジでその場で免税"]),
    ("500万ウォンまで", ["1回の入国で即時免税を", "受けた買い物の合計"])]),
 "zh-tw": dict(t=["看收據上的總額"], tot="總額(含稅)", c=[
    ("15,000 韓元以上", ["同一家店單筆", "就能退稅"]),
    ("未滿 100 萬韓元", ["結帳時現場退稅"]),
    ("最多 500 萬韓元", ["同一次入境現場退稅", "的消費加起來"])]),
}
def tr1(lang):
    d = TR1[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    x0, x1, top = 84, 316, f.y
    h = 196
    zig = " ".join(f"L{x1 - i*14.5} {top+h + (0 if i % 2 == 0 else 8)}" for i in range(17))
    f.raw(f'<path d="M{x0} {top} H{x1} V{top+h} {zig} L{x0} {top+h} Z" fill="{WHITE}" stroke="{RULE}"/>')
    f.raw(f'<rect x="{x0+60}" y="{top+16}" width="{x1-x0-120}" height="30" rx="6" fill="{INK}"/>')
    f.raw(T((x0 + x1) / 2, top + 37, "TAX FREE", 16, 700, WHITE, "middle"))
    for i, w in enumerate([150, 120, 160]):
        yy = top + 66 + i * 22
        f.raw(f'<rect x="{x0+18}" y="{yy}" width="{w}" height="10" rx="5" fill="{SOFT}"/>')
        f.raw(f'<rect x="{x1-58}" y="{yy}" width="40" height="10" rx="5" fill="{SOFT}"/>')
    f.raw(f'<path d="M{x0+14} {top+136} H{x1-14}" stroke="{RULE}" stroke-dasharray="4 4"/>')
    f.raw(f'<rect x="{x0+8}" y="{top+146}" width="{x1-x0-16}" height="36" rx="6" fill="none" stroke="{RED}" stroke-width="2"/>')
    f.raw(T(x0 + 18, top + 170, d["tot"], 16, 700))
    f.raw(f'<rect x="{x1-58}" y="{top+159}" width="40" height="10" rx="5" fill="{INK}"/>')
    f.y = top + h + 24
    for i, (hd, ls) in enumerate(d["c"]):
        f.card(hd, ls, chip=str(i+1), chip_fill=RED if i < 2 else INK, chip_ink=WHITE)
    return f

# ---------- tax-refund-2: which route ----------
TR2 = {
 "en": dict(t=["Which route does", "your receipt take?"], q=[
    (["Receipt under ₩15,000?"], ["No refund", "Batch buys in one shop"]),
    (["₩1,000,000 or more", "on one receipt?"], ["Refund slip", "Claim before you check bags"]),
    (["No “Tax Free” sign", "at the till?"], ["Refund slip", "Airport or downtown kiosk"])],
    f=("Instant refund at the till", ["Show your physical passport"])),
 "ko": dict(t=["내 영수증은 어느 쪽?"], q=[
    (["영수증이 15,000원 미만?"], ["환급 안 돼요", "한 매장에서 몰아서 사기"]),
    (["영수증 한 장이", "100만 원 이상?"], ["환급 전표 받기", "짐 부치기 전에 환급"]),
    (["계산대에 Tax Free", "표시가 없다?"], ["환급 전표 받기", "공항·시내 키오스크"])],
    f=("계산대에서 즉시 환급", ["실물 여권을 보여 주기"])),
 "ja": dict(t=["レシートはどのルート?"], q=[
    (["レシートが15,000ウォン未満?"], ["対象外", "店ごとにまとめ買い"]),
    (["1レシートが", "100万ウォン以上?"], ["還付書類をもらう", "荷物を預ける前に手続き"]),
    (["レジに Tax Free の", "表示がない?"], ["還付書類をもらう", "空港か市内のキオスク"])],
    f=("レジで即時免税", ["パスポートの実物を見せる"])),
 "zh-tw": dict(t=["你的收據走哪一條?"], q=[
    (["單筆未滿 15,000 韓元?"], ["不能退稅", "同一家店一次買"]),
    (["單筆 100 萬韓元", "以上?"], ["索取退稅單", "托運行李前辦理"]),
    (["櫃檯沒有 Tax Free", "標示?"], ["索取退稅單", "機場或市區退稅機"])],
    f=("結帳時現場退稅", ["出示護照正本"])),
}
def tr2(lang):
    d = TR2[lang]; y, n, pw = pill(lang)
    f = Fig(" ".join(d["t"])); f.title(d["t"])
    for q, o in d["q"]:
        f.question(q, y, o, pw); f.arrow(n)
    f.card(d["f"][0], d["f"][1], stroke=RED, sw=2, head_fill=RED, line_fill=INK)
    return f

# ---------- tax-refund-3: what comes back ----------
TR3 = {
 "en": dict(t=["What actually comes back"], h=("10% VAT is inside the price", ["Refund operators keep a fee,", "so about 5–8% comes back"]),
    r=[("You spend ₩50,000", "≈ ₩2,500"), ("You spend ₩300,000", "≈ ₩15,000–24,000"), ("You spend ₩1,000,000", "≈ ₩60,000–80,000")],
    n=["Estimates. Your slip shows the exact amount."]),
 "ko": dict(t=["실제로 돌려받는 돈"], h=("가격 안에 부가세 10%", ["환급 사업자가 수수료를 떼서", "약 5~8%를 돌려받아요"]),
    r=[("₩50,000 구매", "약 ₩2,500"), ("₩300,000 구매", "약 ₩15,000~24,000"), ("₩1,000,000 구매", "약 ₩60,000~80,000")],
    n=["대략값이에요. 정확한 금액은 전표에 나와요."]),
 "ja": dict(t=["実際に戻る金額"], h=("価格に付加価値税10%込み", ["還付会社が手数料を引くので", "戻るのは約5〜8%"]),
    r=[("50,000ウォン", "約2,500ウォン"), ("300,000ウォン", "約15,000〜24,000"), ("1,000,000ウォン", "約60,000〜80,000")],
    n=["目安です。正確な額は還付書類に。"]),
 "zh-tw": dict(t=["實際能拿回多少"], h=("售價已含 10% 加值稅", ["退稅公司會扣手續費,", "實際約拿回 5–8%"]),
    r=[("消費 50,000 韓元", "約 2,500"), ("消費 300,000 韓元", "約 15,000–24,000"), ("消費 1,000,000 韓元", "約 60,000–80,000")],
    n=["估計值(韓元),實際以退稅單為準。"]),
}
def tr3(lang):
    d = TR3[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    f.card(d["h"][0], d["h"][1], fill=SOFT, stroke=SOFT, red_lines=(1,))
    f.box_start()
    for i, (a, b) in enumerate(d["r"]):
        f.row2(a, b, top_rule=i > 0)
    f.box_end()
    f.note(d["n"])
    return f

# ---------- e-arrival-card-4: the form, in order ----------
EA4 = {
 "en": dict(t=["What the form asks, in order"], s=["Type in English or Korean only"], r=[
    ("Terms + email", "Representative, 14 or older"), ("Passport", "Scan or upload the photo page"),
    ("Arrival", "Date and flight number"), ("Departure", "Date required, flight optional"),
    ("Purpose + occupation", "Tourism, for example"), ("Address in Korea", "Where you stay, in English"),
    ("Review + submit", "Check against your passport"), ("Issuance number", "PDF and email: keep it")]),
 "ko": dict(t=["신고서 입력 순서"], s=["입력은 영어나 한국어만"], r=[
    ("약관 동의 + 이메일", "대표 신청자, 만 14세 이상"), ("여권", "사진면 스캔 또는 업로드"),
    ("입국 정보", "도착일과 항공편명"), ("출국 정보", "날짜 필수, 항공편명 선택"),
    ("입국 목적 + 직업", "예: 관광"), ("국내 체류지", "숙소 주소(영문)"),
    ("확인 후 제출", "여권과 한 글자씩 대조"), ("발급번호", "PDF와 이메일로 보관")]),
 "ja": dict(t=["入力する順番"], s=["入力は英語か韓国語だけ"], r=[
    ("規約同意+メール", "代表者、14歳以上"), ("パスポート", "顔写真ページを読み取り"),
    ("入国情報", "到着日と便名"), ("出国情報", "日付は必須、便名は任意"),
    ("入国目的+職業", "例:観光"), ("韓国での滞在先", "ホテルの住所(英語)"),
    ("確認して提出", "パスポートと見比べる"), ("発行番号", "PDFとメールで保存")]),
 "zh-tw": dict(t=["填寫順序"], s=["欄位只能輸入英文或韓文"], r=[
    ("同意條款 + email", "代表人,年滿 14 歲"), ("護照", "掃描或上傳資料頁"),
    ("入境資訊", "抵達日期與班機號碼"), ("出境資訊", "日期必填,班機可不填"),
    ("入境目的 + 職業", "例如觀光"), ("在韓住址", "飯店的英文地址"),
    ("確認後送出", "逐字對照護照"), ("核發號碼", "存 PDF、收 email")]),
}
def ea4(lang):
    d = EA4[lang]; f = Fig(d["t"][0]); f.title(d["t"], d["s"])
    top = f.y
    f.raw(f'<rect x="{M}" y="{top}" width="{W-2*M}" height="10" rx="0" fill="none"/>')
    idx = len(f.parts)
    f.y = top + 52
    f.steps([(h, l, i in (5, 7)) for i, (h, l) in enumerate(d["r"])], x=M + 12, w=W - 2 * M - 24)
    h = f.y - top + 6
    f.parts.insert(idx, f'<rect x="{M}" y="{top}" width="{W-2*M}" height="{h}" rx="22" fill="{SOFT}" stroke="{INK}" stroke-width="2"/>'
        f'<rect x="{M+12}" y="{top+12}" width="{W-2*M-24}" height="28" rx="14" fill="{WHITE}"/>'
        + T(W / 2, top + 32, "e-arrivalcard.go.kr", 16, 700, INK, "middle"))
    f.y = top + h + 10
    return f

# ---------- e-arrival-card-5: K-ETA vs e-Arrival Card ----------
EA5 = {
 "en": dict(t=["Two different things"], k=["Travel authorisation", "₩10,000, applied for before you fly",
    "22 countries and regions incl. the US:", "exempt until 31 December 2027"],
    e=("e-Arrival Card", ["Replaces the paper arrival card", "Free, in the 3 days before you land"]),
    n=["Valid K-ETA? Then no e-Arrival Card."]),
 "ko": dict(t=["서로 다른 두 제도"], k=["전자여행허가", "1만 원, 출발 전에 신청", "미국·일본·대만 등 22개 국가·지역", "2027년 12월 31일까지 면제"],
    e=("전자입국신고서", ["종이 입국신고서를 대신해요", "무료, 도착 전 3일 안에"]),
    n=["유효한 K-ETA가 있으면 신고서는 안 내요."]),
 "ja": dict(t=["別々の2つの制度"], k=["電子渡航認証", "1万ウォン、渡航前に申請", "日本など22の国・地域は", "2027年12月31日まで免除"],
    e=("電子入国申告書", ["紙の入国カードの代わり", "無料、到着前3日以内に"]),
    n=["有効なK-ETAがあれば申告書は不要。"]),
 "zh-tw": dict(t=["兩個不同的制度"], k=["電子旅行許可", "1 萬韓元,出發前申請", "臺灣等 22 個國家和地區", "免申請到 2027 年 12 月 31 日"],
    e=("電子入境卡", ["取代紙本入境卡", "免費,抵達前 3 天內填"]),
    n=["持有效 K-ETA 就不用填入境卡。"]),
}
def ea5(lang):
    d = EA5[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    f.card("K-ETA", d["k"], fill=SOFT, stroke=SOFT)
    f.card(d["e"][0], d["e"][1], stroke=RED, sw=2, head_fill=RED, line_fill=INK)
    f.note(d["n"], INK, 700)
    return f

# ---------- tax-refund-4: refund slip at the airport ----------
TR4 = {
 "en": dict(t=["Refund slip at the airport"], r=[
    ("Goods in your hand luggage", "Customs may ask to see them", False),
    ("Refund first", "Before you check in your bags", True),
    ("Then check in your bags", "", False)], n=["Or claim at a downtown refund kiosk.", "Goods must leave Korea within 3 months."]),
 "ko": dict(t=["환급 전표, 공항에서는"], r=[
    ("물건은 기내 가방에", "세관이 물건을 확인할 수 있어요", False),
    ("환급부터", "짐을 부치기 전에", True),
    ("그다음 짐 부치기", "", False)], n=["시내 환급 키오스크에서도 돼요.", "구매 후 3개월 안에 반출해야 해요."]),
 "ja": dict(t=["還付書類は空港で"], r=[
    ("商品は機内持ち込みに", "税関で提示を求められることも", False),
    ("先に還付手続き", "荷物を預ける前に", True),
    ("それから荷物を預ける", "", False)], n=["市内の還付キオスクでもOK。", "購入から3か月以内に持ち出す。"]),
 "zh-tw": dict(t=["退稅單在機場這樣辦"], r=[
    ("商品放隨身行李", "海關可能要求查看", False),
    ("先辦退稅", "在托運行李之前", True),
    ("再托運行李", "", False)], n=["也可以在市區退稅機辦理。", "購買後 3 個月內要帶出韓國。"]),
}
def tr4(lang):
    d = TR4[lang]; f = Fig(d["t"][0]); f.title(d["t"])
    f.steps(d["r"])
    f.note(d["n"])
    return f

FIGS = {"e-arrival-card-1": ea1, "e-arrival-card-2": ea2, "e-arrival-card-3": ea3,
        "money-1": mo1, "money-2": mo2, "money-3": mo3,
        "tax-refund-1": tr1, "tax-refund-2": tr2, "tax-refund-3": tr3,
        "e-arrival-card-4": ea4, "e-arrival-card-5": ea5, "tax-refund-4": tr4}
if __name__ == "__main__":
    for name, fn in FIGS.items():
        for lang in LANGS:
            p = f"{OUT}/{lang}/{name}.svg"
            open(p, "w", encoding="utf-8").write(fn(lang).svg())
    print("written", len(FIGS) * len(LANGS))
