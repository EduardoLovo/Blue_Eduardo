# a. Crie uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i. tipoCombustivel.
# ii. valorLitro.
# iii. quantidadeCombustivel.
# b. A classe deve possuir no mínimo esses métodos:
# i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que
# foi colocada no veículo.
# ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor
# a ser pago pelo cliente.
# iii. alterarValor( ) – altera o valor do litro do combustível.
# iv. alterarCombustivel( ) – altera o tipo do combustível.
# v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class bombaCombustivel():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self):
        self.valor = int(input('Qual valor deseja abastecer? '))
        total = self.valor * self.quantidadeCombustivel
        print(f'foi abastecido {total} de litros')

    def abastecerPorLitro(self):
        self.valorL = int(input('Quantos litros deseja abastecer? '))


    def alterarValor(self):
        self.gasolina = gasolina
        self.etanol = 3

    def alterarCombustivel(self):
        self.gasolina = gasolina
        self.etanol = etanol

    def alterarQuantidadeCombustive(self):
        self.quantidadeCombus = 1

gasolina = 5
etanol = 3
modo = input('deseja abastecer por litro ou por valor?')
if modo == 'litro':
    bombaCombustivel.abastecerPorLitro
    abastecer = int(input('quantos litros deseja abastecer?'))



carro1 = bombaCombustivel('gasolina',gasolina,modo)