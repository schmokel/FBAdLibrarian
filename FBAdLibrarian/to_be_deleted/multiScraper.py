# -*- coding: utf-8 -*-
"""
Created on Sat May  9 00:57:49 2020

@author: rasmu
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:16:29 2020

@author: rhs
"""
#https://www.facebook.com/ads/archive/render_ad/?id=626309958222260&access_token=EAAVoiDn8xHMBANJS3G4klvYAyf8qep0FGLQsZBbVUeuFQnyuOaKPIAj9oJpZCSK7MzdrFqLW3kZCARyWwxW2mUJo5Jlte6w8Gf3gMaY2ilhQPHBTHtZAovXFuiZCMI6brnG8jH53FWyASmt1oiELU4eFmvyTpr5vbHSQQnDoOvDhMHtHyPICKvdZBcLqfm0tfngGoZCBgEsyGCZAL4cwDS4IpDZCC6RiZCyjdswdPozln7edUyojQMh3IW

import selenium
from selenium import webdriver
#import openpyxl
import pandas as pd
import os
import io
import requests
from PIL import Image
import hashlib
import yaml
import click
from datetime import datetime
import pickle
import multiprocessing

#@click.command()
#@click.argument('url_filename')
#@click.argument('ad_id_filename')
#@click.argument('output_dir')

output_dir = r"C:\Users\rasmu\Documents\Repositories\AdsProject\adImageScraper\test"
    
ad_id_filename = r"logs\ad_lib_urls20200508_235819.txt"
url_filename= r"logs\url_list20200508_235819.txt"


      
def get_image_id(string):
    _, _, string = map(str.strip, string.partition('_'))
    string1, sep, string2 = map(str.strip, string.partition('_'))
    return string1

def persist_image(folder_path:str, image_url:str, ad_lib_url:str):
    
    try:
        image_content = requests.get(image_url).content

    except Exception as e:
        print(f"ERROR - Could not download {image_url} - {e}")
        raise Exception

    try:
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file).convert('RGB')
        file_path = os.path.join(folder_path, str(ad_lib_url) + '.jpg')
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print("SUCCESS - saved {}".format(str(ad_lib_url)))
    except Exception as e:
        print(f"ERROR - Could not save {image_url} - {e}")
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
            currentPlace = line[:-1]
            # add item to the list
            out_list.append(currentPlace)
    return out_list

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

   


    
def write_log(list_name, log_prefix, timestamp, n):
    with open(log_prefix + timestamp + ".txt", 'w') as filehandle:
        for listitem in list_name[n:]:
            filehandle.write('%s\n' % listitem)
        

credentials = yaml.load(open(os.path.abspath('..') + '\\Credentials.yaml'))

# access values from dictionary
access_token = credentials['facebook']['access_token']

#load ad_id_list
adlib_id_list_temp = load_txt_to_list(str(ad_id_filename))

adlib_id_list = []
for n in adlib_id_list_temp:
    adlib_id_list.append(int(n))
    
url_list = load_txt_to_list(str(url_filename))
url_list = clean_url(url_list, access_token)

#Getting name / ID's from alle the scraped images
already_scraped = os.listdir(str(output_dir))
#converting from string to int to be able to compare lists
temp = []
for n in range(len(already_scraped)):
    temp.append(int(already_scraped[n][:-4]))
already_scraped = temp    
#tjek = [x for x in adlib_id_list if x not in temp]

# Converting to dict to remove elements from urls and id's by index
#already_scraped = from_list_to_dict(temp)


adlib_id_list = from_list_to_dict(adlib_id_list)
adlib_id_list = filter_parent_dict(adlib_id_list, already_scraped)


#filtering the ad ids from the ad urls so it is the same
temp = []
for n in adlib_id_list.keys():
    temp.append(url_list[n])
url_list = temp

#converting dict back to list    
adlib_id_list = [ v for v in adlib_id_list.values() ]
                        


DRIVER_PATH = os.path.abspath('.') + r"\chromedriver.exe"
wd = webdriver.Chrome(executable_path=DRIVER_PATH)
api_block_string = "Blocked from Searching or Viewing the Ad Library"
#url_list
#adlib_id_list
if len(url_list) == 0:
    print("All images has been scraped")

def scraping(url_list, ad_id_list, output_dir):
    
   
    try:
  
        
        #print(url)
 
        from selenium.common.exceptions import NoSuchElementException

        
        #time.sleep(2)

        #wd.get("https://www.facebook.com/ads/archive/render_ad/?id=803109676766123&access_token=EAAVoiDn8xHMBAG64X0JdLkF6rEyakzj6aNw06vsSa6sri1Onrc2URuZB88JMMZBK5cmwXCh0BVQO8D6gnhUS6RIMqn4oySvLDrlqtMuGZAZBHBZAEKWdOrzL1rZBp3Uv6XhpobTr4dbO2VcBZBBaU9mncHo7vNkYqhFQekMY2mQIsXZBloek7dZAwGuPvuZC2uHYbMEvxn4ZBm08iZBWN6v01hi7jP1MG97YViQ8o7xSoRJhP6xSZBuQVNKoZC")
        wd.get(url_list)
        
        #checking if session has been logged out
        try:
            if wd.find_element_by_css_selector('div._70g9'):

                raise CSSClassError
                
        except NoSuchElementException:
            pass
        
        #Checking if API has been blocked
        html_content = wd.page_source
        if api_block_string in html_content == True:
              

            raise GeneralError("You have been locked out of the api")
        else:
            pass
                
           
        try:
            image_box = wd.find_element_by_css_selector('img._7jys')
            
        except NoSuchElementException:
            print("No image - continuing")

        
        
        
        if image_box.get_attribute('src') and 'http' in image_box.get_attribute('src'):
            image_url = image_box.get_attribute('src')
            adlib_id = adlib_id_list[n]
            
            
            
            persist_image(folder_path = str(output_dir),
                      image_url = image_url,
                      ad_lib_url = adlib_id)
            
   
        

        
    except GeneralError:
        raise GeneralError

    except KeyboardInterrupt:
 
        print(str(KeyboardInterrupt))
        raise KeyboardInterrupt
    except requests.ConnectionError:
     
        raise requests.ConnectionError
    
    
    wd.close()           

    
    
    #else:
   #     print("Length of ad ID's is not equalto length of ad Url's")
        
if len(url_list) == len(adlib_id_list):
        
    #resolved_urls = []
    output_list = [output_dir for n in range(len(url_list))]
    argumentList = [url_list, adlib_id_list, output_list]
    #argument = []
    #argument[0] = url_list
   # argument[1] = adlib_id_list
   # argument[2] = [output_dir]
    
    pool = multiprocessing.Pool(4)
    res = pool.imap(scraping, argumentList)

    
    for n in res:
        print(n)
 #       ts = datetime.now().strftime("%Y%m%d_%H%M%S")
#        write_log(adlib_id_list, "logs/ad_lib_urls", ts, n)
 #       write_log(url_list, "logs/url_list", ts, n)

pool.terminate()    

#if __name__ == "__main__":
#    main()
