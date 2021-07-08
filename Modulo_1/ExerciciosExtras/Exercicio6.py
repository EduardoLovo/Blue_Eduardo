# 6.Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada
# aluno, imprima o número de alunos com média maior ou igual a 7.0

media = []

print('==~~'*5)
for i in range(10):
    nota1 = float(input('Digite a primeria nota:\n'))
    nota2 = float(input('Digite a segunda nota:\n'))
    nota3 = float(input('Digite a terceira nota:\n'))
    nota4 = float(input('Digite a quarta nota:\n'))
    m = (nota1 + nota2 + nota3 + nota4)//4
    if m >= 7.0:
        media.append(m)

print(f'As medias maiores ou iguais a 7.0 são {media}')   
print()
print('Fim do programa')
print('==~~'*5)