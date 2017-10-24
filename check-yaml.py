#!/usr/bin/env python

import yaml
import json
import sys
from pprint import pprint
import glob
import os
import subprocess

in_yaml = False
content = []
counter = 0

readmes = glob.glob(os.path.expanduser("~") + "/github/bigdata-i523/hid*/README.yml")

# pprint(readmes)
print('yaml error')
print("=====================")

for readme in readmes:
    try:
        with open(readme, 'r') as f:
            content  = f.read()
        d = yaml.load(content)
        # print ("* [+]", readme)
    except Exception as e:
        print ("* [-]", readme)        

print('wrong quote (") found ')
print("=====================")

        
reports = glob.glob(os.path.expanduser("~") + "/github/bigdata-i523/hid*/paper1/report.tex")
cmd = "grep -nr '\"' ../hid*/paper1/report.tex"
found = subprocess.check_output(cmd, shell=True).splitlines()
print()
for line in found:
    data = str(line).split(":")
    data[0] = data[0].replace("b'","")
    print ("*", data[0], "Line:", data[1])

    
