##TERMINAR
import pickle

##criamos um objeto
L  = [1,2,3,4]

#usar o método dumps para serializar
serializado = pickle.dumps(L)
print(serializado)

#usamos o método loads para deserializar
deserializado = pickle.loads(serializado)
print(deserializado)

class Cliente:
    def __init__(self,nome,telefone):
        self.__nome = nome
        self.__tel = telefone
    def __str__(self):
        return f'Nome: {self.__nome}, telefone:{self.__tel}'

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome_set(self,nome):
        self.__nome = nome
        
    @property
    def telefone(self):
        return self.__tel
    @nome.setter
    def telefone_set(self,telefone):
        self.__tel = telefone

class Lista:
    def __init__(self):
        self.__lista = []
    def inserir(self,nome,telefone):
        self.__lista.append((nome,telefone))
    @property
    def lista(self):
        return self.__lista
        
class Persistencia:
    @staticmethod
    def lerArquivo(nomeArquivo):
        '''Carrega um arquivo e retorna um objeto cliente'''
        lista = Lista()
        with open("lista.pkl", "wb") as arquivo:
            piclkle.dump(nomeArquivo, arquivo)
        
        with open("lista.pkl", "rb") as arquivo: 
            dados = pickle.load(arquivo)
            for cliente in dados:
                cliente = Cliente(nome,telefone)
                lista.inserir(cliente)

            
        return lista
    @staticmethod
    def gravarArquivo(lista,nomeArquivo):
        '''Salva os dados do objeto agenda em um arquivo'''
        with open(nomeArquivo, 'wb') as arquivo:
            for c in lista:
                pickle.dump(c)

c1 = Cliente('João da Silva', 28)
c2 = Cliente("Maria Santos", 34)
L = [c1,c2]
with open("clientes.pkl", 'wb') as arquivo:
    pickle.dump(L,arquivo)
with open("clientes.pkl", 'rb') as arquivo:
    dados = pickle.load(arquivo)
    for cliente in dados:
        print(cliente)
