import turtle as t
from random import randint
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
    for y in range(n):
        for x in range(n,n-y,-1):
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
    for x in range(n):
        for y in range(n):
            if y > n-x and y > x:
                t.color('blue')
            elif y < n-x and y > x:
                t.color('green')
            elif y < n-x and y < x:
                t.color('purple')
            elif y > n-x and y < x:
                t.color('red')
            elif y == n-x or y == x:
                t.color('black')
                
            t.goto(10*x,10*y)
            t.dot()    
                
            #Interseção das retas -x+1 e x
def desenha_al(n):
    t.speed('fastest')
    t.hideturtle()
    t.up()
    t.color('red')
    for x in range(randint(0,n)):
        for y in range(randint(0,n)):
            t.goto(10*x,10*y)
            t.dot()
            
def selection_sort(L,n):
    '''Ordena uma lista de n elementos usando o algoritmo de inserção
       L - lista
       n - número de elementos'''
    for i in range(n):
        for j in range(i,n):
            if L[j] < L[i]:
                aux = L[i]
                L[i] = L[j]
                L[j] = aux
    return L
                
                
def selection_sortV2(L,n):
    '''Ordena uma lista de n elementos usando o algoritmo de inserção
       L - lista
       n - número de elementos'''
    for i in range(n):
        pos_min = i
        #vai encontrar a posição mínima
        for j in range(i+1,n):
            if l[j] < l[pos_min]:
                pos_min = j
        #trocar i por pos_min
                aux = L[m]
                L[m] = L[n]
                L[n] = aux
    return L
        
def menor_lista(L, n):
    '''Retorna a posição do menor elemento de uma lista de n elementos'''
    pos_min = 0
    for i in range(1,n):
        if L[i] < L[pos_min]:
            pos_min = i
    return pos_min
    
