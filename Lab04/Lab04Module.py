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

def getPriceOf(sbc, provider) -> float:
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
                    price = p.strip()
                    if element in resultDict:
                        if min(resultDict[element].minPrice, price) == price:
                            value = sbc(min(resultDict[element].minPrice, price),provider.replace('.dat', ''))
                            resultDict[element] = value
                    else:
                        resultDict[element] = sbc(price,provider.replace('.dat', ''))

    return resultDict


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    getDifference('provider1', 'provider4')
    getPriceOf('Rasp. Pi-4702MQ', 'provider2')
    r = {'Rasp. Pi-4702MQ', 'Rasp. Pi-6700', 'Rasp. Pi-5557U', 'Rasp. Pi-6700HQ'}
    checkAllPrices(r)