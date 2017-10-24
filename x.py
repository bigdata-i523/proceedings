#! /usr/bin/env python
import yaml
import sys
import os
import glob

filename = sys.argv[1]

with open(filename, "r") as f:
    config = yaml.load(f)

print (config)

cmds = """
rm -rf {destination}
mkdir -p {destination}
""".format(**config['proceedings']['copy']).split("\n")

for cmd in cmds:
    print (cmd)
    os.system(cmd)

sources = glob.glob(config["proceedings"]["copy"]["source"])

print (sources)

for base in sources:
    cmd = "cp -r {base} {destination}".format(base=base, **config['proceedings']['copy'])
    print (cmd)
    os.system(cmd)
