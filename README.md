# FBAdLibrarian - a helpful librarian for the Facebook Ad Library 

The FBAdLibrarian is a simple, command line tool that archives images from unique hyperlinks offered by the Facebook Ad Library API.

At the time of writing, Facebook permits the downloading of individual ad creatives such as images for academic research purposes. The Librarian assists researchers with this process. Users must have verified their identity with Facebook, received the appropriate access tokens for the API, and use this tool only for academic research purposes. 

The Librarian works as follows. First, the Librarian takes the ad_snapshot_url of an ad and creates a unique hyperlink, using the researcher's access tokens. Then, the Librarian looks up each ad individually. If the ad includes an image, the Librarian saves the image to an output folder and names the image according to the post’s unique ad identification number (or "adlib_id"). If the ad includes an embedded video, the Librarian will pass over the ad, but it will document the adlib_id as a video in an accompanying "metadata.txt" file. 


## Prerequisites
* Python 3 (Currently tested on 3.7 but might work on other versions)
* Verified access to Facebook Ad Library 
* Output data from Facebook Ad Library in xlsx format with semi-colon seperator (other formats and seperators are not supported as of now)  


## Installation
In order to install FBAdLibrarian you can either build from source or install via pip from the wheel distributable

In terminal/CMD:

If installing from wheel-file:
```bash
pip install "dist/FBAdLibrarian-0.1.4-py3-none-any.whl"
```

If building from source:

```bash
python setup.py install 
```

You have now installed the FBAdLibrarian!


## Usage

FBAdLibrarian is a CLi (Command line tool). You use the tool with the terminal/cmd.

Start a new project-folder for your data.
Assuming your project folder is called 'FBALproject', navigate to the project-folder.

In terminal/cmd:
```bash
cd "[your individual folder structure]/FBALproject"
```

First, initialiaze the project. This command will setup the librarians environment with necessary folders and files:
```bash
FBAL init "name-and-path-to-data-file-from-fb-ad-library"
```
The FBAdLibrarian creates the necessary files and folder. 
In the credentials-file insert your Facebook Ad Library tokens.
You are now all set to archive images for research.

Now, still in the project folder simply start the librarian:
```bash
FBAL start 
```
The program is now running and you should see the archived images in the output-folder.  

If the librarian stops for whatever reason (e.g. if your token is expired), fix the issue and simply type the 'FBAL start'-command again and the librarian will restart where it left off.


For further help see the [documentation](https://fbadlibrarian.readthedocs.io/en/latest/index.html). 



## Contributing
Please refer to the project's style for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

1. Fork the repo on GitHub
2. Clone the project to your own machine
3. Commit changes to your own branch
4. Push your work back up to your fork
5. Submit a Pull request so that we can review your changes  



## License
FBAdLibrarian is published under the GNU General Public License v3.0.  
Read the license [here](LICENSE).

