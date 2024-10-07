#Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print() 

print_pattern(5)

