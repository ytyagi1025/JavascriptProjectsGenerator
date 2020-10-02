# What is it?

This script generate empty templates for new javascript projects.
You can use it to quickly generate the basic files and directory structure for any javascript lib or project. 

# Features

Generate new JavaScript project structure with:

- Quick build & minify script
- Make-version script
- Built-in z-lib license
- Example html template
- README.md template file
- Required files to build an npm package out of it
- Basic source files with project's namespace, version and license

You can check out an example project generated in **example.zip**.

# No Grunt

You might wonder why on earth this generator doesn't use grunt.
The answer is to keep it as simple as possible, and without requiring any additional configuration / installs.

This is not the best approach and it is recommended to switch to grunt once the project grows.

Also, take a look at this fine javascript template: https://github.com/jeremyckahn/lib-tmpl

It requires more work to setup, but its more suitable for large npm libraries.

# How to create a new project

To create a new project from this template, run the **create_project.py** script and answer a few questions.
This will create a new folder with your project name ready to be used.


## Things to do after creating the project

Its recommended that you take few steps after creating a new project:

- Update the readme.md file in the project root (will have some TBDS for you to fill-in).
- If you want to distirbute the lib as npm package, be sure to validate the data in dist/npm/package.json.
- If you want a license other than zlib, replace LICENSE.txt with your new license and update the src/license.js file.


# How to use the newly created project

After the new project is created, there are few things you need to know about how to use it:

## Build the project

Inside your new project dir you will find a python script called **build.py**.

Running it will build your entire project (eg combine all source files into a single javascript file) and will also create a minified version.
The output files will be in the dist/dev/ folder.

Note: this script will build only javascript files that are listed in "files_to_build.txt".
Whenever adding new javascript files, be sure to update the list as well.

## Making a version

Making a version will update the dist folder.
Basically it will do the following:

- Copy the files from /dist/dev/ into /dist/, and add version number to the name.
- Update the version number for the next build (will affect future compilations)
- Updat the /dist/npm/ folder with latest readme.md file and compiled version. This will also update the package.json file.

To make a new version simply run the script **make_version.py**.

## About

This projects generator is made by Ronen Ness.
Feel free to use / modify it for any purpose (commercial & educational).
* These files and scripts are not intended for malicious purposes

To contact me:
RonenNess@gmail.com
