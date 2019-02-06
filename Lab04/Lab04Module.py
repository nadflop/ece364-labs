#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/6
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
from collections import namedtuple
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################
DataPath = os.path.expanduser("~ee364/DataFolder/Lab04")

#--------------------------------------------------problem 1------------------------------------------------------------
def getDifference(provider1: str, provider2: str) -> set:
    set1 = set()
    filename1 = provider1 + '.dat'
    DataFile = os.path.join(DataPath, 'providers')
    Data1Text = os.path.join(DataFile, filename1)
    set2 = set()
    filename2 = provider2 + '.dat'
    Data2Text = os.path.join(DataFile, filename2)

    try:
        with open(Data1Text) as f:
            data = [line.split(',') for line in f.read().splitlines()]
        for item in data[3:]:
            board = item[0].strip()
            set1.add(board)
    except:
        raise FileNotFoundError("File for provider1 doesn't exists")

    try:
        with open(Data2Text) as f:
            data = [line.split(',') for line in f.read().splitlines()]
        for item in data[3:]:
            board = item[0].strip()
            set2.add(board)
    except:
        raise FileNotFoundError("File for provider 2 doesn't exists")

    result = set1.difference(set2)

    return result
#--------------------------------------------------problem 2------------------------------------------------------------
def getPriceOf(sbc: str, provider: str) -> float:
    price = 0.00
    filename = provider + '.dat'
    DataFile = os.path.join(DataPath, 'providers')
    DataText = os.path.join(DataFile, filename)

    try:
        with open(DataText) as f:
            data = [line.split(',') for line in f.read().splitlines()]
        for item in data[3:]:
            if item[0].strip() == sbc: #get the price
                p = item[1].replace('$', '')
                price = p.strip()
    except:
        raise FileNotFoundError("File doesn't exist")

    if price == 0.00:
        raise ValueError("The provider doesn't carry the SBC requested")

    return float(price)
#--------------------------------------------------problem 3------------------------------------------------------------
def checkAllPrices(sbcSet: set) -> dict:
    sbc = namedtuple("sbc", ["minPrice", "provider"])
    DataFile = os.path.join(DataPath, 'providers')
    filename = [ ]
    resultDict = { }

    for root, dirs, files in os.walk(DataFile):
        for fl in files:
            filename.append(fl)

    for provider in filename:
        DataText = os.path.join(DataFile, provider)
        with open(DataText) as f:
            data = [line.split(',') for line in f.read().splitlines()]
        for element in sbcSet:
            for item in data[3:]:
                if item[0].strip() == element: #get the price
                    p = item[1].replace('$', '')
                    price = float(p.strip())
                    if element in resultDict:
                        if min(resultDict[element].minPrice, price) == price:
                            value = sbc(min(resultDict[element].minPrice, price),provider.replace('.dat', ''))
                            resultDict[element] = value
                    else:
                        resultDict[element] = sbc(price,provider.replace('.dat', ''))

    return resultDict
#--------------------------------------------------bonus------------------------------------------------------------
def getFilter() -> dict:
    v = '000'
    number = [ ]
    resultDict = { }
    DataFile = os.path.join(DataPath, 'phones.dat')
    with open(DataFile) as f:
        data = [line.split(',') for line in f.read().splitlines()]

    for item in data[1:]:
        number.append(item[1])

    for i in range(0,1000):
        for no in number:
            s1 = no.replace('(', '')
            s = s1.replace(')', '')
            s2 = s.replace(' ', '')
            s3 = s2.replace('-', '')
            if v in s3:
                if v in resultDict:
                    del resultDict[v]
                else:
                    resultDict[v] = no

        temp = str(int(v) + 1)
        if len(temp) < 3:
            if len(temp) == 1:
                v = '0' + '0' + temp
            elif len(temp) == 2:
                v = '0' + temp
        else:
            v = str(temp)

    return resultDict

# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    from pprint import pprint as pp
    getDifference('provider1', 'provider4')
    getPriceOf('Rasp. Pi-4702MQ', 'provider2')
    r = {'Rasp. Pi-4702MQ', 'Rasp. Pi-6700', 'Rasp. Pi-5557U', 'Rasp. Pi-6700HQ'}
    checkAllPrices(r)
    pp(getFilter())