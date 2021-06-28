
def autoriza_voto(anoDeNascimento):
    
    idade = 2021 - anoDeNascimento

    if idade >= 18:
        autorizacao = 'Voto obrigatorio'
    elif idade <= 17 and idade == 16:
        autorizacao = 'Voto opcional'
    else:
        autorizacao = 'Voto negado'
    return autorizacao    



def votacao(autorizacao,voto):
    if autorizacao == 'Voto obrigatorio':
        print('Voto obrigatorio!')
        conf = '[0] : Confirmar' , '[1] : Cancelar'
        if voto == '1':
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gustavo", insira "0" para confirmar ou "1" para cancelar: '))
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gustavo", insira "0" para confirmar ou "1" para cancelar: '))
            else:
                print('ok')
            if confirmação == '0':
                d['Gustavo'] += 1
                print('CONFIRMADO')
            if confirmação == '1':
                print('CANCELADO')
                
            if voto == '2':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Gabriel'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '3':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Eduardo", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou em "Eduardo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Eduardo'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '4':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou "Nulo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Voto Nulo'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '5':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou "Nulo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Voto em Branco'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

    if autorizacao == 'Voto opcional':
        print('Voto opcional!')
        conf = '[0] : Confirmar' , '[1] : Cancelar'
        if voto == '1':
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gustavo", insira "0" para confirmar ou "1" para cancelar: '))
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gustavo", insira "0" para confirmar ou "1" para cancelar: '))
            else:
                print('ok')
            if confirmação == '0':
                d['Gustavo'] += 1
                print('CONFIRMADO')
            if confirmação == '1':
                print('CANCELADO')
                
            if voto == '2':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Gabriel'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '3':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Eduardo", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou em "Eduardo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Eduardo'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '4':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou "Nulo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Voto Nulo'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')

            if voto == '5':
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "0" para confirmar ou "1" para cancelar: '))
                while confirmação != '0' and confirmação != '1':
                    print('Escolha apenas uma das duas opções')
                    for i in conf:
                        print(i)
                    confirmação = str(input('Você votou "Nulo", insira "0" para confirmar ou "1" para cancelar: '))  
                else:
                    print('ok')
                if confirmação == '0':
                    d['Voto em Branco'] += 1
                    print('CONFIRMADO')
                if confirmação == '1':
                    print('CANCELADO')
    if autorizacao == 'Voto negado':
        print('"Voto negado", Você não pode votar, por não ter 16 ou mais!')
    
    resultado = input('ver resultado da votação aperte "0", para continuar aperte qualquer outra tecla: ')
    if resultado == '0':
        print('Gustavo recebeu', d['Gustavo'], 'votos')
        print('Gabriel recebeu', d['Gabriel'], 'votos')
        print('Eduardo recebeu', d['Eduardo'], 'votos')
        print(d['Voto Nulo'], 'pessoas votaram "Nulo"')
        print(d['Voto em Branco'], 'pessoas votaram em "Branco"')
        if d['Gustavo'] > d['Gabriel'] and d['Gustavo'] > d['Eduardo'] :
            print('Gustavo é o campeão')
        elif d['Gabriel'] > d['Gustavo'] and d['Gabriel'] > d['Eduardo']:
            print('Gabriel é o campeão')
        elif d['Eduardo'] > d['Gabriel'] and d['Eduardo'] > d['Gustavo']:
            print('Eduardo é o campeão')
        else:
            print('Não teve campeão')

    ###
d = {'Gustavo' : 0 , 'Gabriel' : 0 , 'Eduardo' : 0 , 'Voto Nulo' : 0 , 'Voto em Branco' : 0}     
candidatos = '[1] : candidato 1','[2] : candidato 2','[3] : candidato 3','[4] : Voto Nulo','[5] : Voto em Branco'
candidatos1 = {1:'Gustavo',2:'Gabriel',3:'Eduardo',4:'Voto Nulo',5:'Voto em Branco'} 

    ###
while True:
    Anod = int(input('Digite o ano de nascimento '))
    autoriz = autoriza_voto(Anod)
    for i in candidatos:
        print(i)
    vot = int(input('faça seu voto: '))    
    votacao(autoriz,vot)
    proxVoto = input('Deseja vortar novamente? [s/n]: ')
    if proxVoto == 's':
        pass
    else:
        break