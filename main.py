def print_pattern(n: int):
    ''' function that takes 1 parameter of type int , then it prints out the result formatted'''
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Print documentation
print(print_pattern.__doc__)

# call the function
print_pattern(5)
