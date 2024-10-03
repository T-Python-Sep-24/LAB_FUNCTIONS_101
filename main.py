'''
# LAB_FUNCTIONS_101
'''
#creat a function
def descending_number(num:int):
   '''this function takes one int number then prints the number sequence in descending order'''
   while num!=0:
    for i in range(num, 0, -1):
        print(i, end=' ')
    print()    
    num -= 1    


#calling the function
descending_number(5)
#print the documentation of function
print(descending_number.__doc__)
