  #### Jogo Super Batata ####

# clima - aleatorio
# força inicial - 10
# força do inimigo - 13 - 20
# uma missao por fase
# um exercicio por fase
# batalha

import random

class Person:
    def __init__(self):
        self.forca = 10

    def __str__(self):
        return 'Bom dia Super Batata, é um otimo dia para derrotar os vilões que ameaçam a "BlueFarm".'

    def forca(self):
        return f'Sua força é {self.forcaBatata}'

    def aumenta_forca(self):
        self.forca += 1111

    def perde_forca(self):
        self.perde_forca = 0


        



if (__name__ == '__main__'):
    fase = 1
    exercicio = False
    missao = False
    tempo = True
    

    while True:
        print('==~~'*5)
        print(Person)
        print()
        print(Tempo())
        print()
        print(Fase.fase)
        print('==~~'*5)
        print('Ações')
        print('[1] : Fazer exercicio para aumentar força. (necessario 6 de energia')
        print('[2] : Cumprir missão (necessario 4 de energia')
        print('[3] : Lutar contra vilão')
        opcao = input('Escolha sua ação: ')
        if opcao == 1:
            Heroi.exercicio()
                # energia perde 6
        if opcao == 2:
            Heroi.missao()
                # energia perde 4
        if opcao == 3:
            # se força for maior que força do vilão, ganha.


