# 1 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


print()
sexo = str(input('Digite seu sexo biologico [M/F]:')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Por favor digite apenas "M" para masculino ou "F" para feminino')
    sexo = str(input('Digite seu sexo biologico [M/F]:')).strip().upper()

print(sexo)
print()
print('Fim do Programa')