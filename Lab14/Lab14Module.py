#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 3/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from Lab14.measurement import calculateDistance
import re
from enum import Enum
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab14")

class Direction(Enum):
    Incoming = 1
    Outgoing = 2
    Both = 3

class Leg:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        zip_source = re.search(r'\s([0-9]{5})', self.source)
        zip_dest = re.search(r'\s([0-9]{5})', self.destination)
        return f"{zip_source.group()} => {zip_dest.group()}"

    def calculateLength(self, locationMap):
        zip_source = re.search(r'\s([0-9]{5})', self.source)
        zip_dest = re.search(r'\s([0-9]{5})', self.destination)
        lat1 , lon1 = locationMap.get(zip_source.group().strip())
        lat2, lon2 = locationMap.get(zip_dest.group().strip())
        dist = calculateDistance((float(lat1),float(lon1)), (float(lat2),float(lon2)))
        return round(dist,2)

class Trip:
    def __init__(self, person, leg):
        self.person = person
        self.leg = leg

    def calculateLength(self, locationMap):
        zip_source = []
        zip_dest = []
        for item in self.leg:
            i = re.search(r'\s([0-9]{5})', item.source)
            zip_source.append(i.group().strip())
            i = re.search(r'\s([0-9]{5})', item.destination)
            zip_dest.append(i.group().strip())
        dist = 0.00

        for item in zip_source:
            if type(item) != None:
                lat = locationMap.get(item)
                lat2 = locationMap.get(zip_dest[zip_source.index(item)])
                if lat != None and lat2 != None:
                    dist += calculateDistance((float(lat[0]), float(lat[1])), (float(lat2[0]), float(lat2[1])))
        return round(dist, 2)

    def getLegsByZip(self, zipcode, direction):
        result = list()
        if direction is Direction.Incoming: #zip_dest
            for item in self.leg:
                if zipcode in item.destination:
                    result.append(item)
        elif direction is Direction.Outgoing: #zip_source
            for item in self.leg:
                if zipcode in item.source:
                    result.append(item)
        elif direction is Direction.Both: #zip either
            for item in self.leg:
                if zipcode in item.source:
                    result.append(item)
                elif zipcode in item.destination:
                    result.append(item)
        return result

    def getLegsByState(self, state, direction):
        result = list()
        if direction is Direction.Incoming:  # zip_dest
            for item in self.leg:
                if state in item.destination:
                    result.append(item)
        elif direction is Direction.Outgoing:  # zip_source
            for item in self.leg:
                if state in item.source:
                    result.append(item)
        elif direction is Direction.Both:  # zip either
            for item in self.leg:
                if state in item.source:
                    result.append(item)
                elif state in item.destination:
                    result.append(item)
        return result

    def __add__(self, other):
        if isinstance(other, Leg):
            zip_source = other.leg[0].source
            zip_dest = other.leg[-1].destination
            if zip_source != zip_dest:
                raise ValueError("First zip source must be the same as the zip destination for the last one")
            temp = []
            temp.append(self.leg)
            temp.append(other)
            return Trip(self.person, temp)
        elif isinstance(other, Trip):
            if self.person != other.person:
                raise ValueError("Must be the same person")
            temp = []
            temp.append(self.leg)
            temp.append(other.leg)
            return Trip(self.person, temp)
        else:
            raise TypeError("Argument must be either a Leg or Trip")

class RoundTrip(Trip):
    def __init__(self, *args, **kwargs):
        args = [v for v in kwargs.values()]
        if type(args[0]) is Trip:
            Trip.__init__(self, args[0].person, args[1].leg)
            if len(self.leg < 2):
                raise ValueError("Legs must be a round trip")
            else:
                zip_source = self.leg[0].source
                zip_dest = self.leg[-1].destination
                if zip_source != zip_dest:
                    raise ValueError("First zip source must be the same as the second one")
        else:
            Trip.__init__(self, args[0], args[1])
            if len(self.leg < 2):
                raise ValueError("Legs must be a round trip")
            else:
                zip_source = self.leg[0].source
                zip_dest = self.leg[-1].destination
                if zip_source != zip_dest:
                    raise ValueError("First zip source must be the same as the zip destination for the last one")

