"""dojo module."""

mapping = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz',
}


def combination(*args: str) -> list[str]:
    """Combination."""
    match len(args):
        case 1:
            return list(args)
        case 2:
            return [f'{x}{y}' for x in args[0] for y in args[1]]
        case 3:
            return [
                f'{x}{y}{z}' for x in args[0] for y in args[1] for z in args[2]
            ]
        case 4:
            return [
                f'{x}{y}{z}{w}'
                for x in args[0]
                for y in args[1]
                for z in args[2]
                for w in args[3]
            ]


def dojo(num: int | str, qdig: int = 4) -> list[str]:
    """Dojo answer."""
    msgs = [f'`num` max {qdig} digits.', 'only numbers between 2 to 9.']
    result = []

    if num != 0 and not num:
        return result

    num = str(num)
    if len(num) > qdig:
        raise ValueError(msgs[0])

    if not num.isdigit() or not all(int(x) in mapping for x in num):
        raise TypeError(msgs[1])

    if len(num) == 1:
        return list(mapping.get(int(num)))
    return combination(*[mapping.get(int(x)) for x in num])
