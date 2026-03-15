peso_peixes = float(input("Digite o peso dos peixes (em kg): "))
limite = 50
multa_por_kg = 4.00

if peso_peixes > limite:
    excesso = peso_peixes - limite
    multa = excesso * multa_por_kg
    print(f"Peso excedente: {excesso:.2f} kg. Multa a pagar: R$ {multa:.2f}")
else:
    print("Peso dentro do regulamento. Não há multa a pagar.")