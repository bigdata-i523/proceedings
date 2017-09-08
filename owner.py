import os
import yaml
import pprint
import glob
import os.path


def get_data(filename):
    with open(filename, 'r') as content_file:
        content = content_file.read().splitlines()

    # print (content)

    cleaned = []
    for line in content:
        line = line
        if line.startswith("#") or "```" in line or line is '':
            pass
        else:
            cleaned.append(line)

    yaml_text = '\n'.join(cleaned)

    # print (yaml_text)

    body = yaml.load(yaml_text)
    return body

    # print(body)

    # print (body['owner'])


data = get_data('r.txt')
                    
print ('hid{hid}, {name}'.format(**data['owner']))

dirs = glob.glob('../hid*')

ok = []
missing = []

for dir in dirs:
    hid = dir.replace("../","")
    readme = dir + '/README.md'
    if os.path.isfile(readme):
        data = get_data(readme)
        if data is None:
             missing.append("{hid}, owner data is missing in README.md".format(hid=hid))
        else:
            ok.append("{hid}, {owner}".format(hid=hid, owner=data['owner']['name']))

print ("Owner Data Found")            
print ("\n".join(ok))
print()
#print ("Owner Data Missing")            
#print ("\n".join(missing))

