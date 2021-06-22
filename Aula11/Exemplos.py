contatos_lista = [('Gustavo', '8888-7777'),('Gabriel', '2222-4242'),('Joao', '9999-5656'),('Carlos', '8484-6161')]


# dicionarios1 = {'Chave':'Valor'}

# contatos = dict(contatos_lista)
# print(contatos)
# print(contatos['Gustavo'])
# dic1 = {'Gustavo': '8888-7777', 'Gabriel': '2222-4242', 'Joao': '9999-5656', 'Carlos': '8484-6161'}
# nome = input('Digite o nome da pessoa: ')
# print(dic1.get(nome,'Desculpa, não encontrei.'))

vingadores = {'Chris Evans' : 'Capitão América' , 'Mark Ruffalo' : 'Hulk' , 'Tom Hiddleston' : 'Loki' , 'Chris Hemworth' : 'Thor' , 
'Robert Downey Jr' : 'Homem de Ferro' , 'Scarlett Johansson' : 'Viúva Negra'}

print('Hulk' in vingadores.values())
print('Hulk' in vingadores.keys())

vingadores['Tom holland'] = 'Homem aranha'
nome = input('Digite o nome do ator: ')
personagem = input('Digite o nome do personagem: ')
print(vingadores)
print()
del vingadores['Tom holland']

vingadores[nome] = personagem
print(vingadores)
