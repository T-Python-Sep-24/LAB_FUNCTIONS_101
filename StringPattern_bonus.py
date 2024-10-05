def returnTriangle(x:int):
    ''' This function returns a Triangle of numbers. It takes an ineger number which is the width of the Triangle. '''
    pattren = ''
    for i in range(x):
        for j in range(x - i):
            value = x - j - i
            pattren += f'{value} '
        pattren += '\n'
    return pattren
        
thePattren = returnTriangle(5)
print(thePattren)
print(returnTriangle.__doc__)