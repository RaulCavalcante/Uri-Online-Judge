'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada:            Saida:
576                 576
                    5 nota(s) de R$ 100,00
                    1 nota(s) de R$ 50,00
                    1 nota(s) de R$ 20,00
                    0 nota(s) de R$ 10,00
                    1 nota(s) de R$ 5,00
                    0 nota(s) de R$ 2,00
                    1 nota(s) de R$ 1,00
'''
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

N = int(input())

tirar = N

print( N )

n100 = N//100
tirar = tirar - n100 * 100

print(n100,"nota(s) de R$ 100,00")

n50 = tirar//50
tirar = tirar - n50 * 50

print(n50,"nota(s) de R$ 50,00")

n20 = tirar//20
tirar = tirar - n20 * 20

print(n20,"nota(s) de R$ 20,00")

n10 = tirar//10
tirar = tirar - n10 * 10

print(n10,"nota(s) de R$ 10,00")

n5 = tirar//5
tirar = tirar - n5 * 5

print(n5,"nota(s) de R$ 5,00")

n2 = tirar//2
tirar = tirar - n2 * 2

print(n2,"nota(s) de R$ 2,00")

n1 = tirar//1
tirar = tirar - n1 * 1

print(n1,"nota(s) de R$ 1,00")
