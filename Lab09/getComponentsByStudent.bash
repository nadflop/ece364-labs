#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/20/2019
########################################################
DataPath=~ee364/DataFolder/Lab09
CircPath=${DataPath}/circuits
StudPath=${DataPath}/maps/students.dat

id=$(grep -h "$1" $StudPath | cut -d'|' -f2 | tr -d '[:space:]')

grep -E "[A-Z]{3}\-[0-9]{3}" $(grep -l "$id" $CircPath/*.dat) | grep -E -o "[A-Z]{3}\-[0-9]{3}" | sort -u


