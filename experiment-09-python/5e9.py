#Create a class for operator overloading which adds two Point Objects where Point has x & y values
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Main program
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print("Result of adding Point1 and Point2:", result)
