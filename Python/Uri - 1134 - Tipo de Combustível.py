'''
Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.

Entrada
A entrada contém apenas valores inteiros e positivos.

Saída
Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de clientes que abasteceram cada tipo de combustível, conforme exemplo.

Exemplo de Entrada	
8
1
7
2
2
4
Exemplo de Saída
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
'''
gas = 0
al = 0
di = 0

x = int(input())

while x != 4:
    
    if x == 1:

        al += 1

    elif x == 2:

        gas += 1

    elif x == 3:

        di += 1

    x = int(input())

print("MUITO OBRIGADO")
print("Alcool:",al)
print("Gasolina:",gas)
print("Diesel:",di)