def getShortestTrip(source, destination, stops):
    DataText = os.path.join(DataPath, 'locations.dat')
    with open(DataText, "r") as f:
        data = [line.split(',') for line in f.read().splitlines()]
    lat1 = 0.0
    lat2 = 0.0
    lon1 = 0.0
    lon2 = 0.0
    zip_source = re.search(r'\s([0-9]{5})', source)
    dist = []
    for element in stops:
        zip_dest = re.search(r'\s([0-9]{5})', element)
        for item in data[1:]:
            if zip_source.group().strip() in item[0]:
                lat1 = item[2].strip().replace(' ', '').replace('"', '')
                lon1 = item[3].strip().replace(' ', '').replace('"', '')
            if zip_dest.group().strip() in item[0]:
                lat2 = item[2].strip().replace(' ', '').replace('"', '')
                lon2 = item[3].strip().replace(' ', '').replace('"', '')
        dist.append(calculateDistance((float(lat1), float(lon1)), (float(lat2), float(lon2))))

    best = dist[0]
    leg1 = 0
    for item in dist[1:]:
        best = min(item, best)
        leg1 = dist.index(item)

    dist = []
    zip_dest = re.search(r'\s([0-9]{5})', destination)
    for element in stops:
        zip_source = re.search(r'\s([0-9]{5})', element)
        for item in data[1:]:
            if zip_source.group().strip() in item[0]:
                lat1 = item[2].strip().replace(' ', '').replace('"', '')
                lon1 = item[3].strip().replace(' ', '').replace('"', '')
            if zip_dest.group().strip() in item[0]:
                lat2 = item[2].strip().replace(' ', '').replace('"', '')
                lon2 = item[3].strip().replace(' ', '').replace('"', '')
        dist.append(calculateDistance((float(lat1), float(lon1)), (float(lat2), float(lon2))))

    best = dist[0]
    leg2 = 0
    for item in dist[1:]:
        best = min(item, best)
        leg2 = dist.index(item)

    l1 = Leg(source, stops[leg1])
    l2 = Leg(stops[leg2], destination)
    return Trip("", [l1,l2])

def getTotalDistanceFor(person):
    dist = 0.0
    DataText = os.path.join(DataPath, 'trips.dat')
    with open(DataText, "r") as f:
        data = [line.split('"') for line in f.read().splitlines()]
    DataText = os.path.join(DataPath, 'locations.dat')
    with open(DataText, "r") as f:
        temp = [line.split('"') for line in f.read().splitlines()]
    for lines in data:
        if person in lines[1].strip():
            if len(lines) == 7:
                locationMap = {}
                lat1 = 0.0
                lon1 = 0.0
                lat2 = 0.0
                lon2 = 0.0
                source = lines[3]
                zip_source = re.search(r'\s([0-9]{5})', source)
                dest = lines[5]
                zip_dest = re.search(r'\s([0-9]{5})', dest)
                l1 = Leg(source,dest)
                for item in temp[1:]:
                    if zip_source.group().strip() in item[0]:
                        lat1 = item[2].strip().replace(' ', '').replace('"', '')
                        lon1 = item[3].strip().replace(' ', '').replace('"', '')
                    if zip_dest.group().strip() in item[0]:
                        lat2 = item[2].strip().replace(' ', '').replace('"', '')
                        lon2 = item[3].strip().replace(' ', '').replace('"', '')

                locationMap['zip_source'] = (lat1, lon1)
                locationMap['zip_dest'] = (lat2, lon2)

                dist += l1.calculateLength(locationMap)
            else:
                leg = []
                source = []
                dest = []
                for element in lines:
                    if lines.index(element) % 2 != 0:
                        leg.append(element)
                for i in range(len(leg)):
                    try:
                        locationMap = {}
                        lat1 = 0.0
                        lon1 = 0.0
                        lat2 = 0.0
                        lon2 = 0.0
                        source = lines[3]
                        zip_source = re.search(r'\s([0-9]{5})', leg[i])
                        dest = lines[5]
                        zip_dest = re.search(r'\s([0-9]{5})', leg[i+1])
                        l1 = Leg(leg[i], leg[i+1])
                        for item in temp[1:]:
                            if zip_source.group().strip() in item[0]:
                                lat1 = item[2].strip().replace(' ', '').replace('"', '')
                                lon1 = item[3].strip().replace(' ', '').replace('"', '')
                            if zip_dest.group().strip() in item[0]:
                                lat2 = item[2].strip().replace(' ', '').replace('"', '')
                                lon2 = item[3].strip().replace(' ', '').replace('"', '')

                        locationMap['zip_source'] = (lat1, lon1)
                        locationMap['zip_dest'] = (lat2, lon2)

                        dist += l1.calculateLength(locationMap)
                    except:
                        pass


def getRoundTripCount():
    pass

def getTrafficCount(**kwargs):
    pass

def getClosestIn(sourceState, destinationState):
    pass

#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
   '''
   temp = {}
   temp['28655'] = (float(36.427702), float(-92.11109))
   temp['01450'] = (float(36.427702), float(-71.55109))
   l = Leg("Morganton, NC 28655", "Groton, MA 01450")
   print(l.calculateLength(temp))
   l1 = Leg("Packwooo, WA 98361", "Naples, FL 34108")
   l2 = Leg("Naples, FL 34108", "Hillard, FL 32046")
   l3 = Leg("Hillard, FL 32046", "Putnam Station, NY 12861")
   t = Trip("Taylor, Brian", [l1,l2,l3])
   loc = {}
   loc['98361'] = (float(36.427702), float(-92.11109))
   loc['34108'] = (float(36.427702), float(-71.55109))
   loc['12861'] = (float(11.430201), float(-51.02109))
   print(t.calculateLength(loc))
   f1 = t.getLegsByZip("34108", Direction.Both)
   stop = ["Plantation, FL 33317", "Johnstown, OH 43031", "Summer, MO 64681"]
   p = getShortestTrip("Wallingford, PA 19086", "Packwood, WA 98361", stop)
   print(p)
   getTotalDistanceFor("Garcia, Martha")
   '''