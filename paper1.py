import os
import yaml
import pprint
import glob
import os.path
import textwrap

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

    body = yaml.load(yaml_text)
    return body


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
            ok.append("\n")
            ok.append('# {hid}, {author}, {title}'.format(hid=hid,
                          author=", ".join(data['paper1']['author']),
                          title=data['paper1']['title']))
            #ok.append(data['paper1']['abstract'])
            ok.append("")            
            #block = "        " + "\n        ".join(textwrap.wrap(data['paper1']['abstract'],70))
            block = "\n".join(textwrap.wrap(data['paper1']['abstract'],70))            
            ok.append(block)
print ("Paper 1 Data Found")            
print ("\n".join(ok))
print()
#print ("Paper 2 Data Missing")            
#print ("\n".join(missing))

