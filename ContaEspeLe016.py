from ContaLe014 import Conta,Cliente

class ContaEspecial(Conta):
    def __init__(self,cliente,numero,saldo = 0,limite=0):
        Conta.__init__(self,cliente,numero,saldo)
        self.limite = limite

    ##Sobreescrita do método saque (polimorfismo)

    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque",valor])

def principal():
    cliente1 = Cliente("João", "(21)98765421")
    #cliente.imprime()
    maria = Cliente("Maria da Silva", "(21)985206321")
    c2 = ContaEspecial(maria, 2,500,1000)
    c2.deposito(300)
    c2.saque(1500)
    
if __name__ == "__main__":
    principal()
    
##ajustar dps
