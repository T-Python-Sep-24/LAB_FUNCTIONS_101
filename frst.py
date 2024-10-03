def new_func(i:int):
    for x in range(i,0,-1):
        for y in range(x,0,-1):
            print(y, end=' ')
        print()
new_func(i=5)
