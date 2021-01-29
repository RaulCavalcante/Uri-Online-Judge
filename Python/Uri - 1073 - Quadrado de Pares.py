'''
Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

Entrada:        Saida:
6               2^2 = 4
                4^2 = 16
                6^2 = 36
'''
x = int(input())

i = 1

while i <= x:

    if i % 2 == 0:

        y = ( i ** 2 )

        print('{}^2 = {}'.format(i,y))

    i += 1