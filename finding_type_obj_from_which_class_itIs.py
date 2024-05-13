#problem statement:
""" 
 Check type of an object
Write a program to determine which class a given Bus object belongs to.
"""

# parent class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

#child class
class Bus(Vehicle):
    pass



School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))

    

