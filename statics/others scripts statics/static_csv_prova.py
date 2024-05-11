import subprocess
import csv
import logging
import sys


# Example to run this script: 
# sudo python3 static_csv.py csv/webs.csv statics_projects/ logs/log_file
class FilesStatics:

    def read(self, ficherocsv):
        # logging.info(self)
        logging.info(ficherocsv)
        myNewListUrl = []

        with open(ficherocsv, 'r', newline='') as csvfile:  
            logging.info('Starting to read from csv: ')
            
            # logging.error('Something happened - never starting 
            # to read from csv')
            reader = csv.reader(csvfile)

            # print(File.closed)
            for row in reader:
                # compara si running == TRUE i tecnology == 'Static'
                # Si es així afegirà al array la url i el alias
                # Es a dir feim la llista de url amb els alias que volem baixar
                if row[2] == 'TRUE' and row[3] == 'Static':
                
                    logging.info('Append url: ' + row[0])
                    myNewListUrl.append(row[0])  # guardarà l'url
                    # myNewListUrl.append(row[1]) # guardarà l'alias

            logging.info('Finished to reading!!')

        return myNewListUrl 

    def download(self, myNewListUrl, routeDownload):
        # tenc la llista de urls que volem baixar
        # ListUrl = FilesStatics().read()
        cont = 0

        params = [ 
            '--cipher', 'DEFAULT:!DH',
            '--no-check-certificate',
            '--mirror',
            '--convert-links',
            '--adjust-extension',
            '--page-requisites',
            '--no-parent',
            '-P', routeDownload,
            '-a', "logs/log_wget_file"
        ]

        logging.info('Starting to downloding')
        
        for element in myNewListUrl:
            try:
                # JUNTAMOS ARRAYS
                # Base para hacer wget
                new_params1 = ['wget', '-r', element]
                # Juntamos a la base los parametros
                new_params1.extend(params)
                # print(new_params1)
                # subprocess.call(new_params1)

                # Si el xsubprocess dona diferent de 0 es que no a anat be 
                # i no s'ha pogut devallar
                xsubprocess = subprocess.call(new_params1)
                if xsubprocess != 0:
                    logging.error(str(xsubprocess)
                                  + ' Unable to resolve host address: '
                                  + element)
                    cont += 1
                else:
                    logging.info(str(xsubprocess)+' Downloading:' + element)

            except Exception as e:
                logging.error('Error downloading from url' + element)
                logging.error(e)
            
            # print(element)
        if cont == 0:
            logging.info('Congrats!! All downloads complete without errors!!')
        else:
            logging.info('All downloads complete, but with ', str(cont) 
                         + 'errors. Please check errors')

        
def start_log(filelog):
    logging.basicConfig(filename=filelog, level=logging.INFO)
    logging.info('Started')
    # do_something()


def finished_log():
    logging.info('Finished script!! \n\n')
    

if __name__ == '__main__':
    try:
        ficherocsv = sys.argv[1]
        routeDownload = sys.argv[2]
        filelog = sys.argv[3]

        start_log(filelog)
        # logging.info(x)
        # Em treu llistat de url's que volem baixar
        myNewListUrl = FilesStatics().read(ficherocsv)
        
        # El llistat de url el pas a la funció download perque amb la url 
        # les baixarà amb el wget
        FilesStatics().download(myNewListUrl, routeDownload)

        finished_log()

    except Exception as e:
        logging.error('Error ocurred: ' + str(e))
