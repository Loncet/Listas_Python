
resultado = "Original (Global)"

def minha_funcao():
    
    resultado = "Alterado (Local)"
    
    local_especifica = "Eu só existo aqui dentro!"
    
    print(f"Dentro da função: {resultado}")
    print(f"Dentro da função: {local_especifica}")



minha_funcao()

print(f"Fora da função: {resultado}")

