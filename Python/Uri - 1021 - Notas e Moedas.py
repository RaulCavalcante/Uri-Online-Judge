'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
A seguir mostre a relação de notas necessárias.

Entrada:            Saida:NOTAS:
576.73              5 nota(s) de R$ 100.00
                    1 nota(s) de R$ 50.00
                    1 nota(s) de R$ 20.00
                    0 nota(s) de R$ 10.00
                    1 nota(s) de R$ 5.00
                    0 nota(s) de R$ 2.00
                    MOEDAS:
                    1 moeda(s) de R$ 1.00
                    1 moeda(s) de R$ 0.50
                    0 moeda(s) de R$ 0.25
                    2 moeda(s) de R$ 0.10
                    0 moeda(s) de R$ 0.05
                    3 moeda(s) de R$ 0.01

'''
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

n1 = 0
n05 = 0
n025 = 0
n010 = 0
n005 = 0
n001 = 0

N = float(input())

tirar = N

print("NOTAS:")

n100 = N//100
tirar = tirar - n100 * 100

print("%0.0f nota(s) de R$ 100,00" %n100)

n50 = tirar//50
tirar = tirar - n50 * 50

print("%0.0f nota(s) de R$ 50,00" %n50)

n20 = tirar//20
tirar = tirar - n20 * 20

print("%0.0f nota(s) de R$ 20,00" %n20)

n10 = tirar//10
tirar = tirar - n10 * 10

print("%0.0f nota(s) de R$ 10,00" %n10)

n5 = tirar//5
tirar = tirar - n5 * 5

print("%0.0f nota(s) de R$ 5,00" %n5)

n2 = tirar//2
tirar = tirar - n2 * 2

print("%0.0f nota(s) de R$ 2,00" %n2)

n1 = tirar//1
tirar = tirar - n1 * 1

print("MOEDAS:")

print("%0.0f moeda(s) de R$ 1,00" %n1)

n05 = tirar//0.5
tirar = tirar - n05 * 0.5

print("%0.0f moeda(s) de R$ 0,50" %n05)

n025 = tirar//0.25
tirar = tirar - n025 * 0.25

print("%0.0f moeda(s) de R$ 0,25" %n025)

n010 = tirar//0.10
tirar = tirar - n010 * 0.10

print("%0.0f moeda(s) de R$ 0,10" %n010)

n005 = tirar//0.05
tirar = tirar - n005 * 0.05

print("%0.0f moeda(s) de R$ 0,05" %n005)

n001 = tirar//0.01

print("%0.0f moeda(s) de R$ 0,01" %n001)