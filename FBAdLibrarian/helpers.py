# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 16:31:31 2020

@author: rasmu
"""
import os
import pickle
from PIL import Image
#from datetime import datetime
import io
import requests

def delete_downloaded_element(url_list_out, adid_list_out, n):
    del url_list_out[n]
    del adid_list_out[n]
    return url_list_out, adid_list_out

def save_image(output_path:str, image_url:str, ad_id:str):
    
    try:
        image_content = requests.get(image_url).content
    
    except Exception:
        raise Exception
    
    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(output_path, str(ad_id) + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print("Completed - saved {}".format(str(ad_id)))
        
    except Exception:
        raise Exception
        
        

def from_list_to_dict(_dict):
    return { i : _dict[i]
            for i in range(0, len(_dict))}

def filter_parent_dict(parent_dict, derived_list):
    #remove values from parent_dict that are in derived_dict
    return {k: v for k, v in parent_dict.items() if v not in derived_list}

def load_txt_to_list(list_name:str):
    out_list = []              
    with open(list_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            line = line.replace('\n', '')
            # add item to the list
            out_list.append(line)
        lines = [line for line in out_list if line is not '']
    return lines


class CSSClassError(Exception):
    """The image class isn't in link"""
    
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
        self.standard = "CSSClassError"
    
    def __str__(self):
        if self.message:
            return "You are requesting the login page. CSSClassError has been raised {0}".format(self.message)
        else:
            return "You are requesting the login page. CSSClassError has been raised."
        
class GeneralError(Exception):
    """The image class isn't in link"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
        self.standard = "CSSClassError"
    
    def __str__(self):
        if self.message:
            return "General error has been catched {0}".format(self.message)
        else:
            return "General error has been catched"

def clean_url(url_list, access_token):
    temp = []
    for url in range(len(url_list)):
        temp.append(url_list[url].split('access_token=', 1)[0] + "access_token=" + access_token)
    return temp

   

    
def write_log(list_name, log_prefix, timestamp):
    with open(log_prefix + timestamp + ".txt", 'w') as filehandle:
        for listitem in list_name:
            filehandle.write('%s\n' % listitem) 
