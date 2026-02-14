#wap to count number of capital letters in the string
s = input("Enter a string: ")
count = 0
for i in s:
    if i.isupper():
        count += 1
        print(i)
print("Number of capital letters in the string: ", count)