import math

area_a_pintar = float(input("Digite o tamanho da área a ser pintada (em m²): "))

area_com_folga = area_a_pintar * 1.1

cobertura_por_litro = 6
litros_necessarios = area_com_folga / cobertura_por_litro

print(f"Área com folga: {area_com_folga:.2f} m². Litros necessários: {litros_necessarios:.2f} L.")

preco_lata = 80.00
litros_lata = 18
latas_necessarias = math.ceil(litros_necessarios / litros_lata)
custo_apenas_latas = latas_necessarias * preco_lata
print(f"\nOpção 1 (apenas latas): {latas_necessarias} lata(s) de 18L. Custo: R$ {custo_apenas_latas:.2f}")

preco_galao = 25.00
litros_galao = 3.6
galoes_necessarios = math.ceil(litros_necessarios / litros_galao)
custo_apenas_galoes = galoes_necessarios * preco_galao
print(f"Opção 2 (apenas galões): {galoes_necessarios} galão(ões) de 3.6L. Custo: R$ {custo_apenas_galoes:.2f}")

latas_mix = math.floor(litros_necessarios / litros_lata)
litros_restantes = litros_necessarios % litros_lata
galoes_mix = math.ceil(litros_restantes / litros_galao)
custo_mix = (latas_mix * preco_lata) + (galoes_mix * preco_galao)
print(f"Opção 3 (misto): {latas_mix} lata(s) de 18L e {galoes_mix} galão(ões) de 3.6L. Custo: R$ {custo_mix:.2f}")