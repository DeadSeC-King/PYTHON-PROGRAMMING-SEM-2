# 4. Create a dictionary of n persons where key is name and value is city.
# a) Display all names
# b) Display all city names
# c) Display student name and city of all students.
# d) Count number of students in each city.

n = int(input("Enter number of persons: "))
people = {}

for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    people[name] = city

print("Names:", list(people.keys()))
print("Cities:", list(people.values()))

print("Name and City:")
for name, city in people.items():
    print(name, "->", city)

city_count = {}
for city in people.values():
    city_count[city] = city_count.get(city, 0) + 1

print("Students in each city:", city_count)
