'''
Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo
que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e
máxima de 24 horas.

Entrada:                Saida:
16 2                 	O JOGO DUROU 10 HORA(S)
'''
x,y = map(int, input().split())

if ( x > y ):
    
    a = 24 - x
    
    h = a + y
    
    print("O JOGO DUROU %d HORA(S)" %h)

elif ( y > x ):
    
    h = y - x
    
    print("O JOGO DUROU %d HORA(S)" %h)

elif x == y:
    
    h=24
    
    print("O JOGO DUROU %d HORA(S)" %h)