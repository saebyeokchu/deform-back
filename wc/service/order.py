import json
import os
import requests
import base64
import logging
import datetime
from woocommerce import API

class Order : 
    def create(newPost) :
        #crendtials
        username = 'user'
        password = 'MUBS 2xOA PboP dwK4 hpHQ DlK1'
        credentials = username + ':' + password
        cred_token = base64.b64encode(credentials.encode())

        #code
        header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}
        data = {
            'title' : newPost['title'] ,
            'author' : newPost['author'],
            'status': 'publish',
            'slug' : 'custom-work',
            # 'content': newPost['content'] ,
            'content': "<img src=\""+newPost['contentImgUrl']+"\" /> <br /> <p>"+newPost['content']+"</p>",
            'featured_media' : newPost['featured_media'] 
        }

        response = requests.post('https://dawn-test.xyz/wp-json/wp/v2/posts', headers=header, json=data)
        os.remove( newPost['deleteImgUrl'] )
        
        return json.loads(response.text)

    def make(orderData):
        consumer_key = "ck_a4c80ba803896185c152917c831cae9d8ff12c6a"
        consumer_secret = "cs_75c9402c341a5dab93b8483b4dd2ac9a65891da0"

        wcapi = API(
            url="https://dawn-test.xyz",
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            wp_api=True,
            version="wc/v3"
        )

        return wcapi.post("orders", orderData).json()

