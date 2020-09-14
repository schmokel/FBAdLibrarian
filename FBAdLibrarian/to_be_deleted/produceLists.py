# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:35:53 2020

@author: rasmu
"""

import pandas as pd
import os

datafile = r"C:\Users\rasmu\Documents\Repositories\AdsProject\adImageScraper\Data\Ads 110568-221136 Michael.xlsx"
data = pd.read_excel(datafile)


adlib_id_list = list(data['adlib_id'])

url_list = list(data['ad_snapshot_url'])
#url_list = url_list[:500]
#adlib_id_list = adlib_id_list[:500]

with open("url_110568-221136.txt", 'w') as filehandle:
    for listitem in url_list:
        filehandle.write('%s\n' % listitem)

with open("adid_110568-221136.txt", 'w') as filehandle:
    for listitem in adlib_id_list:
        filehandle.write('%s\n' % listitem)

import re

temp = []
for url in range(len(url_list)):
    res = re.search('\?id=(.+?)&access_token', url_list[url])
    if res:
        temp.append(int(res.group(1)))
       

comparison = [i for i, j in zip(temp, adlib_id_list) if i == j]



