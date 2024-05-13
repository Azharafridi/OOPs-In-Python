
# parent class

""" 
problem statement: 
                Define a property that must have the same value for every class instance (object)
                Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
                the output should be like :
                Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
                Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

"""

class Vehicle:
    color = 'white'
    def __init__(self, name, max_speed,mileage):
        self.name = name
        self.mileage = mileage
        self.max_speed = max_speed
        
class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

def main():
    school_bus = Bus('School Volvo', 180, 12)
    print('Color:', school_bus.color, ', vehicle name: ', school_bus.name, ', speed:', school_bus.max_speed, ', mileage:', school_bus.mileage)
    
    car = Car('Audi Q5', 240, 18)
    print('Color:', car.color, ', vehicle name: ', car.name, ', speed:', car.max_speed, ', mileage:', car.mileage)
main()