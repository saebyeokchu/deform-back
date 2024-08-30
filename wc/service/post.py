import json
import os
import requests
import base64
import logging
import datetime

class Post : 
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
            'content': "<img src=\""+newPost['image_url']+"\" />",
            'featured_media' : newPost['featured_media'] 
        }

        response = requests.post('https://dawn-test.xyz/wp-json/wp/v2/posts', headers=header, json=data)
        # os.remove( newPost['deleteImgUrl'] )
        
        return json.loads(response.text)

    def read():
        api_url = 'https://dawn-test.xyz/wp-json/wp/v2/posts'
        print(api_url)
        response = requests.get(api_url)
        response_json = response.json()
        print(response_json)

