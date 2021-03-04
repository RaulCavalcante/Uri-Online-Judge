'''
Faça um programa que leia um vetor A[100]. No final, mostre todas as 
posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado
 em cada uma das posições.

 Entrada
 A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

 Saída
Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a 
posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto
decimal.
'''

v = []
v_P = []
i = 0
while i < 100:
    x = float(input())
    v.append(x)
    if x <= 10 :
        v_P.append(i)
    i+=1
i2 = 0
for a in range(len(v_P)):
    print('A[{}] = {:.1f}'.format(v_P[i2],v[v_P[i2]]))
    i2+=1