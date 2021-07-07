# 3.Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

primeiraNota = float(input('Digite a primeira nota:\n'))
segundaNota = float(input('Digite a segunda nota:\n'))
terceiraNota = float(input('Digite a terceira nota:\n'))
quartaNota = float(input('Digite a quarta nota:\n'))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota) // 4
print()
print(f'sua media é: {media}')
print()
print('Fim do programa')
print()
