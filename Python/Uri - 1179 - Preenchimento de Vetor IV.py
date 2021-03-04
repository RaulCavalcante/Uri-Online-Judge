'''
Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme
estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois
vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, 
você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos 
números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo 
que restou em cada um dos dois vetores, imprimindo primeiro os valores do 
vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for 
necessário.

Entrada
A entrada contém 15 números inteiros.

Saída
Imprima a saída conforme o exemplo abaixo.
'''
v1 = []
v2 = []
for i in range (15):
    x = int(input())
    if x % 2 == 0:
        v1.append(x)
    else:
        v2.append(x)
    if len(v1) == 5:
        i = 0
        while i < 5:
            print('par[{}] = {}'.format(i,v1[i]))
            i+=1
        v1.clear()
    if len(v2) == 5:
        i = 0
        while i < 5:
            print('impar[{}] = {}'.format(i,v2[i]))
            i+=1
        v2.clear()
i = 0
while i < len(v2) or i == 0:
    print('impar[{}] = {}'.format(i,v2[i]))
    i+=1
i = 0
while i < len(v1) or i == 0:
    print('par[{}] = {}'.format(i,v1[i]))
    i+=1
