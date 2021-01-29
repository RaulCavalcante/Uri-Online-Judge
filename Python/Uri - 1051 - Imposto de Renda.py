'''
Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos,
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em 
benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.

Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb.
Em seguida, calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo
a tabela abaixo.

Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas sobre
R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00 é isenta de 
Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de 8% sobre
R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total. O valor deve ser
impresso com duas casas decimais.

Entrada:                Saida: 
3002.00                 R$ 80.36
'''

renda = float(input())

imposto = 0

if 0 <= renda <= 2000:

    print("Isento")

elif 2000 < renda :

    imposto8 = renda // 2000

    imposto18 = renda // 3000

    imposto28 = renda // 4500

    if imposto28 != 0:

        imposto += ((renda - 4500) * 28) / 100

        renda = 4500

    if imposto18 != 0:

        imposto += ((renda - 3000) * 18) / 100

        renda = 3000

    if imposto8 != 0:

        imposto += ((renda - 2000) * 8) / 100

    print("R$ %0.2f" %imposto)