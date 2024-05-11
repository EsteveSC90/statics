import subprocess
import sys
 
print("Número de parámetros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

#NOTA: Primer argument el nom del archiu

if len(sys.argv) == 1 :
    
    my_urls = [
        # "www.gefenol.es/FisEs/",
        # "www.gefenol.es/school2011/",
        # "www.gefenol.es/school2013/",
        # "www.gefenol.es/school2014/",

        # "https://crossroads2017.ifisc.uib-csic.es//undefined?1663076024185",
        # "http://crossroads2017.ifisc.uib-csic.es/favicon.ico",
        "http://school.rice.hbar.es/media/"
        # "http://www.eunoia-project.eu/static/js/topup/javascripts/top_up-min.js"

        # "https://fises18.gefenol.es/static/main/css/bootstrap-responsive.min.css",
        # "https://fises18.gefenol.es/static/main/images/camera_skins.png",
        # "https://fises18.gefenol.es/static/main/images/camera-loader.gif",
        
        # "https://fises17.gefenol.es/static/main/js/jquery.min.js",
        # "https://fises17.gefenol.es/static/main/css/modifications.css",
        # "https://fises17.gefenol.es/static/main/images/camera_skins.png"
        # "https://fises17.gefenol.es/static/main/images/camera-loader.gif"

        #"https://ifisc.uib-csic.es/LINCschool/",
        #"https://ifisc.uib-csic.es/futurict/",
        #"https://fises15.gefenol.es/",
        #"http://www.eunoia-project.eu/",
        #"https://fises17.gefenol.es/",
        


    ]

else:

    my_urls = sys.argv
    #Eliminam la primera posició del array tret per arguments que era el nom del archiu
    my_urls.pop(0)


# Array de parametros utilizados (NORMALMENTE NO SE TIENEN PORQUE TOCAR)
my_params = [ 
    '--cipher', 'DEFAULT:!DH',
    '--no-check-certificate',
    '--mirror',
    '--convert-links',
    '--adjust-extension',
    '--page-requisites',
    '--no-parent',
 ]


i = 0
# longitud array de urls
# print(len(my_urls))
while i < len(my_urls):

    # JUNTAMOS ARRAYS
    # Base para hacer wget
    new_params1 = ['wget', '-r', my_urls[i]]
    # print(new_params1)

    # Juntamos a la base los parametros
    new_params1.extend(my_params)
    # print(new_params1)
    subprocess.call(new_params1)
    i += 1
    # print(i)

