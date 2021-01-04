'''
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D 
segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada:                    Saida:
5                           DIFERENCA = -26
6
7
8
'''
A = int(input())
B = int(input())
C = int(input())
D = int(input())

calculo = ( A * B ) - ( C * D )

print("DIFERENCA =" , calculo )