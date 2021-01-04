'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e 
calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada:                Saida:
25                      NUMBER = 25
100                     SALARY = U$ 550.00
5.50
'''
numero = int(input())

horasTrabalhada = int(input())

dinheiro_Hora = float(input())


salario = horasTrabalhada * dinheiro_Hora

print("NUMBER =", numero)

print("SALARY = U$ %0.2f" %salario)