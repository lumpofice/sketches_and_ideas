#!/usr/bin/env python3

import subprocess 
import pandas as pd
import numpy as np
from IPython.display import display

subprocess.call('team_strength_init.sh')

flag = True
while flag:
    prompt_data = input('Next students one-rep maxes? '
                        '(press y for yes or press return for no) ')
    if not prompt_data:
        flag = False
    else:
        subprocess.call('team_strength.sh')

student_lift_data = pd.read_csv('team_strength.csv')
display(student_lift_data)

press_avg = student_lift_data['press'].mean()
print(f'We have a bench press average of {press_avg}')

squat_avg = student_lift_data['squat'].mean()
print(f'We have a squat average of {squat_avg}')

clean_avg = student_lift_data['clean'].mean()
print(f'We have a clean average of {clean_avg}')
