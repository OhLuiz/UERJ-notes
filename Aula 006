def conta_vogais(texto):
    '''Código retorna a quantidade de vogais que o texto possui'''
    vogais = 'AEIOUÁÃÂÀÉÊẼÈÍÌĨÎÓÒÕÔÚÙŨÛ'
    total = 0
    i = 0
    texto2 = texto[:].upper()
    while i < len(texto2):
        if texto2[i] in vogais:
            total+=1
        i+=1
    return total

def inverter_str(texto):
    '''Retorna a string escrita ao crontrário
    (str) -> str
    '''
    return texto[::-1]

def inverter(texto): ##não vamos usar a numeração negativa
    '''Retorna a string escrita ao crontrário
    (str) -> str
    '''
    texto2 = ''
    count  = len(texto) - 1
    while count>=0:
        texto2 += texto[count]
        count-=1
    return texto2

def eh_vogal(caracter):
    '''Retorna se o caractere inserido é uma vogal ou não
    (str) -> str
    len(caracter) = 1; len(caracter) > 1 error
    '''
    vogais = 'AEIOUÁÃÂÀÉÊẼÈÍÌĨÎÓÒÕÔÚÙŨÛ'
    ch = caracter.upper()
    if ch in vogais:
        return True
    else:
        return False
    
def remove_vogais(texto):
    '''Retorna a string escrita sem as vogais sem a função eh_vogal()
    (str) -> str
    '''
    vogais = 'AEIOUÁÃÂÀÉÊẼÈÍÌĨÎÓÒÕÔÚÙŨÛ'
    texto2 = ''
    count = 0
    while count<len(texto):
        if texto[count].upper() not in vogais:
            texto2 += texto[count]
        count+=1
    return texto2

def remove_vogais2(texto):
    '''Retorna a string escrita sem as vogais com a função eh_vogal()
    (str) -> str
    '''
    texto2 = ''
    count = 0
    while count<len(texto):
        if not eh_vogal(texto[count]):
            texto2 += texto[count]
        count+=1
    return texto2

def remove_espacos(texto):
    '''Retorna a string escrita sem espaços
    (str) -> str
    '''
    texto2 = ''
    count = 0
    while count<len(texto):
        if texto[count] != ' ':
            texto2 += texto[count]
        count+=1
    return texto2
            

def palindromo(texto):
    '''Retorna se o caractere inserido é um palindromo ou não
    (str) -> str'''
    texto2 = inverter(remove_espacos(texto)).upper()
    texto1 = remove_espacos(texto).upper()
    return texto1 == texto2

    
def mascarar_texto(texto):
    ###Testar a função .replace('O que vai ser trocado','o que vai substituir')
    '''Substitui as vogais de um texto por caractere X
    (str) -> str'''
    texto2 = ''
    count = 0
    while count<len(texto):
        if eh_vogal(texto[count]):
            texto2+='X'
        else:
            texto2+=texto[count]
        count+=1
    return texto2

def count_palvras(palavra,texto): ##VERIFICAR
    count = 0
    listaEspaco = []
    ct = 0
    while count<len(texto):
        if texto[count] == ' ':
            listaEspaco.append(count)
        count+=1
    c1 = 0
    for c in listaEspaco:
        if palavra == texto[c1:c]:
            ct+=1
            c1 = c
    return ct

def count_palavras(palavra, texto):
    ###Usar o .split('O que vai ser usado como corte')
    ###Usar a .find('O que queremos achar, retorna o primeiro que achar', a posição que começará a procurar, a poisção de final de procura)
    count = 0
    ct = 0
    listaEspaco = texto.split(' ')
    for c in listaEspaco:
        if palavra.upper() == c.upper():
            ct+=1
    return ct

def cifrar_texto(texto,chave):
    ##ord(str()) retorna o valor da tabela ascii para um numero
    ##chr(int()) retorna uma str da tabela ascii relacionada ao numero
    lista1 = []
    lista2 = []
    texto2 = ''
    for c in texto:
        lista1.append(ord(c))
    for v in lista1:
        lista2.append(c+chave)
    for i in lista2:
        texto2+=chr(i)
    return print(texto2)
