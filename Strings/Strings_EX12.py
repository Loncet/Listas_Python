telefone = input("Digite o número de telefone (com ou sem hífen): ")

telefone_numerico = telefone.replace("-", "")

if len(telefone_numerico) == 7:
    telefone_corrigido = "3" + telefone
    print(f"Telefone corrigido: {telefone_corrigido}")
elif len(telefone_numerico) == 8:
    print("O telefone já possui 8 dígitos.")
else:
    print("O número de telefone não tem 7 ou 8 dígitos.")