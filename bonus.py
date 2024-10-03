'''
# Bonus
'''

#creat a function
def descending_number(num:int):
   '''this function takes one int number then prints the number sequence in descending order'''
   
   numbers_string="" 
   while num!=0:
    for i in range(num, 0, -1):
        numbers_string += str(i) + " "
    numbers_string+='\n'    
    num -= 1
   return numbers_string   
    

#calling the function and print the result
sequance_of_numbers=descending_number(5)
print(sequance_of_numbers)

#print the documentation of function
print(descending_number.__doc__)