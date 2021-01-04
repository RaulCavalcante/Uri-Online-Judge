'''
A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

Entrada:            Saida:
2.00                A=12.5664
'''
X = float(input())

A = 3.14159 * ( X * X )

A = round( A , 4 )

print("A=%0.4f" %A )
