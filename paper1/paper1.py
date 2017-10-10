from cloudmesh.proceedings.api.proceedings import Proceedings
import os
import sys
from pprint import pprint

kind = 'paper1'

def read_file(filename):
    with open(filename) as f:
        s = f.read()
        return (s)

print (read_file("title.tex"))

print ("""
\chapter{Preface}
\section{List of Papers}

\\begin{footnotesize}
\\begin{longtable}{|p{1cm}p{5cm}p{9cm}|}
\\hline \\textbf{Name} & \\textbf{HID} & \\textbf{Title} \\\\ \\hline \\hline
""")

p = Proceedings()
hids = p.read_hid_list()

# print (hids)

for hid in hids:
    print(hid, file=sys.stderr)
    owner = p.attribute(hid, 'owner')
    paper = p.attribute(hid, kind)
    d = dict(paper)
    d["name"] = owner["name"] or None
    d["hid"] = hid
    print(d, file=sys.stderr)
    print ("{hid} & {name} & {title}  \\\\".format(**d))
    print ("\\hline")

print("""\\end{longtable}
\\end{footnotesize}
\\newpage
""")

data = {}
for hid in hids:
    data[hid] = p.attribute(hid, kind)


# pprint(data)

broken = []
chapters = []
for hid in hids:
    if 'chapter' in data[hid]:
        chapters.append(data[hid]['chapter'])
    else:
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

for chapter in order:

    print("\\phantomsection")

    print("\\addtocounter{chapter}{1}")
    print("\\addcontentsline{toc}{chapter}{\\arabic{chapter} ",chapter, "}")

    # print(70 * "%")
    # print("\chapter{",chapter,"}", sep="")
    # print(70 * "%")

    for hid in hids:
        if data[hid]['chapter'] == chapter:
            get_paper(hid)


'''
for hid in hids:
    get_paper(hid)
'''

print (read_file("end.tex"))
