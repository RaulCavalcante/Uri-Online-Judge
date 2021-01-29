'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada:        Saida:
4               2 in
14              2 out
123
10
-25
'''
i = int(input())

dentro = 0
fora = 0

for i in range(i):

    x = int(input())
    
    if 10 <= x <= 20:

        dentro += 1

    else:

        fora += 1

print("%d in" %dentro)

print("%d out" %fora)