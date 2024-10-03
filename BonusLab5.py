# Bonus Lab 5

#The answer
def myNumber(x: int) -> str:
    """
    This function takes 1 parameter and returns a string that contains
    the numbers in descending order in a pattern.
    """

    result = ""
    for i in range(x, 0, -1):
        for n in range(i, 0, -1):
            result += str(n) + ""
        result += "\n"
    return result

# Print the documentation
print(myNumber.__doc__)

finalNumber = myNumber(5)
print(finalNumber)