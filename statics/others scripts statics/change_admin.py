import os


def delete_admin(the_directory):
    depth = 0
    while True:
        subdirectories = ''
        for _ in range(depth):
            subdirectories += '/*'
        # new_files = glob.glob(the_directory + subdirectories + '/*.html')
        os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects" + subdirectories + ".html")

    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*/*.html")
    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*/*/*.html")
    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*/*/*/*.html")
    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*/*/*/*/*.html")
    # os.system("sed -i \"s#<a href='admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*/*/*/*/*/*.html")


def delete_admin_fises17():
    # Fises'17
    os.system("sed -i \"s#<a href='paneles\/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='horarios\/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='conferencias_orales\/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='conferencias_invitadas/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='como_llegar/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='alojamiento/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")
    os.system("sed -i \"s#<a href='donde_comer/admin\/index.html'>admin<\/a># #gI\" copy_statics_projects/*/*.html")


if __name__ == '__main__':

    delete_admin()
    delete_admin_fises17()
    
