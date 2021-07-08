# Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def maiorMenor(num1,num2):
    if num1 > num2:
        numeroMaior = num1
        return numeroMaior
    elif num1 < num2:
        numeroMaior = num2
        return numeroMaior
    else:
        print('Os numero são iguais')
        
    

n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))

numeroMaior = maiorMenor(n1,n2)
print(numeroMaior, 'é maior')