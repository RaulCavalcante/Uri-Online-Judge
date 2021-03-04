'''
Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento
com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 
11º. Mostre o vetor modificado.

Entrada
A entrada contém 20 valores inteiros, positivos ou negativos.

Saída
Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e 
Y é o valor armazenado naquela posição.
'''

n=[]
for i in range (20):
    x = int(input())
    n.append(x)
i = 0
i2 = 19
for i in range (10):
    v = n[i]
    n[i] = n[i2]
    n[i2] = v
    i+=1
    i2-=1
i = 0
while i < 20:
    print('N[{}] = {}'.format(i,n[i]))
    i += 1
