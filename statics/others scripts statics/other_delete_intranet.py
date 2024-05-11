#!/usr/bin/env python
from bs4 import BeautifulSoup
import sys
import glob
import re


def remove_login_tag(infile_path, outfile_path):
    
    with open(infile_path, 'r') as archive:
        full_archive = archive.read()
        soup = BeautifulSoup(full_archive, 'html')
        # check if the tag exists
        # print("-infile_path:", infile_path)
        s = None
        # s = soup.find('a', href=re.compile("page/show/id/5.htm"))
        # s = soup.find('a', href=re.compile("intranet/presentations.html"))
        # s = soup.find('a', href=re.compile("newcar.html"))
        # s = soup.find('a', href=re.compile("futurict/backend.php"))
        # s = soup.find('a', href=re.compile("nloa2012/login"))
        s = soup.find('link', href=re.compile("static/js/nivo-slider/style.css"))
        if s is not None:
            parent_of_a_login = s.parent
            parent_of_a_login.extract()
            # s.extract()
        print(s)

    with open(outfile_path, 'w') as write_archive:
        # soupString = str(soup)
        write_archive.write(str(soup))


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
        print('Add directory. Usage: python delete_intranet.py files_directory')
        # example: python3 delete_intranet.py copy_statics_projects/ifisc.uib-csic.es/futurict/
        # example: python3 delete_intranet.py ../copy_statics_projects/ifisc.uib-csic.es/futurict/
    basic_directory = sys.argv[1]
    # basic_directory = 'copy_statics_projects/ifisc.uib-csic.es'
    files_list = find_html_files_in_directory(basic_directory)

    for fpath in files_list:
        # remove_login_tag(fpath, fpath + '_new.html')
        remove_login_tag(fpath, fpath)
