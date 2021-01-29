'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a 
tabela abaixo:

Salário	                    Percentual de Reajuste
0 - 400.00                          15%    
400.01 - 800.00                     12%
800.01 - 1200.00                    10%
1200.01 - 2000.00                   7%
Acima de 2000.00                    4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste 
ganho e o índice reajustado, em percentual.

Entrada:                Saida:
400.00                  Novo salario: 460.00
                        Reajuste ganho: 60.00
                        Em percentual: 15 %
'''
salario = float(input())

if 0 <= salario <= 400:

    salario_Atualizado = salario + ((salario * 15) / 100)
    aumento = ((salario * 15) / 100)
    porcento = 15

elif 400.01 <= salario <= 800:

    salario_Atualizado = salario + ((salario * 12) / 100)
    aumento = ((salario * 12) / 100)
    porcento = 12

elif 800.01 <= salario <= 1200:

    salario_Atualizado = salario + ((salario * 10) / 100)
    aumento = ((salario * 10) / 100)
    porcento = 10

elif 1200.01 <= salario <= 2000:

    salario_Atualizado = salario + ((salario * 7) / 100)
    aumento = ((salario * 7) / 100)
    porcento = 7

elif salario > 2000:

    salario_Atualizado = salario + ((salario * 4) / 100)
    aumento = ((salario * 4) / 100)
    porcento = 4


print("Novo salario: %0.2f" %salario_Atualizado)
print("Reajuste ganho: %0.2f" %aumento)
print("Em percentual:",porcento,"%")