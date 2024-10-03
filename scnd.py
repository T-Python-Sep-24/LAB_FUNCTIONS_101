def new_func2(n):
    list1 = []
    for i in range(n, 0, -1):
        end = ' '.join(str(j) for j in range(i,0,-1))
        list1.append(end)
    return '\n'.join(list1)
var1 = new_func2(5)
print(var1)
print(type(var1))