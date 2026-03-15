nome = input("Digite seu nome: ").upper() 
 
print("\nSeu nome em formato de escada:") 
for i in range(1, len(nome) + 1): 
    print(nome[:i]) 