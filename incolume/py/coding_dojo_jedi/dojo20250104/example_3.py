"""Soluçao desafio-11.

Author: recursiveError
Data: 19-01-2023
disponível em: https://github.com/OsProgramadores/op-desafios/blob/master/desafio-11/RecursiveError/python/main.py


minha primeira solução para esse exercico, era sem recurção
era lido byte por byte, o problema era quando chegava no 5 nos
primeiros digitos
41 5 '9265' <- n é primo 358979323846

então resolvi começar pegando direto 4 bites e ir tirando 1 por 1
isso funcionou até ps primeiro mil digitos
mas em uma sequencia de 1M existem muitas possibilidades para isso
 dar errado então parei para ler o exemplo com mais calma

41 59 2 653 5 89 7 9323
meus codidos só retornavam
4159 ....
41 5 ....
nunca 41 59

eu tinha que volta a o 5 se a sequncia seguinte não fosse primo
foi ai que me lembrei de um algoritmos de permutação que usavam
recursão e para percorrer um array adaptando a ideia cheguei
neste resultado


notas de otimização:
esse codigo é lento, eu tentei de muitas formas não usar variaveis
 globais e retornar o valor mas pela minha falta de experiência não
  consegui chegar no resultado esperado

como pylint não deixa codigo com variaveis globais mutaveis passar
resolvi passar por referencia, o que me obriga a usar metodos de
array em python em vez de passar diretamenta array = sequencia
o que diminui ainda mais a eficiencia do codigo
"""

import sys
from pathlib import Path

from icecream import ic


def get_prime(limit: int) -> list[int]:
    """Get prime.

    Retorna todos os numeros primos de 2
    ate limit usando Crivo de Eratóstenes.
    """
    _primes = []
    for _num in range(2, limit + 1, 1):
        for _prime in _primes:
            if _num % _prime == 0:
                break
        else:
            _primes.append(_num)
    return _primes


def load_file(_file):
    """Carrega os bytes do arquivo em uma array, e remove 3."""
    char = _file.read(1)
    _bytes = ''
    while char:
        _bytes += char
        char = _file.read(1)
        if char == '.':
            _bytes = ''
            char = _file.read(1)
        if char.isalpha():
            ic('ERRO: arquivo deve conter apenas numeros')
            sys.exit(1)
    return _bytes


def get_bigger_seq(prime_array, array, begin, seq, bigger_seq):
    """Gera a maior seuqencia de primos possiveis em uma sequencia de bytes."""
    char = ''
    prime_to_add = ''
    num = 0
    for i in range(begin, begin + 4):
        try:
            char += array[i]
            num = int(char)
        except IndexError:
            break

        if num in prime_array:
            prime_to_add = seq + char
            get_bigger_seq(prime_array, array, i + 1, prime_to_add, bigger_seq)

    if len(prime_to_add) > len(bigger_seq[0]):
        bigger_seq.clear()
        bigger_seq.append(prime_to_add[::])


primes = get_prime(10000)
biggest_seq = ['']
if len(sys.argv) < 2:  # noqa: PLR2004
    ic(
        'chame este programa passando o nome'
        ' de um arquivo ex: python main.py numeros.txt',
    )
    sys.exit(1)

file_name = Path(sys.argv[1])
try:
    with file_name.open(encoding='utf-8') as file:
        loaded_file = load_file(file)
        for index in range(len(loaded_file)):
            get_bigger_seq(primes, loaded_file, index, '', biggest_seq)
        ic(biggest_seq[0])
except FileNotFoundError:
    ic(f'arquivo: {file_name} não encontrado')
    sys.exit(1)
