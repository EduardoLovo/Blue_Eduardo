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
        self.forcaBatata = 10
        return f'Sua força é {self.forcaBatata}'

    def aumenta_forca(self):
        self.aumenta_forca

    def perde_forca(self):
        self.perde_forca = 0

    def tempo(self):
        self.tempo = ['Chuva','Sol']
        t =random.choice(self.tempo)
        if t == 'Chuva':
            self.forca += 5
        else:
            return 'O dia esta ensolarado, sua força continua a mesma'
        

class Heroi():
    def heroi(self, super_batata):
        self.super_batata = super_batata
        energia = 10

    def exercicio(self):
        lista_exercicio = ['Seus exercicios matutinos foram muito bons e você ganhou 5 de forca',
        'Enquanto praticava seus exercicios choveu e você conseguiu ficar muito forte, sua força aumenta 7',
        'O de hoje ta pago! haha. Você ganhou 3 de força',
        'Hoje foi um tempo de seca e seus exercicios não foram muito bons, você ganha 2 de força',
        'Você começou seus exercicios mais cedo e conseguiu dobrar seus exercicios, você ganha 4 de força ']
        exer = random.choice(lista_exercicio)
        return exer
        
    def missao(self):
        lista_missao = [f'Na sua missao diaria uma gange de Pulgões te atacou e voce perdeu {self.perde_forca} de forca.',
        f'Na sua missao diaria você achou nutrientes e sua força aumentou para {self.aumenta_forca}. '
        'Você impediu que porcos invadissem a orta "BlueFarm", muito bem! Você ganhou força'
        'Na sua missão diaria você descobriu o ponto fraco do seu inimigo, seu inimigo perdeu 5 de força'
        'Você salvou as couves de pragas, muito bem! Ganhou força']
        
        
        random.choice(lista_missao)

class Vilao:
    def vilao(self):
        # self.vilao = vilao
        lista_vilao = ['cenoura','beterrava','alface','tomate','abobrinha','pepino','cebolinha','mandioca','rabanete','brocolis']
        vilao = random.choice(lista_vilao)
        return vilao
    def batalha(self):
        # se força da batata for maior que a força do Vilao
        # batata vence
        # else  GAME OVER

class Fase:
    def fase(self, fase):
        self.fase = fase
        if fase == 1:
            fase1 = f'O vilão {Vilao.vilao} quer roubar todos os adubos só pra ele, derrote-o para distribuir os adubos para todos'
        elif fase == 2:
            fase2 = f'Agora o vilao {Vilao.vialo} invadio a area de frutas, e quer roubar a terra dos limões para procriar apenas sua especie naquele lugar.'
        elif fase == 3:
            fase3 = f''
        elif fase == 4:
            fase4 = f''
        else:
            fse5 = f''

if (__name__ == '__main__'):
    fase = 1
    exercicio = False
    missao = False
    tempo = True
    
    while True:
        print('==~~'*5)
        print(Person)
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
        if opcao == 2:
            Heroi.missao()
        if opcao == 3:
