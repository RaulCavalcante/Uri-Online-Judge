'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia =

Entrada:            Saida:
1.0 7.0             4.4721
5.0 9.0
'''
X = [1]
Y = [1]

X = input().split()
Y = input().split()

X[0] = float(X[0])
X[1] = float(X[1])

Y[0] = float(Y[0])
Y[1] = float(Y[1])


A = ( ( Y[0] + (-X[0]) ) ** 2)
B = ( ( Y[1] + (-X[1]) ) ** 2) 

distancia = ( (A + B) **  0.5 )  

print("%0.4f" %distancia)