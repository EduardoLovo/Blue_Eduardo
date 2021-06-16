# 04 - Desenvolva um código em que o usuário vai entrar vários números e no final vai apresentar a
# soma deles (o usuário vai dizer quantos números serão informados antes de começar)

soma = 0

quantidade_Numeros = int(input('Quantidade de somas: '))

for i in range(quantidade_Numeros):
    soma = soma + int(input('Qual o numero da vez '))

print('A soma é: ', soma)
print()
print('Fim do programa')
print()