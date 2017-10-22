#fgrep \" ../hid*/paper1/report.tex | awk -F':' '{print $1}' | sort -u


fgrep @ ../hid*/paper1/report.bib |fgrep _ | awk -F',' '{print $1}' | sort -u
