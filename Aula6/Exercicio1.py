# 01 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte
# quantas vezes aparece as vogais a,e,i,o,u

frase = str(input('Digite uma frase:\n')).strip()
lista = [a,e,i,o,u]
for i in frase:
    if i == lista:
        print(i)
