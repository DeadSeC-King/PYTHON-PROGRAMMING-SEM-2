# =========================
# Q1. Perform operations on name.txt
# a) Count number of names
# b) Count names starting with vowel
# c) Find longest name
# =========================

with open("name.txt", "r") as f:
    names = [line.strip() for line in f]

# a)
print("Total names:", len(names))

# b)
vowels = ('A', 'E', 'I', 'O', 'U')
vowel_count = sum(1 for name in names if name.upper().startswith(vowels))
print("Names starting with vowel:", vowel_count)

# c)
longest_name = max(names, key=len)
print("Longest name:", longest_name)