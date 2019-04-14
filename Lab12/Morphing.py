#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
import numpy as np
import imageio
from scipy import interpolate, spatial
from scipy.spatial import Delaunay
from matplotlib.path import Path
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
        #x, y = np.meshgrid(np.arange(300), np.arange(300))
        #x, y = x.flatten(), y.flatten()
        #points = np.vstack((x,y)).T
        #p = Path(self.vertices)
        #grid = p.contains_point(points)
        #mask = grid.reshape(300,300)
        #temp = np.vstack((self.vertices[1:],self.vertices[:1]))
        #test = temp - self.vertices
        #m = test[:,1]/test[:,0]
        #c = self.vertices[:,1]-m*self.vertices[:,0]
        #print(self.vertices)
        #temp = [tuple(i) for i in self.vertices]
        #print(temp)
        #x, y = np.meshgrid(np.arange(300), np.arange(300))
        #x, y = x.flatten(), y.flatten()
        #points = np.vstack((x,y)).T
        #print(len(points))
        #p = Path(temp)
        #print(p)
        #grid = p.contains_point(points)
        #mask = grid.reshape(300,300)
        #print(mask)
        #xval = ()
        #area = 1/2 * abs(self.vertices[0][0](self.vertices[1][1]-self.vertices[2][1])
         #                + self.vertices[1][0](self.vertices[2][1]-self.vertices[0][1])
         #                + self.vertices[2][0](self.vertices[0][1]-self.vertices[1][1]))
        x = np.array((self.vertices[0][0],self.vertices[1][0],self.vertices[2][0]),dtype='float64')
        y = np.array((self.vertices[0][1],self.vertices[1][1],self.vertices[2][1]),dtype='float64')
        #possible range of coordinates
        x_range = np.arange(np.min(x),np.max(x)+1)
        y_range = np.arange(np.min(y),np.max(y)+1)
        X, Y = np.meshgrid(x_range,y_range) #fill in 1 for the triangle
        xc = np.mean(x)
        yc = np.mean(y)
        #set points outside the triangle as 0
        triangle = np.ones(X.shape,dtype=bool)
        for i in range(3):
            j = (i+1)%3
            if x[i] == x[j]:
                if xc>x.all():
                    include = (X > x[i])
                else:
                    include = (X < x[i])
            else:
                slope = (y[j]-y[i])/(x[j]-x[i])
                poly = np.poly1d([slope,y[i]-x[i]*slope])
                if yc > poly(xc):
                    include = (Y > poly(X))
                else:
                    include = (Y < poly(X))
            triangle*=include

        result = [[X[triangle][i],Y[triangle][i]] for i in range(0,len(X[triangle]))]
        result = np.array(result,dtype = 'float64')
        return result

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
        '''
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

        for i in range(0, len(self.leftTriangles)):

            A = np.array([
                        [middle_tri[i].vertices[0][0],middle_tri[i].vertices[0][1],1,0,0,0],
                        [0,0,0,middle_tri[i].vertices[0][0],middle_tri[i].vertices[0][1],1],
                        [middle_tri[i].vertices[1][0], middle_tri[i].vertices[1][1], 1, 0, 0, 0],
                        [0, 0, 0, middle_tri[i].vertices[1][0], middle_tri[i].vertices[1][1], 1],
                        [middle_tri[i].vertices[2][0], middle_tri[i].vertices[2][1], 1, 0, 0, 0],
                        [0, 0, 0, middle_tri[i].vertices[2][0], middle_tri[i].vertices[2][1], 1],
                        ], dtype = 'float64')
            b = np.reshape(self.leftTriangles[i].vertices, (6,1))
            print(b)
            h = np.linalg.solve(A, b)
            H = np.vstack([np.reshape(h, (2,3)), [0,0,1]])
        '''
        #create empty array of same dimensions as image
        image1 = np.empty(self.leftImage.shape, dtype = 'float64')
        image2 = np.empty(self.rightImage.shape, dtype = 'float64')
        #interpolate left and right image to find the middle one
        #for i in range(0,1):
        #    x = np.arange(np.amin(self.leftTriangles), np.amax())
        #    spline = interpolate.RectBivariateSpline(x, y, z, kx = 1, ky = 1)

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    from pprint import pprint as pp
    t = np.array([[np.float64(0.0),np.float64(0.0)],
                  [np.float64(0.0),np.float64(5.0)],
                  [np.float64(5.0),np.float64(0.0)]])
    pp(np.shape(t))
    new_triangle = Triangle(t)
    pp(new_triangle.getPoints())
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