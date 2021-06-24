# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:

def area(largura,comprimento):
    area = largura * comprimento
    print(f'A area é {area}')

a = input('Deseja calcular a area?')
if a == 'sim':
    largura = float(input('Digite a largura: '))
    comprimento = float(input('Digite o comprimento: '))
    area(largura,comprimento)
