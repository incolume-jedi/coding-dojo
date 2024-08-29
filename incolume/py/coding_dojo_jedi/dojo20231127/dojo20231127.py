"""Dojo."""


def get_planet_name0(id_planet: int) -> str:  # noqa: C901
    """Get planet name."""
    name = ''
    match id_planet:
        case 1:
            name = 'Mercury'
        case 2:
            name = 'Venus'
        case 3:
            name = 'Earth'
        case 4:
            name = 'Mars'
        case 5:
            name = 'Jupiter'
        case 6:
            name = 'Saturn'
        case 7:
            name = 'Uranus'
        case 8:
            name = 'Neptune'
    return name


def get_planet_name(id_planet: int) -> str:
    """Get planet name."""
    names = {
        1: 'Mercury',
        2: 'Venus',
        3: 'Earth',
        4: 'Mars',
        5: 'Jupiter',
        6: 'Saturn',
        7: 'Uranus',
        8: 'Neptune',
    }
    return names[id_planet]
