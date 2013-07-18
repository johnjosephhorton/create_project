#!/usr/bin/env python

import argparse 
import os 
import sys 
from jinja2 import Environment, PackageLoader 
import settings 

env = Environment(loader=PackageLoader('create_project', 'templates'))

def create_file_structure(project_name, project_dir):
    """This creates basic file structure for the project."""
    dirs = settings.dirs 
    os.mkdir(os.path.join(project_dir, project_name))
    for d in dirs:
        os.makedirs(os.path.join(project_dir, project_name, d))

def create_stub_files(project_name, project_dir):
    """Creates stub files in the target directory. In the files_to_create 
    list, the ordering is (template, name, location)."""
    bibliography_line  = "\\bibliography{%s.bib}" % project_name
    latex_template = env.get_template('base_latex.tex').render(project_name = project_name, 
                                                               author = settings.author, 
                                                               school = settings.school, 
                                                               footnote = settings.footnote, 
                                                               bibliography_line = bibliography_line)
    bibtex_template = env.get_template('base_bibtex.bib').render() 
    makefile_template = env.get_template('make_template').render(project_name = project_name)
    files_to_create = [(latex_template, "%s.tex" % project_name, "writeup"), 
                       (bibtex_template, "%s.bib" % project_name, "writeup"), 
                       (makefile_template, "Makefile", "writeup")]
    for template, file_name, location in files_to_create: 
        f = open(os.path.join(project_dir, project_name, location, file_name), "w")
        f.write(template)
        f.close() 

def main():
    parser = argparse.ArgumentParser(description = "Create a new project folder structure")
    parser.add_argument("name", help = "Project name") 
    args = parser.parse_args()
    name = args.name 
    if "_" in args.name: 
        answer = raw_input("""Ironically, project names with '_' are problematic. 
                              Is the name %s instead OK? [Y/n]? """% (name.replace("_", "")))
        if answer in ("Y", "y", "Yes", "yes", "YES", "Ja", "Sure", "Si"): 
            name = name.replace("_", "")
        else:
            print("Project creation canceled.")
            exit 
    create_file_structure(name, os.getcwd())
    create_stub_files(name, os.getcwd())
    print("Project created. To test, change directory to ./%s/writeup and run 'make' to create the pdf" % name )

if __name__ == '__main__':
    main() 






