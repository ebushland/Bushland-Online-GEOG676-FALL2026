
# create classes
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape): 
    def __init__(self, width, height): # (self, l, w):
        self.width = width # self.length = l
        self.height = height # self.width = w

    def area(self): # getArea(self):
        return self.width * self.height # return self.length * self.width

class Circle(Shape):
    def __init__(self, radius): # (self, r):
        self.radius = radius # self.radius = r

    def area(self): # getArea(self):
        return 3.14 * self.radius * self.radius 

class Triangle(Shape):
    def __init__(self, base, height): # (self, b, h):
        self.base = base # self.base = b
        self.height = height # self.height = h

    def area(self): # getArea(self):
        return 0.5 * self.base * self.height # return 0.5 * self.base * self.height

# read text file
file = open(r"C:\Users\ebush\Desktop\TexasAM\GEOG-676\GitHub\GEOG-676-FALL26\Week04\Labs\shape.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(",")
    shape = components[0]

    if shape == "Rectangle":
        rectangle = Rectangle(float(components[1]), float(components[2]))
        print("Area of Rectangle:", rectangle.area())
    elif shape == "Circle":
        circle = Circle(float(components[1]))
        print("Area of Circle:", circle.area())
    elif shape == "Triangle":
        triangle = Triangle(float(components[1]), float(components[2]))
        print("Area of Triangle:", triangle.area())
    else:
        pass