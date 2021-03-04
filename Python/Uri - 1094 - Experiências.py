'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

'''
cob = 0
coe = 0
ra = 0
sa = 0

x = int(input())

while x > 0:

    q,t = input().split()

    q = int(q)

    cob += q

    if t == "C":

        coe += q
    
    elif t == "R":

        ra += q

    elif t == "S":

        sa += q

    x -= 1

pocoe = ( coe / cob ) * 100
pora = ( ra / cob ) * 100
posa = ( sa / cob ) * 100

print("Total: %d cobaias" % cob)
print("Total de coelhos: %d" % coe)
print("Total de ratos: %d" % ra)
print("Total de sapos: %d" % sa)
print('Percentual de coelhos: {:.2f} %'.format(pocoe))
print('Percentual de ratos: {:.2f} %'.format(pora))
print('Percentual de sapos: {:.2f} %'.format(posa))
