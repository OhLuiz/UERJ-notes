from math import pi

class Circulo:
    #Encapsulamento, usando atributos privados protege os dados dentro das classes, arquivos que não podem ser modificados
    #como saldo de conta bancária, CPF e dados imutáveis.
    def __init__(self,raio):
        self.__raio = raio #atributo privado raio

    #outros métodos
    def area(self):
        return float(f"{pi*self.__raio**2:.2f}")

    # métodos de acesso (gettera - receber a infromação(get) e settera - trocar uam informação(setar))
    def getRaio(self):
        '''Permite retornar o valor de atributo raio, usa prefixo get'''
        return self.__raio
    def setRaio(self,raio):
        '''Permite alterar o valor de um atributo(raio), usa prefixo set'''
        self.__raio = raio

    #podemos fazer "configurar" os valores como se fosse uma "função", mas sem parentesis, como se fosse uma variável

    @property
    def raio(self):
        print("Get raio")
        return self.__raio
    
    @raio.setter
    def raio(self,value):
        print("Set raio")
        self.__raio = value

    @raio.deleter
    def raio(self):
        print("Delete raio")
        del self.__raio
###Teste
##c = Circulo(10)
##print("Area:",c.area())
####print("Retorna raio", c.__raio) #dá erro, atributo privado
##print("Retorna raio", c.getRaio()) #forma certa de acessar atributo privado
##c.setRaio(7)
##print("Retorna raio", c.getRaio()) #forma certa de acessar atributo privado

