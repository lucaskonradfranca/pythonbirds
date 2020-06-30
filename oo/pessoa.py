class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=28):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodoEstatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return None


class Homem(Pessoa):
    pass

if __name__ == '__main__':
    filho = Pessoa(nome='Filho')
    lucas = Pessoa(filhos=filho, nome='Lucas')
    print(Pessoa.cumprimentar(lucas))
    print(id(lucas))
    print(lucas.cumprimentar())
    print(lucas.nome)

