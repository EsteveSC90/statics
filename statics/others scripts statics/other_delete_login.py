#!/usr/bin/env python
from bs4 import BeautifulSoup
import glob
import sys


def remove_tag_login(infile_path, outfile_path, stringLogin):

    with open(infile_path, 'r') as archive:

        full_archive = archive.read()
        soup = BeautifulSoup(full_archive, 'html')
        
        # try here if the tag exist or no for extract
        # provar aquí si el tag existe o no para extraerlo.
        s = soup.find("a", string=stringLogin)
        if s is not None:
            parent_of_a_login = s.parent
            parent_of_a_login.extract()
            print("fet")

    with open(outfile_path, 'w') as writeArchive:
        # change to string the object soup
        # paso a string el objeto soup
        soupString = str(soup)
        writeArchive.write(soupString)


def find_html_files_in_directory(the_directory):
    files_lst = []
    adding_files = True
    depth = 0
        
    while adding_files:
        subdirectories = ''
        for _ in range(depth):
            subdirectories += '/*'
        # find files with correct depth and html extension
        new_files = glob.glob(the_directory + subdirectories + '/*.html')
        files_lst.extend(new_files)

        # continue adding depth levels only if in this level we've found at least one file
        if depth == 10:
            return files_lst

        depth += 1

    return files_lst


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Add directory. Usage: python delete_login.py files_directory tag')
        # example: python3 delete_login.py copy_statics_projects/fises15.gefenol.es/ Login
        # example: python3 delete_login.py ../copy_statics_projects/fises15.gefenol.es/ Login
    basic_directory = sys.argv[1]
    tag = sys.argv[2]
    # basic_directory = 'copy_statics_projects/ifisc.uib-csic.es'
    files_list = find_html_files_in_directory(basic_directory)
    # print("-----", files_list)
    for fpath in files_list:
        # print("***", fpath)
        fpath_split = fpath.split(".html")
        # remove_tag_login(fpath, fpath + '_new.html', tag)
        remove_tag_login(fpath, fpath, tag)
