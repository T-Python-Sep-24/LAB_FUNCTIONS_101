enterOfUser= int(input("Enter a number:"))

def drwa(variableControl : int):
     """
    This function draws a descending pyramid pattern. You can enter any number to generate the pattern.
    Parameters:
    variableControl (int): The starting number for the pyramid.
    Thank you, Teacher Aqeel and Teacher Wjadan, for this simple trick!
    """ 
     for largeVariable  in range(variableControl,1-1,-1) :
        for samllVariable in range(largeVariable,1-1,-1):
            print(samllVariable,end=' ') 
        print(end='\n')

drwa(enterOfUser)
print(drwa.__doc__)
