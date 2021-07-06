import random

class Tempo:
    def tempo(self):
        self.tempo = ['Chuva','Sol']
        t =random.choice(self.tempo)
        if t == 'Chuva':
            self.forca += 5         # ganha força
        else:
            return 'O dia esta ensolarado, sua força continua a mesma'   # força fica igual