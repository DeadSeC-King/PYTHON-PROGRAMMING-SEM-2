#7.	Write functions to explain mentioned concepts:
#a.	Keyword argument
#b.	Default argument
#c.	Variable length argument
def student(name, age):
    print("Name:", name)
    print("Age:", age)
student(age=20, name="Rahul")
def greet(name="Guest"):
    print("Hello", name)
greet("Krran")
greet()
def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    print("Sum:", total)

add_numbers(1, 2, 3)
add_numbers(10, 20, 30, 40)