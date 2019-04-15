#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import numpy as np
import imageio
from scipy import interpolate, spatial
from scipy.spatial import Delaunay
from PIL import ImageDraw, Image
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
        #got this algorithm from stackoverflow
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
                if xc>x[i]:
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

    def _process(self, src, dest):

        A = np.array([
            [src.vertices[0][0], src.vertices[0][1], 1, 0, 0, 0],
            [0, 0, 0, src.vertices[0][0], src.vertices[0][1], 1],
            [src.vertices[1][0], src.vertices[1][1], 1, 0, 0, 0],
            [0, 0, 0, src.vertices[1][0], src.vertices[1][1], 1],
            [src.vertices[2][0], src.vertices[2][1], 1, 0, 0, 0],
            [0, 0, 0, src.vertices[2][0], src.vertices[2][1], 1],
        ], dtype='float64')
        b = np.reshape(dest, (6, 1))
        h = np.linalg.solve(A, b)
        H = np.vstack([np.reshape(h, (2, 3)), [0, 0, 1]])

        return H

    def getImageAtAlpha(self, alpha):
        #create empty array of same dimensions as image
        image1 = np.empty(self.leftImage.shape, dtype = 'float64')
        target = []
        #create the middle triangle
        for i in range(len(self.leftTriangles)):
            target.append(Triangle((1-alpha)*self.leftTriangles[i].vertices + alpha*self.rightTriangles[i].vertices))
        #do affine transformation for left triangle to the target triangle
        xrange1 = np.arange(0, self.leftImage.shape[0])
        yrange1 = np.arange(0, self.leftImage.shape[1])
        spline_left = interpolate.RectBivariateSpline(xrange1, yrange1, self.leftImage,kx=1,ky=1)
        xrange2 = np.arange(0, self.rightImage.shape[0])
        yrange2 = np.arange(0, self.rightImage.shape[1])
        spline_right = interpolate.RectBivariateSpline(xrange2, yrange2, self.rightImage,kx=1,ky=1)

        for j in range(len(self.leftTriangles)):
            #find forward projection
            H_left = self._process(self.leftTriangles[j],target[j].vertices)
            H_right = self._process(self.rightTriangles[j],target[j].vertices)
            #find inverse projection
            hInv_left = np.linalg.inv(H_left)
            hInv_right = np.linalg.inv(H_right)
            #iterate over the points in the target triangle
            for points in target[j].getPoints():
                c = np.array([points[0],points[1],1])
                c = np.reshape(c, (3,1))
                orig_left = np.matmul(hInv_left,c)
                orig_right = np.matmul(hInv_right,c)
                image1[int(points[1]),int(points[0])] = np.round((1-alpha)*spline_left.ev(orig_left[1],orig_left[0])
                                               + (alpha)*spline_right.ev(orig_right[1],orig_right[0]))

        return image1.astype('uint8')
        #spline = interpolate.RectBivariateSpline(x, y, self.leftImage, kx = 1, ky = 1)
        #print(spline)
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    ...
    '''
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
    actualImage = morpher.getImageAtAlpha(0.75)
    #num_photos, x, y, z = actualImage.shape
    #morph_list = []
    #from PIL import Image as im
    #for i in range(0, num_photos):
    #    image = im.fromarray(actualImage[i,:,:,:], 'RGB')
    #    morph_list.append(actualImage[i,:,:,:])
    #    image.save('photo.jpg')
    #    image.show()
    #    plt.show()
    print(actualImage.shape)
    imageio.imwrite('test.png', actualImage)
    '''