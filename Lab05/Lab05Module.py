#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/13
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from collections import namedtuple
from collections import Counter
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab05")

def techData(key: int):
    DataText = os.path.join(DataPath, 'people.dat')
    techDict = { }

    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]
    if key == 0: #name as key, ID as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[name] = item[-1]
    elif key == 1:#ID as key, name as value
        for item in data[2:]:
            name = item[0] + ' ' + item[1]
            techDict[item[-1]] = name

    return techDict

def getPin():
    DataText = os.path.join(DataPath, 'pins.dat')
    pins = namedtuple("pins", ["date", "code"])
    pinsDict = {}

    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]
    #get the dates first
    date = data[1]
    for item in data[3:]:
        name = item[0]
        for code in item[1:]:
            if name in pinsDict:
                pinsDict[name] += [pins(date[item.index(code)],code)]
            else:
                pinsDict[name] = [pins(date[item.index(code)],code)]

    return pinsDict

def getLog(key: int):
    DataText = os.path.join(DataPath, 'log.dat')
    logDict = {}
    log = namedtuple("log", ["date", "place"])
    access = namedtuple("access", ["place", "ID"])

    with open(DataText) as f:
        data = [line.split() for line in f.read().splitlines()]

    if key == 0:
        for item in data[3:]:
            employeeID = item[-1]
            place = item[2]
            date = item[0]
            if employeeID in logDict:
                logDict[employeeID] += [log(date, place)]
            else:
                logDict[employeeID] = [log(date,place)]
    elif key == 1:
        for item in data[3:]:
            employeeID = item[-1]
            place = item[2]
            date = item[0]
            if date in logDict:
                logDict[date] += [employeeID]
            else:
                logDict[date] = [employeeID]
    elif key == 2:
        for item in data[3:]:
            employeeID = item[-1]
            place = item[2]
            date = item[0]
            if date in logDict:
                logDict[date] += [place]
            else:
                logDict[date] = [place]

    return logDict

def getPinUser(id):
    peopleDict = techData(0)
    pinsDict = getPin()
    data = set()


    for employeeID in id:
        data.add(pinsDict.get(employeeID))


    return data

def getPinFor(name, date):
    peopleDict = techData(0)
    pinsDict = getPin()
    code = ''

    try:
        employeeID = peopleDict.get(name)
    except:
        raise ValueError("name doesn't exists")

    try:
        data = pinsDict.get(employeeID)
        for elements in data:
            if date == elements:
                i = data.index(elements)
                code = data[i+1]
    except:
        raise ValueError("date doesn't exists")

    return code

def getUserOf(pin,date):
    peopleDict = techData(1)
    pinsDict = getPin()
    name = ''
    employeeID = ''

    try:
        for k,v in pinsDict.items():
            for items in v:
                if items == date:
                    i = v.index(items)
                    if v[i+1] == pin:
                        employeeID = k
    except:
        raise ValueError("date/pin doesn't exists")

    name = peopleDict.get(employeeID)
    return name

def getUsersOn(date):
    peopleDict = techData(1)
    logDict = getLog(1)
    pinsDict = getPin()
    name = set()

    try:
        logs = logDict.get(date)

    except:
        raise ValueError("date doesn't exist")

    for id in logs:
        employeeID = getUserOf(id, date)
        name.add(employeeID)

    return name

def getResourcesOn(date):
    logDict = getLog(2)
    result = set()

    try:
        value = logDict.get(date)
        for item in value:
            result.add(item)
    except:
        raise ValueError("date doesn't exist")

    return result

def getMostActiveUserOn(dates: set):
    peopleDict = techData(1)
    logDict = getLog(1)
    pinsDict = getPin()
    name = set()
    user = []
    temp = Counter()
    try:
        for date in dates:
            logs = logDict.get(date)
            if len(temp) == 0:
                temp = Counter(logs)
            else:
                temp += Counter(logs)

    except:
        raise ValueError("date doesn't exist")

    for item in temp.elements():
        user = temp.most_common(1)


def getMostAccessedOn(dates):
    pass

def getAbsentUsers():
    peopleDict = techData(1)
    logDict = getLog(1)
    t1 = set(peopleDict.keys())  # set of all techID
    #user = getPinUser(t1)
    t2 = set()
    result = set()

    for v in logDict.values():
        for value in v:
            t2.add(value)

    temp = t1.difference(t2)

    if len(temp) != 0:
        for item in temp:
            result.add(peopleDict.get(item))

    return result

def getDifference():
    pass


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    from pprint import pprint as pp
    print(getPin())
    getPinFor('Bailey, Catherine', '03/18')
    getUserOf('710','03/18')
    print(getLog(1))
    getUsersOn('04/15')
    #pp(getResourcesOn('03/03'))
    pp(getMostActiveUserOn({'01/05','01/27'}))
    getAbsentUsers()