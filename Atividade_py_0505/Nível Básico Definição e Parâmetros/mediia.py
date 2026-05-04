def media(nota1, nota2, nota3):

    soma = nota1 + nota2 + nota3
    mfinal = soma / 3
    return mfinal

valor1 = float(input("Nota 1: "))
valor2 = float(input("Nota 2: "))
valor3 = float(input("Nota 3: "))


print(f"A nota media é: {media(valor1, valor2, valor3):.2f}")

