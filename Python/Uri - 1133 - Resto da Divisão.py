'''
Escreva um programa que leia 2 valores X e Y e que imprima todos os valores entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3.

Entrada
O arquivo de entrada contém 2 valores positivos inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima todos os valores conforme exemplo abaixo, sempre em ordem crescente.

Sample Input	
10
18
Sample Output
12
13
17
'''
a1 = int(input())
b1 = int(input())

if a1 > b1 :

    a = b1
    b = a1 

if a1 <= b1:

    a = a1
    b = b1

a = a + 1

while a < b:

    if a % 5 == 2 or a % 5 == 3 :

        print(a)

    a = a + 1
