print("Responda com 'S' para Sim ou 'N' para Não.")

respostas_positivas = 0

if input("Telefonou para a vítima? ").upper() == 'S': respostas_positivas += 1
if input("Esteve no local do crime? ").upper() == 'S': respostas_positivas += 1
if input("Mora perto da vítima? ").upper() == 'S': respostas_positivas += 1
if input("Devia para a vítima? ").upper() == 'S': respostas_positivas += 1
if input("Já trabalhou com a vítima? ").upper() == 'S': respostas_positivas += 1

if respostas_positivas == 2:
    print("\nClassificação: Suspeita")
elif 3 <= respostas_positivas <= 4:
    print("\nClassificação: Cúmplice")
elif respostas_positivas == 5:
    print("\nClassificação: Assassino")
else:
    print("\nClassificação: Inocente")