candidatos = '[1] : candidato1','[2] : candidato2','[3] : candidato3','[4] : Voto Nulo','[5] : Voto em Branco'
# candidatos1 = {'candidato1': 1 ,'candidato2': 2 ,'candidato3': 3 ,'Voto Nulo': 4 ,'Voto em Branco': 5 }
candidatos1 = {1:'candidato1',2:'Gabriel',3:'candidato3',4:'Voto Nulo',5:'Voto em Branco'}
# for i in candidatos:
#     print(i)
voto = int(input('faça seu voto '))
# a = dict.values(candidatos1)
if voto not in candidatos1:
    print('vote novamnte')
else:
    print(f'Voce votou em {candidatos1[voto]}')
# print(a)
# print(dict.values(candidatos1))
# print(f'seu voto {candidatos1[voto]}')
# voto = input(candidatos['faça seu voto']