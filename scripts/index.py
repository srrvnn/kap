# python script to organize files into meaning folders 
# part of an ambitious project to maintain files on a computer

# author: srrvnn

import os
import os.path

import shutil

import rules_pictures
import rules_documents
# import rules_videos
# import rules_music

folders = ["Pictures", "Documents", "Projects", "Music", "Videos", "Academics", "Trash"]
subfolders = []

for f in folders:
	if str(f) in ("Projects", "Academics","Trash"): continue
	subfolders.append(os.path.join(f,"Unsorted"))

root = 'C:\Users\esgee\Projects\kap\_world'
debug = False

# ------------------------------
# ROOT FOLDERS

# make root level folders if they don't exist

for d in folders:
	if not os.path.exists(os.path.join(root,d)):
		os.makedirs(os.path.join(root,d))

# make sub folders if they don't exist

for d in subfolders:
	if not os.path.exists(os.path.join(root,d)):
		os.makedirs(os.path.join(root,d))

# ------------------------------
# SORTING PICTURES 

# move all pictures-only folders into 'Pictures'

for d in os.listdir(root):

	file_path = os.path.join(root,d);

	# ignore if is isn't a directory

	if not os.path.isdir(os.path.join(root,d)): continue

	# ignore if it is an empty directory 

	if not os.listdir(os.path.join(root,d)): continue

	# ignore if is not a all pictures directory

	if not rules_pictures.isallpictures(os.path.join(root,d)): continue

	shutil.move(file_path, os.path.join(root, "Pictures"))

# move all pictures into 'Pictures'

for f in os.listdir(root):

	file_path = os.path.join(root, f);

	if rules_pictures.isapicture(f):

		shutil.move(file_path, os.path.join(root, "Pictures", "Unsorted"));

# ------------------------------
# SORTING DOCUMENTS 
	
# move all document-only folders into 'Documents'

# move all documents into 'Documents'

for f in os.listdir(root):

	file_path = os.path.join(root, f);

	if rules_documents.isadocument(f):

		shutil.move(file_path, os.path.join(root, "Documents", "Unsorted"));

# ------------------------------
# SORTING ACADEMICS

# ------------------------------
# SORTING ZIP FILES 

# what to do about .zip files?

# ------------------------------
# PRINTING FINAL LIST

# list the final folders for debug

if debug: 

	print "List all files:"
	print "---------------"

	for f in os.listdir(root):
		print f

