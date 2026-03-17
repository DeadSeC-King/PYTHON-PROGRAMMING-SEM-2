# =========================
# Q6. Program execution counter
# =========================

filename = "counter.txt"

try:
    with open(filename, "r") as f:
        count = int(f.read())
except:
    count = 0

count += 1

with open(filename, "w") as f:
    f.write(str(count))

print("Program executed", count, "times")