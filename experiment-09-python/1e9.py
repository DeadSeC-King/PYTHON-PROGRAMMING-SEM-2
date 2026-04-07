class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks  # [phy, chem, maths]

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.marks[0])
        print("Chemistry:", self.marks[1])
        print("Maths:", self.marks[2])


students = []

# Input for 3 students
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    
    name = input("Enter Name: ")
    sap_id = int(input("Enter SAP ID: "))
    
    print("Enter marks (Physics Chemistry Maths):")
    marks = list(map(float, input().split()))
    
    students.append(Student(name, sap_id, marks))


# Display all students
print("\n===== All Student Details =====")
for s in students:
    s.display()