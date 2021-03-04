'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
i = 1
numero_M = 0

while i <= 100:

    x = int(input())

    if x > numero_M:

        numero_M = x
        posicao = i

    i += 1

print(numero_M)
print(posicao)
