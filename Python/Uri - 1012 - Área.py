'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.

Entrada:                Saida:
3.0 4.0 5.2             TRIANGULO: 7.800
                        CIRCULO: 84.949
                        TRAPEZIO: 18.200
                        QUADRADO: 16.000
                        RETANGULO: 12.000
'''
X = [2]

X = input().split()

X[0] = float(X[0])
X[1] = float(X[1])
X[2] = float(X[2])

pi = 3.14159

print("TRIANGULO: %0.3f" %( ( X[0] * X[2] ) / 2 ) )

print("CIRCULO: %0.3f" %( ( X[2] * X[2] ) * pi ) )

print("TRAPEZIO: %0.3f" %( ( ( X[0] + X[1] ) / 2 ) * X[2] ) )

print("QUADRADO: %0.3f" %( X[1] * X[1] ) )

print("RETANGULO: %0.3f" %( X[0] * X[1] ) ) 