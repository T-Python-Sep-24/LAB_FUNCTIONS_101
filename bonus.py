def name(n: int) -> str:
    result = ""
    '''
    the function takes the parameters in integer and returns string then print the given integer down to 1.
    '''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
               result += f"{j} " 
        result += "\n"

    return result    
        
print(name(5))