'''
Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

Entrada
O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

Saída
Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

Sample Input	
100
200
Sample Output
13954
'''

a1 = int(input())
b1 = int(input())

if a1 > b1 :

    a = b1
    b = a1 

if a1 <= b1:

    a = a1
    b = b1

soma = 0

while a <= b:

    if a % 13 != 0:

        soma += a

    a += 1

print(soma)