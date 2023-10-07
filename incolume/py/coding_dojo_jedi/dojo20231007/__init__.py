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
    """for i in lista:
        soma = soma + i
    return soma"""