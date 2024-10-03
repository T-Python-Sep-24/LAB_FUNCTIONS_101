
number = int(input("Enter a number: "))


def myFunction(number):
    myString = ""
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            myString = myString + str(j) + " "
        myString = myString + "\n"
    return myString  # returning a string rather that printing it

result = myFunction(number)
print(result)