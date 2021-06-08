class Account:
    def __init__(self,name,balance,min_balance):
        self.name = name
        self.balance = balance
        self_min = min_balance


    def depositar(self,amount):
        self.balance += amount #a data da esquerda é igual a ela mesma + a da direita

    def sacar(self,amount):
        if self.balance - amount >=self.min_balance:
            self.balance -= amount
        else:
            print("Fundos insuficientes.")

    def statement(self):
        print("Extrato: R${}".format(self.balance))

class Corrente(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = -1000)

    def __str__(self):
        return "Conta Corrente de {}: extrato R${}".format(self.name, self.balance)

class Investimento(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return "Conta de Investimento de {}: extrato R${}".format(self.name, self.balance)
