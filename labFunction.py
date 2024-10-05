## Create a function that takes 1 parameter of type int ,
#  then it prints out the result formatted like the following patter (if we give it 5 for example):

def print_pattern(n: int):
    for i in range(n, 0, -1):
        # Create a list of numbers from i down to 1
        line = ' '.join(str(x) for x in range(i, 0, -1))
        print(line)

# Example usage
print_pattern(5)