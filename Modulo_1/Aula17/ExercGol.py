d = {}
l = []
g = []
while True:
    jogador = input('Nome do jogador: ')
    d[jogador] = 0
    partidas = int(input('Quantas partidas jogadas: '))
    l.append(partidas)
    for i in range(partidas):
        gols = int(input(f'Marcou quantos gols na {i}º partida: '))
        g.append(gols)
    soma = sum(g)
    # print(d)
    print(l)
    print(soma)
    d[jogador] = partidas, soma
    print(d)
    print()


