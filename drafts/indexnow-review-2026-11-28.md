# 독립 검토: IndexNow 열쇠 파일·전송 도구 (커밋 f3b74d6, 작성자 아닌 하위 작업이 판정)
필수 수정: 없음
| # | 항목 | 판정 | 근거 |
|---|---|---|---|
| 1 | 열쇠 형식·파일(8~128자, {key}.txt, 내용=열쇠, 맨 위) | 통과 | dist/<key>.txt 32바이트, build.py |
| 2 | 전송 형식(host·key·keyLocation·urlList, Content-Type, www.bing.com/indexnow는 FAQ 참여 목록에 있음, 1만 한도) | 통과 | indexnow.org documentation·faq |
| 3 | 안전장치(열쇠 미공개면 안 보냄, 사이트맵 밖 주소 거부, --send 없으면 안 보냄) | 통과 | 직접 실행·모의 시험 |
| 4 | 사이트맵 160개 모두 잡음 | 통과 | dist·공개 sitemap 둘 다 160 |
| 5 | 첫 전송 --all(160개) | 조건부 | FAQ "Should I submit URLs that changed before I started using IndexNow? No. … not intended for retroactive submission of older changes" — Bing은 이미 사이트맵으로 160개 받음 |
| 6 | 다른 빌드 결과 영향 | 통과 | diff -rq: 열쇠 파일 1개만 추가 |
| 7 | 열쇠 노출 | 위험 낮음(추론) | 파일은 원래 공개 구조, 이 호스트 주소만 보낼 수 있음, 교체 절차 있음 |
| 8 | 로그·코드 기타 | 대체로 통과 | 권장 2~5 |
검토 중 사고: 검토자가 짠 첫 명령 묶음에 --send가 실수로 들어 있었고 권한 검사가 실행 전에 막음(전송 없음, 열쇠 파일 미공개라 도구도 첫 단계에서 멈추는 상태였음).

## 권장과 처리(Claude, 커밋 다음)
1. 첫 전송 --all → FAQ 원문대로 바꿈: 열쇠 공개 뒤 바뀐 페이지만 보냄(공개할 때마다 그 페이지 주소). 도구 설명에 FAQ 문장 넣음.
2. curl 시간 제한·실패 처리 → 넣음(--max-time 30/60, curl 실패 시 멈춤·'000 not delivered' 기록)
3. 로그에 보낸 주소 → 넣음(주소 목록 접어 두기)
4. 인자 확인 → '--all'은 단독만, '--since'는 YYYY-MM-DD만, 주소 목록에 '--' 섞이면 멈춤(모의 시험 7가지 확인)
5. 로그 저장 → 보낸 뒤 Claude가 커밋(도구가 안내 출력)
