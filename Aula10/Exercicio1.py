# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.

lista = []

for i in range(3):
    nome = (input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    
    lista.append([nome,idade])
# print(lista)
# print()
    for j in lista:
        if lista[0][1] >= 18:
            print(f'{lista[0][0]} é maior de idade')
        else:
            print(f'{lista[0][0]} é menor de idade')
            
        
print()
   