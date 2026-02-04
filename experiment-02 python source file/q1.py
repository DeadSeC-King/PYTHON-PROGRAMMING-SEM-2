#wap to check weather a number is divisible by 3 and 5 or not
x=int(input("Enter a number: "))
if (x%3==0 and x%5==0):
    print("it is divisible by both 3 and 5")
else:
    print("it is not divisible by both or any one of 3 and 5")