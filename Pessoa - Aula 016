class Pessoa:
    def __init__(self,nome,cpf,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.respirar = 0
        
    def __str__():
        return f'Pessoa: {self.nome}\nCPF: {self.cpf}\nTel.: {self.telefone}\nRespiradas: {self.respirar}'
    def respirar(self):
        self.respirar+=1
        
    @property
    def nome(self):
        print(f'self.__name')
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def cpf(self):
        print(f'self.__cpf')
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        print(f'self.__telefone')
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone


class Aluno(Pessoa):
    def __init__(self,aluno,cpf,telefone,matricula,CR):
        super().__init__(self,aluno,cpf,telefone)
        self.__matricula = matricula
        self.__CR = CR
        self.__aula = 0
    def __str__(self):
        return f'Aluno: {self.nome}\nCPF: {self.cpf}\nTel.: {self.telefone}\nMatrícula:{self.__matricula}\nCR:{self.__CR}\nAulas assistidas: {self.__aulas}\n'
    def assistirAula(self):
        self.aula+=1
        
    @property
    def matricula(self):
        print(f'self.__matricula')
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula = matricula

    @property
    def CR(self):
        print(f'self.__CR')
    @CR.setter
    def CR(self,CR):
        self.__CR = CR


   
