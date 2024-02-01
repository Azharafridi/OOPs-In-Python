"""
 
 Exercice 42: Person class and child Student class ||  Solution
Create a Python class Person with attributes: name and age of type string.
Create a display() method that displays the name and age of an object created via the Person class.
Create a child class Student  which inherits from the Person class and which also has a section attribute.
Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
Create a student object via an instantiation on the Student class and then test the displayStudent method.   
"""

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        print("my name is : ", self.name, " and age is :", self.age)
        

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section
        
    def display_student(self):
        print("student name is {}, age is {}, section is {} ".format(self.name, self.age, self.section))
        
# create student object 
stud_object = Student('azhar ud din', '20', 'Section A')

stud_object.display_student()
        