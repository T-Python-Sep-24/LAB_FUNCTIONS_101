
number = int(input("Enter a number: "))


def myFunction(number) -> str:
    """
    This Function takes a number and
    returns a string that shapes a pyramid out of the deciding numbers from the inputted number

    """
    myString = ""
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            myString += str(j) + " "
        myString += "\n"
    return myString  # returning a string rather that printing it

result = myFunction(number)
print(result)