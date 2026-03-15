nome = input("Digite seu nome: ").upper() 
 
print("\nSeu nome em formato de escada invertida:") 
for i in range(len(nome), 0, -1): 
    print(nome[:i]) 