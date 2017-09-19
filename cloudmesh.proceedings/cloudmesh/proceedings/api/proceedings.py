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

    def clean(self):
        hids = self.read_hid_list(filename='list.txt')
        for hid in hids:
            os.system("rm -rf ../{hid}".format(hid=hid))


    def clone(self,filename='list.txt'):
        """ clones all hid dirs int .."""
        """returns all hids that have an issue"""
        hids = self.read_git_list(filename=filename)
        for hid in hids:
            if "/hid" in hid:
                os.system("cd ..; git clone " + hid)

    def pull(self, filename='list.txt'):
        """does a git pull in all hid dirs in .."""
        """returns all hid the have an issue"""
        hids = self.read_hid_list(filename=filename)
        print (hids)
        for hid in hids:
            print (hid)
            os.system("cd ../{hid}; git pull ".format(hid=hid))

    def commit(self, filename='list.txt', msg="update"):
        """does a git pull in all hid dirs in .."""
        """returns all hid the have an issue"""
        hids = self.read_hid_list(filename=filename)
        print (hids)
        for hid in hids:
            print (hid)
            os.system('cd ../{hid}; git commit -m "{msg}" . '.format(hid=hid, msg=msg))

    def push(self, filename='list.txt'):
        """does a git pull in all hid dirs in .."""
        """returns all hid the have an issue"""
        hids = self.read_hid_list(filename=filename)
        print (hids)
        for hid in hids:
            print (hid)
            os.system('cd ../{hid}; git push'.format(hid=hid))


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

    def extract_yaml_text(self,s):
        """
        Takes a string and returns all lines between ``` if they start at the beginning of the line
        :return: text between ^```
        """
        output = ""
        flag = False
        try:
            for o in s.split("\n"):
                if o.strip().startswith("```") and not flag:
                    flag = True
                    continue
                if flag and not o.strip().startswith("```"):
                    output = output + o + "\n"
                if o.strip().startswith("```") and flag:
                    flag = False
                    continue
        except Exception as e:
            print (e)
            return None

        return output.strip()

    def get_file(selfself, filename):
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except Exception as e:
            print(e)
            content = None
        return content

    def readme(self, hid):
        filename = "../{hid}/README.md".format(hid=hid)
        if os.path.isfile(filename):
            content = self.get_file(filename)
            content = self.extract_yaml_text(content)
        else:
            content = None
        return content


    def attribute(self, hid, name):
        if hid is not None:
            s = self.readme(hid)
            if s is None:
                return None
            try:
                data = yaml.load(s)
            except Exception as e:
                data = None

            if data is None:
                return None
            return data[name]

        else:
            ok = {}
            missing = []
            dirs = glob.glob('../hid*')
            for dir in dirs:
                hid = dir.replace("../","")
                print (hid)
                filename = dir + '/README.md'
                if os.path.isfile(filename):
                    data = self.attribute(hid, name)
                    print (data)
                    if data is None:
                         missing.append("{hid}, owner data is missing in README.md".format(hid=hid))
                    else:
                        ok[hid] = data
            return ok, missing


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
                print ("dd", data)
                if data is None:
                     missing.append("{hid}, owner data is missing in README.md".format(hid=hid))
                else:
                    ok.append(data['owner'])

        print ("Owner Data Found")            
        print ("\n".join(ok))
        print()
        #print ("Owner Data Missing")            
        #print ("\n".join(missing))

