'''
Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.

Entrada
A entrada contém um número inteiro N. Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.

Saída
Para cada caso mostre o resultado da divisão com um dígito após o ponto decimal, ou “divisao impossivel” caso não seja possível efetuar o cálculo.

Obs.: Cuide que a divisão entre dois inteiros em algumas linguagens como o C e C++ gera outro inteiro. Utilize cast :)

Exemplo de Entrada	
3
3 -2
-8 0
0 8
Exemplo de Saída
-1.5
divisao impossivel
0.0
'''
i = int(input())

x = [2]

while i > 0:

    x = input().split()

    a = float(x[0])
    b = float(x[1])

    if b != 0:

        result = a / b 

        print('{:.1f}'.format(result))

    else:

        print("divisao impossivel")

    i -= 1
