class Avatar:
    def __init__(self, user, mana):
        self.nome = user
        self.energia = mana
        self.dinheiro = 100

    def alimenta(self):
        self.dinheiro -= 10

    def move_direita(self):
        print("Move direita...")
    
    def move_esquerda(self):
        print("Move esquerda...")
