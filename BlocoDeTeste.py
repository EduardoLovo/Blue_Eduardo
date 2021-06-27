
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
    
    # gjj = input('deseja votar novamente?')
    if gjj == 'n':
        if voto == 1:
            gustavo = 1
            
            return gustavo
        if voto == 2:
            gabriel = 2
            return gabriel
        if voto == 3:
            eduardo = 3
            return eduardo
        if voto == 4:
            votoNulo = 4
            return votoNulo
        if voto == 5:
            votoBranco = 5
            return votoBranco
        print(f'gustavo teve {gus} votos')

    if autorizacao == 'Voto obrigatorio':
        if voto == 1:
            gustavo = 1
            return gustavo
        if voto == 2:
            gabriel = 2
            return gabriel
        if voto == 3:
            eduardo = 3
            return eduardo
        if voto == 4:
            votoNulo = 4
            return votoNulo
        if voto == 5:
            votoBranco = 5
            return votoBranco
    
    
    # elif autorizacao == 'Voto opcional':
    #     a = input('Voto opcional, deseja votar? ')
    #     if a == 'sim':
    #         if voto == 1:
    #             gustavo = 1
    #         if voto == 2:
    #             gabriel = 1
    #         if voto == 3:
    #             eduardo = 1
    #         if voto == 4:
    #             votoNulo = 1
    #         if voto == 5:
    #             votoBranco =1
    # else:
    #     print('Voto invalido, você não tem idade para votar')
    
    # candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
    
    # for i in candidatos:
    #     print(i)
    
# Anod = int(input('Digite o ano de nascimento '))
# autorizacao = autoriza_voto(Anod)
# print(autoriza_voto(Anod))

# candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
# candidatos1 = {1:'Gustavo',2:'Gabriel',3:'Eduardo',4:'Voto Nulo',5:'Voto em Branco'}
# for i in candidatos:
    # print(i)
# voto = int(input('faça seu voto: '))
gusta =[]
gus = sum(gusta)
gabr = []
edu = []
vnulo = []
vbranco = []
while True:
    an = int(input('digite seu ano de nascimento: '))
    autoriza_voto(an)
    if autoriza_voto(an) == 'Voto obrigatorio':
        candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
        for i in candidatos:
            print(i)
        vv = int(input('faça  seu voto: '))
        if vv == 1:
            gusta.append(1)
            gus = sum(gusta)
        votacao(autoriza_voto(an),vv)
        # if autoriza_voto == 'Voto obrigatorio':
            
        
            # if votacao(autoriza_voto(an),vv) == 2:
            #     gabr.append(1)
            # if votacao(autoriza_voto(an),vv) == 3:
            #     edu.append(1)
            # if votacao(autoriza_voto(an),vv) == 4:
            #     vnulo.append(1)
            # if votacao(autoriza_voto(an),vv) == 5:
            #     vbranco.append(1)
            
    hh = input('deseja votar novamente? [s/n]') 
    if hh == 's':
        pass
    else:
        break
        