
class Conta():
    def __init__(self, id, nome, saldo):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def creditar(self, valor):
        self.saldo += valor
    
    def debitar(self, valor):
        self.saldo -= valor

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Saldo: {self.saldo}"
    