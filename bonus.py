# define the function
def myfunction(n: int) -> str:
    pattern: str = ""
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j)
        pattern += "\n"
    
    return(pattern)
            
# call the function
result = myfunction(5)
print(result)