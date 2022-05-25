#!/bin/bash

read -p "How much can the student bench press? " press
read -p "How much can the student squat? " squat
read -p "How much can the student clean? " clean

currentdir=$(pwd)
echo "${press},${squat},${clean}" >> ${currentdir}/team_strength.csv

exit 0
