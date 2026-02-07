n = 5
for i in range(n):
    # L
    for j in range(1, n - i + 1):
        print(j, end="")
    #m
    if i > 0:
        for k in range(2 * i - 1):
            print("*", end="")
    #r
    for j in range(n - i, 0, -1):
        print(j, end="")
    print()
