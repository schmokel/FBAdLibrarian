# FBAdLibrarin - a helpful librarian for Facebook Ad Library


## Installation


## Usage

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