def LAB_FUNCTIONS_101(n: int) -> None:
 
    for i in range(n, 0, -1):
        line = ''
        for j in range(i, 0, -1):
            line += str(j) + ' '
        print(line.strip())

print(LAB_FUNCTIONS_101.__doc__)
LAB_FUNCTIONS_101(5)

def LAB_FUNCTIONS_101_string(n: int) -> str:
   
    result = ''
    for i in range(n, 0, -1):
        line = ''
        for j in range(i, 0, -1):
            line += str(j) + ' '
        result += line.strip() + '\n'
    return result.strip()

output_string = LAB_FUNCTIONS_101_string(5)
print(output_string)
