# Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def funcao(num1):
    if num1 > 0:
        positivo = 'P'
        return positivo
    elif num1 < 0:
        negativo = 'N'
        return negativo
    else:
        igual = '0'
        return igual

numero = int(input('Digite um numero: '))
print(funcao(numero))