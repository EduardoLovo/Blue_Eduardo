# 1 – Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) 
# e seus valores correspondentes aos quadrados desses números.

lista1 = [ 1 , 4 , 5 , 6 , 7 , 9 ]
numeros_quadrados = {}
for i in lista1:
    numeros_quadrados[i] = i**2
print(numeros_quadrados)


# 2 – Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.​

quadrados = {}

for i in range(1,11):
    quadrados[i] = i**2
print(quadrados)

    ## com input:
quadrados2 = {}
numero = int(input('Digite um numero: '))
for i in range(1,numero+1):
    quadrados2[i] = i**2
print(quadrados2)

