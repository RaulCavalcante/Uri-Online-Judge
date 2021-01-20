'''
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média
com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média
for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem
"Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem 
"Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: 
" acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). 
e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos).
Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média 
final para esse aluno.

Entrada:                        Saida:
2.0 4.0 7.5 8.0                 Media: 5.4
6.4                             Aluno em exame.
                                Nota do exame: 6.4
                                Aluno aprovado.
                                Media final: 5.9
'''
lista = [3]

lista = input().split()

lista[0] = float(lista[0])
lista[1] = float(lista[1])
lista[2] = float(lista[2])
lista[3] = float(lista[3])


media = ( ( lista[0] * 2 ) + ( lista[1] * 3 ) + ( lista[2] * 4 ) + ( lista[3] * 1 ) ) / 10

print("Media: %0.1f" %media)

if ( media >= 7 and media <= 10):

    print("Aluno aprovado.") 
    

elif ( media >= 5 and media < 7):

    print("Aluno em exame.")

    exame = float(input())

    print("Nota do exame: %0.1f" %exame)

    final = ( exame + media ) / 2

    if ( final >= 5 and final <= 10 ) :

        print("Aluno aprovado.")

    elif ( final < 5 and final >= 0 ) :

        print("Aluno reprovado.")
    

    print("Media final: %0.1f" %final)
    

elif ( media < 5 and media >= 0 ):

    print("Aluno reprovado.")

