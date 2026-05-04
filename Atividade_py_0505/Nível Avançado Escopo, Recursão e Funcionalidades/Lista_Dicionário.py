def produto_mais_caro(lista_produtos):
    
    if not lista_produtos:
        return None

    
    mais_caro = lista_produtos[0]

    
    for produto in lista_produtos:
        
        if produto['preco'] > mais_caro['preco']:
            
            mais_caro = produto
            
    return mais_caro

estoque = [
    {"nome": "Mouse", "preco": 50.0},
    {"nome": "Teclado", "preco": 150.0},
    {"nome": "Monitor", "preco": 900.0},
    {"nome": "Headset", "preco": 250.0}
]

resultado = produto_mais_caro(estoque)
print(f"O produto mais caro é: {resultado['nome']} custando R$ {resultado['preco']}")