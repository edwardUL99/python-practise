import math

class Geometry:
    def __init__(self, length = 0.0):
        self.length = length;
        
    def distance(self, x1, y1, x2, y2):
        point1 = "(" + str(x1) + "," + str(y1) + ")" 
        point2 = "(" + str(x2) + "," + str(y2) + ")"
        print("The distance of point %s and point %s is:" % (point1, point2))
        return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

p1 = Geometry()
print(p1.distance(-4,-3,4,3))
p1.length = 10.0   

#for x in range(1, 21):
    #print(x)
