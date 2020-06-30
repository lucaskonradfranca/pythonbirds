class Motor:
    velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade = max(0, self.velocidade - 2)

