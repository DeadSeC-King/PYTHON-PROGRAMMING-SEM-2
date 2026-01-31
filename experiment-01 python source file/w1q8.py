#wap to left shift and right shift value of a number
num = int(input("Enter a number: "))
n=int(input("Enter number of positions to shift: "))
left_shift = num << n
right_shift = num >> n
print("Left shift of", num, "by", n, "is:", left_shift)
print("Right shift of", num, "by", n, "is:", right_shift)