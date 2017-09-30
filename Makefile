clean:
	cd paper1; rm -rf *.aux *.out *.toc
	cd paper2; rm -rf *.aux *.out *.toc
	cd project; rm -rf *.aux *.out *.toc

install:
	mkdir ~/github
	mkdir ~/github/bigdata-i523
	cd ~/github
	cd ~/github; git clone https://github.com/cloudmesh/cloudmesh.common.git
	cd ~/github; git clone https://github.com/cloudmesh/cloudmesh.cmd5.git
	cd ~/github; git clone https://github.com/cloudmesh/cloudmesh.sys.git
	cd ~/github; git clone https://github.com/cloudmesh/proceedings.git
	cd ~/github/cloudmesh.common;	pip install .
	cd ~/github/cloudmesh.cmd5; 	pip install .
	cd ~/github/cloudmesh.sys;  	pip install .
	cd ~/github/proceedings/cloudmesh.proceedings; 	pip install .

checkout:
	cd ~/github/bigdata-i523
	cms proceedings git list
	cms proceedings clean
	cms proceedings clone

paper1:
	cd ~/github/bigdata-i523/paper1; make

paper1-proc:
	cd ~/github/bigdata-i523/paper1; make proc

update:
	cms proceedings pull
	cms proceedings commit \"fix readme\"

