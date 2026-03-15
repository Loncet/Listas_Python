litros = float(input("Quantos litros foram vendidos? "))
tipo = input("Qual o tipo de combustível (A-álcool, G-gasolina)? ").upper()

preco_gasolina = 2.50
preco_alcool = 1.90
valor_a_pagar = 0

if tipo == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor_a_pagar = litros * (preco_alcool * (1 - desconto))
elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor_a_pagar = litros * (preco_gasolina * (1 - desconto))
else:
    print("Tipo de combustível inválido!")

if valor_a_pagar > 0:
    print(f"O valor a ser pago é: R$ {valor_a_pagar:.2f}")