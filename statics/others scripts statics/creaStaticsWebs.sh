#!/bin/bash
contador=0
my_array=(https://crossroads2017.ifisc.uib-csic.es/ majonext2017.ifisc.uib-csic.es https://ifisc.uib-csic.es/LINCschool/)
termina=${#my_array[@]}
echo $termina

while [ $contador -le $termina ]

do
	wget --cipher 'DEFAULT:!DH'  --mirror --convert-links --adjust-extension --page-requisites --no-parent  ${my_array[$contador]}
	let contador=$[$contador+1]
done
