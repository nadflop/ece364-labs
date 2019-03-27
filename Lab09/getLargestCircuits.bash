#! /bin/bash
########################################################
# Author: Nur Nadhira Aqilah Binti Mohd Shah
# Email:  mohdshah@purdue.edu
# ID:     ee364g02
# Date:   3/20/2019
########################################################
DataPath=~ee364/DataFolder/Lab09
ProjPath=${DataPath}/maps/projects.dat
CircPath=${DataPath}/circuits
StudPath=${DataPath}/maps/students.dat

wc -c $(ls -S $CircPath/*.dat) | grep -E -h "\s[2-9]{1}[0-9]{2} " | cut -d'_' -f 2 | cut -d'.' -f 1 | sort -u
