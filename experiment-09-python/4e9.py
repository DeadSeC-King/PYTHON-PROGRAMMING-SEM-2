#. Create a class to implement method Overriding.
class Parent:
    def display(self):
        print("This is the parent class method.")
class Child(Parent):
    def display(self):
        print("This is the child class method.")
# Main program
parent_obj = Parent()
child_obj = Child()
print("Parent Object:")
parent_obj.display()
print("\nChild Object:")
child_obj.display()

