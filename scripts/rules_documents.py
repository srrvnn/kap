import os 
import os.path

image_extensions = ["TXT", "RTF", "PDF", "ODT", "WPD", "XLS", "XLSX", "ODS", "DOC", "DOCX"]

# function to detect if the give file is a document

def isadocument(f):
	
	ext = os.path.splitext(str(f))[-1].upper()
	ext = ext.replace(".","");

	if ext in image_extensions: return True
	else: return False