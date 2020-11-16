import math
#write your code here
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        self.per = (self.a + self.b + self.c)
        return self.per
    def area(self):
        self.halfper = self.per/2
        self.ar = math.sqrt( ( self.halfper )*( self.halfper - self.a )*(self.halfper - self.b)*(self.halfper - self.c) )
        return self.ar

side1 = int(input("Enter first side of the triangle: "))
if( side1 <= 0):
    print("Incorrect Input")
else:
    side2 = int(input("Enter second side of the triangle: "))
    if( side2 <= 0):
        print("Incorrect Input")
    else:
        side3 = int(input("Enter third side of the triangle: "))
        if( side3 <= 0):
            print("Incorrect Input")
        else:
            tri_obj1 = Triangle(side1,side2,side3)
            print("Perimeter of the triangle:",tri_obj1.perimeter() )
            print("Area of the triangle:",tri_obj1.area() )