
number = int(input("Enter a number: "))


def myFunction(number):
    for i in range(number, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print(" ")


myFunction(number)
