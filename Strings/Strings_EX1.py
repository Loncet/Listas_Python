string1 = input("Digite a primeira string: ") 
string2 = input("Digite a segunda string: ") 
 
print(f"\nConteúdo da primeira string: '{string1}'") 
print(f"Tamanho da primeira string: {len(string1)} caracteres") 
 
print(f"\nConteúdo da segunda string: '{string2}'") 
print(f"Tamanho da segunda string: {len(string2)} caracteres") 
 
print("\n--- Comparações ---") 
print(f"As duas strings possuem o mesmo tamanho? {'Sim' if len(string1) == len(string2) else 'Não'}") 
print(f"O conteúdo das duas strings é igual? {'Sim' if string1 == string2 else 'Não'}") 