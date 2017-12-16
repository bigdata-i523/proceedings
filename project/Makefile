PAPER=project
DOCUMENT=proceedings


all: 
	cms proceedings pdf all $(PAPER) make
	make -f Makefile proc

proc: 
	python $(PAPER).py > $(DOCUMENT).tex
	pydflatex $(DOCUMENT)
	pydflatex $(DOCUMENT)
	pydflatex $(DOCUMENT)

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
	cp proceedings.pdf  ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523-v3.pdf
	rm -f ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523-v3-1.pdf
	rm -f ~/github/laszewsk/laszewski.github.io/papers/vonLaszewski-i523-v3-2.pdf

	cd ~/github/laszewsk/laszewski.github.io/papers; yes | gs -dBATCH -sOutputFile=vonLaszewski-i523-v3-1.pdf -dFirstPage=1 -dLastPage=500 -sDEVICE=pdfwrite vonLaszewski-i523-v3.pdf >& /dev/null
	cd ~/github/laszewsk/laszewski.github.io/papers; yes | gs -dBATCH -sOutputFile=vonLaszewski-i523-v3-2.pdf -dFirstPage=501 -sDEVICE=pdfwrite vonLaszewski-i523-v3.pdf >& /dev/null

	#cd ~/github/laszewsk/laszewski.github.io/papers; pdfseparatetar -czvf vonLaszewski-i523-v3.tar.gz vonLaszewski-i523-v3.pdf
	#cd ~/github/laszewsk/laszewski.github.io/papers; tar -czvf vonLaszewski-i523-v3.tar.gz vonLaszewski-i523-v3.pdf

	cd ~/github/laszewsk/laszewski.github.io/papers ; git commit -m "update vonLaszewski-i523-v3.pdf" vonLaszewski-i523-v3-1.pdf ; git push
	cd ~/github/laszewsk/laszewski.github.io/papers ; git commit -m "update vonLaszewski-i523-v3.pdf" vonLaszewski-i523-v3-2.pdf ; git push

pull:
	cms proceedings pull

readme:
	cms proceedings commit \"fix readme\"
