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
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab13")



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

class Package:

    def __init__(self, company, source, destination):
        zip_source = re.search(r'\s([0-9]{5})', source)
        zip_dest = re.search(r'\s([0-9]{5})', destination)
        self.company = company
        self.source = source
        self.destination = destination
        self.cost = getCost(str(zip_source.group()).strip(),str(zip_dest.group()).strip())

    def __str__(self):
        price = format(self.cost, ".2f")
        zip_source = re.search(r'\s([0-9]{5})', self.source)
        zip_dest = re.search(r'\s([0-9]{5})', self.destination)
        return f"{str(zip_source.group()).strip()} => {str(zip_dest.group()).strip()}, Cost = ${price}"

    def __add__(self, other):
        if isinstance(self,Package) == False:
            raise TypeError("Argument must be an instance of Package")
        elif isinstance(other,Package) == False:
            raise TypeError("Argument (other) must be an instance of Package")
        else:
            if self.company != other.company:
                raise ValueError("Packages must be in the same company")
            else:
                temp = []
                temp.append(self)
                temp.append(other)
                new_comp = PackageGroup(self.company,temp)
                return new_comp

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
    def __init__(self, company, packages):
        self.company = company
        #temp = sorted(packages, key= self.cost)
        self.packages = packages
        #self.getPackage(self.company)
        self.cost = self.getCost(self.packages)
    '''
    def __str__(self):
        pck = format(self.packages, "3d")
        price = format(self.cost, ".2f")
        return f"{self.company}, {pck} Shipments, Cost ${price}"
    '''
    def __contains__(self, item):
        if isinstance(item, Package) == False:
            raise TypeError("Must be type Package")
        pass

    def getPackage(self, name):
        list_packages = loadPackages()
        result = 0
        for item in list_packages:
            if name in item[0]:
                result =  item[1]

        return result

    def getCost(self, list_packages):
        result = 0.0
        #list_packages = loadPackages()
        for item in list_packages:
            pass
        return result

    def getByZip(self, zip_code):
        pass

    def getByState(self, state):
        pass

    def getByCity(self, city):
        pass

def loadPackages():
    DataText = os.path.join(DataPath, 'packages.dat')
    temp = []
    company = {}
    with open(DataText, "r") as f:
        data = [line.split('"') for line in f.read().splitlines()]
    #data =
    for lines in data[1:]:
        temp.append([lines[1],lines[3],lines[5]])

    for item in temp:
        name = item[0]
        zip_source = re.search(r'\s([0-9]{5})', item[1])
        zip_dest = re.search(r'\s([0-9]{5})', item[2])
        cost = getCost(str(zip_source.group()).strip(), str(zip_dest.group()).strip())
        package = Package(name, item[1],item[2])
        #print(package)

        if name in company:
            #new_shipment = 1 + company[name][0]
            #new_cost = float(cost + company[name][1])
            if len(company[name] == 1):
                new_package = package + company[name]
            else:
                pass
            company[name] = new_package
        else:

            #shipment = 1
            company[name] = package
            #company[name] = [shipment,cost]

    result = []
    
    for items in company.keys():
        temp1 = company.get(items)
        temp2 = [items, temp1[0],temp1[1]]
        result.append(temp2)

    company = sorted(result, key= lambda x:x[0])


    return company




#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
   from pprint import pprint as pp
   #pp(getCost('99337','35115'))
   pp(loadPackages())
   pack1 = Package("Domain Lands", "9384 Gonzales St., Lansdowne, PA 19050", "8693 Grant Lane, Dedham, MA 02026")
   pack2 = Package("Domain Lands", "947 Mayfield Rd., Elmhurst, NY 11373", "66316 Country Club Street, Kissimmee, FL 34741")
   print(pack1)
   print(pack2)
   troe = PackageGroup('Domain Lands', [pack1,pack2])
   print(troe)

