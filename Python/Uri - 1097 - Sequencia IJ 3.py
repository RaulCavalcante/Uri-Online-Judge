'''
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
'''
j = 7
i = 1

while i <= 9:

    a = j

    for x in range(3):
    
        print('I={} J={}'.format(i,j))

        j -= 1
    

    j = a + 2
    i += 2
  