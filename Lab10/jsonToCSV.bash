#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/16/2019
########################################################

DataPath=~ee364/DataFolder/Lab10
Fac=${DataPath}/facilities

echo "FACILITYNAME,FACILITYNUMBER,STREETADDRESS,TELEPHONE"
grep -h "$1" $Fac/*.json | tr -d '[:blank:]'  |  cut -d"," -f2-7 | cut -d":" -f2,3,4,5-8

