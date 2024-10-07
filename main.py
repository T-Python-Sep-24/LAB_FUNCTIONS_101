def fun1(number:int):
    """
    this function Prints a pattern of decreasing numbers, starting from the given integer `number` down to 1, 
    and reducing the number of elements on each subsequent line.
    """
    for i in range(number , 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()
fun1(5)
