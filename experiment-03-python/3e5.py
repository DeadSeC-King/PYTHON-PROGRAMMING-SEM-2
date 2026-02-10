#wap to check weather a given number is palindrome or not
num = int(input("Enter a number: "))
text=str(num)
rev=text[::-1]
rev=int(rev)
print("The reverse of the number is: ", rev)
if num==rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    