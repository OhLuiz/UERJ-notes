class Contato:
    def __init__(self,nome,telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}'

class Agenda:
    def __init__(self):
        '''Cria uma lista de contatos'''
        self.contatos = []

    def inserir(self,contato):
        '''Adiciona um contato novo à agenda'''
        self.contatos.append(contato)
    def pesquisar(self,nome):
        '''Pesquisa um contato por nome e retorna a posição'''
        nome = nome.lower()
        for indice,contato in enumerate(self.contatos):
            if contato.nome.lower() == nome:
                return indice
        return None
    def listar(self):
        '''Lista os contatos existentes na agenda'''
        print("------Agenda------")
        for pos,contato in enumerate(self.contatos):
            print(f'{pos+1}.{contato}')
            
    def apagar(self,nome):
        '''Apaga um contato da agenda'''
        p = self.pesquisar(nome)
        if p!=None:
            del self.contatos[p]
        else:
            print('Contato não encontrado.')

    def alterar(self,nome):
        '''Altera um contato da agenda'''
        p = self.pesquisar(nome)
        if p!=None:
            print("Encontrado: ")

            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            contato = Contato(nome,telefone)
            self.contatos[p] = contato
        else:
            print("Nome não encontrado.")

##enumerate associa um número à cada atributo da lista, criando uma lista de tuplas

class Persistencia:
    @staticmethod##define que é um método estático
    def lerArquivo(nomeArquivo):
        '''Carrega um arquivo e retorna um objeto agenda'''
        arquivo = open(nomeArquivo,'r',encoding='utf-8')
        agenda = Agenda()
        for l in arquivo.readlines():
            nome,telefone = l.strip().split("#")
            contato = Contato(nome,telefone)
            agenda.inserir(contato)
        arquivo.close()

        return agenda
    @staticmethod
    def gravarArquivo(agenda,nomeArquivo):
        '''Salva os dados do objeto agenda em um arquivo'''
        arquivo = open(nomeArquivo,'w',encoding='utf-8')
        for contato in agenda.contatos:
            arquivo.write(f"{contato.nome}#{contato.telefone}\n")
        arquivo.close()

def numero_valido(tel):
    tamanhos = [8,9,10,11]
    if type(tel) == int:
        telefone = str(tel)
        if len(telefone) in tamanhos:
            return True
        else:
            return False
    else:
        return False
    
def nome_sem_especial(nome):
    nome2 = ''
    especial = "1234567890!@#$%¨&*()_+=-{}[]?/\|°ºª§¬¢£³²¹"
    for c in nome:
        if c not in especial:
            nome2+=c
    return nome2
        
def menu():
    print("""============= Agenda ==============
    1 - Novo contato
    2 - Alterar contato
    3 - Apagar contato
    4 - Listar contato
    5 - Gravar agenda
    6 - Ler agenda
    7 - Tamanho da agenda
    8 - Sair
    """)

if __name__ == '__main__':
    agenda = Agenda()

    while True:
        menu()
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            nome = nome_sem_especial(input("Nome: "))
            telefone = input("Telefone: ")
            while not numero_valido(telefone):
                print("Digite o número de telefone apenas com números e\ou o número correto")
                telefone = input("Telefone: ")
            c = Contato(nome, telefone)
            agenda.inserir(c)
        elif opcao == 2:
            nome = input("Nome: ")
            agenda.alterar(nome)
        elif opcao == 3:
            nome = input("Nome: ")
            agenda.apagar(nome)
        elif opcao == 4:
            agenda.listar()
        elif opcao == 5:
            nome = input("Nome arquivo: ")
            Persistencia.gravarArquivo(agenda,nome)
        elif opcao == 6:
            nome = input("Nome arquivo: ")
            agenda = Persistencia.lerArquivo(nome)
        ##Pergunta 1
        elif opcao == 7:
            nome = input("Nome arquivo: ")
            ct = 0
            agenda = Persistencia.lerArquivo(nome)
            for contato in agenda.contatos:
                ct+=1
            print(f"A agenda tem {ct} contatos")
        elif opcao == 8:
            break
        else:
            print("Opção inválida")

##PONTO EXTRA RESPONDENDO ITEM POR ITEM
