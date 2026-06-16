import re
from zhconv import convert

_S2T_CORRECTIONS = {
    "回復": "回覆",
    "公裡": "公里",
    "一鬥": "一斗",
    "鬥車": "斗車",
    "幾鬥": "幾斗",
    "大鬥": "大斗",
    "小鬥": "小斗",
    "升鬥": "升斗",
    "才鬥": "才斗",
    "鬥米": "斗米",
    "鬥酒": "斗酒",
    "漏鬥": "漏斗",
    "熨鬥": "熨斗",
    "煙鬥": "煙斗",
    "抽鬥": "抽斗",
    "泰鬥": "泰斗",
    "星鬥": "星斗",
    "北鬥": "北斗",
    "南鬥": "南斗",
    "鬥笠": "斗笠",
    "鬥篷": "斗篷",
}

_T2S_CORRECTIONS = {
    "回覆": "回复",
}

_S2T_PATTERN = re.compile("|".join(re.escape(k) for k in _S2T_CORRECTIONS))
_T2S_PATTERN = re.compile("|".join(re.escape(k) for k in _T2S_CORRECTIONS))


def s2t(text: str) -> str:
    result = convert(text, "zh-tw")
    result = _S2T_PATTERN.sub(lambda m: _S2T_CORRECTIONS[m.group()], result)
    return result


def t2s(text: str) -> str:
    result = convert(text, "zh-cn")
    result = _T2S_PATTERN.sub(lambda m: _T2S_CORRECTIONS[m.group()], result)
    return result
