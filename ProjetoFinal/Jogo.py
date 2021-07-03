  #### Jogo Super Batata ####

import random

class Pesonagem:
    def __init__(self):
        self.forca = 8

    def __str__(self):
        return 'Bom dia Super Batata, é um otimo dia para derrotar os vilões que ameaçam a "BlueFarm".'

    def forca(self):
        self.forcaBatata = 8
        return f'Sua força é {self.forcaBatata}'

    def aumenta_forca(self):
        self.aumenta_forca
        if self.tempo == 'Chuva':
            self.forca += 5
        else:
            return 'O dia o dia esta ensolarado, sua força continua a mesma'

    def perde_forca(self):
        self.perde_forca = 0

    def tempo(self):
        self.tempo = ['Chuva','Sol']
        t =random.choice(self.tempo)
        return t

class Heroi():
    def heroi(self, super_batata):
        self.super_batata = super_batata

    def exp(self):
        self.aumenta_exp += 20

    def exercicio(self):
        lista_exercicio = ['Seus exercicios matutinos foram muito bons e você ganhou 5 de forca'
        'Enquanto praticava seus exercicios choveu e você conseguiu ficar muito forte, sua força aumenta 7'
        'Hoje foi um tempo de seca e seus exercicios não foram muito bons, você perde 3 de força']
        ''
        ''
    def missao(self):
        lista_missao = [f'Na sua missao diaria uma gange de Pulgões te atacou e voce perdeu {self.perde_forca} de forca.',
        f'Na sua missao diaria você achou nutrientes e sua força aumentou para {self.aumenta_forca}. '
        'Na sua missão diaria você descobriu o ponto fraco do seu inimigo, seu inimigo perdeu 5 de força']
        ''
        ''
        random.choice(lista_missao)

class Vilao:
    def vilao(self, vilao):
        self.vilao = vilao
        lista_vilao = ['cenoura','beterrava','alface','tomate','abobrinha','pepino','cebolinha','mandioca','rabanete','brocolis']
        vilao = random.choice(lista_vilao)
        return vilao

class Fase:
    def fase(self):
        fase1 = f'O vilão {Vilao.vilao} quer roubar todos os adubos só pra ele, derrote-o para distribuir os adubos para todos'
        fase2 = f'Agora o vilao {Vilao.vialo} invadio a area de frutas, e quer roubar a terra dos limões para procriar apenas sua especie naquele lugar.'
        fase3 = f''
        fase4 = f''
        fase5 = f''

if (__name__ == '__main__'):
    fase = 1
    exercicio = False
    missao = False
    tempo = True
    
    while True:
