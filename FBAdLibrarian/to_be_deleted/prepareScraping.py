# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:34:53 2020

@author: rasmu
"""

import click
import pandas as pd
import os
import yaml
from datetime import datetime

@click.command()
@click.argument('datafile')
def main(datafile):
    

    data = pd.read_excel(str(datafile))
    
    
    adlib_id_list = list(data['adlib_id'])
    
    url_list = list(data['ad_snapshot_url'])

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    with open("temp/url_list_" + timestamp + ".txt", 'w') as filehandle:
        for listitem in url_list:
            filehandle.write('%s\n' % listitem)
    
    with open("temp/adid_list_" + timestamp + ".txt", 'w') as filehandle:
        for listitem in adlib_id_list:
            filehandle.write('%s\n' % listitem)
            
if __name__ == "__main__":
    main()        