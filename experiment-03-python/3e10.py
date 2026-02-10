n = 5

for i in range(n, 0, -1):

    # Print numbers from 1 to i
    for j in range(1, i + 1):
        print(j, end="")

    # Print stars
    stars = n - i
    print("*" * (1* stars), end="")

    # Print numbers from i to 1
    for j in range(i, 0, -1):
        print(j, end="")

    print()  # New line
