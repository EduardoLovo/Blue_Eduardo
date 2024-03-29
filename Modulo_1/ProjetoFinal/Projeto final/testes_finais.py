from random import choice
from time import sleep
from random import randint
from abertura import abertura
from gameover import gameover


class Personagem:
    def __init__(self,clima):
        forca=10   #força padrão de qualquer personagem
        self.forca= forca
        self.clima= clima
        self.nome= ''
       
class Heroi(Personagem):
    def __init__(self,clima):
        super().__init__(clima)
        self.vitalidade= 3 # vida do Herói
        self.clima= clima

    def atacar(self,treino=0):
        self.força_adicional = treino

    def treinar(self,clima):
        dic_treino = {5:'Seus exercícios matutinos foram muito bons e você ganhou +5 de força.',7:
        'Enquanto praticava seus exercícios a terra foi adubada e você ficou muito forte!\nSua força aumentou em +7 pontos.',3:'O de hoje ta pago...hahahahaha!\nVocê ganhou + 3 de força.',2:'Houve um tempo de seca e suas raízes não tiveram de onde puxar nutrientes.\nVocê ganhou +2 de força', 4:'Você começou a treinar mais cedo e conseguiu dobrar seus exercicios!\nVocê ganha +4 de força.'}
        ganho_forca = choice(list(dic_treino.keys()))
        self.forca += ganho_forca

        if clima == 'chovendo':
            influencia_clima = 3
            self.forca += influencia_clima

            print()
            sleep(0.5)
            print('-='*30)
            sleep(1)
            print(dic_treino[ganho_forca])
            sleep(1.5)
            print('\nA chuva irrigou o solo da Bluefarm.\nVocê ganhou +3 de bônus!')
            sleep(1.5)
            print('-='*30)
            sleep(1)
            print(f'Sua força total agora é: {self.forca} pts')
            sleep(2)
            print('\nVá para casa descansar, pois amanhã será um longo dia...........')
            for i in range (30):
                print('.',end='', flush=True )
                sleep(0.05)
            sleep(3)
            print()
            print('.'*60)
        else:

            print()
            sleep(0.5)
            print('-='*30)
            sleep(1)
            print(dic_treino[ganho_forca])
            sleep(1.5) 
            print('-='*30)
            sleep(1)
            print(f'Sua força total agora é: {self.forca} pts')
            sleep(2)
            print('\nVá para casa descansar, pois amanhã será um longo dia...........')
            for i in range (60):
                print('.',end='', flush=True )
                sleep(0.05)
            sleep(3)
            print()
            print('.'*60)
            

class Vilao(Personagem):
    def __init__(self,clima):
        super().__init__(clima)
        ganho_forca= randint(1,5)
        self.forca += ganho_forca
        self.clima= clima
         

    def escolher_vilão(self):
        lista_viloes= ['cenouras','beterrabas','alfaces','tomates','abobrinhas','pepinos','cebolinhas','mandiocas','rabanetes','brócolis']
        lista_jaForam = list()
        
        if lista_jaForam == lista_viloes: # VENCEU O JOGO
            print("Parabéns!!!\nVocê derrotou todos os vilões e livrou a Bluefarm dos vegetais Tóxicos de uma vez por todas!!!")
            exit()
            
        escolha_vilao = choice(lista_viloes) #Escolhe um vilão da lista_viloes    
        while escolha_vilao in lista_jaForam:
            escolha_vilao = choice(lista_viloes) # Se o vilão escolhido já estiver na lista_jaForam escolhe novamente.

        self.nome= escolha_vilao
        


        lista_jaForam.append(escolha_vilao) # adiciona o vilão escolhido na lista dos vilões que já foram
                
        if self.clima == 'ensolarado': #influencia do clima na força do vilão escolhido
            self.forca += 3
              
        return escolha_vilao        
 
# Abertura do jogo
#abertura()

# Começo do jogo
lista_clima = ['chovendo','ensolarado']
clima= choice(lista_clima)

batata= Heroi(clima)
vilao= Vilao(clima)

