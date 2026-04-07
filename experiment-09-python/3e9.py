#Create programs to implement different types of inheritances
#Single Inheritance
class Parent:
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def child_method(self):
        print("This is the child method.")
# Multiple Inheritance
class Mother:

    def mother_method(self):
        print("This is the mother method.")

class Father:
    def father_method(self):
        print("This is the father method.")

class Child(Mother, Father):
    def child_method(self):
        print("This is the child method.")

# Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method.")

class Parent(Grandparent):

    def parent_method(self):
        print("This is the parent method.")
class Child(Parent):
    def child_method(self):
        print("This is the child method.")

# Hierarchical Inheritance

class Parent:
    def parent_method(self):
        print("This is the parent method.")
class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method.")
class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method.")
# Hybrid Inheritance
class Base:
    def base_method(self):
        print("This is the base method.")
class Derived1(Base):

    def derived1_method(self):
        print("This is the derived1 method.")
class Derived2(Base):
    def derived2_method(self):
        print("This is the derived2 method.")
class Hybrid(Derived1, Derived2):
    def hybrid_method(self):
        print("This is the hybrid method.")
        