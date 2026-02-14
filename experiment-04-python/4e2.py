#wap to count number of vowels in the string
s = input("Enter a string: ")
count = 0
for i in s:
    if i in 'AEIOUaeiou':
        count += 1
print("Number of vowels in the string: ", count)