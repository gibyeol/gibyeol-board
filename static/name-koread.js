/* How to read foreign names in Hangul (shown in the Korean interface). Mostly following the Korean loanword rules (외래어 표기법).
   Key 'Language|Form' wins over plain 'Form' where a language reads the same spelling differently. */
window.NADRI_KOREAD = (function () {
  var raw = 'Alejandro 알레한드로|Ana 아나|Benjamín 벤하민|Carla 카를라|Carlota 카를로타|Carolina 카롤리나|Chela 첼라|Cloe 클로에|Daniel 다니엘|David 다비드|Enrique 엔리케|Estela 에스텔라|Estrella 에스트레야|Félix 펠릭스|Gracia 그라시아|Graciela 그라시엘라|Guillermo 기예르모|Iago 이아고|Isabel 이사벨|Izan 이산|Jaime 하이메|Juan 후안|León 레온|María 마리아|Miguel 미겔|Pablo 파블로|Pedro 페드로|Santiago 산티아고|Sofía 소피아|' +
    'Alexandre 알렉상드르|Amélie 아멜리|André 앙드레|Anne 안|Annette 아네트|Annick 아니크|Chloé 클로에|Cloé 클로에|Estelle 에스텔|Guillaume 기욤|Henri 앙리|Irène 이렌|Isabeau 이자보|Isabelle 이자벨|Jacky 자키|Jacques 자크|Jacquy 자키|Jean 장|Lili 릴리|Liliane 릴리안|Léo 레오|Léon 레옹|Manon 마농|Margot 마르고|Marguerite 마르그리트|Marie 마리|Marion 마리옹|Mathieu 마티외|Mattéo 마테오|Michaël 미카엘|Michel 미셸|Mickaël 미카엘|Pierre 피에르|Sacha 사샤|Sophie 소피|Zoé 조에|Ève 에브|Élisabeth 엘리자베트|Élise 엘리즈|Émilie 에밀리|' +
    'Alexander 알렉산더|Amalia 아말리아|Amalie 아말리에|Amelie 아멜리|Andreas 안드레아스|Anna 안나|Elisabeth 엘리자베트|Elsa 엘자|Emilia 에밀리아|Emilie 에밀리에|Greta 그레타|Gretel 그레텔|Hans 한스|Heinrich 하인리히|Heinz 하인츠|Ilse 일제|Isabell 이자벨|Isabella 이자벨라|Jakob 야코프|Johannes 요하네스|Lilli 릴리|Lukas 루카스|Margarete 마르가레테|Matthias 마티아스|Michael 미하엘|Rosa 로자|Rosalie 로잘리|Sophia 조피아|Wilhelm 빌헬름|' +
    'Alessandro 알레산드로|Arrigo 아리고|Beniamino 베니아미노|Carlotta 카를로타|Daniele 다니엘레|Danilo 다닐로|Davide 다비데|Elisabetta 엘리자베타|Elmo 엘모|Enrico 엔리코|Felice 펠리체|Giacomo 자코모|Giovanni 조반니|Grazia 그라치아|Graziella 그라치엘라|Guglielmo 굴리엘모|Leone 레오네|Lilia 릴리아|Liliana 릴리아나|Luca 루카|Michele 미켈레|Noè 노에|Paolo 파올로|Pietro 피에트로|Rosalia 로잘리아|Samuele 사무엘레|Sofia 소피아|Sonia 소니아|Tommaso 톰마소|Vittoria 비토리아|' +
    'Amália 아말리아|Amélia 아멜리아|Anita 아니타|Anália 아날리아|Benjamim 벤자밍|Davi 다비|Ema 에마|Emília 에밀리아|Gracinda 그라신다|Gracília 그라실리아|Graça 그라사|Guilherme 길레르미|Henrique 엔히키|João 주앙|Leão 레앙|Olívia 올리비아|Paulo 파울루|Tiago 치아구|Tomás 토마스|Vitória 비토리아|' +
    'Aleksandr 알렉산드르|Amaliya 아말리야|Ameliya 아멜리야|Arina 아리나|Daniil 다닐|Danil 다닐|Danila 다닐라|Emiliya 에밀리야|Feliks 펠릭스|Irina 이리나|Ivan 이반|Karolina 카롤리나|Lev 레프|Luka 루카|Mariya 마리야|Mikhail 미하일|Oliviya 올리비야|Pavel 파벨|Pyotr 표트르|Samuil 사무일|Sofiya 소피야|Sofya 소피야|Veniamin 베니아민|Viktoriya 빅토리야|Yakov 야코프|Yelizaveta 옐리자베타|Zoya 조야|' +
    'Aleksander 알렉산데르|Beniamin 베니아민|Dawid 다비드|Elżbieta 엘주비에타|Ewa 에바|Gracja 그라치아|Henryk 헨리크|Irena 이레나|Irmina 이르미나|Jakub 야쿠프|Jan 얀|Leon 레온|Maria 마리아|Marianna 마리안나|Michał 미하우|Oliwia 올리비아|Paweł 파베우|Piotr 표트르|Tomasz 토마시|Wiktoria 빅토리아|Zofia 조피아|Zoja 조야|Zosia 조시아|Łukasz 우카시|' +
    'Andries 안드리스|Chloë 클로이|Daan 단|Dani 다니|Daniël 다니엘|Els 엘스|Eva 에바|Gratia 그라시아|Hendrik 헨드릭|Henk 헹크|Jacob 야코프|Joost 요스트|Jozef 요제프|Liesbeth 리스벳|Margriet 마르흐리트|Matthijs 마테이스|Michiel 미힐|Roos 로스|Sofie 소피|Thijs 테이스|Willem 빌럼|Zoë 조이|' +
    'Aimilia 에밀리아|Alexandros 알렉산드로스|Daniil 다니일|Eirini 이리니|Elisavet 엘리사벳|Ioannis 이오아니스|Liza 리자|Loukas 루카스|Margarita 마르가리타|Matthaios 마테오스|Michail 미하일|Michalis 미할리스|Mihail 미하일|Pavlos 파블로스|Petros 페트로스|Viktoria 빅토리아|Zoi 조이|' +
    'Binyamin 빈야민|Boulos 불루스|Boutros 부트로스|Bulus 불루스|Butrus 부트루스|Danial 다니알|Daniyal 다니얄|Daoud 다우드|Daud 다우드|Dawood 다우드|Hanna 한나|Hannah 한나|Hawa 하와|Hawwa 하와|Iskandar 이스칸다르|Mariam 마리암|Maryam 마르얌|Mikha\'il 미하일|Nuh 누흐|Yacoub 야쿠브|Yahia 야히아|Yahya 야흐야|Yakub 야쿠브|Yaqoob 야쿠브|Yaqub 야쿠브|Youssef 유세프|Yuhanna 유한나|Yusuf 유수프|' +
    'Chana 하나|Chanah 하나|Chava 하바|Eitan 에이탄|Eithan 에이탄|Elisheva 엘리셰바|Eytan 에이탄|Hana 하나|Margalit 마르갈리트|Matityahu 마티트야후|Mikha\'el 미하엘|Miryam 미리암|Noach 노아흐|Shmuel 슈무엘|Ya\'aqov 야아코브|Yochanan 요하난|Yosef 요세프|Danyal 다니얄|' +
    // concept and born-in names
    'Stella 스텔라|Aster 아스테르|Tara 타라|Najma 나즈마|Setareh 세타레|Yıldız 이을드즈|Seren 세렌|Zvezdana 즈베즈다나|Hoshiko 호시코|Xing 싱|Hanbyeol 한별|Primo / Prima 프리모 / 프리마|Hajime 하지메|Yuan 위안|Hikmat 히크마트|Bilge 빌게|Chie 지에|Hui 후이|Seulgi 슬기|Lucia 루치아|Lucy 루시|Lucía 루시아|Nur 누르|Svetlana 스베틀라나|Jyoti 조티|Aydın 아이든|Hikari 히카리|Guang 광|Bitna 빛나|Celeste 셀레스테|Ourania 우라니아|Akash 아카시|Samaa 사마|Sora 소라|Tian 톈|Haneul 하늘|Marina 마리나|Kai 카이|Moana 모아나|Derya 데리야|Rio (river) 리오|Umi 우미|Hai 하이|Bada 바다|Flora 플로라|Anthea 안테아|Pua 푸아|Çiçek 치체크|Zahra 자흐라|Blossom 블로섬|Hua 화|Padma 파드마|Kamala 카말라|Nilufar 닐루파르|Ren 렌|Lian 롄|Bahar 바하르|Vesna 베스나|Haru 하루|Chun 춘|Bom 봄|Summer 서머|Natsu 나쓰|Xia 샤|Autumn 오텀|Aki 아키|Qiu 추|Neve 네베|Nieves 니에베스|Yuki 유키|Xue 쉐|Luna 루나|Selene 셀레네|Chandra 찬드라|Qamar 카마르|Aylin 아일린|Yue 웨|Sol 솔|Helios 헬리오스|Surya 수리야|Shams 샴스|Güneş 귀네시|Hinata 히나타|Yang 양|Aurora 아우로라|Dawn 돈|Eos 에오스|Usha 우샤|Fajr 파즈르|Şafak 샤파크|Xiao 샤오|Irene 이레네|Paz 파스|Frida 프리다|Shalom 샬롬|Shanti 샨티|Barış 바르시|Kazu 가즈|Ping 핑|Joy 조이|Felicity 펠리시티|Gioia 조이아|Ananda 아난다|Farah 파라|Sevinç 세빈치|Xin 신|Amanda 어맨다|Priya 프리야|Habiba 하비바|Sevgi 세브기|Lyubov 류보피|Ai 아이|Sarang 사랑|Hope 호프|Esperanza 에스페란사|Elpida 엘피다|Nadezhda 나데즈다|Amal 아말|Umut 우무트|Asha 아샤|Nozomi 노조미|Grace 그레이스|Kripa 크리파|Megumi 메구미|Eunhye 은혜|Bella 벨라|Callista 칼리스타|Jamila 자밀라|Sundari 순다리|Mika 미카|Mei 메이|Areum 아름|Valentin 발렌틴|Isamu 이사무|Yong 융|Clement 클레먼트|Karim 카림|Daya 다야|Hitoshi 히토시|Alethea 알레테아|Vera 베라|Satya 사티아|Sadiq 사디크|Faith 페이스|Makoto 마코토|Zhen 전|Aurelia / Aurelio 아우렐리아 / 아우렐리오|Sona 소나|Jin 진|Jade 제이드|Gemma 젬마|Margarita (pearl) 마르가리타|Lulu (pearl) 룰루|Mutiara (pearl) 무티아라|Ratna 라트나|Tama 다마|Yu 위|Silvia 실비아|Oren (pine) 오렌|Shin 신|Lin 린|Draco 드라코|Drake 드레이크|Ryu 류|Long 룽|Sher 셰르|Babur 바부르|Tora 도라|Hu 후|Rex 렉스|Basil 바실|Leroy 르루아|Malik 말리크|Raja 라자|Wang 왕|Zoe 조이|Vita 비타|Chaim 하임|Hayat 하야트|Hisashi 히사시|Shou 서우|Victoria / Victor 빅토리아 / 빅터|Nicole / Nicholas 니콜 / 니컬러스|Zafar 자파르|Zafer 자페르|Vijay 비자이|Masaru 마사루|Sheng 성|Tahira 타히라|Safiya 사피야|Kiyoshi 기요시|Jie 제|Perpetua 페르페투아|Sarmad 사르마드|Anant 아난트|Anatole 아나톨|Azuma 아즈마|Dong 둥|Magnus 마그누스|Akbar 아크바르|Futoshi 후토시|Da 다|Cosmo 코스모|Melody 멜로디|Shira 시라|Gita 기타|Yin 인|Fumi 후미|Wen 원|William 윌리엄|Liam 리엄|Mamoru 마모루|Noah 노아|Yasushi 야스시|Hokuto 호쿠토|Beichen 베이천|Arthur 아서|Dao 다오|Kazuko 가즈코|Heping 허핑|Santi 산티|Panya 판야|Saeng 생|Sophia 소피아|Hannah 해나|Bandar 반다르|Minato 미나토|Chloe 클로이|Chloris 클로리스|Khadra 하드라|Blerta 블레르타|Midori 미도리|Sui 스이|Qing 칭|Bích 빅|Nalini 날리니|Liên 리엔|Ubon 우본|Yasmin 야스민|Jasmine 재스민|Yasemin 야세민|Jazmín 하스민|Gelsomina 젤소미나|Hasmik 하스미크|Mallika 말리카|Melati 믈라티|İpek 이페크|Reshma 레시마|Tsumugi 쓰무기|Oliva 올리바|Olive 올리브|Olivier 올리비에';
  var o = {};
  raw.split('|').forEach(function (p) { var i = p.search(/[\uAC00-\uD7A3]/); if (i > 0) o[p.slice(0, i).trim()] = p.slice(i).trim(); });
  // the same spelling read differently by language
  o['German|David'] = '다비트'; o['German|Sophie'] = '조피'; o['German|Daniel'] = '다니엘'; o['French|Daniel'] = '다니엘'; o['Portuguese|Daniel'] = '다니에우'; o['Portuguese|David'] = '다비드';
  o['Portuguese|Isabel'] = '이자벨'; o['Portuguese|Jaime'] = '자이메'; o['Portuguese|Miguel'] = '미게우'; o['Portuguese|Pedro'] = '페드루'; o['Portuguese|Sofia'] = '소피아';
  o['Dutch|Elisabeth'] = '엘리사벳'; o['Dutch|Jakob'] = '야코프'; o['Dutch|Johannes'] = '요하너스'; o['Dutch|Sophie'] = '소피'; o['Dutch|Rosa'] = '로사'; o['Spanish|Rosa'] = '로사';
  o['Spanish|Carolina'] = '카롤리나'; o['Hebrew|David'] = '다비드'; o['Spanish|Daniel'] = '다니엘'; o['Spanish|Félix'] = '펠릭스'; o['French|Félix'] = '펠릭스';
  o['Greek|Sofia'] = '소피아'; o['Greek|Andreas'] = '안드레아스'; o['Greek|Leon'] = '레온'; o['Greek|Amalia'] = '아말리아';
  return o;
})();
window.nadriKoRead = function (form, lang) { var R = window.NADRI_KOREAD || {}; return (lang && R[lang + '|' + form]) || R[form] || ''; };

