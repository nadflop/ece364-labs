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
from scipy.spatial import Delaunay
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

def loadTriangles(leftPointFilePath, rightPointFilePath):
    DataPath1 = os.path.expanduser(leftPointFilePath)
    DataPath2 = os.path.expanduser(rightPointFilePath)
    array1 = []
    with open(DataPath1, "r") as f:
        data = [line.strip().split(' ') for line in f.read().splitlines()]
    for element in data:
        array1.append([np.float64(element[0]),np.float64(element[-1])])
    points1 = np.array(array1)
    left_tri = Delaunay(points1) #create the left triangle

    array2 = []
    with open(DataPath2, "r") as f:
        data = [line.strip().split(' ') for line in f.read().splitlines()]
    for element in data:
        array2.append([np.float64(element[0]),np.float64(element[-1])])

    leftTriangles = []
    rightTriangles = []
    for coord in points1[left_tri.simplices]:
        leftTriangles.append(Triangle(coord))
        temp = []
        for element in coord:
            for item in array1:
                if element[0] == item[0] and element[1] == item[1]:
                    temp.append(array2[array1.index(item)])
        temp = np.array(temp)
        rightTriangles.append(Triangle(temp))

    return leftTriangles, rightTriangles

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
        for element in leftImage.flatten():
            if isinstance(element,np.uint8) == False:
                raise TypeError("leftImage must be type uint8")
        for element in rightImage.flatten():
            if isinstance(element,np.uint8) == False:
                raise TypeError("leftImage must be type uint8")
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
        x_m = []
        y_m = []
        middle_tri = []
        for i in range(0, len(self.leftTriangles)):
            x_m = []
            y_m = []
            for j in range(0,3):
                x_m.append((1-alpha)*self.leftTriangles[i].vertices[j][0] + alpha*(self.rightTriangles[i].vertices[j][0]))
                y_m.append((1 - alpha) * self.leftTriangles[i].vertices[j][1] + alpha * (self.rightTriangles[i].vertices[j][1]))
            temp = [[x_m[0],y_m[0]],[x_m[1],y_m[1]],[x_m[2],y_m[2]]]
            temp = np.array(temp)
            middle_tri.append(Triangle(temp))
        
        # for point in tri:
        #    print(point)


#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from pprint import pprint as pp
    t = np.array([[np.float64(12.2),np.float64(12.2)],
                  [np.float64(3.21),np.float64(4.09)],
                  [np.float64(5.012),np.float64(6.112)]])
    pp(np.shape(t))
    new_triangle = Triangle(t)
    points_left = "~ee364/DataFolder/Lab12/TestData/points.left.txt"
    points_right = "~ee364/DataFolder/Lab12/TestData/points.right.txt"
    leftTriangles, rightTriangles = loadTriangles(points_left, points_right)
    TestFolder = "~ee364/DataFolder/Lab12/TestData/"
    leftImagePath = os.path.join(TestFolder, 'LeftGray.png')
    rightImagePath = os.path.join(TestFolder, 'RightGray.png')
    expectedPath = os.path.join(TestFolder, 'Alpha50Gray.png')
    from imageio import imread as libread
    def imread(filePath):
        startImage = libread(filePath)
        return np.array(startImage)
    leftImage = imread(leftImagePath)
    rightImage = imread(rightImagePath)
    morpher = Morpher(leftImage, leftTriangles, rightImage, rightTriangles)
    actualImage = morpher.getImageAtAlpha(0.50)