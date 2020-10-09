# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:31:59 2020

@author: rasmu
"""
import click
import pandas as pd
from datetime import datetime
import os
import re
import facebookScraper.scraper as sp
#from colorama import Fore, Back, Style


@click.group()
def main():
    pass
   

@main.command()
@click.argument('datafile')
def init(datafile):
    #creating project structure
    folders = ['temp', 'output']
    
    for folder in folders:
        print("Creating %s-folder" % folder)
        if os.path.exists('./%s' % folder):
            click.echo(click.style("%s-folder already exists" % folder, fg = 'yellow'))
        else:
            try:
                os.mkdir(folder)
            except OSError:
                click.echo(click.style("Creation of the directory %s failed" % folders, fg = 'red'))
            else:
                #print(Fore.GREEN + "Succesfully created %s-folder" % folder)
                click.echo(click.style("Succesfully created %s-folder" % folder, fg = "green"))
        
      
    if os.path.isfile('facebookAccessToken.txt'):
        click.echo(click.style("Warning! Credentials-file already exists", fg = "yellow"))
    else:
        print('Creating credentials-file: facebookAccessToken.txt')
        with open("facebookAccessToken.txt", 'w') as writer:
            writer.write("")
        writer.close()
        click.echo(click.style("Succesfully created credentials-file", fg = "green"))
        
        
    if os.path.isfile('metadata.txt'):
        click.echo(click.style("Warning! Metadata-file already exists", fg = "yellow"))   
    else:
        print('Creating metadata-file')
        with open("metadata.txt", 'w') as writer:
            writer.write("link, adid, content_type")
        writer.close()
        click.echo(click.style("Succesfully created metadata-file", fg = "green")) 


    #creating lists
    print('Creating internal data')
    data = pd.read_excel(str(datafile))
    adid_list = list(data['adlib_id'])
    url_list = list(data['ad_snapshot_url'])
    click.echo(click.style('Succesfully creating internal data', fg = "green")) 
    
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    with open("temp/url_list_" + timestamp + ".txt", 'w') as filehandle:
        for listitem in url_list:
            filehandle.write('%s\n' % listitem)
    
    with open("temp/adid_list_" + timestamp + ".txt", 'w') as filehandle:
        for listitem in adid_list:
            filehandle.write('%s\n' % listitem)




@main.command()
def start():
    folder = 'temp/'
    files = os.listdir(folder)

    adid_pattern = re.compile(r'adid_list_\d{14}\.txt$')
    adid_file = max(filter(adid_pattern.search, files))
    
    url_pattern = re.compile(r'url_list_\d{14}\.txt$')
    url_file = max(filter(url_pattern.search, files))
    
    print("Using input: \n url_file: %s \n adid_file: %s" % (url_file, adid_file))

    
    with open("facebookAccessToken.txt", "r") as reader:
        facebookAccesToken = reader.read()
        
    sp.adImageScraper(url_filename = folder + url_file,
                      adid_filename = folder + adid_file,
                      facebookAccesToken = facebookAccesToken,
                      outputDir = 'output')
    
if __name__ == "__main__":
    main()        







