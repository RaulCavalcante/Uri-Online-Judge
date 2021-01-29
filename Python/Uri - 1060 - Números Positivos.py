'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos 
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada:        Saida:
7               4 valores positivos
-5
6
-3.4
4.6
12
'''
positivo = 0

for x in range(6):

    i = float(input())

    if i > 0:

        positivo += 1


print("%d valores positivos" %positivo)
