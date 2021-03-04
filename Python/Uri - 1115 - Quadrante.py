'''
Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

Entrada
A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

Saída
Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

Exemplo de Entrada	
2 2
3 -2
-8 -1
-7 1
0 2
Exemplo de Saída
primeiro
quarto
terceiro
segundo
'''
quadrante = []

loop = True

while loop:

    quadrante = input().split()

    a = int(quadrante[0])

    b = int(quadrante[1])

    if a == 0 or b == 0:

        loop = False
        break

    elif a > 0 and b > 0:
        print("primeiro")
    elif a < 0 and b < 0:
        print("terceiro")
    elif a > 0 and b < 0:
        print("quarto")
    elif a < 0 and b > 0:
        print("segundo")
