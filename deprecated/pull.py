import os

# do this in the shell git clone
# curl https://api.github.com/orgs/bigdata-i523/repos?per_page=200 | fgrep ssh_url > list.txt

with open('list.txt', 'r') as content_file:
    content = content_file.readlines()

print (content)

for line in content:
    hid = line.split('"')[3]
    print (hid)
    #os.system("cd ../{hid}; git pull ".format(hid=hid))


