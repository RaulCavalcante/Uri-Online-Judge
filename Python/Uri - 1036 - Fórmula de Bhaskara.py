'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, 
mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada:                    Saida:
10.0 20.1 5.1               R1 = -0.29788
                            R2 = -1.71212
'''
L = []

L = input().split()

A = float(L[0])
B = float(L[1])
C = float(L[2])

delta = ( B ** 2 ) - ( 4 * A * C ) 

if ( delta >= 0 ): 

    X1 =  (-B) + ( delta ** 0.5 ) 

    X2 =  (-B) - ( delta ** 0.5 ) 

    if ( X1 != 0 and X2 != 0 ):

        X1 = X1 / (2*A)
        X2 = X2 / (2*A)

        print("R1 = %0.5f" %X1)

        print("R2 = %0.5f" %X2)

    else:

        print("Impossivel calcular")

else:

    print("Impossivel calcular")