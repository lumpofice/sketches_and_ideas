#!/usr/bin/env python3

import subprocess
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')

logging.debug('Start of program' + f'\n')

# The statement below will take in the initial user input of minutes vs.
# seconds
m = input('Choose either m or s, where m is for minutes and s is for seconds: ')

# The statements below will taken in the second user input of how many
# minutes vs. how many seconds
if m == 'm':
    n = int(input('How many minutes? '))
    subprocess.call(['timer_displays_seconds.sh',f'-{m}', f'{n}'])
if m == 's':
    n = int(input('How many seconds? '))
    subprocess.call(['timer_displays_seconds.sh',f'-{m}', f'{n}'])
else:
    print('You failed to choose either minutes m or seconds s. Goodbye!')
    



