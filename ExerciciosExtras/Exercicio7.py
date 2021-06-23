# 7.Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = [1,2,3,4,5]

soma = sum(lista)  ## soma entre os numeros da lista
multiplicação = lista[0]*lista[1]*lista[2]*lista[3]*lista[4]  ## multiplicação entre os numeros da lista

print('==~~'*5)
print(lista)
print(f'A soma dos numeros da lista é {soma}')
print(f'A mulplicação dos numeros da lista é {multiplicação}')
print()
print('Fim do programa')
print('==~~'*5)