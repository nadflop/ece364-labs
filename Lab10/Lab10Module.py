#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from Lab10.measurement import calculateDistance
import re
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab10")


def getCost(sourceZip: str, destinationZip:str):
    DataText = os.path.join(DataPath, 'coordinates.dat')
    with open(DataText, "r") as f:
        data = [line.split(',') for line in f.read().splitlines()]
    lat1 = 0.0
    lat2 = 0.0
    lon1 = 0.0
    lon2 = 0.0
    for item in data[1:]:
        if sourceZip in item[0]:
            lat1  = item[2].strip().replace(' ', '').replace('"', '')
            lon1 = item[3].strip().replace(' ', '').replace('"', '')
        elif destinationZip in item[0]:
            lat2 = item[2].strip().replace(' ', '').replace('"', '')
            lon2 = item[3].strip().replace(' ', '').replace('"', '')

    dist = calculateDistance((float(lat1),float(lon1)), (float(lat2), float(lon2)))
    cost = dist * 0.01
    return round(cost, 2)

def loadPackages():
    DataText = os.path.join(DataPath, 'packages.dat')
    temp = []
    with open(DataText, "r") as f:
        data = [line.split(',') for line in f.read().splitlines()]
    for lines in data[1:]:
        pass


class Package:

    def __init__(self, source, destination):
        zip_source = re.findall(r'\s([0-9]{5})', source)
        zip_dest = re.findall(r'\s([0-9]{5})', destination)
        self.source = source
        self.destination = destination
        self.cost = getCost(zip_source,zip_dest)

    def __str__(self):
        price = format(self.cost, ".2f")
        zip_source = re.findall(r'\s([0-9]{5})', self.source)
        zip_dest = re.findall(r'\s([0-9]{5})', self.destination)
        return f"{zip_source} => {zip_dest}, Cost ${price}"

    def __eq__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost == other.cost

    def __lt__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost < other.cost

    def __gt__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost > other.cost

    def __le__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost <= other.cost

    def __ge__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost >= other.cost

    def __ne__(self, other):
        if isinstance(other, Package) == False:
            raise TypeError("Argument must be type Package")
        return self.cost != other.cost

class PackageGroup:
    def __init__(self, company):
        self.company = company

    def __str__(self):
        pck = format(self.packages, "3d")
        price = format(self.cost, ".2f")
        return f"{self.company}, {pck} Shipments, Cost ${price}"

    def getByZip(self):
        pass

def getNumberPattern():
    pass

def getTagPattern():
    pass



#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    print(getCost('35179', '54729'))
    print(loadPackages())
    #test1 = Package('3 N. Ocean Court, Victoria, TX 77904', '8 Magnolia Lane, Nanuet, NY 10954')

