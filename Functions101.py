def triangle(x:int):
    ''' This function prints a Triangle. It takes an ineger number which is the width of the Triangle. '''
    for i in range(x):
        for j in range(x - i):
            print(x - j - i, end=' ')
        print('')
        
triangle(5)
print('')
print(triangle.__doc__)