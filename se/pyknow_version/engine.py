from pyknow import Fact, Field, KnowledgeEngine, Rule, W, AS, NOT, EXISTS, P

from se.utils.helpers import pyread_float


class Torre(Fact):
    operacao = Field(str, mandatory=True)


class Data(Fact):
    ph = Field(float, mandatory=False)
    vazao_produto = Field(float, mandatory=False)
    vazao_agua_lavagem = Field(float, mandatory=False)
    injecao_neutralizante = Field(float, mandatory=False)


class ESEngine(KnowledgeEngine):

    @Rule(~Data(vazao_produto=W()))
    def read_vazao_produto(self):
        self.declare(Data(vazao_produto=pyread_float('Digite a Vazão do Produto: ')))

    @Rule(~Data(ph=W()),
          AS.data << Data())
    def read_ph(self, data):
        self.modify(data, ph=pyread_float('Digite o PH: '))

    @Rule(~Data(vazao_agua_lavagem=W()),
          AS.data << Data())
    def read_vazao_agua_lavagem(self, data):
        self.modify(data, vazao_agua_lavagem=pyread_float('Digite a Vazão Água Lavagem: '))

    @Rule(~Data(injecao_neutralizante=W()),
          AS.data << Data())
    def read_injecao_neutralizante(self, data):
        self.modify(data, injecao_neutralizante=pyread_float('Digite a Injeção de Neutralizante: '))

    @Rule(Data(vazao_produto=P(lambda x: x > 0)))
    def is_operating(self):
        self.declare(Torre(operacao='operando'))

    @Rule(
        Torre(operacao='operando'),
        Data(ph=5.9)
    )
    def normal_state(self):
        print('Corrosão sob controle na torre')

    @Rule(
        Torre(operacao='operando'),
        Data(ph=5.0, vazao_agua_lavagem=P(lambda x: x < 130 * 1.1 and x < 115))
    )
    def increase_vazao_lavagem(self):
        print('Risco elevado de corrosão na torre')
        print(f'Ajustar a vazão de água de lavagem para > {130 * 0.9}')

    @Rule(
        Torre(operacao='operando'),
        Data(ph=5.0, vazao_agua_lavagem=P(lambda x: 130 * 1.1 > x > 130 * 0.9))
    )
    def increase_increase_neutralizante(self):
        print('Risco elevado de corrosão na torre')
        print(f'Aumentar a injeção de neutralizante em 10%')
