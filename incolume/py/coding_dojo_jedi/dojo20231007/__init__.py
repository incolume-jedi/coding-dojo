from sys import maxsize


def max_sequence(lista: list) -> int:
    """_Soma os valores dentro de um array.
    """
    soma = 0
    # TODO identificar se os números são negativos
    resultado = []

    for x in lista:
        resultado.append(x < 0)

    if all(resultado):
        return 0

    resultado.clear()
    for y in lista:
        resultado.append(y >= 0)

    if all(resultado):
        soma = 0
        for numero in lista:
            soma = soma + numero
        return soma
    #[-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # 4, -1, 2, 1,
    #[10, -11, 2, 3, 4, 5, -5,  6, 7, -50, 8,-7, 9]
    # 2, 3, 4, 5,
    return resultado


def maxSubArraySum(a):
    """Python program to print largest contiguous array sum.

    Function to find the maximum contiguous subarray
    and print its starting and end index

    """
    size = len(a)
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):

        max_ending_here += a[i]

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    print("Maximum contiguous sum is %d" % (max_so_far))
    print("Starting Index %d" % (start))
    print("Ending Index %d" % (end))
    return max_so_far
