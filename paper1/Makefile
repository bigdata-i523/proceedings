
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

publish:
	cp proceedings.pdf  ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523.pdf
	cd ~/github/laszewsk/laszewski.github.io/papers ; git commit -m "update vonLaszewski-i523.pdf" vonLaszewski-i523.pdf ; git push

pull:
	cms proceedings pull

readme:
	cms proceedings commit \"fix readme\"
