import turtle as t

def desenha_quadrado(x):
    '''Desenha quadrado de lado x'''
    n = 4
    while n>0:
        t.forward(x)
        t.left(90)
        n-=1

def desenha_pentagono(x):
    '''Desenha pentagono de lado x'''
    n = 5
    while n>0:
        t.forward(x)
        t.left(90)
        n-=1
        
def desenha_pol(x, n=999, rotate = 0,cor = 'black'):
    '''Desenha poligonos regulares de lado x e quantidade de lados a
       Caso número de lados não seja especificado, retornará um circulo
       Caso queira que ele esteja virado para baixo, use True em mirror e caso queira para cima mantenha False
       em cor escolhe uma cor para o polígono, por padrão é preto'''
    angle = 180 - (((n-2)*180)/n)
    t.left(rotate)
    t.color(cor)
    t.speed('fastest')
    
    if n == 999:
        t.circle(x)
        
    elif n>2:
        while n>0:
            t.forward(x)
            t.right(angle)
            n-=1
        
    else:
        print(f'não existe polígono de {n} lados!')




def desenhos(x,qt,n=999):
    '''Função para criar figuras a partir de poligonos regulares de n lados de valor x
       qt se refere a quantidade de giros de qt graus a serem feitos'''
    quant = 360/qt
    while quant>0:
        desenha_pol(x,n,qt)
        quant-=1
    
def arvore(n):
    i = 1
    n1 = n
    if n <= 1:
        print('não existe arvore assim')
    else: 
        while i<=n:
            print(' '*(n1-1)+'* '*i)
            i+=1
            n1-=1
            print(" "*(n-2) + '||')

def desenha_pontos(n):
    t.up()
    i=1
    while i<=n:
        j = 1
        while j<=1:
            t.goto(15*i,15*j)
            t.dot()
            j = j + 1
        i = i + 1

def fibonacci(n):
    i = n
    a = 0
    b = 1
    while i>0:
        print(a)
        print(b)
        a = b
        b = a+b
        i-=1
    
