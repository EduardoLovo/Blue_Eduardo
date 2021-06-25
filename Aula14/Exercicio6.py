# Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def nota(num1):
    if num1 >= 9:
        notaConvertida = 'A'
    elif num1 >= 8:
        notaConvertida = 'B'
    elif num1 >= 7:
        notaConvertida = 'C'
    elif num1 >= 6:
        notaConvertida = 'D'
    elif num1 >= 5:
        notaConvertida = 'E'
    else:
        notaConvertida = 'F'
    return notaConvertida
nota1 = float(input('Digite sua nota: ').replace(',','.'))
notaConvertida = nota(nota1)
print(notaConvertida)