#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from Lab13.measurement import calculateDistance
import re
import numpy as np
import scipy
import imageio
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

def loadTriangles(leftPointFilePath, rightPointFilePath):
    pass

    #return tuple(leftTriangles, rightTriangles)

class Triangle:
    def __init__(self, vertices):
        if np.shape(vertices) != (3,2):
            raise ValueError("Input must have the dimension 3 x 2")
        for element in vertices.flatten():
            if isinstance(element, np.float64) == False:
                raise ValueError("Input must be type float64")

        self.vertices = vertices

    def getPoints(self):
        pass

class Morpher:
    def __init__(self,leftImage,leftTriangles,rightImage,rightTriangles):
        if isinstance(leftImage, np.array):
            for element in leftImage.flatten():
                if isinstance(element,np.uint8) == False:
                    raise TypeError("leftImage must be type uint8")
        else:
            raise TypeError("leftImage must be an array")
        if isinstance(rightImage, np.array):
            for element in rightImage.flatten():
                if isinstance(element,np.uint8) == False:
                    raise TypeError("leftImage must be type uint8")
        else:
            raise TypeError("leftImage must be an array")
        for item in leftTriangles:
            if isinstance(item,Triangle) == False:
                raise TypeError("leftTriangles must be type Triangle")
        for item in rightTriangles:
            if isinstance(item, Triangle) == False:
                raise TypeError("rightTriangles must be type Triangle")

        self.leftImage = leftImage
        self.leftTriangles = leftTriangles
        self.rightImage = rightImage
        self.rightTriangles = rightTriangles

    def getImageAtAlpha(self, alpha):
        #calculate middle triangle that corresponds to the given a
        #transform left triangle onto the target triangle
        #transform the right triangle onto the right triangle
        pass


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from pprint import pprint as pp
    t = np.array([[np.float64(12.2),np.float64(12.2)],
                  [np.float64(3.21),np.float64(4.09)],
                  [np.float64(5.012),np.float64(6.112)]])
    pp(np.shape(t))
    new_triangle = Triangle(t)