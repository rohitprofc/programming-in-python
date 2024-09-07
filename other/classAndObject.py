class Circle():
    def __init__(self, r):
        self.__radius = r
        self.__Pi = 3.14

    def area(self):
        return (self.__radius**2)*(self.__Pi)
    
    def perimeter(self):
        return 2*(self.__radius)*(self.__Pi)

c = Circle(5)
print(c.area())
print(c.perimeter())
