def pattern(n: int):
    """Prints a descending number pattern starting from n to 1."""
    for i in range(n, 0, -1):
        print(" ".join(str(x) for x in range(i, 0, -1)))
pattern(5)

def get_pattern(n: int) -> str:
    """Returns a descending number pattern as a string."""
    pattern = []
    for i in range(n, 0, -1):
        pattern.append(" ".join(str(x) for x in range(i, 0, -1)))
    return "\n".join(pattern)
result = get_pattern(5)
print(result)
