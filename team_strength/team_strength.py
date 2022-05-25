#!/usr/bin/env python3

import subprocess 
import pandas as pd
import numpy as np
from IPython.display import display
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s'
    ' - %(message)s')

logging.debug('Start of program' + '\n')

subprocess.call('team_strength_init.sh')

# The statements below take in student strength data with user input
flag = True
while flag:
    prompt_data = input('Next students one-rep maxes? '
        '(press y and return for yes or press return for no) ')
    
    if not prompt_data:
        flag = False
    else:
        subprocess.call('team_strength.sh')

student_lift_data = pd.read_csv('team_strength.csv')
print(f'\n')
display(student_lift_data)

# We get some statistics below for strength in these different lifts
press_avg = student_lift_data['press'].mean()
print(f'\nWe have a bench press average of {press_avg}')

squat_avg = student_lift_data['squat'].mean()
print(f'\nWe have a squat average of {squat_avg}')

clean_avg = student_lift_data['clean'].mean()
print(f'\nWe have a clean average of {clean_avg}')
