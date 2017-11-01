from cloudmesh.proceedings.api.proceedings import Proceedings
import os
import sys
from pprint import pprint
import subprocess

kind = 'paper1'

def read_file(filename):
    with open(filename) as f:
        s = f.read()
        return (s)

print (read_file("title.tex"))

print ("\chapter{Preface}")

print (read_file("preface.tex"))

print("""
\section{List of Papers}

\\begin{footnotesize}
\\begin{longtable}{|p{1cm}p{5cm}p{9cm}|}
\\hline \\textbf{HID} & \\textbf{Author} & \\textbf{Title} \\\\ \\hline \\hline
""")

p = Proceedings()
hids = p.read_hid_list()



#print (hids)

#print ("LLLL", p)

for hid in hids:
    # print(hid, file=sys.stderr)
    try:
        owner = p.attribute(hid, 'owner')
        paper = p.attribute(hid, kind)
        d = dict(paper)
        d["name"] = ', '.join(d['author']) or None
        d["hid"] = ', '.join(str(x) for x in d["hid"])
    except Exception as e:
        # print (e)
        d["name"] = "error: yaml"
        d["hid"] = hid
    # print(d, file=sys.stderr)
    print ("{hid} & {name} & {title}  \\\\".format(**d))
    print ("\\hline")

    
print("""\\end{longtable}
\\end{footnotesize}
\\newpage
""")

data = {}
for hid in hids:
    try:
        data[hid] = p.attribute(hid, kind)
    except:
        data[hid] = None

# pprint(data)

broken = []
chapters = []
for hid in hids:
    if data[hid] is not None and 'chapter' in data[hid]:
        chapters.append(data[hid]['chapter'])
    elif data[hid] is not None:
        broken.append(hid)
        data[hid]['chapter'] = 'TBD'

# print (broken)
chapters = sorted(list(set(chapters)))
# print(chapters)
# chapters

#print([entry['chapter'] for entry in data if 'chaoter' in entry])


order = ['Biology',
         'Business',
         'Edge Computing',
         'Education',
         'Energy',
         'Environment',
         'Government',
         'Health',
         'Lifestyle',
         'Machine Learning',
         'Media',
         'Physics',
         'Security',
         'Sports',
         'Technology',
         'Text',
         'Theory',
         'Transportation',
         'TBD']

def filetype(kind, path):
    cmd =     "/usr/bin/file -b --mime {path}".format(path=path)
    r = str(subprocess.check_output(cmd, shell=True))
    return kind in r


def get_paper(hid):
    pages = 1
    owner = p.attribute(hid, 'owner')
    paper = p.attribute(hid, kind)
    d = paper
    d["author"] = ', '.join(paper["author"]) or None
    d["hid"] = hid
    d["title"] = paper["title"] or None
    d["pages"] = 1
    d["report"] = "report.pdf"
    d["home"] = p.home
    if 'status' not in d:
        d['status'] = 'unkown'
    if 'in progress' in d['status'].lower():
        d['status'] = '0%'
    d['status'] = d['status'].replace("%", "\\%")

    pdf = "{home}/{hid}/{paper}/report.pdf".format(paper=kind, home=d["home"], hid=hid)
    log = "{home}/{hid}/{paper}/report-latex.log".format(paper=kind, home=d["home"], hid=hid)
    if not filetype("pdf", pdf):
        return
    print (paper, file=sys.stderr)
    if 'duplicate' in paper:
        return
    
    #print (pdf)
    #print (pdf)

    print("\\phantomsection")

    print("\\addtocounter{section}{1}")
    print("\\addcontentsline{toc}{section}{\\arabic{section} ",
          hid, '\\hfill', 'Status:', d["status"], "\\newline",
          # d["chapter"], "\\newline",
          d["title"], "\\newline",
          d["author"], "}")
    if os.path.exists(pdf):
        print ("\\includepdf[pages=-,pagecommand=\\thispagestyle{plain}]{" + pdf + "}")
    else:
        print ("%", pdf, " not found")
    if os.path.exists(log):
        print ("\\VerbatimInput{" + log + "}")
    else:
        print ("%", log, " not found")

for chapter in order:

    print("\\phantomsection")

    print("\\addtocounter{chapter}{1}")
    print("\\addcontentsline{toc}{chapter}{\\arabic{chapter} ",chapter, "}")

    # print(70 * "%")
    # print("\chapter{",chapter,"}", sep="")
    # print(70 * "%")

    for hid in hids:
        # print (hid)
        if data[hid] is not None and data[hid]['chapter'] == chapter:
            try:
                get_paper(hid)
            except:
                pass

'''
for hid in hids:
    get_paper(hid)
'''

#print("""

#\\appendix

#\\section{Errors}

#\VerbatimInput{check.rst}
#\VerbatimInput{check-report.rst}
#\VerbatimInput{check-all.rst}
#""")

print (read_file("end.tex"))
