class Conta:
    def __init__(self,cliente,numero,saldo = 0):
        self.saldo = 0
        self.__cliente = cliente
        self.__numero = numero
        self.operacoes = []
        if saldo != 0:
            self.deposito(saldo)
        
    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(['    Saque',valor])
        else:
            print("Saldo em conta insuficiente para saque")
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append([' Depósito', valor])
        
    def extrato(self):
        print(f'Extrato conta n° {self.__numero}: ')
        if len(self.operacoes) == 0:
            print("Nenhuma operação registrada")
        else:
            for op in self.operacoes:
                print(f"{op[0]}     R${op[1]:.2f}")
            print(f"Saldo:   {self.saldo}")
    @property
    def saldo(self):
        print("Get saldo")
        return self.saldo
    def conta(self):
        print("Get conta")
        return self.__numero
    def cliente(self):
        print("Get cliente")
        return self.__cliente
            
class Cliente:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone
    def imprime(self):
        print("---Cliente---")
        print("Nome:", self,nome)
        print('telefone', self.telefone)

class Elevador:
    def __init__(self,andar,total_andar,capacidade):
        self.andarat = andar
        self.andartotal = total_andar
        self.capacidade = capacidade
        self.pessoas = 0
    def entrar(self):
        if self.pessoas == self.capacidade:
            print("Elevador com capacidade máxima")
        else:
            self.pessoas+=1
    def sair(self):
        if self.pessoas == 0:
            print("Elevador vazio")
        else:
            self.pessoas -=1
    def sobe(self):
        if self.andarat == self.andartotal:
            print("Elevador no último andar")
        else:
            self.andarat+=1
    def desce(self):
        if self.andarat == 0:
            print("Elevador no térreo")
        else:
            self.andarat-=1
    def imprime(self):
        print(f"N° de pessoas: {self.pessoas}"
              f"\nAndar atual: {self.andarat}")
class Moto:
    def __init__(self,marca,modelo,cor,menormarcha,maiormarcha,ligada = False):
        self.marca = marca
        self.modelo = modelo
        self.marcha = 0
        self.maiormarcha = maiormarcha
        self.menormarcha = menormarcha
        self.ligada = ligada
    def marcha_acima(self):
        if self.marcha < self.maiormarcha:
            self.marcha+=1
        else:
            print("Marcha máxima alcançada")
    def marcha_abaixo(self):
        if self.marcha > self.menormarcha:
            self.marcha-=1
        else:
            print("Marcha mínima alcançada")
    def ligar(self):
        if self.ligada == True:
            pass
        else:
            self.ligada = True
    def desligar(self):
        if self.ligada == False:
            pass
        else:
            self.ligada = False
    def imprime(self):
        print(f"Marcha atual: {self.marcha}"
              f"\nSituação atual: {self.ligada}")

    
def main():
    elevador = Elevador(0,15,15)
    elevador.sair()
    for c in range(16):
        elevador.entrar()
    elevador.desce()
    for c in range(16):
        elevador.sobe()
    elevador.desce()
    for c in range(5):
        elevador.sair()
    elevador.imprime()

def main2():
    moto = Moto('Honda','M45',"Azul",0,5)
    moto.marcha_acima()
    for c in range(3):
        moto.marcha_acima()
    moto.marcha_abaixo()
    moto.ligar()
    moto.desligar()
    moto.ligar()
    moto.imprime()
    
