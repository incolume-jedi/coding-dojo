"""
Custo computacional

ipython -i dojo
>>> from dis import dis

dis(mysort0)
dis(mysort1)
dis(mysort)

"""
def mysort0(a,b,c):
    # a < b < c
    if c < a:
        c,a = a,c
    if c < b:
        c,b = b,c
    if b < a :
        b,a = a,b
    return (c,b,a)


def mysort1(a,b,c):
    result = [a, b, c]
    result.sort(reverse=True)
    return tuple(result)


def mysort(a,b,c):
    return tuple(sorted((a, b, c), reverse=True))

