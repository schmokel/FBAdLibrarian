
import requests
import json

#https://developers.facebook.com/docs/marketing-api/reference/ads_archive/
#https://developers.facebook.com/docs/apps/features-reference#reference-PAGES_ACCESSS
#https://developers.facebook.com/docs/marketing-api/campaign-structure
#https://developers.facebook.com/docs/graph-api/using-graph-api/#paging
#https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing
#https://facebookresearch.github.io/Radlibrary/articles/Radlibrary.html

class AdLib:
    

    def __init__(self, access_token, version = "v9.0"):
        self.version = version
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/{version}/ads_archive?access_token={access_token}".format(version = self.version, access_token = self.access_token)
        self.fields = self.get_fields()
        self.request_headers = {}
        self.request_url = None


    def add_parameters(self, **kwargs):
        """
        Add parameters for your Ads search.
        See available fields here: https://developers.facebook.com/docs/marketing-api/reference/ads_archive/

        Example
        -------
                
        >>> ads = api.AdLib("your_access_token")
        >>> ads.add_parameters(ad_delivery_date_min = "2020-01-01", ad_delivery_date_max = "2020-06-06")
        >>> ads.info()
        'https://graph.facebook.com/9.0/ads_archive?access_token=your_access_token&ad_delivery_date_min=2020-01-01&ad_delivery_date_max=2020-06-06'


        """
        kwargs.update(fields = self.get_fields())
        self.request_headers = kwargs
        #self.request_headers += ["&{key}={value}".format(key = str(key), value = str(value)) for key, value in kwargs.items()]



    def _query_builder(self):
        return self.base_url + "".join(self.request_headers)

    def get(self):
        """request and get the response. 
        Remember to add parameters first using the add_parameters method
        """
        
        response = requests.get(self.base_url, params = self.request_headers)
        
        if response.status_code == 200:
            data = response.json()['data']

            while 'paging' in response:
                response = requests.get(response['paging']['next']).json()
                data += response['data']

            return data
        
        else:
            try:
                raise ValueError("Status code {}: {}. {}".format(response.status_code, 
            json.loads(response.text)['error']['error_user_title'],
            json.loads(response.text)['error']['error_user_msg']))
            except:
                raise ValueError(json.loads(response.text)['error']['message'])


    def response(self):
        
        return requests.get(self.base_url, params = self.request_headers)

 
    def get_longlived_token(self, app_id, app_secret, access_token):
        """
        Access token that lasts for 60 days
        app_id:
            same as client_id
        app_secret:
            description of argument
        access_token:
            short lived access_token

        """
        NotImplementedError


    def info(self):
        "inspect the HTTP URL before requesting"
        return self._query_builder()

    def get_fields(self):
        return ("id,ad_creation_time,ad_creative_body,ad_creative_link_caption"
        + ",ad_creative_link_description,ad_creative_link_title,ad_delivery_start_time,ad_delivery_stop_time"
        + ",ad_snapshot_url,currency,demographic_distribution,funding_entity,impressions"
        + ",page_id,page_name,potential_reach,publisher_platforms,region_distribution,spend"
        )