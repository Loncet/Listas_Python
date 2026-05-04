
def inverter_frase(frase):
    frase_invertida = ""
    for caracter in frase:
        frase_invertida = caracter + frase_invertida
    return frase_invertida


teste = input("Sua palavra: ")
print(inverter_frase(teste)) 