'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o 
perímetro do triângulo e apresente a mensagem:


Perimetro = XX.X


Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


Area = XX.X

Entrada:                Saida:
6.0 4.0 2.0             Area = 10.0
'''
a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

if ( (a + b) > c and ( a + c ) > b and ( c + b ) > a ):

    perimetro = a + b + c
    print("Perimetro = %0.1f" %perimetro)

else:

    area = ( ( a + b ) * c ) / 2
    print("Area = %0.1f" %area)

    
    
