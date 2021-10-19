class Circle:
    def __init__(self, diameter):
       self.diameter = diameter

    def circumference(self):
        return self.diameter*3.14
    def area(self):
        return self.diameter/2*self.diameter/2*3.14



p1 = Circle(6)
print("circumference is {}".format(p1.circumference()))
print("area is {}".format(p1.area()))

