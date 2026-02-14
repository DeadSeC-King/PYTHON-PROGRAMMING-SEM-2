'''7.	Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
a)	Fruits which are in both sets s1 and s2
b)	Fruits only in s1 but not in s2
c)	Count of all fruits from s1 and s2'''
s1 = set();s2 = set()
n = int(input("Enter the number of fruits in each set: "))
print("Enter fruits for set s1:")
for i in range(n):
    fruit = input("Fruit {}: ".format(i+1))
    s1.add(fruit)
print("Enter fruits for set s2:")
for i in range(n):
    fruit = input("Fruit {}: ".format(i+1))
    s2.add(fruit)
common_fruits = s1.intersection(s2)
print("Fruits in both sets s1 and s2: ", common_fruits)
unique_s1 = s1.difference(s2)
print("Fruits only in s1 but not in s2: ", unique_s1)
total_fruits = s1.union(s2)
print("Count of all fruits from s1 and s2: ", len(total_fruits))