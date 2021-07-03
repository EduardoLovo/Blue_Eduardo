import random

dic_de_viloes = ['tomate' , 'cenoura' , 'brocolis' , 'beterraba' ]

personagem = {'superbatata' : 8}
exp = 0
fase = 0
vilao = random.choice(dic_de_viloes).lower()
força = random.randint(7, personagem['superbatata']+5)
força_do_vilao = {vilao : força}
while True:
    fase += 1
    print(f'fase {fase}')
    
    
    print(f'a orta "blueFarm" corre perigo o vilão {vilao} esta querendo acabar com a outras verduras para que só a especie dele viva na orta, a força do vilão é {força}')
    
    print('[1] : malhar para ficar mais forte (enquanto voce malha seu inimigo tambem pode malhar para ficar mais forte')
    print('[2] : trocar exp por força (a cada 10 exp vale 1 de força')
    print('[3] : fazer ronda na orta para destruir possiveis pragas e adquirir exp')
    print('[4] : lutar contra vilão')
    p_acao = int(input(f'super Batata o seu poder no momento é {list(personagem.values())} e sua exp é 0 como deseja prosseguir?'))

    if p_acao == 1:
        personagem['superbatata'] += 4
        força += random.randint(1, 6)
        print(f'sua força subiu para {list(personagem.values())} e a força do seu inimigo subiu para {força}')
        print('[1] : malhar para ficar mais forte (enquanto voce malha seu inimigo tambem pode malhar para ficar mais forte')
        print('[2] : trocar exp por força (a cada 10 exp vale 1 de força')
        print('[3] : fazer ronda na orta para destruir possiveis pragas e adquirir exp')
        print('[4] : lutar contra vilão')
        acao = input('o que deseja fazer agora?')
    if p_acao == 2:
        pass
    if p_acao == 3:
        exp += 15
        força += 1
        print(f'sua exp subiu para {exp} e a força do seu inimigo subiu para {força}')
        print('[1] : malhar para ficar mais forte (enquanto voce malha seu inimigo tambem pode malhar para ficar mais forte')
        print('[2] : trocar exp por força (a cada 10 exp vale 1 de força')
        print('[3] : fazer ronda na orta para destruir possiveis pragas e adquirir exp')
        print('[4] : lutar contra vilão')
        acao = input('o que deseja fazer agora?')
    if p_acao == 4:
        if personagem['superbatata'] > força:
            print('super Batata você derrotou o vilão, partiu proxima fase!!!')
        else:
            print('você foi derrotado')


