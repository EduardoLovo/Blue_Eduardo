### Prgrama de contagem de Votos ###

def autoriza_voto(anoDeNascimento):
    # anoDeNascimento = input('Digite seu ano de nascimento')
    idade = 2021 - anoDeNascimento
    # a = obrigatorio
    # b = opcional
    # c = negado
    if idade >= 18:
        return 'Obrigatorio'
    elif idade <= 17 and idade == 16:
        print('Voto opcional')
    else:
        print('Voto negado')

# def votacao(autorizacao,voto):
#     autorização  
#     gustavo = 0
#     gabriel = 0
#     eduardo = 0
#     votoNulo = 0
#     votoBranco = 0
#     print('==~~'*5)
#     candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
#     candidatos1 = {1:'Gustavo',2:'Gabriel',3:'Eduardo',4:'Voto Nulo',5:'Voto em Branco'}
#     while True:
#         for i in candidatos:
#             print(i)
#         voto = int(input('faça seu voto: '))
#         while voto not in candidatos1:
#             print('vote novamnte')
#         else:
#             print(f'Voce votou em {candidatos1[voto]}')
#         if voto == 1:
#             gustavo += 1
#         if voto == 2:
#             gabriel += 1
#         if voto == 3:
#             eduardo += 1
#         if voto == 4:
#             votoNulo += 1
#         if voto == 5:
#             votoBranco +=1
#         proxVoto = input('Votar novamente [s/n]: ')
#         print('==~~'*5)
#         if proxVoto == 'n':
#             break
        
#     print('==~~'*5)
#     print(f'Gustavo teve um total de {gustavo} votos.')
#     print(f'Gabriel teve um total de {gabriel} votos.')
#     print(f'Eduardo teve um total de {eduardo} votos.')
#     print(f'{votoNulo} pessoas votaram nulo.')
#     print(f'{votoBranco} pessoas votaram em branco.')
#     print('==~~'*5)

# votacao()

Anod = int(input('Digite o ano de nascimento '))
if autorizacao == 'Obrigatorio':
    votacao(autorizacao,voto)

 
autoriza_voto(Anod)