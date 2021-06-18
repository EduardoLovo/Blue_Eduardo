# 4.Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
# consoantes

lista = ['a','b','c','d','e','g','h','i','j','k']

print(len(lista))
print()

for i in lista:
    if i in 'aeiou':
        pass    
    else:
        print(i)


print()
print('Fim do programa')
print()