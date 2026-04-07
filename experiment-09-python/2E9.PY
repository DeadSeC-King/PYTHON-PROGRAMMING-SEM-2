class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks  # [phy, chem, maths]

    # a) Display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.marks)

    # b) Calculate percentage
    def marks_percentage(self):
        total = sum(self.marks)
        percentage = total / 3
        return percentage

    # c) Result (Pass/Fail)
    def result(self):
        for m in self.marks:
            if m < 40:
                return "Fail"
        return "Pass"


# d) Function to calculate class average
def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    return total / len(students)


# ---- Main Program ----

n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    
    name = input("Enter Name: ")
    sap_id = int(input("Enter SAP ID: "))
    
    print("Enter marks (Physics Chemistry Maths):")
    marks = list(map(float, input().split()))

    students.append(Student(name, sap_id, marks))


# Display all students + results
print("\n===== Student Details =====")
for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    print("Result:", s.result())


# Class average
avg = class_average(students)
print("\nClass Average Percentage:", avg)