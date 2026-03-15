kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))

preco_morango = 2.50 if kg_morango <= 5 else 2.20
preco_maca = 1.80 if kg_maca <= 5 else 1.50

valor_total = (kg_morango * preco_morango) + (kg_maca * preco_maca)

peso_total = kg_morango + kg_maca

if peso_total > 8 or valor_total > 25.00:
    valor_final = valor_total * 0.90 # Aplica desconto de 10%
else:
    valor_final = valor_total

print(f"\nResumo da Compra:")
print(f"{kg_morango:.2f} Kg de morangos: R$ {kg_morango * preco_morango:.2f}")
print(f"{kg_maca:.2f} Kg de maçãs: R$ {kg_maca * preco_maca:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")
if valor_final != valor_total:
    print(f"Valor com desconto: R$ {valor_final:.2f}")
print(f"\nValor a ser pago pelo cliente: R$ {valor_final:.2f}")