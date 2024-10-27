from woocommerce import API
from ..enums import Constant
from dotenv import load_dotenv
load_dotenv()
import os

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

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def wordpressPostAPI(sendUrl, sendData) :
    hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
    return requests.post(Constant.wordpress_url + sendUrl, headers=hed, json=sendData)

def wordpressPutAPI(sendUrl, sendData) :
    hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
    return requests.put(Constant.wordpress_url + sendUrl, headers=hed, json=sendData)

def wordpressDeleteAPI(sendUrl) :
    print(sendUrl)
    hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
    responce = requests.delete(Constant.wordpress_url + sendUrl, headers = hed)
    return responce

