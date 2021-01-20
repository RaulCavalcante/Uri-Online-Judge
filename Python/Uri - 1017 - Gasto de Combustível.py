'''
Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L.
Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na
viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos
litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

Entrada:            Saida:
10                  70.833
85
'''
Tempo = int(input())

Velocidade = int(input())

distancia = Tempo * Velocidade

Litros_Necessario = distancia / 12

print("%0.3f" %Litros_Necessario)