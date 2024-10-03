def fun1(number:int):
    result = ""
    for i in range(number , 0, -1):
        for j in range(i, 0, -1):
            result += str(j) + " "
        result+= "\n"
    return result



res = fun1(5)
        
print(res)