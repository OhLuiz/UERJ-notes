#Heranças simples: herda a caracteristica de apenas uma superclasse
#herança compostoa: herda a característica de mais de uma superclasse

#super() é usado entre heranças de classes, ele nos proporciona extender/subscrever métodos de uma superclasse(classe pai)

class Retangulo():
    def __init__(self, ladoA, ladoB):
        self.__ladoA = ladoA
        self.__ladoB = ladoB

    def area(self):
        return self.__ladoA*self.__ladoB

    def perimetro(self):
        return 2*self.__ladoA+2*self.__ladoB

##    @property
##    def ladoA(self):
##        print("Get lado A")
##        return self.__ladoA
##    def ladoB(self):
##        print("Get lado B")
##        return self.__ladoB
##    
##    @ladoA.setter
##    def ladoA(self,value):
##        print("Set lado A")
##        self.__ladoA = value
##        
##    @ladoB.setter
##    def ladoB(self,value):
##        print("Set lado B")
##        self.__ladoB = value
##        
##    @ladoA.deleter
##    def ladoA(self):
##        del self.__ladoA
##        
##    @ladoB.deleter 
##    def ladoB(self):
##        del self.__ladoB
        
class Quadrado(Retangulo): ##colocamos a herança no espaços entre os parentesis
    def __init__(self,lado):
        super(Quadrado,self).__init__(lado,lado) #podemos fazer isso desde que as variáveis da classe pai sejam  públicos
        
