# FBAdLibrarin - a helpful librarian for Facebook Ad Library
Desciprtion of the package

## Getting started


## Prerequisites
* Python 3 (Is tested on 3.7 but might work on other versions)
* Data from Facebook Ad Library in csv format with semi-colon seperation (other formats and seperators are not supported as of now)

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
FBAL init "path-to-data-from-fb-ad-library-csv-file"
```
The FbAdLibrarian have created the necessary files and folder. 
In the credentials-files insert your Facebook Ad Library token.
You are now all set to fetch images.

Now, simply start the librarian
```bash
FBAL start 
```
The program is now running and you should see the fetched images in the output-folder.
If the librarian stops for whatever reason, simply type the 'FBAL start' command again and the librarian will restart from where it left off.



For futher help see the [documentation](docs/build/html/index.html)

## Contributing


## License

Be sure that the Credentials.yaml is updated with a working access token (keep it in the root-folder /AdsProject)
```

facebook:
    access_token: [insert_acces_token_here]
    
amazon:
    personal_access_key : [insert_personal_access_key_here]
    secret_access_key : [insert_secret_access_key_here]

```



Set up pipenv-environment and run the installation for necessary dependencies.
- install pipenv via pip

```
pip install pipenv
```

- In CMD navigate to the project-folder: 'CD [path_to_project_folder]


- Afterwards install necessary dependencies using:

```

pipenv install --dev

```
- To start and run  pipenv shell:

```
pipenv shell
```

- then run the prepareScraping.py from commandoprompt / terminal
The prepareScraping is a command line interface (CLI) taking the datafile from the graph API by it's relative or absolute path

```
python prepareScraping.py <name_of_file>
```

This app places two txt-files from in the samme path as the app. This is two files containing the url-list and the ad id-list respectively.
Use these as input to the scraper, which is also a CLI

```
python scraper.py <name_of_url_list_file> <name_of_ad_id_list_file> <output_dir>
```

if the code breaks it SHOULD place a log in the logs-folder.
This folder can be used to take up the scraping from where it left off.
