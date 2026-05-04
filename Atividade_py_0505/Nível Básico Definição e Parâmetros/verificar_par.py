def verificar_par(valor):
    if valor % 2 == 0:
        return True
    else:
        return False


numero = float(input("insira o valor: "))


print(verificar_par(numero))


