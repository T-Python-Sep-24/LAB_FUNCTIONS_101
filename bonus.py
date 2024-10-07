# define the function
def myfunction(n: int) -> str:
    """
    prints out a formatted pattern like the following (n = 3):
    3 2 1
    2 1
    1
    
    Args:
        n (int): a number as start for printing the pattern

    Returns:
        str: a formated pattern as a string

    """
    pattern: str = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j)
        pattern += "\n"
    
    return(pattern)
            
# call the function
result = myfunction(5)
print(result)