# 1- Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

l = [5, 7, 2, 9, 4, 1, 3]
tamanho = len(l)
maior = max(l)
menor = min(l)
soma = sum(l)

print(l)
print(f'A lista tem {tamanho} valores')
print(f'O maior valora da lista é {maior}')
print(f'O menor valor da lista é {menor}')
print(f'A soma dos valores é {soma}')
print('A lista em ordem crescente é: ')
crescente = l.sort()
print(l)
print(f'A lista em ordem decrescente é: ')
decrescente = l.reverse()
print(l)
print()
print('Fim do programa')
print()
