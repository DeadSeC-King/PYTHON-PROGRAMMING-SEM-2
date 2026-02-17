s = input("Enter a string: ")
sub = input("Enter a substring to count: ")

count = 0
i = 0

while i <= len(s) - len(sub):
    if s[i:i+len(sub)] == sub:
        count += 1
    i += 1

print("Count =", count)
