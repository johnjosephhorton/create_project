create_project
==============
This is a Python script for creating the directory structure and some of the files needed for a new project. 
[Here](https://dl.dropboxusercontent.com/u/420874/permanent/testproject.pdf) is an example of the PDF created by `create_project.py`. 
To set it up, download the package and symlink the `create_project.py` to `/usr/local/bin` e.g., 
	
	git clone git@github.com:johnjosephhorton/create_project.git
	ln -s create_project/create_project.py /usr/local/bin 

Next, modify the `settings.py` with your name, school, preferred directory structure and so on. 
For example, my `settings.py` is: 

```
author = "John J. Horton" 
school = "NYU Stern" 
footnote = """Author contact information, datasets and code are currently or will be available at \\href{http://www.john-joseph-horton.com/}{http://www.john-joseph-horton.com/}."""
bibliography_style = "aer" 

dirs = [
    'literature', 
    'code/R', 
    'code/SQL', 
    'code/python', 
    'data',
    'models',    
    'submit', 
    'writeup/images', 
    'writeup/numbers', 
    'writeup/plots', 
    'writeup/tables',
    'writeup/diagrams', 
]
```

Once you save your changes, you can simply run: 

	create_project.py PROJECTNAME 

The script will create a new directory `PROJECTNAME` with associated sub-directories specified in the `dir` variable in `settings.py`. 
The script will also populate these folders with "stub" files, depending upon the files specified in the function `created_stub_files` and the templates in the `./templates` folder. 
In this default configuration, the stub files created are a latex file, a bibtex file and a Makefile, all in the `./writeup` folder.

Runnning `make` to build your PDF 
---------------------------------
`create_project.py` creates a simple R file that generates a PDF of a histogram, which it places in `writeup/plots`. 
By default, `writeup/Makefile` is set to have this histogram PDF as a dependency for the `PROJECT_NAME.pdf` and so running `make` from the writeup directory will cause R to run. 
The packages R will need are: 
	
	ggplot2 
	testthat 
	scales 

License
-------
See the `licence` file. 




	
