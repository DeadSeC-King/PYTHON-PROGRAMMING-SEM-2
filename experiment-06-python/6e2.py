def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total


# Example
print(sum_of_cubes(5))  # 1^3 + 2^3 + 3^3 + 4^3 = 100