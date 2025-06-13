##listas e tuplas
#tupla = ()//imutavel
#lista = []//mutavel
#para ter uma tupla unitária, é necessário colocar o valor antecedido a uma virgula
#zip(tupla1,tupla2) faz quase um dicionário com a combinação de cada elemento respectivo de uma tupla
#podemos usar a tupla como se fossem strings, usando [] ṕara operá-las

## ------------------------ Aula -------------------------------
def cria_tupla_numérica(n=10):
    '''Retorna uma tupla numéria com n elementos, todas digitadas pelo usuário'''
    f = 0
    tupla = ()
    while f < n:
        number = int(input(f"Digite o valor {f+1} da tupla:"))
        tupla += (number,)
        f+=1
    return tupla

def imprime_tupla(tupla):
    '''Imprime uma tupla sem o parenteses'''
    i = 0
    while i< len(tupla):
        if i == (len(tupla)-1):
            print(tupla[i])
        else:
            print(tupla[i],end=',')
        i+=1
    
def tuplas_pares(n=10):
    '''De uma tupla de entrada retira todos seus números pares e imprime uma outra tupla apenas com esse números pares'''
    f,i = 0,0
    tupla = ()
    while f < n:
        number = int(input(f"Digite o valor {f+1} da tupla:"))
        tupla += (number,)
        f+=1
    tupla_par = ()
    while i < len(tupla):
        if tupla[i] % 2 == 0:
            tupla_par += (tupla[i],) ##Só pode concatenar com objetos de mesma classe, logo transformamos a int em tupla
        i += 1
    return imprime_tupla(tupla_par)


def soma(n):
    '''Retorna a soma dos elementos de uma tupla de números'''
    tupla = cria_tupla(n)
    i,soma = 0,0
    while i<n:
        soma += tupla[i]
        i+=1
    return soma

def minimo(t):
    '''Retorna o menor valor da tupla de números'''
    tupla = cria_tupla(t)
    i,menor = 0,tupla[0]
    while i<t:
        if tupla[i]<menor:
            menor = tupla[i]
        i+=1
    return menor

def media(t): 
    '''Retorna a média dos valores da tupla de números'''
    media = soma(t)/t
    return media

def existe(t,x):
    '''Retorna True se o elemento x existe na tupla t e false caso contrario'''
    i = 0
    while i<len(t):
        if x==t[i]:
            return True
        i+=1
    return False

def minimo_v2(tupla):
    '''Retorna o valor e a poisção do menor elemento de uma tupla de números'''
    i,pos,menor = 0,0,tupla[0]
    while i<len(tupla):
        if tupla[i]<menor:
            menor = tupla[i]
            pos = i
        i+=1
    return print(f'O menor valor é de {menor} e está na posição {pos+1}')

##Essas funções não funcionariam se fosse uma tupla de tuplas

def media_pares_impares(t):
    '''Retorna uma tupla com os valores de média dos números pares e dos números impares da tupla, respectivamente'''
    i,countp,counti = 0,0,0
    mediap,mediai = 0,0
    while i<len(t):
        if t[i]%2 == 0:
            countp+=1
            mediap+=t[i]
        else:
            counti+=1
            mediai+=t[i]
        i+=1
    return (mediap/countp,mediai/counti)

notas = (('João da Silva', 8.5, 9, 6),
        ('Eduardo Cunha', 4.8, 7.2, 5),
        ('Maria Campos', 6.9, 9.4, 8.1),
        ('Cartlos Botello', 4.5, 6.1, 3.9),
        ('Emily Lima', 7.9, 9.5, 7.3),
        ('Ana Clara', 6.8, 7.5, 4.9),)

def calcula_media_aluno(notas):
    '''Retorna uma tupla de tuplas contendo o nome de aluno e média das notas'''
    resultado = ()
    i = 0
    while i<len(notas):
        nome = notas[1][0]
        media = round((notas[1][1]+notas[1][2]+notas[1][3])/3,1)
        elemento = (nome,media)
        resultado += elemento
        i+=1
    return resultado

def gera_relatorio(notas):
    '''Recebe uma tupla de notas e imprime o nome dos alunos com a maior média, menor media e o número de alunos reprovados'''
    
