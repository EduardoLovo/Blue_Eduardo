import random

class Heroi(): # Person
    def heroi(self, super_batata):
        self.super_batata = super_batata
        energia = 10


    def exercicio(self):
        lista_exercicio = {
        5 : 'Seus exercicios matutinos foram muito bons e você ganhou 5 de forca',  # ganha 5 de força
        7 : 'Enquanto praticava seus exercicios choveu e você conseguiu ficar muito forte, sua força aumenta 7', # ganha 7 de força
        3 : 'O de hoje ta pago! haha. Você ganhou 3 de força', # ganha 3 de força
        2 : 'Hoje foi um tempo de seca e seus exercicios não foram muito bons, você ganha 2 de força', # ganha 2 de força
        4 : 'Você começou seus exercicios mais cedo e conseguiu dobrar seus exercicios, você ganha 4 de força '} # ganha 4 de força
        exer = random.choice(lista_exercicio)
        return exer
        
    def missao(self):
        lista_missao = [f'Na sua missao diaria uma gange de Pulgões te atacou e voce perdeu {self.perde_forca} de forca.', # perde força
        f'Na sua missao diaria você achou nutrientes e sua força aumentou para {self.aumenta_forca}. ' # ganha força
        'Você impediu que porcos invadissem a orta "BlueFarm", muito bem! Você ganhou força' # ganha força
        'Na sua missão diaria você descobriu o ponto fraco do seu inimigo, seu inimigo perdeu 5 de força' # inimigo perde força
        'Você salvou as couves de pragas, muito bem! Ganhou força'] # ganha força