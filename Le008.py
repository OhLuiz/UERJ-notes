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
        nome = notas[i][0]
        media = round((notas[i][1]+notas[i][2]+notas[i][3])/3,1)
        elemento = (nome,media)
        resultado += (elemento,)
        i+=1
    return resultado

def gera_relatorio(notas):
    '''Recebe uma tupla de notas e imprime o nome dos alunos com a maior média, menor media e o número de alunos reprovados'''
    medias = calcula_media_aluno(notas)
    minimo = medias[0][1]
    maximo = medias[0][1]
    alunoMax = medias[0][0]
    alunoMin = medias[0][0]
    reprovados = 0
    i = 1
    while  i< len(medias):
        if medias[i][1]<minimo:
            minimo = medias[i][1]
            alunoMin = medias[i][0]
        if medias[i][1]>maximo:
            maximo = medias[i][1]
            alunoMax = medias[i][0]
        if medias[i][1] < 5:
            reprovados +=1
        i+=1
        
    #imprime relatório
    print('Menor média: ',minimo, 'Aluno:  ', alunoMin)
    print('Maior média: ',maximo, 'Aluno:  ', alunoMax)
    print('Reprovados: ', reprovados)
    
from random import randint

def jogo_de_dados():
    i = 0
    lista = ''
    while True:
        n1 = randint(1,6)
        n2 = randint(1,6)
        print(f'O dado um deu {n1}')
        print(f'O dado dois deu {n2}')
        print('-='*40)
        i+=1
        if f'{n1},{n2}'in lista or f'{n2},{n1}' in lista:
            break
        lista += f'{n1},{n2} '

    print(f'Foram necessárias {i} jogadas para a combinação de valores se repetir')

################################################################################################################for
##frutas = ['maçã', 'banana', 'laranja']
##for fruta in frutas:
##    print(fruta)

###equivale a:
##i = 0
##while  i < len(frutas):
##    print(frutas[i])
##    i+=1

def calcular_media(lista):
    '''
    Calcula a média dos valores em uma lista usando comandor for
    list -> float
    '''
    soma = 0
    for valor in lista:
        soma +=valor
    return soma/len(lista)
def contar_vogais(texto):
    '''
    Conta o número de vogais de uma string
    str -> int
    '''
    total = 0
    for letra in texto:
        if letra in 'aeiouAEIOU':
            total+=1
    return total


