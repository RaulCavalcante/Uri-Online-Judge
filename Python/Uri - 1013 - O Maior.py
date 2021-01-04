'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = 

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar 
no resultado esperado.

Entrada:            Saida:
7 14 106            106 eh o maior
'''
X = [2]

X = input().split()

X[0] = int(X[0])
X[1] = int(X[1])
X[2] = int(X[2])

maior = X[0]

if ( maior < X[1] ):

    maior = X[1]

if ( maior < X[2] ):

    maior = X[2]

print(maior,"eh o maior")