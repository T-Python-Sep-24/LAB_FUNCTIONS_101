# define the function
def myfunction(n: int):
    """
    prints out a formatted pattern like the following (n = 3):
    3 2 1
    2 1
    1
    
    Args:
        n (int): a number as start for printing the pattern

    Returns:
        None: no returned value

    """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
            
# call the function
myfunction(5)
