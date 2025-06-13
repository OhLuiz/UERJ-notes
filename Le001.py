##regras de operadores:
##1. Parenteses;
##2. Exponenciação
##3. Multiplicação de divisão
##4. SOma e multiplicação
##TODAS AS OPERAÇÕES SÃO REALIZADAS DA ESQUERDA PARA DIREITA
##Criação de constantes em maiusculo
##print(valor1, valor2, ..., sep = ' ', end = '\n')
##sep diz o separador dos valores no print e o \n diz que no fim terá quebra de linha

##nome = 'Maria' #cria-se variável de nome
##idade = 25 #cria-se variável de idade
##print(f'Nome:{nome}\nIdade:{idade}') #imprime no compilador os dados

nota1 = float(input("Digite o valor da nota da P1:")) #definindo a entrada para a variável da nota da P1
nota2 = float(input("Digite o valor da nota da P2:")) #definindo a entrada para a variável da nota da P2
lista11 = float(input("Digite o valor da lista 1 da P1:")) #definindo a entrada para a variável da nota da lista 1
lista12 = float(input("Digite o valor da lista 2 da P1:")) #definindo a entrada para a variável da nota da listta 2
lista21 = float(input("Digite o valor da lista 1 da P2:")) #definindo a entrada para a variável da nota da lista 1
lista22 = float(input("Digite o valor da lista 2 da P2:")) #definindo a entrada para a variável da nota da listta 2
notaT = float(input("Digite o valor da nota do trabalho:")) #definindo a entrada para a variável da nota do trabalho

P1 = nota1*0.7+(lista11+lista12)*0.15 #calculando a P1
P2 = nota2*0.7+(lista21+lista22)*0.15 #calculando a P2
media_final = (P1+P2)*0.4 + notaT*0.2 #calculando a média final
##print(f"A média é: {media_final:.2f}") #imprimindo o valor da média final

if media_final>=7: #caso o aluno passe direto
    print(f"PARABÉNS, você foi aprovado com {media_final:.2f} de média")
    
elif media_final < 7 and media_final>=3: #criando uma estrutura IF para caso o aluno não passe direto!
    print("infelizmente sua nota não foi suficiente para passar direto, será necessária uma prova final!")
    notaF = float(input("Digite o valor da nota da PF:")) #definindo a entrada para a variável da nota da PF
    media_final = (media_final+notaF)/2
    if media_final >= 5: #caso aprove
        print(f"PARABÉNS, você foi aprovado com {media_final:.2f} de média")
    else: #caso reprove
        print(f"Infelizmente você foi reprovado com média {media_final:.2f}")
        
else: #caso o aluno reprove direto
    print(f"Infelizmente você foi reprovado direto com média {media_final:.2f}")
    
