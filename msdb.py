import os
import pytest
header = ["artist-","trackid-","song"+"\n"]
subdirectory = []
path = "/Users/adamgoldstein/Desktop/GTown/Adam_SSP/FLAC/"
with open("file.txt","w+") as source:
	for field in header:
		source.write(field)
	for root, dirs, files in os.walk(path):
		try:
			for file in files:
				if file.endswith(".flac") and file[0].isalpha():
					a = file.replace(".flac","")
					source.write(a+'\n')
		except:
			continue

 


#from os import walk
#path = "/Users/adamgoldstein/Desktop/GTown/Adam_SSP/FLAC"

#with open('file.txt','w+') as file:
#	for (dirpath, dirnames, filenames) in walk(path):
#		for x in filenames:
#			ds = x.split(".DS_Store")
#			file.write(ds[0]+'\n')

	
