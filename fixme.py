import os
from glob import glob
import operator

hids = glob("../hid*")
hids = [hid.replace('../', '') for hid in hids]
#print (hids)


cwd = os.getcwd()

fixme = []
for hid in hids:
    os.system ('cd ../{hid}; git log | fgrep "fix readme" > {cwd}/count.txt'.format(hid=hid,cwd=cwd))
    with open('count.txt') as f:
        lines = f.readlines()
    fixme.append ([len(lines), hid])

print (fixme)    
fixme= sorted(fixme, key=operator.itemgetter(0), reverse=True)

for v in fixme:
    print (v[0], v[1])
