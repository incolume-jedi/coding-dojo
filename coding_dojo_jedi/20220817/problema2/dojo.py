def mysort0(a,b,c):
    # a < b < c
    if c < a:
        c,a = a,c
    if c < b:
        c,b = b,c
    if b < a :
        b,a = a,b
    return (c,b,a)


def mysort(a,b,c):
    return tuple(sorted((a, b, c), reverse=True))
