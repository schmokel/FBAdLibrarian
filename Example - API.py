# -*- coding: utf-8 -*-


from FBAdLibrarian import api
import pandas as pd

ads = api.AdLib("INSERT-ACCESS-TOKEN",
                version='v10.0')


#add parameters for your search
# For available parameters, visit https://developers.facebook.com/docs/marketing-api/reference/ads_archive/v9.0
ads.add_parameters(ad_delivery_date_min = "2021-01-01", ad_delivery_date_max = "2021-01-05", ad_type = "POLITICAL_AND_ISSUE_ADS",
                   ad_reached_countries = 'US', ad_active_status = "ALL", impression_condition = 'HAS_IMPRESSIONS_LAST_90_DAYS',
                   search_terms = "Biden")


# get the data
df = ads.get()

# if you wanna do pandas, you just do pandas
df2 = pd.DataFrame(df)



#%%


