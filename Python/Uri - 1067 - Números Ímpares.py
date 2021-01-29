'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada:        Saida:
8               1
                3
                5
                7
'''
x = int(input())

i = 1

while i <= x:

    if i % 2 != 0:

        print(i)

    i += 1
