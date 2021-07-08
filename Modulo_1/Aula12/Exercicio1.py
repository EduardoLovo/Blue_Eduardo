# 1. Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

dicionario = {}
aluno = input('Digite o nome do aluco: ')
media = float(input(f'Digite a media de {aluno}: '))

dicionario[aluno] = media

if dicionario[aluno] >= 7:
    print(f'{dicionario.keys()} foi aprovado!')
elif dicionario[aluno] < 6.9 and dicionario[aluno] >= 5:
    print(f'{dicionario.keys()} esta de recuperação!')
else:
    print(f'{dicionario.keys()} foi reprovado!')

print(dicionario)