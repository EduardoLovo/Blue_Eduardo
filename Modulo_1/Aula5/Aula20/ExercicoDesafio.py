# 4 - Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar
# adivinhar qual número foi escolhido até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

numeroCorreto = 10
a = 0

numero = int(input('Adivinhe qual o numero que estou pensado de 0 a 10\n'))
print()
while numero != numeroCorreto:
        a = a + 1
        print('Você errou, tente mais uma vez')
        numero = int(input('Adivinhe qual o numero que estou pensado de 0 a 10\n'))
        print()

print('Você acertou!!')    
print(f'voce errou {a} vezes.')
print()
print('Fim do programa')