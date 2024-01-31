"""
this problem is taken from the website my-course.net whose link is :
:https://www.my-courses.net/2020/02/exercises-with-solutions-on-oop-object-oriented-programming-in-python.html

Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the 
area of ​​the rectangle.
Create a method display() that display the length, width, perimeter and area of an object created using an
instantiation on rectangle class.
Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute and 
another Volume() method to calculate the volume of the Parallelepiped.

"""
class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self,length, width):
        return 2*(self.length+ self.width)
    
    def area(self, length, width):
        return self.length * self.width
    
    def display(self):
        print("the length is :", self.length)
        print("the width is : ", self.width)
        print("the perimeter is :", self.perimeter(self.length, self.width))
        print("the area is : ", self.area(self.length , self.width))
        
class Parallelepiped(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height 
    
    def volume(self, length , width, height):
        return length * width * height   
rect1 = Rectangle(7, 5)
rect1.display()
