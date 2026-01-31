#wap to find a number using membership operator in a sequence
num = int(input("Enter a number to search: "))
sequence = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
if num in sequence:
    print(f"{num} is found in the sequence.")
else:
    print(f"{num} is not found in the sequence.")
    