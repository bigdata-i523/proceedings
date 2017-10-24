#! /bin/sh
#fgrep \" ../hid*/paper1/report.tex | awk -F':' '{print $1}' | sort -u

echo
echo "bibtext _ label error"
echo "====================="
echo
fgrep @ ../hid*/paper1/report.bib |fgrep _ | awk -F',' '{print $1}' |  sort -u

echo
echo "bibtext space label error"
echo "====================="
echo
fgrep @ ../hid*/paper1/report.bib |fgrep " " | awk -F',' '{print $1}' | fgrep -v "url" | fgrep -v "@String" | fgrep -v "@Comment"|  sort -u

echo
echo "bibtext comma label error"
echo "====================="
echo
fgrep @ ../hid*/paper1/report.bib | fgrep -v "@String" | fgrep -v "@Comment"| fgrep -v ',' | sort -u 

echo
echo "latex quote error"
echo "====================="
echo
fgrep @ ../hid*/paper1/report.tex | fgrep  '"' |sort -u 

echo
./check-yaml.py
