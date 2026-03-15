nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 9.0 <= media <= 10.0:
    conceito = 'A'
elif 7.5 <= media < 9.0:
    conceito = 'B'
elif 6.0 <= media < 7.5:
    conceito = 'C'
elif 4.0 <= media < 6.0:
    conceito = 'D'
else: # 0.0 <= media < 4.0
    conceito = 'E'

print(f"\nNotas: {nota1} e {nota2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito in 'ABC':
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")