def para_leet(texto): 
    leet_map = { 
        'a': '4', 'e': '3', 'g': '6', 'i': '1', 
        'o': '0', 's': '5', 't': '7', 'l': '1' 
    } 
     
    texto_leet = "" 
    for char in texto.lower(): 
        texto_leet += leet_map.get(char, char) 
    return texto_leet 
 
texto_original = input("Digite um texto para converter para Leet Speak: ") 
print(f"Texto em Leet: {para_leet(texto_original)}") 