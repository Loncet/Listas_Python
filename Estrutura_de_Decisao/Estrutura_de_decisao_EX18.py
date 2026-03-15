data_str = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    dia, mes, ano = map(int, data_str.split('/'))
    
    data_valida = True
    if not (1 <= mes <= 12 and ano > 0):
        data_valida = False
    else:
        # Verifica o dia máximo para cada mês
        dias_no_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Checa ano bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            dias_no_mes[2] = 29
            
        if not (1 <= dia <= dias_no_mes[mes]):
            data_valida = False

    print(f"A data {data_str} é {'válida' if data_valida else 'inválida'}.")
except (ValueError, IndexError):
    print(f"Formato ou data inválida.")