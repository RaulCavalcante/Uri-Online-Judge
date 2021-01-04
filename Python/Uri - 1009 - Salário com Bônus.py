'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
com duas casas decimais.

Entrada:                    Saida:
JOAO                        TOTAL = R$ 684.54
500.00
1230.30
'''
nome = input()

salario = float(input())

vendas = float(input())

bonus = ( vendas * 15 ) / 100

salario = salario + bonus 

print("TOTAL = R$ %0.2f" %salario)
