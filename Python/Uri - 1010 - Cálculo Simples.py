'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2,
 o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

Entrada:                Saida:
12 1 5.30               VALOR A PAGAR: R$ 15.50
16 2 5.10
'''
A = [2]
B = [2]

A = input().split()
B = input().split()

valor = ( int(A[1]) * float(A[2]) ) + ( int(B[1]) * float(B[2]) )

print("VALOR A PAGAR: R$ %0.2f" %valor)