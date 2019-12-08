class Circle:
    def __init__(self, radius, color):
        self.radius = float(radius)
        self.color = str(color)
    def getRadius(self):
        print(self.radius)
    def setRadius(self):
        self.radius = float(input("Please input the radius: "))
    def getColor(self):
        print(self.color)
    def setColor(self):
        self.color = str(input("Please input the color: "))
    #def toString(self):
        #What is this even supposed to do?
    def getArea(self):
        area = float(2) * 3.14 * self.radius
        print(area)
        return area
class Cylinder(Circle):
    def __init__(self, height, radius, color):
        super().__init__(radius, color)
        self.height = int(height)
    def getHeight(self):
        print(self.height)
    def setHeight(self):
        self.height = int(input("Please input the height: "))
    #def toString(self):
        #Not sure here either
    def getVolume(self):
        volume = super().getArea() * self.height
        print(volume)
x = Circle(1.0, "Red")
y = Cylinder(1, 1.0, "Red")
x.getRadius()
x.setRadius()
x.getColor()
x.setColor()
x.getArea()
y.getHeight()
y.setHeight()
y.getVolume()