/* Behind the Name meaning sentences (name-btn.js) in Korean, for the Korean interface: our translation (Claude, 2026-11-26),
   not Behind the Name's own text and not yet checked by a native editor. The English original stays on the page under it. */
window.NADRI_BTN_KO = {
  sophia: "그리스어로 '지혜'라는 뜻이에요.",
  olivia: "라틴어 oliva('올리브')에서 왔거나, Oliva나 Oliver를 바탕으로 한 이름일 수 있어요. 셰익스피어가 『십이야』에서 처음 썼어요.",
  emma: "본래 '온전한' 또는 '위대한'을 뜻하는 irmin으로 시작하는 게르만어 이름들의 짧은 형태예요.",
  liam: "William의 아일랜드식 짧은 형태예요.",
  noah: "'쉼, 휴식'을 뜻하는 히브리어 이름 Noaḥ에서 왔어요.",
  james: "후기 라틴어 이름 Iacomus의 영어 형태로, 히브리어 이름 Yaʿaqov(야곱)에서 왔어요.",
  santiago: "'성 야고보'라는 뜻으로, 스페인어 santo('성인')와 James의 옛 스페인어 형태 Yago가 합쳐진 이름이에요.",
  grace: "영어 단어 grace(은혜)에서 왔고, 뿌리는 라틴어 gratia예요.",
  anna: "그리스어·라틴어 구약성경에 쓰인 Hannah의 형태예요.",
  john: "Iohannes의 영어 형태로, '야훼는 은혜로우시다'를 뜻하는 히브리어 Yoḥanan에서 왔어요.",
  david: "히브리어 이름 Dawiḏ에서 왔고, '사랑하는 이' 또는 '삼촌'을 뜻하는 doḏ에서 나왔어요.",
  michael: "'누가 신과 같은가?'를 뜻하는 히브리어 이름 Miḵaʾel에서 왔어요.",
  daniel: "'신은 나의 재판관'이라는 뜻이에요.",
  ethan: "'단단한, 오래가는, 굳건한'이라는 뜻이에요.",
  elizabeth: "'나의 신은 맹세'라는 뜻이에요.",
  isabella: "Isabel의 라틴어식 형태예요. Isabel은 Elisabeth('나의 신은 맹세')의 중세 형태예요.",
  charlotte: "Charles의 프랑스어 여성형 애칭이에요.",
  amelia: "Amalia의 변형으로, 게르만어 요소 amal('일')에서 왔어요.",
  emily: "Aemilius의 영어 여성형이에요(라틴어 aemulus, '맞수'에서).",
  henry: "'집을 다스리는 이'라는 뜻이에요.",
  alexander: "'사람들을 지키는'이라는 뜻이에요.",
  benjamin: "'남쪽의 아들' 또는 '오른손의 아들'이라는 뜻이에요.",
  lucas: "그리스어 Loukas(누가)의 라틴어 형태로, '루카니아 출신'이라는 뜻이에요.",
  lily: "순결의 상징인 꽃(백합)의 이름에서 왔어요.",
  chloe: "봄에 새로 돋는 '푸른 새싹'을 뜻하는 그리스어예요.",
  zoe: "'생명'을 뜻하는 그리스어에서 왔어요.",
  peter: "'돌'을 뜻하는 그리스어 Petros에서 왔어요.",
  paul: "라틴어로 '작은'이라는 뜻의 로마 이름 Paulus에서 왔어요.",
  stella: "'별'을 뜻하는 라틴어 단어예요.",
  mia: "Maria의 애칭이에요. '나의'를 뜻하는 이탈리아어 mia와도 우연히 같아요.",
  maria: "그리스어 Maria의 라틴어 형태로, 히브리어 이름 Miriam(Mary)에서 왔어요. 본래 뜻은 확실히 알려져 있지 않아요.",
  ava: "Eve의 변형으로, 히브리어 어근 ḥawa에서 왔어요.",
  eva: "Eve의 한 형태예요(히브리어 Hawwa, '숨 쉬다' 또는 '살다').",
  victoria: "'승리'를 뜻하는 라틴어 단어예요.",
  leo: "'사자'를 뜻하는 라틴어 leo에서 왔어요.",
  felix: "라틴어로 '운 좋은, 성공한'이라는 뜻의 로마 별칭(cognomen)에서 왔어요.",
  irene: "'평화'를 뜻하는 그리스어에서 왔어요.",
  rose: "본래 '이름난 종류'를 뜻하는 게르만어 이름 Hrodohaidis의 노르만 프랑스어 형태였고, 나중에 장미꽃과 이어졌어요.",
  margaret: "라틴어 Margarita에서 왔고, 뿌리는 '진주'를 뜻하는 그리스어 margarites예요.",
  joy: "영어 단어 joy(기쁨) 그대로예요.",
  hope: "영어 단어 hope(희망)에서 왔어요.",
  andrew: "그리스어 이름 Andreas의 영어 형태로, '사내다운, 남자다운'을 뜻하는 andreios에서 왔어요.",
  thomas: "'쌍둥이'를 뜻하는 아람어 이름 Teʾoma의 그리스어 형태예요.",
  william: "'의지 + 투구'를 뜻하는 게르만어 이름 Willehelm에서 왔어요.",
  jacob: "'발꿈치를 잡은 자' 또는 '대신하는 자'라는 뜻으로 풀이돼요.",
  joseph: "'그가 더하리라'를 뜻하는 히브리어 Yosef에서 왔어요.",
  matthew: "Matthaios의 영어 형태로, '야훼의 선물'을 뜻하는 히브리어 Mattityahu에서 왔어요.",
  samuel: "'신의 이름'을 뜻하는 히브리어 이름 Shemuʾel에서 왔어요."
};
