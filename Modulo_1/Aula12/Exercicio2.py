# 2. Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for 
# diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar

d = {}
lista = []
print('--~~--'*5)
cadastro = input('Digite seu nome:\n').title().strip()
print()
ano = int(input(f'Digite o ano que você nasceu:\n'))
print()
idade = 2021 - ano
ctps = int(input('Digite seu o numero da sua carteira de trabalho:\n'))
print()

d['nome'] = [cadastro]
d['idade'] = [ano]
d['ctps'] = [ctps]

if ctps != 0:  
    anoContra = int(input('Digite o ano de contratação:\n'))
    print()
    salario = float(input('Digite seu salario:\nR$ '))
    print()
    d['anoDeContratação'] = [anoContra]
    d['salario'] = [salario]
else:
    print('Informações insuficientes para calcular aposentadoria!')

anoAp = (anoContra + 35) - ano

print(f'Você irá se aposentar com {anoAp}')
print()
print('Fim do programa')
print()
print('--~~--'*5)
print(d)