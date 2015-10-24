"""
quick make-version script, part of the Js project generator.
https://github.com/RonenNess/JavascriptProjectsGenerator
"""

import os
import json
import shutil

# get current version
with open("curr_version.txt", "r") as infile:
	curr_version = str(infile.readlines()[-1]).strip()
print "Make version: %s..." % curr_version

# move previous version to "older"
for root, subFolders, files in os.walk("dist"):
	for file in files:
		if file.lower().endswith(".js"):
			shutil.move(os.path.join("dist", file), os.path.join("dist/older/", file))
	break
	
# copy dev version to current stable version
shutil.copy("dist/dev/<projectname>.dev.js", "dist/<projectname>.%s.js" % curr_version)
shutil.copy("dist/dev/<projectname>.dev.min.js", "dist/<projectname>.%s.min.js" % curr_version)

# copy to npm
shutil.copy("dist/dev/<projectname>.dev.js", "dist/npm/index.js")
shutil.copy("README.md", "dist/npm/README.md")

# update package.json
with open("dist/npm/package.json", "r") as infile:
	package = json.loads(infile.read())
package["version"] = curr_version
with open("dist/npm/package.json", "w") as outfile:
	outfile.write(json.dumps(package, indent=4, separators=(',', ': ')))

# change version
new_version = ""
while len(new_version) == 0:
	new_version = raw_input("Current version is %s, Please provide next version name: " % curr_version)
with open("curr_version.txt", 'a') as outfile:
	outfile.write('\n' + new_version)
	
print "Done!"
print "(Don't forget to update NPM & changelog in README.md!)"
