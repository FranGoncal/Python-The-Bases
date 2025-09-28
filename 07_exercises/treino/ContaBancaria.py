class ContaBancaria:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def levantar(self, valor):
        if (valor <= 0):
            raise ValueError("Montante de "+ str(valor) + " não pode ser levantado.")

        if (not self.saldoSuficiente(valor)):
            raise ValueError("Saldo insuficiente!")
        self.saldo -= valor
        print("Levantou "+ str(valor) +" euros da sua conta.")

    def saldoSuficiente(self, valor):
        return self.saldo >= valor
    
    def extrato(self):
        print("Extrato de " + self.titular)
        print("Saldo: " + str(self.saldo))

conta1 = ContaBancaria("Maria", 33)
conta2 = ContaBancaria("Jorge", 38)

conta1.extrato()
conta2.extrato()


conta1.depositar(22)
conta1.extrato()

conta1.levantar(1)
conta1.extrato()

conta1.levantar(54)
conta1.extrato()



conta2.depositar(1)
conta2.levantar(2)
conta2.extrato()