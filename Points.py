import math

class Points:
    def __init__(self, x1 = 0, y1 = 0, x2 = 0, y2 = 0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def setPoints(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))

    def pointsToString(self, point):
        if point == 1:
            return "(" + str(self.x1) + "," + str(self.y1) + ")"
        elif point == 2:
            return "(" + str(self.x2) + "," + str(self.y2) + ")"
        elif point == 3:
            return "(" + str(self.x3) + "," + str(self.y3) + ")"
        else:
            return ""

    def midPoint(self):
        x = ((self.x1) + (self.x2)) / 2
        y = ((self.y1) + (self.y2)) / 2
        return self.pointToString(x, y)

    def pointToString(self, x, y):
        return "(" + str(x) + "," + str(y) + ")"
        

p1 = Points()
p1.setPoints(-4,-3,4,3)
print("The distance between point %s and point %s is %d\n" % (p1.pointsToString(1), p1.pointsToString(2), p1.distance()))
print("The midpoint of line %s to %s is %s\n" % (p1.pointsToString(1), p1.pointsToString(2), p1.midPoint()))
p1.setPoints(3,7,5,9)
print("The distance between point %s and point %s is %.04f\n" % (p1.pointsToString(1), p1.pointsToString(2), p1.distance()))
print("The midpoint of line %s to %s is %s\n" % (p1.pointsToString(1), p1.pointsToString(2), p1.midPoint()))
