# Creating the function that prints the pattern
def numbersPyramid(num: int):
    '''This is a function that takes 1 parameter of type int, then it prints out the result formatted like an inverted pyramid'''
    
    #Outer loop handles the number of rows
    for i in range(num, 0, -1):
        #Inner loop handles the number of columns 
        for j in range(1, i + 1):
            print(f"{num - j + 1} ", end = " ")
        #Print new row
        print()

#Calling the numbersPyramid with number of rows as argument
numbersPyramid(5)
print(numbersPyramid.__doc__)
print()


#---------------- Bonus ----------------
def numbersPyramidBonus(num: int) -> str:
    '''This is a function that takes 1 parameter of type int, then it returns the result formatted like an inverted pyramid'''
    output: str = ""
    #Outer loop handles the number of rows
    for i in range(num, 0, -1):
        #Inner loop handles the number of columns 
        for j in range(1, i + 1):
            output += f"{num - j + 1} "
        #New row in the string
        output += "\n"
    return output

#Calling the numbersPyramidBonus with number of rows as argument,
#then returning the output instead of printing it
functionResult: str = numbersPyramidBonus(6)
print(functionResult)