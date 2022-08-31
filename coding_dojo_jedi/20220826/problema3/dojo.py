def imc(altura: float, peso: float) -> str:
    imc = peso / altura ** 2
    return [
        'Obesidade III',
        'Obesidade II',
        'Obesidade I',
        'Sobrepeso',
        'peso normal',
        'abaixo do peso',
        ][(imc < 39.9) + (imc < 34.9) + (imc < 29.9) + (imc < 24.9) + (imc < 18.5)]
