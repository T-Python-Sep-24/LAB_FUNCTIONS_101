"""
    This function takes an integer 'n' as input and prints a pattern where the first row 
    contains numbers from 'n' to 1, the second row contains numbers from 'n-1' to 1, 
    and so on until the last row prints just 1.
    
    Returns the pattern as a string, then assigns the result to a variable
    and prints it. """
    
def decreasing_pattern(n: int) -> str:
    pattern = ""  # Initialize an empty string to store the pattern
    for i in range(n, 0, -1):  # Loop from n to 1
        for j in range(i, 0, -1):  # Loop from i  to 1 for each row
            pattern += str(j) + " "  # Add each number followed by a space " "
        pattern += "\n"  # Add a newline (\n) after each row
    return pattern  # Return the complete pattern

# Assign the result to a variable and print it
result = decreasing_pattern(5)
print(result)
print(result.__doc__)

