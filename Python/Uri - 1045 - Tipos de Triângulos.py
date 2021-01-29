'''
Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado
A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados 
formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada:                    Saida:
7.0 5.0 7.0                 TRIANGULO ACUTANGULO
                            TRIANGULO ISOSCELES
'''
lista = [2]

lista = input().split()


lista[0] = float(lista[0])
lista[1] = float(lista[1])
lista[2] = float(lista[2])

lista.sort(reverse = True)

a = lista[0]
b = lista[1]
c = lista[2]

if ( ( b + c ) <= a ):

    print("NAO FORMA TRIANGULO")

elif ( ( ( b ** 2 ) + ( c ** 2 ) ) == ( a ** 2 ) ):

    print("TRIANGULO RETANGULO")

elif ( ( ( b ** 2 ) + ( c ** 2 ) ) < ( a ** 2 ) ):

    print("TRIANGULO OBTUSANGULO")

elif ( ( ( b ** 2 ) + ( c ** 2 ) ) > ( a ** 2 ) ):

    print("TRIANGULO ACUTANGULO")



if ( a == b and b == c and c == a ):

    print("TRIANGULO EQUILATERO")

elif ( a == b or b ==c or c == a ):

    print("TRIANGULO ISOSCELES")

