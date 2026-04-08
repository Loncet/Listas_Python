def valida_string(texto, minimo=1, maximo=100):
    tamanho=len(texto)
    if minimo <= tamanho <= maximo:
        return True
    else:
        return False


print(valida_string("Python"))          
print(valida_string("Algoritmo", 1, 5))

