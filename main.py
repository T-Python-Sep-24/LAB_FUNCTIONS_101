
def labFunction(number:int):
    '''
    print sequence of numbers in descending order
    '''
    for i in range(number,0,-1): 
        for j in range(i,0,-1): 
            print( j , end=' ') 
        print()

number = int(input("enter number : "))
labFunction(number)
print(labFunction.__doc__)