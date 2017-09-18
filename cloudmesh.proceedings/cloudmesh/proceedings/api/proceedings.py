import os
import yaml
import pprint
import glob
import os.path


class Proceedings(object):

    def read_git_list(selfself, filename='list.txt'):
        gits = []
        with open(filename, 'r') as f:
            for line in f:
                url = line.split('"')[3]
                gits.append(url)
        return gits


    def read_hid_list(self, filename='list.txt'):
        hids = []
        gits = self.read_git_list(filename)
        for git in gits:
            rest, hid = git.split("/")
            hid = hid.replace(".git","")
            hids.append(hid)
        return hids
            
    def get_hids_from_git(self):
        """ returns the hids from git"""
        return []

    def get_hids_from_list(self, parameter):
        """use cloudmesh Parameter to generate a list form abreviated list string"""
        """example hid[100-110,116,201-210,301-305]"""
        return
    
    def clone(self,filename='list.txt'):
        """ clones all hid dirs int .."""
        """returns all hids that have an issue"""
        hids = self.read_git_list(filename=filename)
        for line in content:
            if "/hid" in line:
                url = line.split('"')[3]
                os.system("cd ..; git clone " + url)

    def pull(self):
        """does a git pull in all hid dirs in .."""
        """returns all hid the have an issue"""

        self.read_hid_list()        
        for line in content:
            hid = line.split('"')[3]
            print (hid)
            #os.system("cd ../{hid}; git pull ".format(hid=hid))

        
    def set_license(self):
        """put the license in each directory if it is missing"""
        """ this is not working"""
        self.read_hid_list()                
        for line in content:
            directory = line.split('/')[4].split(".")[0]
            if directory.startswith('hid'):
                print (directory)
                #os.system("cp proceedings/LICENSE " + directory)
                #os.system('cd ' + directory + ';  git commit -m "add License" LICENSE; git push')

    def owner(self):
        """this is not yet tested"""
        
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

