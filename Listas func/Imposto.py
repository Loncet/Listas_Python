def soma_imposto(taxa_imposto, custo):
    
    valor_imposto = custo * (taxa_imposto / 100)
    valor_final = custo + valor_imposto
    return valor_final

custo = float(input("Digite o custo do item: "))
imposto = float(input("Digite a taxa de imposto (em %): "))

resultado = soma_imposto(imposto, custo)

print(f"O valor final do produto com imposto é: R$ {resultado:.2f}")