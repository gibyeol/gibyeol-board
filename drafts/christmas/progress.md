# 크리스마스 초안 — 빈칸 채우기 진행 기록 (2026-11-27 새벽, 하위 작업)

지시: review.md의 빈칸(랭킹·할인 코드·다이소 쏠림·A to Z 빈칸·데이터 파일 분리) 채우기. 원두 허용 [7eb4ec94#2712] "전부 허용해 아직 사용량 많이 남았어 작업 계속해".
시각은 서버 `TZ=Asia/Seoul date` 기준.

## 단계
- [x] 1. 원문 수집(01:31~01:36 KST): 새로 열린 호스트에서 텍스트 29건(기사·보도자료 28 + 다이소 재고 페이지 껍데기 1) → wondu-archive `staging/overnight-2026-11-27/raw/christmas/` (커밋 253fee7)
- [x] 2. 데이터 파일 `christmas-data.json` + 생성기 `gen_christmas_block.py` (트렌드 칸을 데이터에서 만듦)
- [x] 3. christmas.md 고침(트렌드 칸 = 생성기 출력, 코어·더 보기 칸 보강) + sources.md
- [x] 4. review.md 다시 판정, 원두 결정 목록

## 이번에 확인된 접근 상태 (01:3x KST)
- 열림: viva100, techm, news2day, shinsegaegroupnewsroom, biz.heraldcorp, www.sedaily(m.sedaily는 안 열림), segye, view.asiae(가끔 끊김), ajunews, etnews, edaily, prdm.daisomall(빈 껍데기 HTML).
- 안 열림(이번에): koreatimes, koreaherald, mediahub.seoul.go.kr, english.visitseoul.net, daiso.co.kr — 어젯밤엔 열렸던 곳. 어젯밤 받은 원문은 보관소에 있으므로 기존 숫자는 그대로 둠.
- 안 열림: 호텔·백화점·이마트·11번가·까사미아·롯데 공식 사이트(000), 올리브영 글로벌(사이트 자체 403 'Access restricted').

## 끝난 상태 (01:5x KST)
- 커밋: 01581f5(데이터·생성기), cad54cd(페이지), 45353f9(sources), 이 커밋(review·progress). 보관소: 253fee7(원문), 스크린숏 커밋.
- 남은 빈칸·원두 결정은 review.md 끝 두 절.
