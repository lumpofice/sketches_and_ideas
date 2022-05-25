#!/bin/bash

# To execute this program, we need to include the a -m or -s argument 
# followed by an input number. For the -m argument, the input number 
# will be interpreted as minutes and converted to seconds. For the -s
# argument, the input number will be interpreted as seconds and will not
# be manipulated.

total_seconds=""

# The getopts block below will interpret user input and store it 
# appropriately
while getopts "m:s:" opt; do
	case "${opt}" in
		m)
			total_seconds=$(( ${total_seconds} + ${OPTARG} * 60 ));;
		s)
			total_seconds=$(( ${total_seconds} + ${OPTARG} ));;
		
		# We have our catch-all scenario in the python file, and below 
		# is our catch-all scenario for those who wish to run the 
		# program from the bash file directly. 
		\?);;
	esac
done

# The while loop below will serve as our countdown clock.
while [ ${total_seconds} -gt 0 ]; do
	echo "$total_seconds"
	total_seconds=$(( ${total_seconds} - 1 ))
	sleep 1s
done

echo "Time is up!"
exit 0
