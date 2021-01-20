'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no 
formato horas:minutos:segundos.

Entrada:            Saida:
556                 0:9:16
'''
T = int(input())

h = 0
m = 0
s = 0

h = T // 3600

T = T - h * 3600

m = T // 60

T = T - m * 60

s = T 

print('{}:{}:{}'.format(h, m, s))


