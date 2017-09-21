from cloudmesh.proceedings.api.proceedings import Proceedings
import os

def read_file(filename):
    with open(filename) as f:
        s = f.read()
        return (s)

print (read_file("title.tex"))

print ("""
\section{List of Papers}

\\begin{footnotesize}
\\begin{longtable}{|p{1cm}p{5cm}p{9cm}|}
\\hline \\textbf{Name} & \\textbf{HID} & \\textbf{Title} \\\\ \\hline \\hline
""")

p = Proceedings()
hids = p.read_hid_list()


for hid in hids:
    # print(hid)
    owner = p.attribute(hid, 'owner')
    paper = p.attribute(hid, 'paper1')
    d = {
        "name": owner["name"] or None,
        "hid": hid,
        "title": paper["title"] or None,
        }
    print ("{hid} & {name} & {title}  \\\\".format(**d))
    print ("\\hline")

print("""\\end{longtable}
\\end{footnotesize}
\\newpage
""")


for hid in hids:
    pages = 1
    owner = p.attribute(hid, 'owner')
    paper = p.attribute(hid, 'paper1')
    d = {
        "author": ', '.join(paper["author"]) or None,
        "hid": hid,
        "title": paper["title"] or None,
        "pages": 1,
        "report": "report.pdf"
        }
    d["home"] = p.home

    pdf = "{home}/{hid}/{paper}/report.pdf".format(paper="paper1", home=d["home"], hid=hid)
    #print (pdf)
    if os.path.exists(pdf):
        #print (pdf)
        print("\\phantomsection")

        print("\\addtocounter{section}{1}")
        print("\\addcontentsline{toc}{section}{\\arabic{section} ",
              hid + "\\newline",
              d["title"],"\\newline",
              d["author"],
              "}")

        print ("\\includepdf[pages=-,pagecommand=\\thispagestyle{plain}]{" + pdf + "}")
    else:
        print ("%", pdf, " not found")


print (read_file("end.tex"))
