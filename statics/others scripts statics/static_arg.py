import subprocess
import sys
 
print("Número de parámetros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

# NOTA: Primer argument el nom del archiu

if len(sys.argv) == 1 :
    
    my_urls = [
        
        "http://www.gefenol.es/school2011/tcs/scripts/jquery-1.2.6.min.js",
        "http://www.gefenol.es/school2011/tcs/scripts/jquery.datePicker.js",
        "http://www.gefenol.es/school2011/tcs/scripts/date.js",
        "http://www.gefenol.es/school2011/tcs/style/datePicker.css",
        "https://www.gefenol.es/school2011/intranet/galleryadm/files/small/"

        # "https://ifisc.uib-csic.es/LINCschool/",
        # "https://ifisc.uib-csic.es/futurict/",
        # "https://fises15.gefenol.es/",
        # "http://www.eunoia-project.eu/",


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

