numero = int(input("Digite um número inteiro menor que 1000: ")) 
 
if 0 < numero < 1000: 
    centenas = numero // 100 
    dezenas = (numero % 100) // 10 
    unidades = numero % 10 
 
    resultado = [] 
 
    if centenas > 0: 
        resultado.append(f"{centenas} {'centena' if centenas == 1 else 'centenas'}") 
    if dezenas > 0: 
        resultado.append(f"{dezenas} {'dezena' if dezenas == 1 else 'dezenas'}") 
    if unidades > 0: 
        resultado.append(f"{unidades} {'unidade' if unidades == 1 else 'unidades'}") 
 
    if len(resultado) > 1: 
        saida = ", ".join(resultado[:-1]) + " e " + resultado[-1] 
    else: 
        saida = resultado[0] if resultado else "zero" 
 
    print(f"{numero} = {saida}") 
else: 
    print("Número fora do intervalo permitido (1 a 999).") 