print("Tipos de carne: [1] Filé Duplo, [2] Alcatra, [3] Picanha")
tipo_carne_cod = input("Digite o número do tipo de carne: ")
quantidade_kg = float(input("Digite a quantidade em Kg: "))
pagamento_cartao = input("A compra será no cartão Tabajara? (S/N): ").upper()

preco_kg = 0
nome_carne = ""

if tipo_carne_cod == '1':
    nome_carne = "Filé Duplo"
    preco_kg = 4.90 if quantidade_kg <= 5 else 5.80
elif tipo_carne_cod == '2':
    nome_carne = "Alcatra"
    preco_kg = 5.90 if quantidade_kg <= 5 else 6.80
elif tipo_carne_cod == '3':
    nome_carne = "Picanha"
    preco_kg = 6.90 if quantidade_kg <= 5 else 7.80
else:
    print("Tipo de carne inválido.")
    exit()

preco_total = quantidade_kg * preco_kg
desconto = 0

if pagamento_cartao == 'S':
    desconto = preco_total * 0.05

valor_a_pagar = preco_total - desconto

print("\n--- Cupom Fiscal ---")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade_kg:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {'Cartão Tabajara' if pagamento_cartao == 'S' else 'Outro'}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
print("--------------------")