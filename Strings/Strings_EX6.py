def data_por_extenso(data_str): 
    try: 
        dia, mes_num, ano = data_str.split('/') 
         
        meses = { 
            '01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', 
            '05': 'Maio', '06': 'Junho', '07': 'Julho', '08': 'Agosto', 
            '09': 'Setembro', '10': 'Outubro', '11': 'Novembro', '12': 'Dezembro' 
        } 
         
        if mes_num in meses: 
            return f"{dia} de {meses[mes_num]} de {ano}" 
        return "Mês inválido." 
    except ValueError: 
        return "Formato de data inválido. Use dd/mm/aaaa." 
 
data_input = input("Digite uma data no formato dd/mm/aaaa: ") 
print(data_por_extenso(data_input)) 