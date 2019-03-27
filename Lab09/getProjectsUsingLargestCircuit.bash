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

circ=($(ls -S $CircPath/*.dat | cut -d'_' -f 2 | cut -d'.' -f 1)) 
#largest file is the first circuit
grep -h "${circ[0]}" $ProjPath | cut -d' ' -f 15 | sort -u
