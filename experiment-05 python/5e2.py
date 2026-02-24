# 2. Create a tuple to store n numeric values and find average of all values.

n = int(input("Enter number of values: "))
nums = []

for i in range(n):
    nums.append(float(input("Enter number: ")))

t = tuple(nums)
avg = sum(t) / len(t)

print("Tuple:", t)
print("Average:", avg)