import math

area_a_pintar = float(input("Digite o tamanho da área a ser pintada (em m²): "))

cobertura_por_litro = 3
litros_por_lata = 18
preco_por_lata = 80.00

litros_necessarios = area_a_pintar / cobertura_por_litro
latas_a_comprar = math.ceil(litros_necessarios / litros_por_lata)
custo_total = latas_a_comprar * preco_por_lata

print(f"Você precisará comprar {latas_a_comprar} lata(s) de tinta, ao custo de R$ {custo_total:.2f}.")