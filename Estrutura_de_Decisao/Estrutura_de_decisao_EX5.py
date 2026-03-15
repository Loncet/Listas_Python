nota1 = float(input("Digite a primeira nota parcial: "))
nota2 = float(input("Digite a segunda nota parcial: "))

media = (nota1 + nota2) / 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")