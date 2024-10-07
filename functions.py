
number = int(input("Enter a number: "))


def myFunction(number):
    """
       This Function takes a number and
       print a pyramid out of the deciding numbers from the inputted number

   """
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print(" ")


myFunction(number)
