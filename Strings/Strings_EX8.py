texto = input("Digite uma palavra ou frase para verificar se é um palíndromo: ") 
 
texto_processado = texto.replace(" ", "").lower() 
 
if texto_processado == texto_processado[::-1]: 
    print(f"'{texto}' é um palíndromo.") 
else: 
    print(f"'{texto}' não é um palíndromo.") 