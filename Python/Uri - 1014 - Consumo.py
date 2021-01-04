'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

Entrada:            Saida:
500                 14.286 km/l
35.0
'''
X = int(input())

Y = float(input())

consumo = X/Y

print("%0.3f km/l" %consumo)