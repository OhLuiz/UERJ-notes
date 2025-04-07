import random as r

##Fibonacci
def fibonacci(n):
    '''Imprime os n primeiros termos da série de fibonacci - não aceito número 0'''
    a,b = 0,1
    while n>0:
        if n%2 == 0:
            print(b, end = ',')
            a = b+a
        else:
            print(a, end = ',')
            b = a+b 
        n-=1

def fibonacci2(n):
    '''Imprime os n primeiros termos da série de fibonacci - não aceito numero 0'''
    a,b = 0,1
    while n>0:
        print(a, end = ',')
        a,b = b, b+a
        n-=1

def fibonacci3(n):
    '''Imprime os n primeiros termos da série de fibonacci - não aceito numero 0'''
    a,b,c = 0,1,0
    while n>0:
        c = a
        print(a, end = ',')
        a = b
        b = c+b
        n-=1
        
##Random
def imprime_random(n,f = 9999):
    '''Imprime n números inteiros aleatórios de uma faixa de valor de até 0 a f, por padrão 9999'''
    while n>0:
        print(r.randint(0,f))
        n-=1
        
def imprime_random_x(x,f = 100):
    '''Imprime números aleatórios [0,f](por padrão f = 100),
    quando gerar o número x para a execução e
    imprime a quantidade de tentativas'''
    num = r.randint(0,f)
    print(num)
    count = 1
    while num !=x:
        num = r.randint(0,f)
        print(num)
        count+=1
    print(f'Você ganhou, foram necessárias {count} tentativas, parabéns amigo')

def imprime_random_diferente_x(n, x, f = 100):
    '''Imprime números aleatórios [0,f](por padrão f = 100),
    diferentes de x'''
    print('Duvido encontrar o número escolhido')
    while n>0:
        num = r.randint(0,f)
        if num == x:
            continue #pula a próxima interação
        print(num)
        n-=1
    print('vai! tente achar ai')

def jogo_do_adivinhao(max_tentativas=5):
    '''Gera um número entre 1 e 50, o jogador tenta adivinhar o valor dando um palpite'''
    num = r.randint(1,50)
    ch,n = 0,0
    
    print('Tente adivinhar o número, ele está entre 1 e 50!! Não se esqueça que você tem apenas 5 tentativas')
    print('-='*30)
    while ch!=num and n<max_tentativas:
        ch = int(input(f"Tente adivinhar o número que escolhi({n+1} tentativa): "))
        print('-='*30)
        if (num-ch) >= 25:
            print('O número que eu escolhi é beem maior que o seu, sem querer me gabar')
        elif (num-ch) < 25 and (num-ch) > 0:
            print('O número que eu escolhi é um pouco maior que o seu')
        elif (num-ch) <= -25:
            print('O número que eu escolhi é beem menor que o seu, não me julgue!')
        elif (num-ch) > -25 and (num-ch) < 0:
            print('O número que eu escolhi é um pouco menor que o seu')
        n+=1
    
    if ch == num:
        print('Parabéns!! Você conseguiu acertar o número que pensei!')
    elif ch != num and n ==max_tentativas:
        print(f'Acabaram suas tentativas cara, o número que pensei era {num},talvez na próxima!')
        
    
    
###String

def conta_vogais(texto):
    '''Código retorna a quantidade de vogais que o texto possui'''
    vogais = 'AEIOU'
    total = 0
    i = 0
    texto2 = texto[:].upper()
    while i < len(texto2):
        if texto2[i] in vogais:
            total+=1
        i+=1
    return total

    print(f'O número de vogais do texto escrito é: {num}')
        
