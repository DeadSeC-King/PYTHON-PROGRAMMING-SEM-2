#6.	Program to count number of unique words in a given sentence using sets.
s = input("Enter a sentence: ")
words = s.split()
unique_words = set(words)
print("Number of unique words in the sentence: ", len(unique_words))