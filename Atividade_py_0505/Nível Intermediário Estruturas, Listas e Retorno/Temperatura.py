def temperatura(valor):
    converter=valor * 1.8 + 32
    return converter

fahrenheit = float(input("Insira o valor em Graus celsius: "))

celsius = temperatura(fahrenheit)

print (f"O valor em fahrenheIt é de {celsius}")