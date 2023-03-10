# -*- coding: utf-8 -*-


from FBAdLibrarian import api
import pandas as pd

ads = api.AdLib("fb-access-token-here",
                version='v16.0')


#add parameters for your search
# For available parameters, visit https://developers.facebook.com/docs/marketing-api/reference/ads_archive/v9.0
# ads.add_parameters(ad_delivery_date_min = "2023-01-01", ad_delivery_date_max = "2023-01-05", ad_type = "POLITICAL_AND_ISSUE_ADS",
#                    ad_reached_countries = ['US'], ad_active_status = "ALL", impression_condition = 'HAS_IMPRESSIONS_LAST_90_DAYS',
#                    search_terms = "Biden")



ads.add_parameters(ad_reached_countries=['US'], search_terms='California', ad_type='POLITICAL_AND_ISSUE_ADS')

#https://graph.facebook.com/<VERSION>/ads_archive?access_token=<ACCESS_TOKEN>&fields=page_id,page_name,ad_snapshot_url&search_terms='california'&ad_type=POLITICAL_AND_ISSUE_ADS&ad_reached_countries=['US']

# get the data
data = ads.get()

# if you wanna do pandas, you just do pandas
df = pd.DataFrame(data)



#%%


