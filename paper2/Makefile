PAPER=paper2
DOCUMENT=proceedings


all: 
	cms proceedings pdf all $(PAPER) make
	make -f Makefile proc

proc: 
	python $(PAPER).py > $(DOCUMENT).tex
	pdflatex $(DOCUMENT)
	pdflatex $(DOCUMENT)
	pdflatex $(DOCUMENT)

compile:
	python all.py


view:
	open $(DOCUMENT).pdf

check:
	cd ..; ./check.sh > $(PAPER)/check.rst
	cd ..; ./check-report.py $(PAPER) > $(PAPER)/check-report.rst 2>&1
	cd ..; ./check-all.py $(PAPER) > $(PAPER)/check-all.rst 2>&1
	# pandoc check.rst -o check.tex

review:
	python reviews.py > reviews.tex
	pdflatex reviews

clean:
	rm *.toc *.aux *.log *.out

publish:
	cp proceedings.pdf  ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523-v2.pdf
	cd ~/github/laszewsk/laszewski.github.io/papers ; git commit -m "update vonLaszewski-i523-v1.pdf" vonLaszewski-i523-v2.pdf ; git push

pull:
	cms proceedings pull

readme:
	cms proceedings commit \"fix readme\"
