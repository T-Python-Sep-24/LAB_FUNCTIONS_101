user = int(input("Enter a number: "))

def pyramid_pattern(variableMax :int ):
    """
    Draws a descending pyramid pattern starting from the specified number down to 1.
    
    Parameters:
    variableMax (int): The starting number for the pyramid.
    Return:
    str: A string representing the pyramid pattern, with each line showing numbers in descending order.

    Thank you, Teacher Aqeel and Teacher Wjadan, for this simple puzzle!
    """
    values = ""
    while variableMax > 0:
        variableMin =variableMax
        while variableMin > 0:
            values+=str(variableMin)
            variableMin -= 1
        values+='\n' 
        variableMax -= 1
    return values

result = pyramid_pattern(user)
print(pyramid_pattern.__doc__)
print(result )

