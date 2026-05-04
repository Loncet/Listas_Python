def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
            
    return contador

# Exemplo de uso:
frase = input("Sua frase: ")
total = contar_vogais(frase)
print(f"O total de vogais é: {total}")