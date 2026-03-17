# =========================
# Q2. Perform operations on numbers file
# a) Find max number
# b) Find average
# c) Count numbers > 100
# =========================

with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

# a)
print("Max number:", max(nums))

# b)
avg = sum(nums) / len(nums)
print("Average:", avg)

# c)
count = sum(1 for n in nums if n > 100)
print("Numbers greater than 100:", count)
