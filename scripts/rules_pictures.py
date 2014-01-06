import os 
import os.path

image_extensions = ["ANI","BMP","CAL","FAX","GIF","IMG","JBG","JPG", "JPEG","JPE","JPG","MAC","PBM","PCD","PCX","PCT","PGM","PNG","PPM","PSD","RAS","TGA","TIFF","WMF"]

# function to detect if the give file is a picture

def isapicture(f):
	ext = os.path.splitext(str(f))[-1].upper()
	ext = ext.replace(".","");

	if ext in image_extensions: return True
	else: return False

# function to detect if the give folder is an all pictures folder

def isallpictures(d):

	# check if all existing files have the extension	

	for f in os.listdir(d):

		if not isapicture(f): return False; 

	return True;

