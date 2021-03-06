"""
quick build script, part of the Js project generator.
https://github.com/RonenNess/JavascriptProjectsGenerator
"""

import os
import sys

# get files list
files = open("files_to_build.txt", "r").read().split("\n")

# get current version
with open("curr_version.txt", "r") as infile:
	curr_version = str(infile.readlines()[-1]).strip()	
print "Build version: %s..." % curr_version
	
# combine all code into a single file
full_code = ""
for file in files:
    if file.startswith("#") or len(file) <= 0:
        continue
    with open(os.path.join("src", file), 'r') as src:
        full_code += "// FILE: " + file + "\r\n\r\n"
        full_code += src.read() + "\r\n\r\n"

compiled_filename = 'dist/dev/<projectname>.dev.js'
minified_filename = 'dist/dev/<projectname>.dev.min.js'

# update version
full_code = full_code.replace("___curr_version___", curr_version)

# write full version
dest = open(compiled_filename, 'w')
dest.write(full_code)
dest.close()

print "Minify..."

# minify
os.system("java -jar yuicompressor-2.4.8.jar %s -o %s" % (compiled_filename, minified_filename))

print "Done!"
