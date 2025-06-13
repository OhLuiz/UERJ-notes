##---------------------------------LISTA-------------------------
##--------------------------------QUESTÃO 6 ---------------------
def sequencia_biologica(dna):
    tamanho = len(dna)
    leucinas, posGG, posRR = 0,0,0
    nDNA = ''
    ##usar comandos de lista como count ou find para fazer essas questões
    for c in range(100):
        nDNA += dna[c]

##---------------------------AULA----------------------------------
##Faça uma função insere(lista,n) que dada uma lista ordenada(crescente) de números e um numero n,
##inclua n na posição corret, ou seja, de tal maneira que a lista continua ordenada.
def maior_que(lista,n):
    lista2= []
    for c in lista:
        if c>n:
            lista2.append(c)
    return lista2

def insere(lista,n): #não necessariamente percorre a lista toda
    i = 0
    while i<len(lista) and lista[i] < n:
        i+=1
    lista.insert(i,n)
    return lista

def insere_V2(lista,n): ##percore a lista 2x
    maiores = maior_que(lista,n)
    menores = []
    
    for c in lista:
        if c not in maiores:
            menores.append(c)
            
    lista = menores
    lista.append(n)
    lista += maiores
    
    return lista

def insere_V3(lista,n): #percorre a lista diversas vezes
    lista.append(x) # insere x no final
    lista.sort() #ordena

##Faça uma função que dada uma frase. retorne o número de palavras da frase. Considere que a frase pode ter espaços
##no inicio e no final e que as palavras são separadas por um único espaço

def conta_palavras(frase):
    frase = frase.strip()
    return frase.count(" ")+1


def conta_palavras_V2(frase):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nome1, palavras,ct = "", [], 0
    for c in frase:
        if c != " ":
            nome1+=c
        else:
            ct+=1
            nome = ""
    if frase[len(frase) - 1] != " ":
        ct+=1
    return len(palavras)
            

def conta_palavras_V3(frase):
    i = 0
    while frase[i] == " ":
        i+=1
    j = len(frase)-1
    while frase[j] == ' ':
        j-=1

    espacos = 0
    for k in range(i, j-1):
        if frase[k]== ' ':
            espacos += 1
            
    return espacos + 1

##Dado um texto armazenado em uma string, faça uma função que conte o número de frases que aparecerem nesse texto.
##Cada frase no texto é terminada com ponto final, um ponto de exclamação, um ponto de interrogação ou três pontos
##em sequência Pontos de exclamação ou de interrogação não aparecerão repetidos em sequência no texto e esses
##simbolos só aparecem no texto terminando uma frase. No exemplo a seguir, são contadas 4 frases:
## "Preciso tirar um cochilho. Meu Deus! Que horas são?



##Crie uma função que simule o lançamento de um dado n = 1000 vezes e retorna um dicionário contendo a face
##do lado e a frequência obtida nos lançamentos


afinidades = {'Leo':['Sofia','Andrea'],
              "Marcos":['Andrea'],
              'Sofia':['Leo'],
              'Alex':['Andrea','Marcos'],
              'Andrea':['Marcos']}

def quem_curtiu(afinidades,fulano):
    '''Recebe um dicionário e o nome de uma pessoa e retorna uma lista com o nome das pessoas que curtiram ele
        dict,st -> list'''
    pessoas = []
    for m in afinidades.keys():
        for n in afinidades[str(m)]:
            if n == fulano:
                pessoas.append(m)
    return pessoas

def deu_match(afinidades,nome1,nome2):
    '''Recebe um dicionário e o nome de duas pessoas e retorna
    True se nome1 curtiu nome2 e vice-versa
    dict, str, str -> bool'''
    SoN = False
    for n in afinidades[nome1]:
        for m in afinidades[nome2]:
            if m == nome1:
                SoN = True
    return SoN
