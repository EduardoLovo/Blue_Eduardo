# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.

import random

lista1 = ['pedra','papel','tesoura']

while True:
    vitorias = 0
    derrotas = 0
    pergunta = int(input('Quantas rodadas deseja jogar? '))
    for i in range(pergunta):
        jk = str(input('Escolha: Pedra, papel ou tesoura:\n')).upper().strip()
        while jk != 'PEDRA' and jk != 'PAPEL' and jk != 'TESOURA':
            print('Escolha apenas uma das 3 opções e verifique se digitou corretamente')
            jk = str(input('Escolha: Pedra, papel ou tesoura:\n')).upper().strip()
        pc = random.choice(lista1).upper()
        print()
        print(f'Você escolheu "{jk}"')
        print(f'Eu escolho "{pc}"')

        if pc == 'PEDRA' and jk == 'PAPEL':
            print('Você ganhou!')  
            vitorias += 1

        if pc == 'PEDRA' and jk == 'TESOURA':
            print('Você perdeu!')
            derrotas += 1   

        if pc == 'PEDRA' and jk == 'PEDRA':
            print('Empate')    

        if pc == 'PAPEL' and jk == 'PAPEL':
            print('Empate')  
            
        if pc == 'PAPEL' and jk == 'TESOURA':
            print('Você ganhou')
            vitorias += 1    

        if pc == 'PAPEL' and jk == 'PEDRA':
            print('Você perdeu')       
            derrotas +=1

        if pc == 'TESOURA' and jk == 'PAPEL':
            print('Voce perdeu')  
            derrotas +=1

        if pc == 'TESOURA' and jk == 'TESOURA':
            print('Empate')   

        if pc == 'TESOURA' and jk == 'PEDRA':
            print('Você ganhou')
            vitorias += 1   
        print()

    if vitorias > derrotas:
        print(f'Você ganhou {vitorias}')
        print(f'Eu ganhei {derrotas}')
        print('VOCÊ É O CAMPEÃO!!!')
    if vitorias < derrotas:
        print(f'Você ganhou {vitorias}')
        print(f'Eu ganhei {derrotas}')
        print('EU SOU O CAMPEÃO!!!')
    if vitorias == derrotas:
        print('Ficamos empatados!!!')
    print()
    pergunta2 = input('Deseja jogar novamente?[sim/não]\n').upper().strip()
    print()
    while pergunta2 != 'NÃO' and pergunta2 != 'SIM':
        print('Responda apenas "sim" ou "não" e verifique se digitou corretamete')
        pergunta2 = input('Deseja jogar novamente?[sim/não]\n').upper().strip()
        
    if pergunta2 == 'NÃO': 
        break
    print()
print()
print('Fim do programa')
print()

