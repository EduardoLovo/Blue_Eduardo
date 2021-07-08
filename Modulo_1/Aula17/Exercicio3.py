# Desafio 3 - Crie uma classe que modele uma pessoa:
# a) Atributos: nome, idade, peso e altura.
# b) Métodos: envelhecer, engordar, emagrecer, crescer.
# Por padrão, a cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm

class pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, qenv):
        a = self.idade + qenv
        print(a)

    def engordar(self):
        print('engordou')

    def emagrecer(self):
        print('Emagreci')

    def crescer(self):
        self.idade = int(self.idade)
        if self.idade <= 21:
            c = self.altura + (0.05 * b)
            print(f'{c:.2f}')

pessoa1 = pessoa('Eduardo', 18, '76kg', 1.61)
b = int(input('quantos anos envelheceu: '))
pessoa1.envelhecer(b)
pessoa1.crescer()


