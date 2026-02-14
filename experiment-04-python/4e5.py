#5.	Given a string containing both upper and lower case alphabets.
#  Write a Python program to count the number of occurrences of each alphabet (case insensitive) and display the same.
s = input("Enter a string: ")
s = s.lower()  # Convert the string to lowercase for case-insensitive counting
alphabet_count = {}
for char in s:
    if char.isalpha():  # Check if the character is an alphabet
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1
print("Occurrences of each alphabet (case insensitive):")
for alphabet, count in alphabet_count.items():
    print(f"{alphabet}: {count}")