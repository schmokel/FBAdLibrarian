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


import helpers

@click.command()
@click.argument('url_filename')
@click.argument('ad_id_filename')
@click.argument('output_dir')
def main(url_filename, ad_id_filename, output_dir):
             
    
    credentials = yaml.load(open(os.path.abspath('..') + '/Credentials.yaml'))
    
    # access values from dictionary
    access_token = credentials['facebook']['access_token']
    
    
    #load ad_id_list
    adlib_id_list = helpers.load_txt_to_list(str(ad_id_filename))
    

    url_list = helpers.load_txt_to_list(str(url_filename))
    url_list = helpers.clean_url(url_list, access_token)
    
    
    
    DRIVER_PATH = os.path.abspath('.') + r"/chromedriver.exe"
    wd = webdriver.Chrome(executable_path=DRIVER_PATH)
    api_block_string = "Blocked from Searching or Viewing the Ad Library"
    
    
    #creating file for metadata    
    if os.path.isfile('metadata.txt'):
        print("Warning! Metadata-file already exists. Appending")
            
    else:
        print('Creating metadata-file')
        with open("metadata.txt", 'w') as writer:
            writer.write("link, adid, content_type")
        writer.close()

        
        
    #url_list
    #adlib_id_list
    if len(url_list) == 0:
        print("All images has been scraped")
    if len(url_list) == len(adlib_id_list):
    

        #setting counter
        counter_max = len(url_list)
        counter = 0
        
        #copying lists to delete already scraped entries
        url_list_out = list(url_list)
        adid_list_out = list(adlib_id_list)
        
        
        for n in reversed(range(0, len(url_list))):
            content_type = "Unknown"
            success = False
            counter+=1
            print("Processing ad {} out of {}".format(counter, counter_max))
            try:
      

     
                from selenium.common.exceptions import NoSuchElementException
    
                #wd.get("https://www.facebook.com/ads/archive/render_ad/?id=803109676766123&access_token=EAAVoiDn8xHMBAG64X0JdLkF6rEyakzj6aNw06vsSa6sri1Onrc2URuZB88JMMZBK5cmwXCh0BVQO8D6gnhUS6RIMqn4oySvLDrlqtMuGZAZBHBZAEKWdOrzL1rZBp3Uv6XhpobTr4dbO2VcBZBBaU9mncHo7vNkYqhFQekMY2mQIsXZBloek7dZAwGuPvuZC2uHYbMEvxn4ZBm08iZBWN6v01hi7jP1MG97YViQ8o7xSoRJhP6xSZBuQVNKoZC")
                wd.get(url_list[n])
                
                #checking if session has been logged out
                try:
                    if wd.find_element_by_css_selector('div._70g9'):
                        
                        ts = datetime.now().strftime("%Y%m%d%H%M%S")
                        helpers.write_log(adid_list_out, "temp/adid_list_", ts)
                        helpers.write_log(url_list_out, "temp/url_list_", ts)
                        
                        raise helpers.CSSClassError("Writing log at {}".format(ts))
                        
                except NoSuchElementException:
                    pass
                
                #Checking if API has been blocked
                html_content = wd.page_source
                if api_block_string in html_content:
                      
                    ts = datetime.now().strftime("%Y%m%d%H%M%S")
                    helpers.write_log(adid_list_out, "temp/adid_list_", ts)
                    helpers.write_log(url_list_out, "temp/url_list_", ts)
                    
                    raise helpers.GeneralError("You have been locked out of the api")
                else:
                    pass
                        
                # Finding the actual image  
                try:
                    image_box = wd.find_element_by_css_selector('img._7jys')
                    
                
                    image_box.get_attribute('src') and 'http' in image_box.get_attribute('src')
                    image_url = image_box.get_attribute('src')

                    
                    helpers.save_image(output_path = str(output_dir),
                              image_url = image_url,
                              ad_id = adlib_id_list[n])
                    
                    content_type = 'image'
                
                except NoSuchElementException:
                    pass
                
                # Checking if video    
                try: 
                    if wd.find_element_by_css_selector("div._8o0a._8o05"):
                        content_type = 'video'
                    
                    
                except NoSuchElementException:
                    pass
         
            
                print("Content type: %s" % content_type)
            

            
            
                #deleting this entry from a copy of the lists
                del url_list_out[n]
                del adid_list_out[n]
            
                link = url_list[n]
                adid = adlib_id_list[n]
                
                
                with open("metadata.txt", 'a') as appender:
                    appender.write('\n')
                    for item in [link, adid, content_type]:
                        appender.write('%s, ' % item)
                        
                success = True
                
                
            except helpers.GeneralError:
                raise helpers.GeneralError("Unknown error")
            except KeyboardInterrupt:
                print("Program has been interrupted")
                print(str(KeyboardInterrupt))
                raise KeyboardInterrupt
            except requests.ConnectionError as e:
                print("Connection Error. Make sure you are connected to Internet")
                print(str(e))
                raise requests.ConnectionError
            finally:
                if success == False:
                    ts = datetime.now().strftime("%Y%m%d%H%M%S")
                    helpers.write_log(adid_list_out, "temp/adid_list_", ts)
                    helpers.write_log(url_list_out, "temp/url_list_", ts)
                    print("Writing log at {} \ns".format(ts))
                                    
                    
    
        
        
    else:
        print("Length of ad ID's is not equalto length of ad Url's")


if __name__ == "__main__":
    main()