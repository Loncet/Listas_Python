def leiaInt(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            valor = int(entrada) 
            return valor        
        except ValueError:
            
            print("ERRO! Digite um número inteiro válido.")


n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")