valor_saque = int(input("Digite o valor do saque (mínimo R$10, máximo R$600): ")) 
 
if 10 <= valor_saque <= 600: 
    valor = valor_saque 
     
    notas100 = valor // 100 
    valor %= 100 
     
    notas50 = valor // 50 
    valor %= 50 
     
    notas10 = valor // 10 
    valor %= 10 
     
    notas5 = valor // 5 
    notas1 = valor % 5 
     
    print(f"\nPara sacar R$ {valor_saque}, você receberá:") 
    if notas100 > 0: print(f"{notas100} nota(s) de R$ 100") 
    if notas50 > 0: print(f"{notas50} nota(s) de R$ 50") 
    if notas10 > 0: print(f"{notas10} nota(s) de R$ 10") 
    if notas5 > 0: print(f"{notas5} nota(s) de R$ 5") 
    if notas1 > 0: print(f"{notas1} nota(s) de R$ 1") 
else: 
    print("Valor de saque inválido.") 