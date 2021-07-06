import Vilao

class Fase:
    def fase(self, fase):
        self.fase = fase
        if fase == 1:
            print(f'O vilão {Vilao.vilao} quer roubar todos os adubos só pra ele, derrote-o para distribuir os adubos para todos')
        elif fase == 2:
            print(f'O vilao {Vilao.vialo} invadiu a area de frutas, e quer roubar a terra dos limões para procriar apenas sua especie naquele lugar.')
            # vilao força + 1 
        elif fase == 3:
            print(f'O vilao fez uma familha de beterrabas de refem. salve as beterrabas do vilao')
            # vilao força + 2
        elif fase == 4:
            print(f'O vialo da orta vizinha quer destruir a BlueFarm.')
            # vilao força + 3
        else:
            print(f'Vilao dos viloes')
            # vilao força + 4