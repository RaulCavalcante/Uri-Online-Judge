'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, 
determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada:            Saida:
4.5 -2.2            Q4
'''
Lista = [1]

Lista = input().split()

X = float(Lista[0])
Y = float(Lista[1])

if ( X == 0 and Y == 0 ):

    print("Origem")

elif ( X > 0 and Y > 0 ):

    print("Q1")

elif ( X > 0 and Y < 0 ):

    print("Q4")

elif ( X < 0 and Y > 0 ):

    print("Q2")

elif ( X < 0 and Y < 0 ):

    print("Q3")

elif ( Y == 0 and ( X < 0 or X >= 0 ) ):

    print("Eixo X")


elif ( X == 0 and ( Y >= 0 or Y < 0 ) ):

    print("Eixo Y")