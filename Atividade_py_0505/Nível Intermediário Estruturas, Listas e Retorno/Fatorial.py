def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

Numero = int(input("Insira o numero: "))
print(f"O fatorial de é {fatorial_iterativo(Numero)}") 