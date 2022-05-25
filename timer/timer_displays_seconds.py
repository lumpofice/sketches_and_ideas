#!/usr/bin/env python3

import subprocess

m = input('Choose either m or s, where m is for minutes and s is for seconds: ')
if m == 'm':
    n = int(input('How many minutes? '))
if m == 's':
    n = int(input('How many seconds? '))
subprocess.call(['timer_displays_seconds.sh',f'-{m}', f'{n}'])


