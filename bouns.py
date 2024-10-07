def fun1(number:int):
    """
    this function Prints a pattern of decreasing numbers, starting from the given integer `n` down to 1, 
    and reducing the number of elements on each subsequent line but the type of result will be a string instead of intger.
    """
    result = ""
    for i in range(number , 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result+= "\n"
    return result



res = fun1(5)
        
print(res)
print(type(res)) 