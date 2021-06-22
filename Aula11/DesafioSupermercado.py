### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

estoque = {'batata' : 10 , 'chocolate' : 5 , 'cerveja' : 18 , 'detergente' : 7 , 'tomate' : 2}

while True:
    compra = input('O que deseja compra?\n')
    if compra not in estoque:
        print('Este produto não temos em estoque')
        compra2 = input('deseja comprar outro produto?').upper()
        if compra == 'SIM':
            compra = input('O que deseja compra?\n')
            pass
    if compra in estoque:
        quantidade = int(input(f'Quantos {compra} deseja?\n'))
        estoque.get(quantidade) = -quantidade
    finalizar = input('Deseja comprar mais algum produto?\n')
    if finalizar == 'SIM':
        pass
    else:
        break
print(estoque)    