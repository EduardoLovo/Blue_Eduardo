# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

lista1 = []
lista2Par = []
lista3Impar = []

count = 0
while count == 0:
    valor = int(input('Digite um valor: '))
    lista1.append(valor)
    if (valor%2) == 0:
        lista2Par.append(valor)
    else:
        lista3Impar.append(valor)
    pergunta = str(input('Deseja digitar um novo valor? ')).upper()
    if pergunta != 'SIM':
        count += 1
print()
print(lista1)
print(lista2Par)
print(lista3Impar)
print()
print('Fim do programa')
print()