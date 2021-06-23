# 3. DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma
# lista. No final, mostre:
# A) Quantas pessoas estão cadastradas.
# B) A média da idade.
# C) Uma lista com as mulheres.
# D) Uma lista com as idades que estão acima da média.
# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando
# perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

lista =[]
d = {}

while True:
    nome = input('Digite seu nome:\n').strip()
    sexo = input('Digite seu sexo biologico [masculino/feminino]:\n').upper().strip()
    while sexo != 'MASCULINO' and sexo != 'FEMININO':
        print('Digite apenas "Masculino" ou "Feminino".')
        sexo = input('Digite seu sexo biologico [masculino/feminino]:\n').upper().strip()
    idade = int(input('Digite sua idade:\n'))
    d['nome'] = [nome]
    d['sexo'] = [sexo]
    d['idade'] = [idade]
    lista.append(d)
    per = input('Deseja fazer outro cadastro? [sim/não]:\n').upper().strip()
    d = {}
    while per != 'SIM' and per != 'NÃO':
        print('Digite apenas "sim" ou "não"')
        per = input('Deseja fazer outro cadastro? [sim/não]\n').upper().strip()
    if per == 'NÃO':
        break
idade = 0

    
print(len(lista))


print(lista)


