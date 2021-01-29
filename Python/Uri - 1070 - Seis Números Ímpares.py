'''
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada:            Saida:                    	
8                   9
                    11
                    13
                    15
                    17
                    19
'''
i = int(input())

cont = 0

while cont != 6:

    if i % 2 == 1:

        print(i)

        cont += 1

    i += 1

    
    
