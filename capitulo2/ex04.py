def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Saudável"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc <= 34.9:
        classificacao = "Obesidade grau I"
    elif imc <= 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return imc, classificacao

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc, classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f} ({classificacao})")