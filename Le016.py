class Base:
    def __init__(self):
        print("Base.__init__")

class A(Base):
    def __init__(self):
        super().__init__()
        print('A__init__')

class B(Base):
    def __init__(self):
        super().__init__()
        print('B__init__')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C__init__')

class Tempo():
    '''Classe tempo com propriedades de leitura/escrita'''
    def __init__(self,hora = 0,minuto = 0,segundo = 0):
        '''inicializa cada atributo(falta validar a hora)'''
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

##    def horas(self):
##        print(f"{self.__hora}:{self.__minuto}:{self.__segundo}")
##    def __str__(self):
##        '''Método especial para retornar uma representação de string de um objeto'''
##        return '%.2d:%.2d:%.2d'%(self.__hora,self.__minuto,self.__segundo)
    @property
    def hora(self):
        '''Retorna o atributo hora'''
        return self.__hora
    @hora.setter
    def hora(self,hora):
        '''Modifica o atributo hora'''
        if not(0<=hora<24):
            print(f"Hora {hora} deve estar entre 0 e 23")
        else:
            self.__hora = hora
    @property
    def minuto(self):
        '''Retorna o atributo minuto'''
        return self.__minuto
    @minuto.setter
    def minuto(self,minuto):
        '''Modifica o atributo minuto'''
        if not(0<=minuto<59):
            print(f"Minuto {minuto} deve estar entre 0 e 59")
        else:
            self.__minuto = minuto
    @property
    def segundo(self):
        '''Retorna o atributo segundo'''
        return self.__segundo
    @segundo.setter
    def segundo(self,segundo):
        '''Modifica o atributo segundo'''
        if not(0<=segundo<59):
            print(f"Segundo {segundo} deve estar entre 0 e 59")
        else:
            self.__segundo = segundo


##função __str__(self)

class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x},{self.y})'
        


