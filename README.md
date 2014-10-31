create_project
==============
This is a Python program for creating the directory structure and some of the files needed for a new project. 
[Here](https://dl.dropboxusercontent.com/u/420874/permanent/testproject.pdf) is an example of the PDF created by `create_project.py`. 

To instal
---------
To set it up, download the package and symlink the `create_project.py` to `/usr/local/bin` e.g., 
	
	git clone git@github.com:johnjosephhorton/create_project.git
	cd create_project

Next, modify the `settings.py` with your name, school, preferred directory structure and so on. 
For example, my `settings.py` is: 

```
author = "John J. Horton" 
school = "NYU Stern" 
footnote = """Author contact information, datasets and code are currently or will be available at \\href{http://www.john-joseph-horton.com/}{http://www.john-joseph-horton.com/}."""
bibliography_style = "aer" 
```

Once you have modified `settings.py`, run: 
	
	sudo python setup.py install 

Once you save your changes, you can simply run: 

	create_project PROJECTNAME 

The script will create a new directory `PROJECTNAME` with associated sub-directories.
The script will also populate these folders with "stub" files, depending upon the files specified in the function `created_stub_files` and the templates in the `./templates` folder. 
In this default configuration, the stub files created are a latex file, a bibtex file and a Makefile, all in the `./writeup` folder.

Runnning `make` to build your PDF 
---------------------------------
`create_project` creates a simple R file that generates a PDF of a histogram, which it places in `writeup/plots`. 
By default, `writeup/Makefile` is set to have this histogram PDF as a dependency for the `PROJECT_NAME.pdf` and so running `make` from the writeup directory will cause R to run. 
The packages R will need are: 
	
	ggplot2 
	testthat 
	scales 
	
Getting a summary of your document
----------------------------------
From the `./writeup` directory, you can execute `make summary.md`
which will generate a markdown file showing lists of important claims
from the LaTeX document (those you have wrapped like so
`\important{Important claim}`). It also does the same for lines wrapped
in `\quantclaim`, which is a quantitative claim (I am always checking
to see if these claims match the tables and figures and this
simplifies the checking). Note that these tools require you to use one
sentence per line in your LaTeX document. This summarization is done
using a bash script called `summary.sh` in the writeup folder.  

License
-------
See the `licence` file. 




	
