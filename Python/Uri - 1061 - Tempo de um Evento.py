'''
Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril,
iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento
vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho
a calcular a duração deste evento.

Entrada:                Saida:
Dia 5                   3 dia(s)
08 : 12 : 23            22 hora(s)
Dia 9                   1 minuto(s)
06 : 13 : 23            0 segundo(s)
'''
def conversao_de_segundos ( T ):
    d = 0
    h = 0
    m = 0
    s = 0

    d = T // 86400

    T = T - d * 86400

    h = T // 3600

    T = T - h * 3600

    m = T // 60

    T = T - m * 60

    s = T 

    print('{} dia(s)'.format(d))
    print('{} hora(s)'.format(h))
    print('{} minuto(s)'.format(m))
    print('{} segundo(s)'.format(s))

inicio = input().split(" ")
inicio_Data_Numero = int(inicio[1])
horario_Inicio = input().split(" : ")
fim =  input().split(" ")
fim_Data_Numero = int(fim[1])
horario_Fim = input().split(" : ")

dia = fim_Data_Numero - inicio_Data_Numero
hora_I = int(horario_Inicio[0])
hora_F = int(horario_Fim[0])
minuto_I = int(horario_Inicio[1])
minuto_F = int(horario_Fim[1])
segundo_I = int(horario_Inicio[2])
segundo_F = int(horario_Fim[2])

quant_Segundos_Inicio = (inicio_Data_Numero * 86400) + (hora_I * 3600) + ( minuto_I * 60) + segundo_I
quant_Segundos_Fim = (fim_Data_Numero * 86400) + (hora_F * 3600) + (minuto_F*60) + segundo_F

quant_Total_Segundos = quant_Segundos_Fim - quant_Segundos_Inicio

conversao_de_segundos(quant_Total_Segundos)