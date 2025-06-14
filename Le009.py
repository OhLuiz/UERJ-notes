def par(num):
    '''
    Verifica se um número é par ou não
    int -> bool
    '''
    if num%2 == 0:
        return True
    else:
        return False
    
def encontrar_pares(lista):
    '''
    Encontra os números pares em uma lista.
    list -> list
    '''
    pares = []
    for c in lista:
        if par(c):
            pares.append(c)
    return pares

def encontrar_pares_while(lista):
    '''
    Encontra os números pares em uma lista usando while.
    list -> list
    '''
    pares = []
    i = 0
    while i<len(lista):
        if par(lista[i]):
            pares.append(lista[i])
        i+=1
    return pares

def remover_duplicatas(lista):
    '''
    Remove elementos duplicados de uma lista,
    list -> list
    '''
    resultado = []
    for valor in lista:
        if valor not in resultado:
            resultado.append(valor)
            
    return resultado

##range(inicio,fim,passo) conta o valor inicial, mas não conta o final

def encontrar_pares_range(lista):
    '''
    Encontra os números pares em uma lista usando range,
    list -> list
    '''
    pares = []
    for c in range(len(lista)):
        if par(lista[c]):
            pares.append(lista[c])

    return pares

def lista_esta_ordenada(lista):
    '''
    Verifica se uma lista está em ordem e caso contrário, retorna ela ordenada em ordem crescente
    list -> list
    '''
    a = True
    for c in range(len(lista)-1):
        if lista[c]<lista[c+1]:
            continue
        else:
            a = False
    if not a:
        for c in range(len(lista)):
            for i in range(len(lista)):
                if lista[c] < lista[i]:
                    lista[c],lista[i] = lista[i],lista[c]
    return lista

