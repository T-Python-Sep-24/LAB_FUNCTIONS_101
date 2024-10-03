
def labFunction(number:int) -> str:

    sequence= "" #initialize an empty string
    for i in range(number,0,-1): 
        for j in range(i,0,-1): 
           sequence += str(j)+ '  '
        sequence +="\n"
    return sequence

number = int(input("enter number : "))
result = labFunction(number)
print(result)
