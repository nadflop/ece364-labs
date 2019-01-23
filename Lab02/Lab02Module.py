#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 1/11
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab02")

def getCodeFor(stateName: str) -> list:
    DataText = os.path.join(DataPath, "zip.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    zipCode = [ ] #list for the zipcodes

    for i in range(0, len(rawData)):
        newData = str(rawData[i]).split(' ')
        if str(newData[0]) == stateName:
            p = newData[-1].split('\n')
            z = p.pop()  # to remove the '\n'
            z = p.pop()  # get the list as string
            zipCode.append(z)

    zipCode.sort()
    return zipCode

#-----------------------problem 2----------------------------------------

def getMinLattitude(stateName: str) -> float:
    zipCode = [ ]
    zipCode = getCodeFor(stateName)

    DataText = os.path.join(DataPath, "coordinates.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    minLat = 100.00

    for j in range(2, len(rawData)):
        coorData = str(rawData[j]).split(' ')
        cr = str(coorData[-1]).split('\n')
        if j + 1 != len(rawData):
            q = cr.pop()
            q = cr.pop()
        for item in zipCode:
            if q in item:
                minLat = min(float(coorData[0]), minLat)

    return minLat

#----------------------------problem 3-----------------------------------

def getMaxLongitude(stateName: str) -> float:
    zipCode = [ ]
    zipCode = getCodeFor(stateName)

    DataText = os.path.join(DataPath, "coordinates.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    maxLong = -1000.00

    for j in range(2, len(rawData)):
        coorData = str(rawData[j]).split('             ')
        cr = coorData[-1].split('\n')
        if j + 1 != len(rawData):
            q = cr.pop()
            q = cr.pop()
        for item in zipCode:
            if q in item:
                val = str(coorData[0]).split('         ')
                new = val.pop()
                maxLong = max(float(new), maxLong)

    return maxLong


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    z = getCodeFor('Florida')
    print(z)
    c = getMinLattitude('Florida')
    print(c)
    d = getMaxLongitude('Florida')
    print(d)