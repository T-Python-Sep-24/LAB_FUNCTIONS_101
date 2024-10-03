def fun1(number:int):
    for i in range(number , 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()
fun1(5)
