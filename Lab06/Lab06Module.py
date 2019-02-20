#######################################################
#    Author: Nur Nadhira Aqilah Binti Mohd Shah
#    email: mohdshah@purdue.edu
#    ID: mohdshah
#    Date: 2/13
#######################################################
import os      # List of  module  import  statements
import sys     # Each  one on a line
import re
# Module  level  Variables. (Write  this  statement  verbatim .)
#######################################################

def extractArguments(commandline: str)-> list:
    #scriptBash switch(switch name) (value)
    temp = re.findall(r'[\\+]([a-z]){1}\s([^\\+][\S]*)', commandline)
    pattern = sorted(temp,key=str)

    return pattern

def extractNumerics(sentence:str)-> list:
    #integers: start with - or +
    #regular floats: start with - or +, have a decimal point
    #scientific notation: start with - or +, single digit before decimal
    pattern = re.findall(r'([-+]?[^[a-zA-Z][\d\.][eE\-\+\d]+|[-+]?\d+\.?\d)', sentence)

    return pattern

# This  block  is  optional
if __name__  == "__main__":
# Write  anything  here to test  your  code.
    ...