##Continuando Classes
##class para definir a classe
##__init__() é utilizado para inicializar objetos das classe; é chamado automaticamente quando um novo objeto da classe é criado
##self utilizado para nos referirmos ao objeto que acabou de ser criado
##Recomendação criar um arquivo com o nome da classe

class Pessoa:
    ##Basicamente o init serve para dar os parametros iniciais e a partir dai, podemos usar funções que vão usar
    ##os parametros inseridos aqui sem colocar nenhum parametro de entrada nas outras.
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    ##Outros métodos    
    def imprime(self):
        print(f"Nome:{self.nome}, idade: {self.idade}")
        
    def aniversariar(self):
        self.idade+=1

    def maioridade(self):
        if self.idade < 18:
            return print(f"Faltam {18 - self.idade} anos para você se alistar!!")
        else:
            return print("Você já se alistou?")
                                                    
        
#criando instancias de pessoa
        
p1 = Pessoa("João", 25)
p2 = Pessoa("Maria", 25)

