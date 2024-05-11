import os

# Elimina el login


def deleteLogin():
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*.html")
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*/*.html")
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"login\/index.html\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*/*/*.html")


def deleteLoginEunoiaProject():
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI' copy_statics_projects/*/*.html")
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI\' copy_statics_projects/*/*/*.html")
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*/*.html")
    os.system("sed -i \'s#<a href=\"http:\/\/www.eunoia-project.eu\/eunoadmin\">Login<\/a># #gI\' copy_statics_projects/*/*/*/*/*/*/*.html")


if __name__ == '__main__':
    deleteLogin()
    deleteLoginEunoiaProject()

