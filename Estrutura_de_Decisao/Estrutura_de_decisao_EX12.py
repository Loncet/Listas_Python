valor_hora = float(input("Digite o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    percentual_ir = 0
elif salario_bruto <= 1500:
    percentual_ir = 5
elif salario_bruto <= 2500:
    percentual_ir = 10
else:
    percentual_ir = 20

desconto_ir = salario_bruto * (percentual_ir / 100)
desconto_sindicato = salario_bruto * 0.03 # O enunciado pedia 3% para o Sindicato
fgts = salario_bruto * 0.11
total_descontos = desconto_ir + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print(f"\nSalário Bruto: ({valor_hora} * {horas_trabalhadas}) : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_ir}%) : R$ {desconto_ir:.2f}")
print(f"(-) Sindicato (3%) : R$ {desconto_sindicato:.2f}") # O exemplo do enunciado mostra INSS, mas o texto pede Sindicato.
print(f"FGTS (11%) : R$ {fgts:.2f}")
print(f"Total de descontos : R$ {total_descontos:.2f}")
print(f"Salário Liquido : R$ {salario_liquido:.2f}")