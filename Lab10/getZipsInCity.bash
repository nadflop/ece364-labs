#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################

DataPath=~ee364/DataFolder/Lab10
Fac=${DataPath}/facilities.txt

grep -h "$1" $Fac | cut -d' ' -f3-5
