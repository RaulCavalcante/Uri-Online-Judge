'''
Escreva um programa que leia um valor inteiro N. Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

Entrada
O arquivo de entrada contém um número inteiro positivo N.

Saída
Imprima a saída conforme o exemplo fornecido.

Exemplo de Entrada	
7
Exemplo de Saída
1 2 3 PUM
5 6 7 PUM
9 10 11 PUM
13 14 15 PUM
17 18 19 PUM
21 22 23 PUM
25 26 27 PUM
'''
x = int(input())

i = -1

while x > 0:

    a = i + 2
    b = i + 3
    c = i + 4

    print('{} {} {} PUM'.format(a,b,c))

    i += 4
    x = x - 1
