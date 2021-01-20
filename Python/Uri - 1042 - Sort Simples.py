'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em
seguida, os valores na sequência como foram lidos.

Entrada:                Saida:
7 21 -14                -14
                        7
                        21

                        7
                        21
                        -14
'''
lista = [2]

lista = input().split()

A,B,C = lista

lista[0] = int(lista[0])
lista[1] = int(lista[1])
lista[2] = int(lista[2])

lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print()
print(int(A))
print(int(B))
print(int(C))
