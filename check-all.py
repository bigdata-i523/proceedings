#!/usr/bin/env python

import yaml
import json
import sys
from pprint import pprint
import glob
import os
import subprocess

paper = sys.argv[1]

print('\\section{Missing Reports}')
print()
    
hids = sorted(glob.glob(os.path.expanduser("~") + "/github/bigdata-i523/hid*"))


for hid in hids:
    file = hid + "/{paper}/report.pdf".format(paper=paper)
    print()
    print ("-", file)
    print (79 * '-')
    print ()
    cmd = "cd {hid}/{paper}; pydflatex report; exit 0 ".format(hid=hid,paper=paper)
    print (cmd)
    
    r = subprocess.check_output(cmd, stderr=subprocess.STDOUT,shell=True).splitlines()
    for l in r:
        print (l)
        
