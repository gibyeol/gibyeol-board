"""Mandarin readings in Hangul for the name tool (static/name-zhko.js).

Pinyin: pypinyin (default reading; standard Mandarin as in Taiwan's 國語 for these characters, tones dropped).
Hangul: the 외래어 표기법 Chinese table (중국어의 주음 부호와 한글 대조표, 국립국어원) as rules below;
checked against names the Korean press writes this way (see CHECK at the bottom: 시진핑, 차이잉원, 천수이볜 ...).
The default reading is used, except: OVERRIDE (characters whose default is wrong in transliterated names: 勒 lè, 柏 bó, 繆 miù),
SURNAME (hanja used as Korean surnames take their surname reading: 朴 Piáo). NADRI_ZHKO_MULTI lists the characters in the table
with two common readings in names (APPROX); the page marks a reading that uses one of them as approximate.
Unihan kMandarin would be the better source for the customary reading; unicode.org was not reachable from the build session (2026-11-26).

Characters covered: every Chinese character the name tool can put in a Chinese line:
NADRI_NAMES zh forms (name-data.js), KO_NAME_HANJA and KO_SURNAME_HANJA (name-ko.js).
Run: python3 tools/build_zhko.py   (needs pypinyin and node)
"""
import json, subprocess, sys
from pathlib import Path
from pypinyin import pinyin, Style

ROOT = Path(__file__).resolve().parent.parent
INI = {'b': 'ㅂ', 'p': 'ㅍ', 'm': 'ㅁ', 'f': 'ㅍ', 'd': 'ㄷ', 't': 'ㅌ', 'n': 'ㄴ', 'l': 'ㄹ', 'g': 'ㄱ', 'k': 'ㅋ', 'h': 'ㅎ',
       'j': 'ㅈ', 'q': 'ㅊ', 'x': 'ㅅ', 'zh': 'ㅈ', 'ch': 'ㅊ', 'sh': 'ㅅ', 'r': 'ㄹ', 'z': 'ㅉ', 'c': 'ㅊ', 's': 'ㅆ', '': 'ㅇ'}
# final -> (vowel, coda, extra syllables written after it)
FIN = {'a': ('ㅏ', '', ''), 'o': ('ㅗ', '', ''), 'e': ('ㅓ', '', ''), 'ê': ('ㅔ', '', ''), 'ai': ('ㅏ', '', '이'), 'ei': ('ㅔ', '', '이'),
       'ao': ('ㅏ', '', '오'), 'ou': ('ㅓ', '', '우'), 'an': ('ㅏ', 'ㄴ', ''), 'en': ('ㅓ', 'ㄴ', ''), 'ang': ('ㅏ', 'ㅇ', ''), 'eng': ('ㅓ', 'ㅇ', ''),
       'er': ('ㅓ', 'ㄹ', ''), 'ong': ('ㅜ', 'ㅇ', ''), 'i': ('ㅣ', '', ''), 'ia': ('ㅑ', '', ''), 'io': ('ㅛ', '', ''), 'ie': ('ㅖ', '', ''),
       'iao': ('ㅑ', '', '오'), 'iu': ('ㅠ', '', ''), 'ian': ('ㅖ', 'ㄴ', ''), 'in': ('ㅣ', 'ㄴ', ''), 'iang': ('ㅑ', 'ㅇ', ''), 'ing': ('ㅣ', 'ㅇ', ''),
       'iong': ('ㅠ', 'ㅇ', ''), 'u': ('ㅜ', '', ''), 'ua': ('ㅘ', '', ''), 'uo': ('ㅝ', '', ''), 'uai': ('ㅘ', '', '이'), 'ui': ('ㅜ', '', '이'),
       'uan': ('ㅘ', 'ㄴ', ''), 'un': ('ㅜ', 'ㄴ', ''), 'uang': ('ㅘ', 'ㅇ', ''), 'ueng': ('ㅝ', 'ㅇ', ''), 'v': ('ㅟ', '', ''), 've': ('ㅞ', '', ''),
       'van': ('ㅟ', '', '안'), 'vn': ('ㅟ', 'ㄴ', '')}
CHO = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
JUNG = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
JONG = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


def syl(c, v, f=''):
    return chr(0xAC00 + (CHO.index(c) * 21 + JUNG.index(v)) * 28 + JONG.index(f))


