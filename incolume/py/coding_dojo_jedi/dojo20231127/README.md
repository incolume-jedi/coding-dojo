# Coding Dojo

**Guilda JEDI Incolume - Grupo Python Incolume**

---

## Problema

**Get Planet Name By ID**

A função a seguir não retorna o valor correto.

```python
def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    switch id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"
        case 8: name = "Neptune"
    return name
```
## Artefatos

- [dojo](dojo20231127.py)
- [tests](test_YYYYMMDD.py)

## Exemplos

```
        (get_planet_name(2), 'Venus')
       ( get_planet_name(5), 'Jupiter')
        (get_planet_name(3), 'Earth')
        (get_planet_name(4), 'Mars')
        (get_planet_name(8), 'Neptune')
        (get_planet_name(1), 'Mercury')
```

## Referências

https://www.codewars.com/kata/515e188a311df01cba000003/train/python
