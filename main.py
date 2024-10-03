#LAB_FUNCTIONS_101
def pattern(n:int):
    for i in range(n):
        for j in range(n-i-1,-1,-1):
            print(j+1,end=" ")
        print()
pattern(5)

#Bonus
print("-"*15)
def patt(x:int):
    pattern= ""
    for i in range(x,0,-1):
        for j in range(i,0,-1):
            pattern+=str(j)+" "
        pattern=pattern+"\n"
    return pattern
        
print(patt(5))