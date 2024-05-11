from bs4 import BeautifulSoup
import sys
import glob


def remove_login_tag(infile_path, outfile_path):

    # print(infile_path)

    with open(infile_path, 'r') as archive:
        full_archive = archive.read()
        soup = BeautifulSoup(full_archive, 'html.parser')
        # provar aquí si el tag existe o no para extraerlo.
        s = soup.find("a", string="Admin")
        if s is not None:
            # print("***", s)
            # print(s)
            # s.extract
            parent_of_a_login = s.parent
            # print(parent_of_a_login)
            parent_of_a_login.extract()

    with open(outfile_path, 'w') as writeArchive:
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
        print(the_directory + subdirectories + '/*.html')
        new_files = glob.glob(the_directory + subdirectories + '/*.html')
        print(len(new_files))
        files_lst.extend(new_files)

        # continue adding depth levels only if in this level we've found at least one file
        adding_files = True
        if depth == 10:
            return
        # adding_files = len(new_files) > 0
        depth += 1

    return files_lst


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Add directory. Usage: python delete_intranet.py files_directory')
    basic_directory = sys.argv[1]
    # basic_directory = 'copy_statics_projects/ifisc.uib-csic.es'
    files_list = find_html_files_in_directory(basic_directory)
    # files_list.extend(glob.glob(basic_directory + '/*/*.html'))
    # files_list.extend(glob.glob(basic_directory + '/*/*/.html'))
    # files_list.extend(glob.glob(basic_directory + '/*/*/*.html'))

    for fpath in files_list:
        print(fpath)
        # remove_login_tag(fpath, fpath + '_new')
