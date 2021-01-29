'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada:            saida:
7                   4 valores positivos
-5                  7.4
6
-3.4
4.6
12
'''
positivo = 0
media = 0

for x in range(6):

    i = float(input())

    if i > 0:

        positivo += 1
        media += i

media = media / positivo

print("%d valores positivos" %positivo)
print("%0.1f" %media)