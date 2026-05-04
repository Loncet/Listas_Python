def calc_media(valores):
    notas = [float(n) for n in valores.replace(',', ' ').split()]
    
    total = sum(notas)
    quant = len(notas)
    media = total / quant 
    
    return media

entrada = input("Insira as notas separadas por espaço ou vírgula: ")

resultado = calc_media(entrada)

print(f"Sua média foi {resultado:.2f}")