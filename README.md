# What is this?

This project is an empty template for new javascript projects.

You can use it to quickly generate the basic files and directory structure for any javascript lib or project. 

# How to create a new project

To create a new project from this template, run the **create_project.py** script and answer a few questions.
This will create a new folder with your project name ready to be used.

# How to use the newly created project

After the new project is created, there are few things you need to know about how to use it:

## Build the project

Inside your new project dir you will find a python script called "build.py".

Running it will build your entire project (eg combine all source files into a single javascript file) and will also create a minified version.
The outout will be in the dist/dev/ folder.

Note: this script will build only javascript files that are listed in "files_to_build.txt".
So whenever adding a new javascript file, be sure to add it to list.

## Things to do after creating the project

- Update the readme.md file in the project root.
- If you want to distirbute the lib in npm, be sure to check dist/npm/package.json to make sure data is ok.
- If you want a license other than zlib, be sure to replace the LICENSE.txt & src/license.js files.

## Making a version

Making a version will update the distribution folder..
Basically it will do the following:

- Copy the files from /dist/dev/ into /dist/, and add version number to the name.
- Advance the version number for next build (will affect future compilations)
- Updat the /dist/npm/ folder with latest readme.md file and compiled version. Will also update the package.json file.

To make a new version simply run the script **make_version.py**.

## About

This projects generator is made by Ronen Ness.
Feel free to use / modify it for any purpose (commercial & educational).

To contact me:
RonenNess@gmail.com