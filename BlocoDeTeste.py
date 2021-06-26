Anod = int(input('Digite o ano de nascimento '))

idade = 2021 - Anod

if idade >= 18:
    autorizacao = 'Voto obrigatorio'
    # autorizacao
elif idade <= 17 and idade == 16:
    autorizacao = 'Voto opcional'
    # autorizacao
else:
    autorizacao = 'Voto negado'
    # autorizacao

print(autorizacao)   