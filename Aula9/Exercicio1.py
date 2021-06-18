# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = []
count = 0
while count == 0:
    valor = int(input('Digite um valor '))
    
    pergunta = str(input('deseja digitar outro valor? ')).upper()    
    
    if pergunta != 'SIM':
        count += 1
    if valor not in lista:
        lista.append(valor)

lista.sort()
print(lista)