def new_func(i:int):
    """
    this is a function take one parameter then print the out the number in reverse

    """
    for x in range(i,0,-1):
        for y in range(x,0,-1):
            print(y, end=' ')
        print()
new_func(i=5)
print(new_func.__doc__)