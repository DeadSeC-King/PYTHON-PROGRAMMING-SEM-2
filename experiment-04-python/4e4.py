#wap to input a string and count a substring repeatedly in the string
s = input("Enter a string: ")
sub = input("Enter a substring to count: ")
count = s.count(sub)
print("The substring '{}' appears {} times in the string.".format(sub, count))