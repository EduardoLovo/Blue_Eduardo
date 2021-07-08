# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
final = somar(num1,num2,num3)
print(final)