def py2ko(p):
    """one toneless pinyin syllable (ü as ü or v) -> Hangul"""
    p = p.lower().replace('ü', 'v')
    alone = {'yi': 'i', 'ya': 'ia', 'yo': 'io', 'ye': 'ie', 'yao': 'iao', 'you': 'iu', 'yan': 'ian', 'yin': 'in', 'yang': 'iang', 'ying': 'ing',
             'yong': 'iong', 'yu': 'v', 'yue': 've', 'yuan': 'van', 'yun': 'vn', 'wu': 'u', 'wa': 'ua', 'wo': 'uo', 'wai': 'uai', 'wei': 'ui',
             'wan': 'uan', 'wen': 'un', 'wang': 'uang', 'weng': 'ueng'}
    ini, fin = '', p
    if p in alone:
        fin = alone[p]
    else:
        for k in ('zh', 'ch', 'sh', 'b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'r', 'z', 'c', 's'):
            if p.startswith(k):
                ini, fin = k, p[len(k):]
                break
        if ini in ('j', 'q', 'x') and fin.startswith('u'):
            fin = 'v' + fin[1:]          # ju = jü
    if fin not in FIN:
        raise ValueError(p)
    v, coda, extra = FIN[fin]
    if not ini and fin == 'ui':          # wei 웨이
        v = 'ㅞ'
    if not ini and fin == 'un':          # wen 원
        v = 'ㅝ'
    if fin == 'i' and ini in ('zh', 'ch', 'sh', 'r', 'z', 'c', 's'):
        v = 'ㅡ'                          # zhi 즈, si 쓰
    c = INI[ini]
    if c in 'ㅈㅉㅊ':                      # after ㅈ ㅉ ㅊ, ㅑ ㅖ ㅛ ㅠ are written ㅏ ㅔ ㅗ ㅜ
        v = {'ㅑ': 'ㅏ', 'ㅖ': 'ㅔ', 'ㅛ': 'ㅗ', 'ㅠ': 'ㅜ'}.get(v, v)
    return syl(c, v, coda) + extra


# surname readings for hanja used as Korean surnames, where the default reading differs (朴 is Piáo as a surname)
OVERRIDE = {'勒': 'le', '柏': 'bo', '繆': 'miu'}
APPROX = '率重強度樂行長'
SURNAME = {'都': 'du', '朴': 'piao', '單': 'shan', '曾': 'zeng', '解': 'xie', '查': 'zha', '區': 'ou', '樂': 'yue', '繆': 'miao', '仇': 'qiu', '尉': 'yu', '盖': 'ge', '蓋': 'ge'}

CHECK = {'習近平': '시진핑', '蔡英文': '차이잉원', '陳水扁': '천수이볜', '鄧小平': '덩샤오핑', '毛澤東': '마오쩌둥', '周恩來': '저우언라이',
         '孫文': '쑨원', '馬英九': '마잉주', '賴清德': '라이칭더', '劉德華': '류더화', '周杰倫': '저우제룬', '范冰冰': '판빙빙', '彭麗媛': '펑리위안',
         '李克強': '리커창', '胡錦濤': '후진타오', '江澤民': '장쩌민', '王毅': '왕이', '郭台銘': '궈타이밍', '朱立倫': '주리룬', '韓國瑜': '한궈위'}


def main():
    js = r"""
global.window={};['name-data.js','name-ko.js'].forEach(f=>require(process.argv[1]+'/static/'+f));
const w=window, out=new Set(), sur=new Set();
for (const v of Object.values(w.NADRI_NAMES)) if (v && typeof v==='object' && v.zh) for (const c of v.zh) out.add(c);
for (const opts of Object.values(w.KO_NAME_HANJA)) for (const o of opts) for (const c of o[0]) out.add(c);
for (const c of Object.values(w.KO_SURNAME_HANJA)) { for (const x of c) { out.add(x); sur.add(x); } }
console.log(JSON.stringify({chars:[...out].filter(c=>/[㐀-鿿]/.test(c)), sur:[...sur]}));
"""
    data = json.loads(subprocess.check_output(['node', '-e', js, str(ROOT)], text=True))
    table, multi = {}, []
    for c in sorted(data['chars']):
        reads = []
        for r in pinyin(c, style=Style.NORMAL, heteronym=True, v_to_u=True)[0]:
            if r not in reads:
                reads.append(r)
        first = SURNAME[c] if c in data['sur'] and c in SURNAME else OVERRIDE.get(c, reads[0])
        table[c] = py2ko(first)
        if c in APPROX:
            multi.append(c)
    bad = []
    for k, want in CHECK.items():
        got = ''.join(py2ko(pinyin(ch, style=Style.NORMAL, v_to_u=True)[0][0]) for ch in k)
        if got != want:
            bad.append((k, got, want))
    for b in bad:
        print('CHECK differs:', *b, file=sys.stderr)
    head = ('/* generated by tools/build_zhko.py: Mandarin reading of each Chinese character in Hangul, by the 외래어 표기법 Chinese table.\n'
            '   Pinyin from pypinyin (default reading, tones dropped); surname hanja of Korean names take the surname reading.\n'
            '   NADRI_ZHKO_MULTI: characters with two common readings in names, so a reading that uses them is shown as approximate. */\n')
    out = ROOT / 'static' / 'name-zhko.js'
    out.write_text(head + 'window.NADRI_ZHKO=' + json.dumps(table, ensure_ascii=False, separators=(',', ':')) + ';\n'
                   + 'window.NADRI_ZHKO_MULTI=' + json.dumps(''.join(multi), ensure_ascii=False) + ';\n', encoding='utf-8')
    print(len(table), 'characters,', len(multi), 'marked approximate,', len(bad), 'check mismatches ->', out)


if __name__ == '__main__':
    main()
