def bmi(peso: float, alt: float) -> str:
    imc = peso / alt ** 2
    if imc <= 18.5:
        return "Underweight"
    elif imc <= 25.0:
        return "Normal"
    elif imc <= 30.0:
        return "Overweight"
    else:
        return "Obese"
