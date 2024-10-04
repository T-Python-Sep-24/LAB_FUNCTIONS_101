def print_pattern(n: int) -> str:
   
    result = []
    for i in range(n):
        line = " ".join(str(n - j) for j in range(i, n))
        result.append(line)
    return "\n".join(result)

pattern_result = print_pattern(5)
print(pattern_result) 