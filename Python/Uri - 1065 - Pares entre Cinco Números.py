'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada:            Saida:
7                   3 valores pares
-5
6
'''
par = 0

for x in range(5):

    i = float(input())

    if i % 2 == 0:

        par += 1

print("%d valores pares" %par)
