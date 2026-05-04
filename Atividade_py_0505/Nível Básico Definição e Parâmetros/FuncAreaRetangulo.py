def calcular_area(base, altura):
    caluculo = base * altura
    return caluculo

base = float(input("Insira o valor da base "))
altura = float(input("Insira o valor da altura"))
resultado = calcular_area(base, altura)

print(f"A area é: {resultado}")