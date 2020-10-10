# FBAdLibrarian - a helpful librarian for Facebook Ad Library 
Desciprtion of the package



## Prerequisites
* Python 3 (Is tested on 3.7 but might work on other versions)
* Access to Facebook Ad Library 
* Output data from Facebook Ad Library in csv format with semi-colon seperator (other formats and seperators are not supported as of now)

## Installation
In order to install the FbAdLibrarin you can either build from source or install via pip from the wheel distributable

In terminal/CMD:

Install from the wheel-file
```bash
pip install "dist/FBAdLibrarian-0.1.4-py3-none-any.whl"
```

or build from source:

```bash
python setup.py install 
```

You have now install the FBAdLibrarian in your python environment.

## Usage

FBAdLibrarian is a CLi (Command line tool). You use the tool with the terminal/cmd.

Start a new project-folder for your data.
Assuming your project folder is called 'testproject', navigate to the project-folder.
In terminal/cmd:
```bash
cd "[your individual folder structure]/testproject"
```

First, initialiaze the project. This command will setup the librarians environment with necessary folders and files
```bash
FBAL init "path-to-csv-file-from-fb-ad-library"
```
The FbAdLibrarian have created the necessary files and folder. 
In the credentials-files insert your Facebook Ad Library token.
You are now all set to fetch images.

Now, simply start the librarian
```bash
FBAL start 
```
The program is now running and you should see the fetched images in the output-folder.
If the librarian stops for whatever reason, fix the issue (e.g. if your token is expired) and simply type the 'FBAL start'-command again and the librarian will restart where it left off.



For futher help see the [documentation](docs/build/html/index.html)

## Contributing


## License
FBAdLibrarian is licensed under the GNU General Public License v3.0
Read the license [here](LICENSE)

