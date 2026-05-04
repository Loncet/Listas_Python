def maior_que(a, b):
    if a > b:
        return a
    else:
        return b
    


numero1 = float(input("Insira o primeiro valor: "))
numero2 = float(input("Insira o segundo valor: "))



resultado = maior_que(numero1,numero2)

print(f"O maior valor é: {resultado:.2f} ")





