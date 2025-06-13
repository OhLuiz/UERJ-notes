class Inteiro():
    def __init__(self,entrada):
        self.__valor = entrada

    @property
    def valor(self):
        return self.__valor

    def __add__(self,outros):
        return self.valor + outro.valor

class Fracao():
    def __init__(self,numerador,denominador):
        self.n = numerador
        self.d = denominador
    def __str__(self):
        return f'{self.n}/{self.d}'
    def __mul__(self,outro):
        n = self.n*outro.n
        d = self.d*outro.d
        return Fracao(n, d)
    ##aprender os métodos
