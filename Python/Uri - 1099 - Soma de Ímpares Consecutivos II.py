'''
Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

Entrada
A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

Saída
Imprima a soma de todos valores ímpares entre X e Y.
'''
i = int(input())

x = []

soma = 0

while i > 0:

    x = input().split()

    a = int(x[0])
    b = int(x[1])

    if a > b:

        b += 1

        while a > b:

            if b % 2 != 0:

                soma += b

            b += 1
            
    elif a < b:

        a += 1

        while b > a:

            if a % 2 != 0:

                soma += a

            a += 1

    print(soma)
    soma = 0
    i -= 1 