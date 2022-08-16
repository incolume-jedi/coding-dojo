def index0(pos: int) -> str:
    s = 'Python'
    ss = ''
    for i in range(pos + 1):
        ss += s
    return ss[pos]


def index(pos: int) -> str:
    s = 'Python'
    return s[pos % len(s)]
