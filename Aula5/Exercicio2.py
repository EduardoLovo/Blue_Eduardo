# 2 - Escreva um programa que pede a senha uma senha ao usuário, e só sai do loop quando digitarem
# corretamente a senha. A senha é “Blue123”
# 2b - Exiba quantas vezes o usuário errou a digitação.

senha = 'Blue123'
entrada = input('Digite sua senha: ')
erros = 0
while senha != entrada:
    erros += 1
    entrada = input('senha incorreta! \nDigite novamente: ')
print('Bem vindo!')
print()
print(f'Você errou {erros} vezes')
print()
print('Fim do programa')
print()
