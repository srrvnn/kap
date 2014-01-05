# python script to organize files into meaning folders 
# part of an ambitious project to maintain files on a computer

# author: srrvnn
# license: not for reproduction

import os
import os.path

import shutil

folders = ["Pictures", "Documents", "Projects", "Music", "Videos", "Academics", "Trash", os.path.join("Pictures","Unsorted")]
image_extensions = ["ANI","BMP","CAL","FAX","GIF","IMG","JBG","JPG", "JPEG","JPE","JPG","MAC","PBM","PCD","PCX","PCT","PGM","PNG","PPM","PSD","RAS","TGA","TIFF","WMF"]

# function to detect if the give folder is an all pictures folder

def isallpictures(d):

	# check if all existing files have the extension	

	for f in os.listdir(d):

		if not isapicture(f): return False; 

	return True;

# function to detect if the give file is a picture

def isapicture(f):
	ext = os.path.splitext(str(f))[-1].upper()
	ext = ext.replace(".","");

	if ext in image_extensions: return True
	else: return False

root = 'C:\Users\esgee\Projects\kap\_world'
debug = False

# make root level folders if they don't exist

for d in folders:
	if not os.path.exists(os.path.join(root,d)):
		os.makedirs(os.path.join(root,d))

# move all pictures-only folders into Pictures

for f in os.listdir(root):

	file_path = os.path.join(root,f);

	# ignore if is isn't a directory

	if not os.path.isdir(os.path.join(root,f)): continue

	# ignore if it is an empty directory 

	if not os.listdir(os.path.join(root,f)): continue

	# ignore if is not a all pictures directory

	if not isallpictures(os.path.join(root,f)): continue

	shutil.move(file_path, os.path.join(root, "Pictures"))

# move all pictures into Pictures

for f in os.listdir(root):

	file_path = os.path.join(root, f);

	if isapicture(f):

		shutil.move(file_path, os.path.join(root, "Pictures", "Unsorted"));
	
# move all document-only folders into documents

# create sub folders projects

# list the final folders for debug

if debug: 

	print "List all files:"
	print "---------------"

	for f in os.listdir(root):
		print f

