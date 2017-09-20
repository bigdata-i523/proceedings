
DOCUMENT=proceedings


all:
	cms proceedings pdf all paper1 make
	make -f Makefile proc

proc:
	python paper1.py > $(DOCUMENT).tex
	pdflatex $(DOCUMENT)
	pdflatex $(DOCUMENT)
	pdflatex $(DOCUMENT)

compile:
	python all.py


view:
	open $(DOCUMENT).pdf


review:
	python reviews.py > reviews.tex
	pdflatex reviews

clean:
	rm *.toc *.aux *.log *.out
