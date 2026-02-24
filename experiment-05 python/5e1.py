# 1. Scan n values in range 0-3 and print the number of times each value has occurred.

n = int(input("Enter number of values: "))
values = []

for i in range(n):
    v = int(input("Enter value (0-3): "))
    if 0 <= v <= 3:
        values.append(v)
    else:
        print("Invalid value, ignored")

count = {0: 0, 1: 0, 2: 0, 3: 0}

for v in values:
    count[v] += 1

for k in count:
    print(f"{k} occurred {count[k]} times")
