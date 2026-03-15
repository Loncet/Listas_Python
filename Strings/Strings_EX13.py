import random

palavras = ["abacaxi", "morango", "laranja", "banana", "melancia"]
palavra_original = random.choice(palavras)

lista_letras = list(palavra_original)
random.shuffle(lista_letras)
palavra_embaralhada = "".join(lista_letras)

print("--- Adivinhe a Palavra ---")
print(f"A palavra embaralhada é: {palavra_embaralhada}")

palpite = input("Qual é a palavra original? ").lower()

if palpite == palavra_original:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você errou. A palavra era '{palavra_original}'.")