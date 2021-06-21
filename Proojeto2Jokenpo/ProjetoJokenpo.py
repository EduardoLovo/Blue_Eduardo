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

pergunta = int(input('Quantas rodadas deseja jogar? '))

for i in range(pergunta):
    jk = str(input('Escolha: Pedra, papel ou tesoura\n'))
    pc = random.choice(lista1)
    print(pc)
    
                
    