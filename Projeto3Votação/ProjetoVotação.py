### Prgrama de contagem de Votos ###

def autoriza_voto(anoDeNascimento):
    
    idade = 2021 - anoDeNascimento

    if idade >= 18:
        autorizacao = 'Voto obrigatorio'
        return autorizacao
    elif idade <= 17 and idade == 16:
        autorizacao = 'Voto opcional'
        return autorizacao
    else:
        autorizacao = 'Voto negado'
        return autorizacao

def votacao(autorizacao,voto):
    if autorizacao == 'Voto obrigatorio':
        pass
    elif autorizacao == 'Voto opcional':
        a = input('Voto opcional, deseja votar? ')
        if a == 'sim':
            pass
    
        
    gustavo = 0
    gabriel = 0
    eduardo = 0
    votoNulo = 0
    votoBranco = 0

    candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
    candidatos1 = {1:'Gustavo',2:'Gabriel',3:'Eduardo',4:'Voto Nulo',5:'Voto em Branco'}
    for i in candidatos:
        print(i)
    voto = int(input('faça seu voto: '))    
    # voto = int(input('faça seu voto: '))
    while voto in candidatos1:
        print(f'Voce votou em {candidatos1[voto]}')
        
        if voto == 1:
            gustavo += 1
        if voto == 2:
            gabriel += 1
        if voto == 3:
            eduardo += 1
        if voto == 4:
            votoNulo += 1
        if voto == 5:
            votoBranco +=1
        proxVoto = input('Votar novamente [s/n]: ')
        # print('==~~'*5)
        if proxVoto == 's':
            voto = int(input('faça seu voto: '))
        else:
            break
    else:
        print('numero invalido')
    print('==~~'*5)
    print(f'Gustavo teve um total de {gustavo} votos.')
    print(f'Gabriel teve um total de {gabriel} votos.')
    print(f'Eduardo teve um total de {eduardo} votos.')
    print(f'{votoNulo} pessoas votaram nulo.')
    print(f'{votoBranco} pessoas votaram em branco.')
    print('==~~'*5)

        # if autorizacao == 'Voto negado':
        #     print()   
        

Anod = int(input('Digite o ano de nascimento '))

autorizacao = autoriza_voto(Anod)
print(autoriza_voto(Anod))

candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
for i in candidatos:
    print(i)
voto = int(input('faça seu voto: '))
votacao(autorizacao,voto)
print(votacao(autorizacao,voto))
# print(b)
# gus = gustavo
# gabriel = 0
# eduardo = 0
# votoNulo = 0
# votoBranco = 0
# print('==~~'*5)
# print(f'Gustavo teve um total de {gustavo} votos.')
# print(f'Gabriel teve um total de {gabriel} votos.')
# print(f'Eduardo teve um total de {eduardo} votos.')
# print(f'{votoNulo} pessoas votaram nulo.')
# print(f'{votoBranco} pessoas votaram em branco.')
# print('==~~'*5)