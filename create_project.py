import re
import os, shutil
import datetime

def validate_input(txt):
	"""
	validate user input
	"""
	return re.match("^[A-Za-z0-9_-]*$", txt)
		
def get_input(desc, validate):
	"""
	get input from user and validate it if needed
	"""
	val = ""
	while len(val) == 0:
		 val = raw_input(desc).strip()
		 if len(val) and validate and not validate_input(val):
			print "Value may only contain English characters, numbers and underscores!"
			val = ""
	return val


# get project info	
print "This script will create a new project directory."
project_name = get_input("Project name: ", True)
project_tagline = get_input("Project tagline: ", False)
author = get_input("Author: ", False).title()
email = get_input("Email: ", False)
date = datetime.datetime.now().ctime()

# create it
shutil.copytree("template", project_name)

# replace all data
valid_extensions = ["js", "md", "txt", "py", "json"]
for root, subFolders, files in os.walk(project_name):
	for file in files:
		if file.lower().split(".")[-1] in valid_extensions:
			with open(os.path.join(root, file), "r") as infile:
				data = infile.read()
			data = data.replace("<Date>", 			date)
			data = data.replace("<Email>", 			email)
			data = data.replace("<Author>", 		author)
			data = data.replace("<author>", 		author.lower().replace(" ", ""))
			data = data.replace("<TagLine>", 		project_tagline)
			data = data.replace("<ProjectName>", 	project_name)
			data = data.replace("<projectname>", 	project_name.lower())
			with open(os.path.join(root, file), "w") as outfile:
				outfile.write(data)
		
print "Done! new project dir is at " + project_name