while True:
    print()
    print()
    if batata.clima == 'chovendo': # Começo para dias de chuva
        sleep(0.5)
        print(f'Bom dia, Super Batata!')
        sleep(1)
        print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
        sleep(1.5)
        print('O que deseja fazer?')
        sleep(1)
        print('\n1- Treinar')
        sleep(1)
        print('2- Derrotar alguns vegetais arruaceiros')
        sleep(1.2)
        print('\nSituação do clima: chovendo')
        sleep(1)
        escolha=input('\nR:')
        while escolha not in ['1','2']:
            print('Entrada inválida!')
            sleep(1)
            print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
            sleep(1.5)
            print('Lembre-se, está chovendo!')
            sleep(1.2)
            escolha = input('R: ')
    else: # Começo para dias de sol
        sleep(0.5)
        print(f'Bom dia, Super Batata!')
        sleep(1)
        print('\nÉ um otimo dia para treinar e derrotar os vilões que ameaçam a "BlueFarm".')
        sleep(1.5)
        print('O que deseja fazer?')
        sleep(1)
        print('\n1- Treinar')
        sleep(1)
        print('2- Derrotar alguns vegetais arruaceiros')
        sleep(1)
        print('\nSituação do clima: ensolarado')
        sleep(0.7)
        escolha=input('\nR:')
        while escolha not in ['1','2']:
            print('Entrada inválida!')
            sleep(1)
            print('\nDigite 1 para treinar ou 2 para enfrentar algum vilão:')
            sleep(1.5)
            print('Lembre-se, está ensolarado!')
            sleep(1.2)
            escolha = input('R: ')
            sleep(0.5)

    # Testando as escolhas 
    if escolha == '2':
        print('\nOs arruceiros estão plantados a mais tempo que você e se beneficiaram do uso de componentes tóxicos.\nTem certeza que deseja ataca-los?')
        sleep(2.5)
        print('\n1- Sim. Eu sou uma Super Batata, irei ataca-los agora mesmo!')
        sleep(1.5)
        print('2- Não, acho melhor treinar mais um pouquinho antes.')
        escolha= input('R: ')
        if escolha == '2':
            batata.treinar(clima)
    
        qnt_treino= 0

        # Escolha do inimigo e Batatalha
        if escolha== '1':
            inimigos = vilao.escolher_vilão()
            print('-='*30)
            sleep(0.5)
            print(f'\nOs arruaceiros da vez são {inimigos.capitalize()}!!!')
            sleep(1)
            print(f'\nHouve uma temporada de seca na horta dos arruaceiros, {vilao.nome} desviaram a irrigação para si ganharam +3 de força.') 
            print(f'{inimigos.capitalize()} têm {vilao.forca} pts de força.')
              
            escolha= input('\nDeseja enfrentar?\n\n1- Bora cair pra dentro\n2- Cê é louco cachoeira?!\nR: ')
            # Batalha
            if escolha =='1':
                if batata.forca < vilao.forca:  # Se o vilão for mais forte
                    print(f'\nSua força atual é: {batata.forca} pts de força')
                    if batata.vitalidade== 3:
                        print(f'Sua vida atual é:███')
                    elif batata.vitalidade== 2:
                        print(f'Sua Vida atual é:██')     
                    elif batata.vitalidade==1:
                        print(f'Sua Vida atual é :█')
                    
                    sleep(0.5)    
                    print(f'\n\n{inimigos.capitalize()} têm {vilao.forca} pts de força.\n')
                    sleep(1)
                    print('-='*30)
                    sleep(0.5)    
                    print(f'Você virou um purê nas mãos dos inimigos.\nAumente seus carboidratos e tente novamente!')
                    sleep(1)
                    print('-='*30)

                    batata.vitalidade -= 1 # Herói Perde 1 de vitalidade 
                    if batata.vitalidade == 0: # Se a vitalidade chegar a 0 dá Game Over
                        gameover()
                        exit()

                elif batata.forca >= vilao.forca:
                    print(f'Força atual: {batata.forca} pts')
                    if batata.vitalidade== 3:
                        print(f'Vida atual:███')
                    elif batata.vitalidade== 2:
                        print(f'Vida atual:██')     
                    elif batata.vitalidade==1:
                        print(f'Vida atual:█')
                    
                    print(f'\n\n{inimigos.capitalize()}: {vilao.forca} pts de força')

                    print(f'\n\nSanta Batatuda...Você derrotou os inimigos!!!\n Mas, calma! A Bluefarm ainda não está livre da gange dos agroTóxicos.')
            elif escolha == '2':
                print('-='*30)
                print(f'\nQue decepção para os Orgânicos assistir a Super Batata fugir de {inimigos.capitalize()}...\nAcho melhor você deixar de ser orgulhoso e ir treinar um pouco')
                print('-='*30)
                print('No dia seguinte') 

    elif escolha == '1':
        batata.treinar(clima)

    # mudar o clima
    clima= choice(lista_clima)
    batata.clima=clima
    vilao.clima=clima    