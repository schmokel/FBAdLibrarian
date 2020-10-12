# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:16:29 2020
@author: rhs
"""

from selenium import webdriver
import requests
from datetime import datetime
#import chromedriver_autoinstaller

from webdriver_manager.chrome import ChromeDriverManager
import FBAdLibrarian.helpers as helpers


def adImageScraper(url_filename, adid_filename, facebookAccesToken, outputDir):

    
    #load ad_id_list
    adlib_id_list = helpers.load_txt_to_list(str(adid_filename))
    
    url_list = helpers.load_txt_to_list(str(url_filename))
    url_list = helpers.clean_url(url_list, facebookAccesToken)

 
    wd = webdriver.Chrome(ChromeDriverManager().install())

    #DRIVER_PATH = os.path.abspath('.') + r"/chromedriver.exe"
    #wd = webdriver.Chrome(executable_path=DRIVER_PATH)
    api_block_string = "Blocked from Searching or Viewing the Ad Library"
    


        
        
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
            #print('Length of url_list_out: %s' % len(url_list_out))
            #print('Length of adid_list_out: %s' % len(adid_list_out))
            
            content_type = "Unknown"
            success = False
            counter+=1
            print("Processing ad {} out of {}".format(counter, counter_max))
            try:
      

     
                from selenium.common.exceptions import NoSuchElementException
    
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
                      
                    raise helpers.GeneralError("You have been locked out of the api")
                else:
                    pass
                        
                # Finding the actual image  
                try:
                    image_box = wd.find_element_by_css_selector('img._7jys')
                    
                
                    image_box.get_attribute('src') and 'http' in image_box.get_attribute('src')
                    image_url = image_box.get_attribute('src')

                    
                    helpers.save_image(output_path = str(outputDir),
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

                url_list_out, adid_list_out = helpers.delete_scraped_element(
                    url_list_out = url_list_out,
                    adid_list_out = adid_list_out, 
                    n = n)

                #Setting objects
                link = url_list[n]
                adid = adlib_id_list[n]
                
                
                with open("metadata.txt", 'a') as appender:
                    appender.write('\n')
                    for item in [link, adid, content_type]:
                        appender.write('%s,' % item)
                        
                success = True
                
                
            except helpers.GeneralError:
                raise helpers.GeneralError("Unknown error")

            except KeyboardInterrupt:
                print("Program has been interrupted")
                print(str(KeyboardInterrupt))
                raise KeyboardInterrupt

            except requests.ConnectionError as e:
                print("Connection Error. Make sure you are connected to the internet")
                print(str(e))
                raise requests.ConnectionError

            finally:
                    if success == False:
                        ts = datetime.now().strftime("%Y%m%d%H%M%S")
                        helpers.write_log(adid_list_out, "temp/adid_list_", ts)
                        helpers.write_log(url_list_out, "temp/url_list_", ts)
                        print("Writing log at {} \n".format(ts))
                                    
                        
    
    else:
        print("Length of ad ID's is not equal to length of ad Url's")


