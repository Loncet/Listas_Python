def valida_cpf(cpf):
    cpf_numerico = ''.join(filter(str.isdigit, cpf))

    if len(cpf_numerico) != 11 or len(set(cpf_numerico)) == 1:
        return False

    soma = sum(int(cpf_numerico[i]) * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf_numerico[9]):
        return False

    soma = sum(int(cpf_numerico[i]) * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    if resto == 10:
        resto = 0
    if resto != int(cpf_numerico[10]):
        return False

    return True


cpf_input = input("Digite um CPF para validação (formato xxx.xxx.xxx-xx): ")

if valida_cpf(cpf_input):
    print("CPF válido.")
else:
    print("CPF inválido.")