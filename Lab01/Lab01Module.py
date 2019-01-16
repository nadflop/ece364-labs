#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 1/16
#######################################################
import os
import sys

def findLongest() -> int:
    sequence = [ ]
    result = []
    starting = 0

    for i in range(1, 1000001):
        starting = i
        sequence = [ ]
        sequence.append(starting)
        while starting > 1:
            mod = starting % 2
            if mod == 0: #even
                starting = starting / 2
                sequence.append(starting)
            else:
                starting = (3 * starting) + 1
                sequence.append(starting)

        if i > 2:
            if len(result) < len(sequence):
                result = sequence
                val = i
        elif i == 2:
            result.append(sequence)

    return val

def findSmallest() -> int:
    num = '1'
    p = 0
    result = 0

    while (1):
        p = 0
        val = int(num) * 1
        for j in range(1,7):
            val = val * j
            if num.find(str(val)):
                p = p + 1
            else:
                j = 7
        if p == 6:
            result = val/6
            break
        newNum = int(num) + 1
        num = str(newNum)


    return result


# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
   ...


