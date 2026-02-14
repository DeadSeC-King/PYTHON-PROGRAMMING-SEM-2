#wap to input a sentence and separate the words and print it
s= input("Enter a sentence: ")
words = s.split()
print("The words in the sentence are: ")
for word in words:
    print(word)