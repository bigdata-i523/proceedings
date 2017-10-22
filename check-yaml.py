import yaml
import json
import sys
from pprint import pprint
import glob
import os
from pprint import pprint

in_yaml = False
content = []
counter = 0

readmes = glob.glob(os.path.expanduser("~") + "/github/bigdata-i523/hid*/README.yml")

pprint(readmes)

print('----------------')

for readme in readmes:
    try:
        with open(readme, 'r') as f:
            content  = f.read()
        d = yaml.load(content)
        # print ("+", readme)
    except Exception as e:
        print ("-", readme)        

