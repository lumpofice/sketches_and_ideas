#!/bin/bash

# The first thing we do is collect data on 3 different lifts
# for each student, using the statements below.
read -p "How much can the student bench press? " press
read -p "How much can the student squat? " squat
read -p "How much can the student clean? " clean

# We create a csv file, storing our data within it, making sure
# the file saves to the directory from which we execute the
# program.
currentdir=$(pwd)
echo "${press},${squat},${clean}" >> ${currentdir}/team_strength.csv

exit 0
