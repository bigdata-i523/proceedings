import yaml
import os
from glob import glob
import operator
from pprint import pprint

hids = glob("../hid*")
hids = [hid.replace('../', '') for hid in hids]
#print (hids)


cwd = os.getcwd()

fixme = []
for hid in hids:
    os.system ('cd ../{hid}; git log | fgrep "fix readme" > {cwd}/count.txt'.format(hid=hid,cwd=cwd))
    with open('count.txt') as f:
        lines = f.readlines()
    os.system ('cd ../{hid}; git log | fgrep commit | wc -l > {cwd}/count.txt'.format(hid=hid,cwd=cwd))
    with open('count.txt') as f:
        count = int(f.read())
    os.system ('cd ../{hid}; git log | fgrep Author: |fgrep -v Gregor |fgrep -v Miao |fgrep -v Silvia |fgrep -v Saber | wc -l > {cwd}/count.txt'.format(hid=hid,cwd=cwd))
    with open('count.txt') as f:
        selbst = int(f.read())
    with open('../{hid}/README.yml'.format(hid=hid)) as f:
        data = yaml.load(f)
        # pprint(data)
    if 'chapter' not in  data['paper1']:
        data['paper1']['chapter'] = None
        
    fixme.append ([len(lines), hid, count, selbst, data['paper1']['chapter']])

#print (fixme)    
fixme= sorted(fixme, key=operator.itemgetter(0), reverse=True)

print ("column 0 - time to correct") 
print ("column 1 - changes in github ")
print ("column 2 - changes in github by student")
print ("column 3 - changes in github by instructor")
print ("column 4 - chapter")


for v in fixme:
    print (v[0], str(v[1])[3], v[2], v[3], v[2] - v[3], v[4], v[1])    
#    print (v[0], str(v[1])[3], v[2], v[3], v[2] - v[3], v[4])
