'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada:            Saida:
6                   5
-5
'''
a = int(input())
b = int(input())

soma = 0

if a < b:

    prov = a
    a = b
    b = prov
    
if a == b:

    print(soma)

b += 1

while b < a:

    if b % 2 != 0:

        soma += b

    b += 1


print(soma)
