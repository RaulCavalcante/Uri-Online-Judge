'''
	
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
'''
j = 7
i = 1

while i <= 9:

    while j >= 5:
    
        print('I={} J={}'.format(i,j))

        j -= 1
    

    j = 7
    i += 2
    