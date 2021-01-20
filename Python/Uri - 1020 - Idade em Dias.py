'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca 
haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de 
testar raciocínio matemático simples.

Entrada:            Saida: 
400             	1 ano(s)
                    1 mes(es)
                    5 dia(s)
'''
T = int(input())

a = 0
m = 0
d = 0

a = T // 365

T = T - a * 365

m = T // 30

T = T - m * 30

d = T 

print(a,"ano(s)")
print(m,"mes(es)")
print(d,"dia(s)")

