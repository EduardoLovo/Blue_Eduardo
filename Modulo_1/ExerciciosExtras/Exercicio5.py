# 5.Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no
# vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []
print('==~~'*5)
for i in range(20):
    numero = int(input('Digite um numero:\n'))
    vetor.append(numero)
    
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print('==~~'*5)
print(vetor)
print(f'Os numeros pares são: {par}')
print(f'Os numeros impares são: {impar}')
print()
print('Fim do programa')
print('==~~'*5)