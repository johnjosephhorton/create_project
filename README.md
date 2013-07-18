create_project.py
=================

This is a python script for building a directory structure and a "hello world" version of a LaTeX paper. 
[Here](https://dl.dropboxusercontent.com/u/420874/permanent/testproject.pdf) is an example of the PDF created by create_project.py. 

Author
------
John J. Horton <john.joseph.horton@gmail.com>

Configuration
-------------
By modifying the file `settings.py`, you can create custom values for author name, affiliation, standard "thanks" footnotes, directory structure, etc. 

How it works
------------
You run: 

	create_project.py PROJECTNAME 

from the directory where you want the project to live.
The script will create a new directory `PROJECTNAME` with associated sub-directories specified in the `dir` variable in `settings.py`. 
The script will also populate these folders with "stub" files, depending upon the files specified in the function `created_stub_files` and the tempaltes in the `./templates` folder. 
In this default configuration, the only stub files created as a latex file, a bibtex file and a Makefil, all in the `./writeup` folder. 

	
