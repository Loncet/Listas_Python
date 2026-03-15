import random 
 
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo", "openai"] 
palavra_secreta = random.choice(palavras) 
letras_descobertas = ["_" for _ in palavra_secreta] 
tentativas = 6 
letras_erradas = [] 
 
print("--- Jogo da Forca ---") 
 
while tentativas > 0 and "_" in letras_descobertas: 
    print(f"\nPalavra: {' '.join(letras_descobertas)}") 
    print(f"Tentativas restantes: {tentativas}") 
    print(f"Letras erradas: {', '.join(letras_erradas)}") 
     
    letra = input("Digite uma letra: ").lower() 
 
    if letra in palavra_secreta: 
        print("Boa! A letra está na palavra.") 
        for i, char in enumerate(palavra_secreta): 
            if char == letra: 
                letras_descobertas[i] = letra 
    else: 
        print("Que pena! A letra não está na palavra.") 
        if letra not in letras_erradas: 
            letras_erradas.append(letra) 
            tentativas -= 1 
 
print("\n--- Fim de Jogo ---") 
if "_" not in letras_descobertas: 
    print(f"Parabéns! Você adivinhou a palavra: '{palavra_secreta}'") 
else: 
    print(f"Você perdeu! A palavra era: '{palavra_secreta}'") 