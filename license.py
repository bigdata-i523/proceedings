import os

# do this in the shell git clone https://api.github.com/orgs/bigdata-i523/repos?per_page=200 | fgrep git_url > list.txt

with open('list.txt', 'r') as content_file:
    content = content_file.readlines()

print (content)

for line in content:
    directory = line.split('/')[4].split(".")[0]
    if directory.startswith('hid'):
        print (directory)
        os.system("cp proceedings/LICENSE " + directory)
        os.system('cd ' + directory + ';  git commit -m "add License" LICENSE; git push')
