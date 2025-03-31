def calcula_imc(massa, altura):
    '''
    Retorna o imc (indice de massa corporal)
    de uma pessoa dado a massa (kg) e altura (m)
    (float, float) -> str
    '''
    
    imc = massa/(altura**2)
    
    if imc < 18.5:
        return print(f'O seu imc é de {imc:.2f}, está na faixa abaixo do peso ideal')
    elif imc <= 25:
        return print(f'O seu imc é de {imc:.2f}, está na faixa do peso ideal')
    elif imc <= 30:
        return print(f'O seu imc é de {imc:.2f}, está com excesso de peso')
    elif imc <= 35:
        return print(f'O seu imc é de {imc:.2f}, está com obesidade(grau I)')
    elif imc <= 40:
        return print(f'O seu imc é de {imc:.2f}, está com obesidade(grau II)')
    else:
        return print(f'O seu imc é de {imc:.2f}, está com obesidade(grau III)')

    
def teste_imc():
    
    massa = float(input("Digite sua massa (kg): "))
    altura = float(input("DIgite a sua altura (m): "))

    imc = calcula_imc(massa,altura)

def  brincadeira(dia,mes,ano):
    '''
    Retorna o perfil da pessoa dada o dia, mes e ano em que nasceu
    (int,int,int) -> str
    '''
    
    exp1 = dia*100 + mes + ano
    exp2 = exp1%100 + (exp1//100)

    resto = exp2%5
    
    if resto == 0:
        return print("Você é timido, vá socializar")
    if resto == 1:
        return print("Você é sonhador, vá dormir")
    if resto == 2:
        return print("Você é timido, vá casar")
    if resto == 3:
        return print("Você é atraente, vá atrair")
    else:
        return print("Você é irresistivel, vá ser resistivel")

def teste_perfil():
    print('digite sua data de nascimento:')
    dia = int(input("dia: "))
    mes = int(input("mẽs: "))
    ano = int(input("ano: "))

    msg = brincadeira(dia,mes,ano)

def avalia_carro(km,l):
    '''
    Função que avalia o consumo de um carro e retorna dicas!
    (float,float) -> str
    '''
    consumo = km/l
    if consumo <=8:
        return print("Venda o carro")
    elif consumo <=14:
        return print('Econômico')
    else:
        return print('Super econômico')
    
def maximo(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2
def minimo(num1, num2):
    if num1<num2:
        return num1
    else:
        return num2
def medio(a,b,c):
    
    lista1 = []
    lista2 = []
    lista1.append(a)
    lista1.append(b)
    lista1.append(c)
    
    num1 = maximo(a,maximo(b,c))
    num2 = minimo(a,minimo(b,c))
     
    lista2.append(num1)
    lista2.append(num2)
    for c in lista1:
        if not (c in lista2):
            return c
    
def cataloga_triangulo(a,b,c):
    '''
    Função que recebe os lados de um triângulo e retorna se o triângulo existe e qual o seu tipo
    (float,float,float) -> str
    a - lado maior
    b - lado médio
    c - lado menor
    '''
    
    if a < (b+c) and b < (a+c) and c < (a+b):
        a1 = maximo(a,maximo(b,c))
        b1 = medio(a,b,c)
        c1 = minimo(a,minimo(b,c)) 
        soma = b1**2 + c1**2
        lado = a1**2
        if lado == soma:
            return print('é um triâgulo retângulo')
        if lado > soma:
            return print('é um triângulo obtusângulo')
        if lado < soma:
            return print('é um triângulo acutângulo')
    
    else:
        return print("não existe triângulo com esses lados")

def imprime(msg,n):
    '''
    Imprime uma mensagem n vezes
    '''
    i = 0
    while i < n:
        print(msg)
        i += 1
        
def soma(n):
    '''Retorna a soma dos n primeiros números'''
    resultado = 0
    i = 1
    while i<=n:
        resultado +=i
        i+=1
    return resultado

def fatorial(n):
    '''Retorna o fatorial do número inteiro n
       (int) -> int
    '''
    fatorial = 1
    while n>1:
        fatorial *= n
        n -= 1
    return fatorial
    
def tabuada(num, n = 10):
    while n>=0:
        print(f'{num}x{n} = {num*n}')
        n-=1
    
def gerar_tabuada(n,m = 10):
    '''Imprime a tabuada completa'''
    i = 1
    while i<=n:
        tabuada(i, m)
        print('-='*20)
        i+=1
