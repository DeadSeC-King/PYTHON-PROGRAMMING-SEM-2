#write a program to print and count all numbers divisible by 5 or 7 between 1 and 100
count = 0
for i in range(1, 101):
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
        count += 1
print("\nTotal count:", count)
