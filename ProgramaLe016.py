class Programa:
    def __init__(self,nome,ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0
        
    def dar_like(self):
        self.__likes+=1

    def __str__(self):
        return f'{self.__nome} de {self.ano} - {self.__likes} likes'
    @property
    def nome(self):
        return self.__name
    @nome.setter
    def nome(self,nome):
        self.__nome = nome.title()
    @property
    def likes(self):
        return self.__likes

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return super().__str__() + f' - duração - {self.duracao} minutos'

