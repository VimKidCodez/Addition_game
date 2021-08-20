from random import *
while True:
    print('Add and type the following numbers')
    a = randrange(1,10)
    b = randrange(1,10)
    print (a )
    print (b )
    d = int(input('Answer: '))
    c = (a+b)

    if (d) == c :
        print('Correct😄\n')

    else:
        print('Incorrect😡\n')
