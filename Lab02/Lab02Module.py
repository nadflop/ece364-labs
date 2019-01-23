#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 1/23
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line

# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab02")

def getCodeFor(stateName: str) -> list:
    state = stateName.split()
    DataText = os.path.join(DataPath, "zip.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    zipCode = [ ] #list for the zipcodes

    for i in range(0, len(rawData)):
        newData = str(rawData[i]).split(' ')
        if len(state) > 1:
            if str(newData[0]).lower() == state[0].lower():
                if str(newData[1]).lower() == state[1].lower():
                    p = newData[-1].split('\n')
                    if i + 1 != len(rawData):
                        z = p.pop()  # to remove the '\n'
                        z = p.pop()  # get the list as string
                    zipCode.append(z)
        else:
            if str(newData[0]).lower() == stateName.lower():
                p = newData[-1].split('\n')
                if i + 1 != len(rawData):
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
    zipCd = [ ]
    zipCd = getCodeFor(stateName)

    DataText = os.path.join(DataPath, "coordinates.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    maxLong = -99999.00

    for j in range(2, len(rawData)):
        coorData = str(rawData[j]).split('             ')
        cr = coorData[-1].split('\n')
        if j + 1 != len(rawData):
            q = cr.pop()
            q = cr.pop()
        for item in zipCd:
            if q in item:
                val = str(coorData[0]).split('         ')
                new = val.pop()
                maxLong = max(float(new), maxLong)

    return maxLong

#-------------------------------------bonus-----------------------------------------
def getMatrixSum(startRowIndex, endRowIndex, startColumnIndex, endColumnIndex):
    #two for loop to iterate through row and column
    DataText = os.path.join(DataPath, "matrix.dat")
    with open(DataText) as f:
        rawData = f.readlines()  # read and return line in files seperately

    pass


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    z = getCodeFor('OHIO')
    print(z)
    c = getMinLattitude('Ohio')
    print(c)
    d = getMaxLongitude('Ohio')
    print(d)