from zhconv import convert


def s2t(text: str) -> str:
    return convert(text, 'zh-tw')


def t2s(text: str) -> str:
    return convert(text, 'zh-cn')
