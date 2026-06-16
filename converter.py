import re
from zhconv import convert as zhconv_convert

VALID_LOCALES = {"zh-cn", "zh-tw", "zh-hk"}

_TW_CORRECTIONS = {
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

_HK_CORRECTIONS = {
    "回復": "回覆",
    "公裡": "公里",
    "公裏": "公里",
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

_CN_CORRECTIONS = {
    "回覆": "回复",
}

_CORRECTIONS_MAP = {
    "zh-tw": _TW_CORRECTIONS,
    "zh-hk": _HK_CORRECTIONS,
    "zh-cn": _CN_CORRECTIONS,
}

_PATTERNS = {}
for _locale, _dict in _CORRECTIONS_MAP.items():
    if _dict:
        _PATTERNS[_locale] = re.compile("|".join(re.escape(k) for k in _dict))


def convert(text: str, locale: str = "zh-tw") -> str:
    if locale not in VALID_LOCALES:
        raise ValueError(f"不支持的 locale: {locale}，可选值: {', '.join(sorted(VALID_LOCALES))}")
    result = zhconv_convert(text, locale)
    if locale in _PATTERNS:
        corrections = _CORRECTIONS_MAP[locale]
        result = _PATTERNS[locale].sub(lambda m: corrections[m.group()], result)
    return result


def s2t(text: str) -> str:
    return convert(text, "zh-tw")


def s2hk(text: str) -> str:
    return convert(text, "zh-hk")


def t2s(text: str) -> str:
    return convert(text, "zh-cn")
