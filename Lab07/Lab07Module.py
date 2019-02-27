#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/24
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from enum import Enum
from math import sqrt as sqrt
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

class Rectangle:

    def __init__(self, llpoint, urpoint):
        self.lowerLeft = llpoint
        self.upperRight = urpoint
        self._verifyCord()

    def _verifyCord(self):
        if (self.lowerLeft[0] < self.upperRight[0]) and (self.lowerLeft[1] < self.upperRight[1]):
            return
        else:
            raise ValueError("The coordinates for the rectangle are wrong")

    def isSquare(self):
        if (self.upperRight[0] - self.lowerLeft[0]) == (self.upperRight[1] - self.lowerLeft[1]):
            return True
        else:
            return False

    def intersectsWith(self, rect):
        if rect.lowerLeft[0] < self.upperRight[0] and self.lowerLeft[0] < rect.lowerLeft[0]:
            return True
        elif rect.upperRight[0] < self.upperRight[0] and self.upperRight[0] < rect.lowerLeft[0]:
            return True
        elif rect.lowerLeft[1] < self.upperRight[1] and self.lowerLeft[1] < rect.lowerLeft[1]:
            return True
        elif rect.upperRight[1] < self.upperRight[1] and self.upperRight[1] < rect.lowerLeft[1]:
            return True
        else:
            return False

    def __eq__(self, another_rectangle):
        if isinstance(another_rectangle,Rectangle) == False:
            raise TypeError("Rectangle2 must be an instance of the Rectangle class")
        x1 = self.upperRight[0] - self.lowerLeft[0]
        y1 = self.upperRight[1] - self.lowerLeft[1]
        x2 = another_rectangle.upperRight[0] - another_rectangle.lowerLeft[0]
        y2 = another_rectangle.upperRight[1] - another_rectangle.lowerLeft[1]
        area1 = x1 * y1
        area2 = x2 * y2
        return area1 == area2

class Circle:

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self._verifyRadius()

    def _verifyRadius(self):
        if self.radius > 0:
            return
        else:
            raise ValueError("Radius must be greater than zero")

    def intersectsWith(self, other):
        if isinstance(other, Rectangle):
            x = (other.upperRight[0] - other.lowerLeft[0])/2
            y = (other.upperRight[1] - other.lowerLeft[1])/2
            cntr = (x,y)
            x1 = pow((cntr[0] - self.center[0]), 2)
            y1 = pow((cntr[1] - self.center[1]), 2)
            distance = sqrt(x1 + y1)
            if cntr[0] == self.center[0] and cntr[1] == self.center[1]:
                return True
            elif distance < (self.radius + x):
                return True
            else:
                return False

        if isinstance(other, Circle):
            x = pow((other.center[0] - self.center[0]),2)
            y = pow((other.center[1] - self.center[1]),2)
            distance = sqrt(x+y)
            if other.center == self.center and other.radius < self.radius:
                return True
            elif distance < self.radius:
                return True
            elif distance < (self.radius + other.radius):
                return True
            else:
                return False


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...