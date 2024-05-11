#!/usr/bin/env python
from bs4 import BeautifulSoup
import sys
import glob


def remove_login_tag(infile_path, outfile_path):
    # print(infile_path)
    with open(infile_path, 'r') as archive:
        full_archive = archive.read()
        # print(full_archive)
        soup = BeautifulSoup(full_archive, 'html.parser')
        # check if the tag exists
        print(infile_path)
        s = soup.find("a", text="Intranet")
        print(s)
        # if s is not None:
        #     # print("***", s)
        #     # print(s)
        #     # s.extract
        #     parent_of_a_login = s.parent
        #     # print(parent_of_a_login)
        #     parent_of_a_login.extract()

    with open(outfile_path, 'w') as write_archive:
        write_archive.write(str(soup))


def find_html_files_in_directory(the_directory):
    files_lst = []
    adding_files = True
    depth = 0
        
    while adding_files:
        subdirectories = ''
        for _ in range(depth):
            subdirectories += '/*'
        print(subdirectories)
        # find files with correct depth and html extension
        new_files = glob.glob(the_directory + subdirectories + '/*.html')
        files_lst.extend(new_files)
        # print(new_files)

        # continue adding depth levels only if in this level we've found at least one file
        adding_files = len(new_files) > 0

        depth += 1

    return files_lst


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Add directory. Usage: python delete_intranet.py files_directory')
    basic_directory = sys.argv[1]
    # basic_directory = 'copy_statics_projects/ifisc.uib-csic.es'
    files_list = find_html_files_in_directory(basic_directory)

    for fpath in files_list:
        fpath_split = fpath.split(".html")
        remove_login_tag(fpath, fpath + '_new.html')

