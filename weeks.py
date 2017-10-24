import dateparser
from pprint import pprint
import collections
from glob import glob
import subprocess
import os
from faker import Faker
anonyomous = Faker()

data = {}


hids = glob('../hid*')

print (hids)



def week_counter(hid, data):

    directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), hid) 
    r = str(subprocess.check_output("git log".format(hid=hid), cwd=directory, shell=True))
    lines = r.split("\\n")
    print(directory)
    
    for line in lines:

        if 'Author:' in line:
            author = line.split('Author:')[1]
            author = author.split(' <')[0]
            if author not in data:
                data[author] = {
                    'name': author,
                    'dates': [],
                    'weeks': []
                    }

        if 'Date:' in line:
            d = line.split('Date:')[1]
            d = dateparser.parse(d)
            # print (d, d.isocalendar()[1])
            data[author]['dates'].append(d)
            data[author]['weeks'].append(d.isocalendar()[1])        


    # pprint(data)

def print_data(data, fake=True ):
    # weeks

    #for author in data:
    #    weeks = sorted(set(data[author]['weeks']))
    #    print (author, ":", weeks)


    # weeks frequency
    for author in data:
        weeks = sorted(data[author]['weeks'])
        counter=collections.Counter(weeks)

        if fake:
            author = anonyomous.name()


        print (author, ":", list(counter.items()))

for hid in hids:
    print (hid)
    week_counter(hid, data)        

    
print_data(data, fake=True)

