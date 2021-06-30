# Marca, Memoria Ram, Placa de video
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Estou ligando')

    def desligar(self):
        print('Estou desligando')
    
    def exibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

mar = input('Qual a marca do computador? ')
qgb = input('Qauntos gigas? ')
placa = input('Qual placa de video? ')
computador1 = Computador(mar,qgb,placa)
computador1.ligar()
computador1.desligar()
computador1.exibirInformacoesDesteComputador()