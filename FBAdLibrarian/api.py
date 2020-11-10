
import requests

#https://developers.facebook.com/docs/marketing-api/reference/ads_archive/
#https://developers.facebook.com/docs/apps/features-reference#reference-PAGES_ACCESSS
#https://developers.facebook.com/docs/marketing-api/campaign-structure
#https://developers.facebook.com/docs/graph-api/using-graph-api/#paging
#https://developers.facebook.com/docs/facebook-login/access-tokens/refreshing
#https://facebookresearch.github.io/Radlibrary/articles/Radlibrary.html

class AdLib:

    

    def __init__(self, access_token):
        self.version = 9.0
        self.access_token = access_token
        self.base_url = "https://graph.facebook.com/{version}/ads_archive?access_token={access_token}".format(version = self.version, access_token = self.access_token)
        self.request_headers = []
        self.request_url = None

        self.api_parameters = ["ad_active_status", "ad_delivery_date_min", "ad_delivery_date_max",
        "ad_reached_countries", "ad_type", "bylines", "delivery_by_region",
        "potential_reach_min", "potential_reach_max", "publisher_platforms", "search_page_ids", "search_terms"]
        

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
        
        self.request_headers += ["&{key}={value}".format(key = str(key), value = str(value)) for key, value in kwargs.items()]


    def _query_builder(self):
        return self.base_url + "".join(self.request_headers)

    def get(self):
        """request and get the response. 
        Remember to add parameters first using the add_parameters method
        """
        return requests.get(self._query_builder())

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

