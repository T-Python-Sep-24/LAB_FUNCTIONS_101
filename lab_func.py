def patternNumber(user_Itration:int):
    '''This function takes a number N to generate a pattern of descending numbers of N where each row starts with N and decrements to 1 '''
    for number in range(user_Itration,0,-1) :
        for i in range(number,0,-1):
            print(i ,end=' ')
        print()

userIn= int(input("Pick a number: "))
patternNumber(userIn)
print(patternNumber.__doc__)