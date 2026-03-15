num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

calc_a = (num_int1 * 2) * (num_int2 / 2)
print(f"O produto do dobro do primeiro com metade do segundo é: {calc_a}")

calc_b = (num_int1 * 3) + num_real
print(f"A soma do triplo do primeiro com o terceiro é: {calc_b}")

calc_c = num_real ** 3
print(f"O terceiro elevado ao cubo é: {calc_c:.2f}")