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
        self.valor = float(input('Qual valor deseja abastecer? '))


    def abastecerPorLitro(self):
        self.valorL = float(input('Quantos litros deseja abastecer? '))

    def alterarValor(self):
        selfvalorGasolina = 
        selfvalorEtanol = 

    def alterarCombustivel(self):
        gasolina = 
        etanol = 

    def alterarQuantidadeCombustive():
        quantidadeCombus = 


BombaGasolina = bombaCombustivel