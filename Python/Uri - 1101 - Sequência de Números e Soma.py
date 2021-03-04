'''
Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

Entrada
O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

Saída
Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

Exemplo de Entrada	
5 2
6 3
5 0
Exemplo de Saída
2 3 4 5 Sum=14
3 4 5 6 Sum=18
'''
while True:
    soma = 0
    a,b = map(int,input().split())
    if b <= 0 or a <=0:
        break
    if a < b:
        a1 = a
        b1 = b
    else:   
        a1 = b
        b1 = a
    while a1 <= b1:
        soma = soma + a1
        print(a1, end=" ")
        a1 = a1 + 1
    print('Sum={}'.format(soma), end="")
    print()
    

    

