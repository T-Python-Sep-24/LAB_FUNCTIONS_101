def get_pattern(n: int) -> str:
    result = []
    for i in range(n, 0, -1):
        line = ' '.join(str(x) for x in range(i, 0, -1))
        result.append(line)
    return '\n'.join(result)

# Example usage
pattern_result = get_pattern(5)
print(pattern_result)