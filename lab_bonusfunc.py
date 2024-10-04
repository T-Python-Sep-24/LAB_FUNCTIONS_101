def patternNumberToString(user_Itration:int)-> str:
    '''This function takes a number N to generate a pattern of descending numbers of N where each row starts with N and decrements to 1 and the result return as a String'''
    result=""
    for number in range(user_Itration,0,-1):
        for i in range(number,0,-1):
            result +=str(i)+" "
        result +="\n"
    return result

userIn= int(input("Pick a number: "))
result=patternNumberToString(userIn)
print("The pattern for the number You picked: \n"+result)
print(patternNumberToString.__doc__)