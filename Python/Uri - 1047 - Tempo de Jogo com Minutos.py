'''
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada:            Saida:
7 8 9 10            O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
'''
a,b,c,d = input().split()

if a == b and b == c and c == d :

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(24,0))

else:

    hora_Inicial = int(a)
    minuto_Inicial = int(b)
    hora_Final = int(c)
    minuto_Final = int(d)   

    quant_Seguntos_Total = ((hora_Final * 3600) + (minuto_Final*60)) - ((hora_Inicial*3600) + (minuto_Inicial*60))

    h = quant_Seguntos_Total // 3600

    quant_Seguntos_Total = quant_Seguntos_Total - h * 3600

    m = quant_Seguntos_Total // 60

    quant_Seguntos_Total = quant_Seguntos_Total - m * 60

    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h,m))