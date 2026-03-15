num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação deseja realizar (+, -, *, /)? ")

resultado = 0
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        exit()
else:
    print("Operação inválida!")
    exit()

print(f"\nO resultado da operação é: {resultado}")

print(f"O número é {'positivo' if resultado > 0 else 'negativo' if resultado < 0 else 'zero'}.")

if resultado == round(resultado):
    print("O número é inteiro.")
    print(f"O número é {'par' if resultado % 2 == 0 else 'ímpar'}.")
else:
    print("O número é decimal.")