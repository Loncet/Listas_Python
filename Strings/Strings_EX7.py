frase = input("Digite uma frase: ") 
 
espacos = frase.count(' ') 
 
vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} 
 
for letra in frase.lower(): 
    if letra in vogais: 
        vogais[letra] += 1 
 
print(f"\nA frase possui {espacos} espaço(s) em branco.") 
print("Ocorrência de vogais:") 
for vogal, quantidade in vogais.items(): 
    print(f"{vogal}: {quantidade}") 