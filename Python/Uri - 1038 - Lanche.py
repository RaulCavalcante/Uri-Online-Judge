'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, 
calcule e mostre o valor da conta a pagar.

Entrada:            Saida:
3 2                 Total: R$ 10.00
'''
L = []

L = input().split()

codigo = float(L[0])
Quantidade = float(L[1])

if ( codigo == 1 ):

    Total = Quantidade * 4

elif ( codigo == 2 ):

    Total = Quantidade * 4.5

elif ( codigo == 3 ):

    Total = Quantidade * 5

elif ( codigo == 4 ):

    Total = Quantidade * 2

else:

    Total = Quantidade * 1.5

print("Total: R$ %0.2f" %Total)
