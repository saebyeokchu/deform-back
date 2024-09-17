from woocommerce import API
from ..enums import Constant
from dotenv import load_dotenv
load_dotenv()
import os

import json
import requests
import base64

def sendWoocommerceAPI() :
    wcapi = API(
            url=Constant.woocommerce_url,
            consumer_key=os.environ.get('WOOCOMMERCE_CONSUMER_KEY'),
            consumer_secret=os.environ.get('WOOCOMMERCE_CONSUMER_SECRET'),
            wp_api=True,
            version="wc/v3"
        )
    
    return wcapi

def wordpressPostAPI(sendUrl, sendData) :
    #crendtials
    credentials = os.environ.get('WORDPRESS_USER_KEY') + ':' + os.environ.get('WORDPRESS_USER_NAME')
    cred_token = base64.b64encode(credentials.encode())

    #code
    header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

    return requests.post(Constant.wordpress_url + sendUrl, headers=header, json=sendData)
    # os.remove( newPost['deleteImgUrl'] )


def wordpressPutAPI(sendUrl, sendData) :
    #crendtials
    credentials = os.environ.get('WORDPRESS_USER_KEY') + ':' + os.environ.get('WORDPRESS_USER_NAME')
    cred_token = base64.b64encode(credentials.encode())

    #code
    header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

    return requests.put(Constant.wordpress_url + sendUrl, headers=header, json=sendData)
    # os.remove( newPost['deleteImgUrl'] )