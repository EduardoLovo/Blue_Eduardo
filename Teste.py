### Prgrama de contagem de Votos ###

def autoriza_voto(anoDeNascimento):
    
    idade = 2021 - anoDeNascimento

    if idade >= 18:
        autorizacao = 'Voto obrigatorio'
    elif idade == 17 or idade == 16:
        autorizacao = 'Voto opcional'
    else:
        autorizacao = 'Voto negado'
    return autorizacao    



def votacao(autorizacao,voto):
    if autorizacao == 'Voto obrigatorio':
        print('Voto OBRIGATÓRIO!')
        print('==~~'*5)
        conf = ('[1] : Confirmar' , '[2] : Cancelar')
        if voto == 1:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gustavo", insira "1"  para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gustavo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Gustavo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)    
        if voto == 2:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gabriel", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "1" para confirmar ou "2" para cancelar: ')).strip()  
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Gabriel'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 3:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Eduardo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Eduardo", insira "1" para confirmar ou "2" para cancelar: ')).strip()  
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Eduardo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 4:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou "Nulo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou "Nulo", insira "1" para confirmar ou "2" para cancelar: ')).strip()  
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Voto Nulo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 5:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Branco", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Branco", insira "1" para confirmar ou "2" para cancelar: ')).strip()  
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Voto em Branco'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
    if autorizacao == 'Voto opcional':
        print('Voto OPCIONAL!')
        print('==~~'*5)
        conf = '[1] : Confirmar' , '[2] : Cancelar'
        if voto == 1:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gustavo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '1' and confirmação != '2':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gustavo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Gustavo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)   
        if voto == 2:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Gabriel", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Gabriel", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            else:
                print('==~~'*5)  
                print('ok')
            if confirmação == '1':
                d['Gabriel'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 3:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Eduardo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou em "Eduardo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            else:  
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Eduardo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 4:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou "Nulo", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou "Nulo", insira "0" (zero) para confirmar ou "1" para cancelar: ')).strip()
            else:
                print('==~~'*5) 
                print('ok')
            if confirmação == '1':
                d['Voto Nulo'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
        if voto == 5:
            for i in conf:
                print(i)
            confirmação = str(input('Você votou em "Branco", insira "1") para confirmar ou "2" para cancelar: ')).strip()
            while confirmação != '0' and confirmação != '1':
                print('Escolha apenas uma das duas opções')
                for i in conf:
                    print(i)
                confirmação = str(input('Você votou "Branco", insira "1" para confirmar ou "2" para cancelar: ')).strip()
            else:
                print('==~~'*5)
                print('ok')
            if confirmação == '1':
                d['Voto em Branco'] += 1
                print('CONFIRMADO')
            if confirmação == '2':
                print('CANCELADO')
            print('==~~'*5)
    if autorizacao == 'Voto negado':
        print('"Voto NEGADO", Você não pode votar, por não ter 16 anos ou mais!')
        print('==~~'*5)
    l = ['[1] : Continuar votação', '[2] : Encerrar votação e exibir resultado']
    for i in l:
        print(i)
    resultado = str(input('Insira "1" para continuar votação ou "2" para encerrar votação e exibir resultado: '))
    if resultado == '2':
        print('==~~'*5)
        print('Gustavo recebeu', d['Gustavo'], 'votos')
        print('Gabriel recebeu', d['Gabriel'], 'votos')
        print('Eduardo recebeu', d['Eduardo'], 'votos')
        print(d['Voto Nulo'], 'pessoas votaram "Nulo"')
        print(d['Voto em Branco'], 'pessoas votaram em "Branco"')
        print('==~~'*5)
        if d['Gustavo'] > d['Gabriel'] and d['Gustavo'] > d['Eduardo'] :
            print('Gustavo é o campeão')
        elif d['Gabriel'] > d['Gustavo'] and d['Gabriel'] > d['Eduardo']:
            print('Gabriel é o campeão')
        elif d['Eduardo'] > d['Gabriel'] and d['Eduardo'] > d['Gustavo']:
            print('Eduardo é o campeão')
        else:
            print('Não teve campeão')
    if resultado == '1': 
        pass  
    ###
d = {'Gustavo' : 0 , 'Gabriel' : 0 , 'Eduardo' : 0 , 'Voto Nulo' : 0 , 'Voto em Branco' : 0}     
candidatos = '[1] : candidato 1','[2] : candidato 2','[3] : candidato 3','[4] : Voto Nulo','[5] : Voto em Branco'
candidatos1 = {1:'Gustavo',2:'Gabriel',3:'Eduardo',4:'Voto Nulo',5:'Voto em Branco'} 

    ###
while True:
    print('==~~'*5)
    Anod = int(input('Digite o ano de nascimento '))
    print('==~~'*5)
    autoriz = autoriza_voto(Anod)
    for i in candidatos:
        print(i)
    vot = int(input('faça seu voto: ')) 
    print('==~~'*5)   
    votacao(autoriz,vot)
    # c = '[s] : sim', '[n] : não'
    # print('==~~'*5)
    # for i in c:
    #     print(i)
    # proxVoto = input('Deseja vortar novamente? [s/n]: ').strip().lower()
    # while proxVoto != 's' and proxVoto != 'n':
    #     print('Escolha apenas entre "s" para sim ou "n" para não.')
    #     for i in c:
    #         print(i)
    #     proxVoto = input('Deseja vortar novamente? [s/n]: ').strip().lower()
    # if proxVoto == 's':
    #     pass
    # else:
    #     break