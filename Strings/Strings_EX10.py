def numero_por_extenso(n): 
    if not 0 <= n <= 99: 
        return "Número fora do intervalo (0-99)." 
 
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"] 
    dezenas_especiais = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"] 
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"] 
 
    if n < 10: 
        return unidades[n] 
    elif n < 20: 
        return dezenas_especiais[n - 10] 
    else: 
        dezena = n // 10 
        unidade = n % 10 
        if unidade == 0: 
            return dezenas[dezena] 
        else: 
            return f"{dezenas[dezena]} e {unidades[unidade]}" 
 
try: 
    numero_input = int(input("Digite um número entre 0 e 99: ")) 
    print(numero_por_extenso(numero_input)) 
except ValueError: 
    print("Entrada inválida. Por favor, digite um número inteiro.") 