#Lab 5

#The answer
def myNumber(x: int) -> None:
    """
    This function will take 1 parameter and will decrement the number by 1.
    """
    for i in range(x, 0, -1):
        for n in range(i, 0, -1):
            print(n, end=" ")
        print() 

# Print the documentation
print(myNumber.__doc__)

myNumber(5)
