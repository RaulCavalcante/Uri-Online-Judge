'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada:            Saida:
-5                  3 valor(es) par(es)
0                   2 valor(es) impar(es)
-3                  1 valor(es) positivo(s)
-4                  3 valor(es) negativo(s)
12
'''

par = 0
impar = 0

positivo = 0
negativo = 0

for i in range(5):

    x = int(input())

    if x > 0 :

        positivo += 1

    if x < 0:

        negativo += 1
        
    if x % 2 == 0:

        par += 1

    else:

        impar += 1

print("%d valor(es) par(es)" %par)
print("%d valor(es) impar(es)" %impar)
print("%d valor(es) positivo(s)" %positivo)
print("%d valor(es) negativo(s)" %negativo)