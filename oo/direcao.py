class Direcao:
    direcao_atual = 0
    valor = 'Norte'
    direcoes = ['Norte', 'Leste', 'Sul', 'Oeste']

    def girar_a_direita(self):
        if self.direcao_atual == 3:
            self.direcao_atual = 0
        else:
            self.direcao_atual += 1

        self.valor = self.direcoes[self.direcao_atual]

    def girar_a_esquerda(self):
        if self.direcao_atual == 0:
            self.direcao_atual = 3
        else:
            self.direcao_atual -= 1

        self.valor = self.direcoes[self.direcao_atual]

