PAPER=`basename ${CURDIR}`
DOCUMENT=proceedings
LATEX=pydflatex
PDFLATEX=pdflatex
VOLUME=v2

all: 
	cms proceedings pdf all $(PAPER) make
	make -f Makefile proc

proc: 
	python $(PAPER).py > $(DOCUMENT).tex
	$(LATEX) $(DOCUMENT) > tmp.log 2>&1
	$(LATEX) $(DOCUMENT) >> tmp.log 2>&1
	$(LATEX) $(DOCUMENT) >> tmp.log 2>&1

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
	$(LATEX) reviews

clean:
	rm *.toc *.aux *.log *.out

publish:
	cp proceedings.pdf  ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523-$(VOLUME).pdf
	cd ~/github/laszewsk/laszewski.github.io/papers ; git commit -m "update vonLaszewski-i523-$(VOLUME).pdf" vonLaszewski-i523-$(VOLUME).pdf ; git push

pull:
	cms proceedings pull

readme:
	cms proceedings commit \"fix readme\"
