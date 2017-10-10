# proceedings

As part of the classes taught we have developed a simple but
sophisticated tool to combine all papers and project reports into
proceedings. 

At this time we support this for the following repository:

https://api.github.com/orgs/bigdata-i523

# Requirements

You must have cmd5 installed from source. This is documented at

* https://github.com/cloudmesh/cloudmesh.cmd5

and can be done while following these steps

    pip install pip -U
    pip install setuptools -U
    mkdir ~/github
    mkdir ~/github/bigdata-i523
    mkdir ~/github/cloudmesh
    cd ~/github/cloudmesh
    git clone https://github.com/cloudmesh/cloudmesh.common.git
    git clone https://github.com/cloudmesh/cloudmesh.cmd5.git
    git clone https://github.com/cloudmesh/cloudmesh.sys.git
    cd ~/github/cloudmesh/bigdata-i523
    git clone https://github.com/bigdata-i523/proceedings.git
    cd ~/github/cloudmesh/cloudmesh.common
    pip install .
    cd ~/github/cloudmesh/cloudmesh.cmd5
    pip install .
    cd ~/github/cloudmesn/cloudmesh.sys
    pip install .
    cd ~/github/bigdata-i523/proceedings/cloudmesh.proceedings
    pip install .


## Checkout

First, you have to check out the proceedings which will be stored at

    ~/github/bigdata-i523

Please note that the clean command we use, will delete all hid*
directories and if you use it it is at your own risk. At times it may
be important to clean the hid directories as students may have
introduced conflicts that you may otherwise spend too much time in
resolving.

    $ cd ~/github/bigdata-i523
    $ cms proceedings git list
    $ cms proceedings clean
    $ cms proceedings clone

## Compile All

To compile the papers into a proceeding, go to the paper1 directory
and call make


    $ cd ~/github/bigdata-i523/paper1
    $ make

This command will brute fore a LaTeX compilation for the report.pdf
file on all hid* directories.

## LaTeX only 

Let us assume the pdf files are ok, but an error occured in the README
leading to a failure in the compilation of proceedings.tex. In this
case you can corret the error in the README.md file of the hid
directory that is reported last and introduces the error.

Than after you correct it you do not have to recreate all PDF files,
but you can create the procedings as follows

    $ cd ~/github/bigdata-i523/paper1 
    $ make proc
    
## Commit and push changes

Once the READMEs are fixed and the proceedings compiles it is
important to check the READMEs back into the reporsitory. This however
may need multiple itterations as we founmd that it is possible that
students modify the README while you also do it, or the students
cahnge a perfectly godd README so it is no longer working.

YOu can pull the lates version via the command

    $ cms proceedings pull

To commit you find good commit message ad do a bulk commit with

    $ cms proceedings commit \"fix readme\"

## List owners

For quick checks you may want to look up who is the owner of a hid
repository. This can be done with the command

    $ cms proceedings list owner

## List paper1

For quick checks on the README for paper1 you may want to use the
following command

    $ cms proceedings list paper1

## List paper2

For quick checks on the README for paper2 you may want to use the
following command

    $ cms proceedings list paper2

## List peoject

For quick checks on the README for paper2 you may want to use the
following command

    $ cms proceedings list project


