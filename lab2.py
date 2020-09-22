import numpy as np

#EX1
class IntegerNum:

    def __init__(self, n1):
        self.value = n1

    def double(self):
        self.value = self.value * 2

    def pow(self,kitevo):
        return self.value ** kitevo

    def square(self):
        self.value *= self.value

    def __str__(self):
        return str(self.value)

#EX2
class Circle:

    pi = 3.14

    def __init__(self,r):
        self.radius = r

    def __str__(self):
        return f"Ez egy kör {self.radius} sugárral és {self.Perimeter()} kerülettel."

    def Perimeter(self):
        return 2 * self.radius * Circle.pi

#o=Circle(54.2)
#print(o)

#EX3
class Rectangle:

    def __init__(self,a,b):
        self.value1 = a
        self.value2 = b

    def area(self):
        return self.value1*self.value2

#eredmeny=Rectangle(3.2,5)
#print(eredmeny.area())

#EX4
class StrUpper:

    def __init__(self):
        self.string=""

    def GetStr(self,szo):
        self.string = szo

    def PrintStr(self):
        print(self.string.upper())

#szoveg=StrUpper()
#szoveg.GetStr("szeemi")
#szoveg.PrintStr()

#EX5
v=[-25, -10, -7, -3, 2, 4, 8, 10]

class Zero:

    def __init__(self,v):
        self.ls = v

    def Nums(self):
        pass

