# 3 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No
# final, mostre:

# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

idade = int(input('Qual sua idade? '))
sexo = str(input('Qual o seu sexo, [masculino/feminino]? ')).strip()
a = 0
b = 0
c = 0
proximoCadastro = str(input('Deseja cadastrar novamnte? ')).strip()
if idade >= 18:
    a = a +1

if sexo == 'masculino':
    b = b +1

if idade >= 20 and sexo == 'feminino':
    c = c +1
print()
while proximoCadastro == 'sim':
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual o seu sexo, [masculino/feminino]? ')).strip()
    proximoCadastro = str(input('Deseja cadastrar novamnte? ')).strip()
    if idade >= 18:
        a = a +1
    if sexo == 'masculino':
        b = b +1
    if idade >= 20 and sexo == 'feminino':
        c = c +1
    print()        

print(f'{a} pessoas tem mais de 18 anos')
print(f'{b} homens foram cadastrados')
print(f'{c} mulheres com mais de 20 anos foram cadastradas')
print()
print('Fim do programa')