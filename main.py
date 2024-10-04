def print_pattern(n: int):
    """
    Prints a pattern of decreasing sequences of numbers from n to 1
    """
    for i in range(n):
        print(" ".join(str(n - j) for j in range(i, n)))


print_pattern(5)


print(print_pattern.__doc__)
