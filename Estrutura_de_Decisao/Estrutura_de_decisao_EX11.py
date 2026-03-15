salario_atual = float(input("Digite o salário do colaborador: R$ "))

if salario_atual <= 280:
    percentual = 20
elif salario_atual <= 700:
    percentual = 15
elif salario_atual <= 1500:
    percentual = 10
else:
    percentual = 5

valor_aumento = salario_atual * (percentual / 100)
novo_salario = salario_atual + valor_aumento

print(f"\nSalário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário, após o aumento: R$ {novo_salario:.2f}")