def contador(n):
    '''
    Faz uma contagem de 1 a 5000000 e toda vez que chegar em 1000000 imprime um número na tela
    importando a função time, podemos contar quanto tempo demora para ele contar até 5M
    '''
    import time
    tempoantes = time.time()
    for c in range(1,n+1):
        if c%1000000 == 0:
            print(c//1000000)
    tempodepois = time.time()
    print(f"O tempo que levou para fazer essa contagem foi de {tempodepois-tempoantes:.3f}ms")
    
import turtle as t
from random import randint
def desenha_pontos(n):
    '''Desenha um quadrado feito de pontos na tela'''
    cores = ('red','blue','yellow','green','purple')
    ch = randint(0,len(cores)-1)
    t.hideturtle()
    t.up()
    t.color(cores[ch])
    for i in range(n):
        for j in range(n):
            t.goto(i*10,y*10)
            t.dot()
            

def desenha_pontos_pos_al(n):
    '''Desenha n pontos coloridos de diferentes tamanhos em posições aleatórias'''
    cores = ('red','blue','yellow','green','purple')
    t.hideturtle()
    for c in range(n):
        t.up()
        ch = randint(0,len(cores)-1)
        t.color(cores[ch])
        t.goto(randint(-400,400),randint(-400,400))
        t.down()
        t.dot(randint(5,25))
        
def desenha_pontos_print(n):
    '''Desenha um quadrado de lado n na tela de asteristicos'''
    for i in range(n):
        for j in range(2*n):
            if (i+j)%2 == 1:
                print('*',end = '')
            else:
                print('   ',end = '')
        print('\n')

import math
def desenha_plano(n):
    '''Desenha o plano cartesiano'''
    t.up()
    t.goto(0,0)
    t.down()
    m = 0
    #desenha x+
    for i in range(n+1):
        m = i
        t.write(m)
        t.forward(100)
    #vá até a origem
    t.up()
    t.goto(0,0)
    t.down()
    #desenha x+
    for i in range(0,-n-1,-1):
        m = i
        t.write(m)
        t.backward(100)
    #vá até a origem
    t.up()
    t.goto(0,0)
    t.down()
    t.left(90)
    #desenha y+
    for i in range(n+1):
        m = i
        t.write(m)
        t.forward(100)
    #vá até a origem
    t.up()
    t.goto(0,0)
    t.down()
    #desenha y-
    for i in range(0,-n-1,-1):
        m = i
        t.write(m)
        t.backward(100)
   
def desenha_funcao(ch):
    '''Desenha uma função matemática'''
    t.clear()
    t.hideturtle()
    t.up()
    t.speed('fastest')
    t.color('black')
    y = 0
    desenha_plano(400)
    t.up()
    if ch == 1:
        for x in range(-400,400):
            y = math.sin(math.radians(x))*100
            t.goto(x,y)
            t.down()
    elif ch == 2:
        for x in range(400):
            y = x**(1/2)*100
            t.goto(x,y)
            t.down()
    elif ch == 3:
        for x in range(-400,400):
            y = x**(2)*100
            t.goto(x,y)
            t.down()
    elif ch == 4:
        desenha_circulo(1000,5000)


def gerarPontos():
    P = []
    Q = []
    #criamos duas listas de pontos
    for x in range(-200,215,15):
        P.append((x,50))
        Q.append((x,-50))

    return P,Q

def desenha_pontos():
    '''Desenha pontos de duas listas'''
    P,Q = gerarPontos()
    #desenha os pontos P e Q
    t.speed('fastest')
    t.up()
    t.hideturtle()
    t.color('blue')
    #Desenha P
    for ponto in P:
        t.goto(ponto)
        t.dot()
    #Desenha Q
    t.color('red')
    for ponto in Q:
        t.goto(ponto)
        t.dot()

def desenha_pontos_zip():
    '''Desenha pontos de duas listas com a função zip'''
    P,Q = gerarPontos()
    t.speed('fastest')
    t.up()
    t.hideturtle()
    #Desenha P e Q
    for p,q in zip(P,Q):
        t.color('blue')
        t.goto(p)
        t.dot()
        t.color('red')
        t.goto(q)
        t.dot()
        
def gera_pontos_circulo(r1,r2):
    for v in range(0,360,5):
        P.append((r1*math.cos(math.radius(v)),r1*math.sin(math.radius(v))))
        Q.append((r2*math.cos(math.radius(v)),r2*math.sin(math.radius(v))))
    return P,Q
def desenha_circulo(r1,r2):
    P,Q = gera_pontos_circulo(r1,r2)
    for p,q in zip(P,Q):
        t.color('blue')
        t.goto(p)
        t.dot()
        t.up()
        t.color('red')
        t.goto(q)
        t.dot()
        t.up()
        
def desenha_triangulo_inferiorD(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('blue')
    for x in range(n):
        for y in range(x):
            t.goto(x*10,y*10)
            t.dot()
def desenha_triangulo_superiorE(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('blue')
    for x in range(n):
        for y in range(x,n):
            t.goto(x*10,y*10)
            t.dot()
def desenha_triangulo_superiorD(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('blue')
    for x in range(n):
        for y in range(x,n):
            t.goto(x*10,y*10)
            t.dot()
def desenha_triangulo_inferiorE(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('blue')
    for y in range(n,0,-1):
        for x in range(0,n-y):
            t.goto(x*10,y*10)
            t.dot()
def desenha_funil(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('blue')
    for x in range(n):
        for y in range(x,n-x):
            t.goto(x*10,y*10)
            t.dot()
            
def desenha_algo(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('red')
    n2 = 2*n
    for x in range(n):
        for y in range(x,n-x):
            t.goto(x*10,y*10)
            t.dot()
    t.color('purple')
    for x in range(n2, n,-1):
        for y in range(x,n2-x,-1):
            t.goto((x-n)*10,(y-n)*10)
            t.dot()
    t.color('green')
    for y in range(n2, n,-1):
        for x in range(y,n2-y,-1):
            t.goto((x-n)*10,(y-n)*10)
            t.dot()
    t.color('blue')
    for y in range(n):
        for x in range(y,n-y):
            t.goto(x*10,y*10)
            t.dot()
    #terminar
            
def desenha_algoV2(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('red')
    n2 = 2*n
    for x in range(n):
        for y in range(n):
            if x > y and y < n - x:
                t.color('blue')
            else:
                t.color('red')
            t.goto(x*10,y*10)
            t.dot()

