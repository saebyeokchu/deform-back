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

        print(data)

        response = requests.post('https://dawn-test.xyz/wp-json/wp/v2/posts', headers=header, json=data)
        # os.remove( newPost['deleteImgUrl'] )
        
        return json.loads(response.text)

    def read(postId):
        api_url = 'https://dawn-test.xyz/wp-json/wp/v2/posts/' + postId
        print(api_url)
        response = requests.get(api_url)
        response_json = response.json()
        return response_json

    def update(data):
        post_id = data["postId"]
        show_post = data["showPost"]

        print(post_id)
        print(show_post)

        #crendtials
        username = 'user'
        password = 'MUBS 2xOA PboP dwK4 hpHQ DlK1'
        credentials = username + ':' + password
        cred_token = base64.b64encode(credentials.encode())

        #code
        header = {'Authorization': 'Basic ' + cred_token.decode('utf-8')}

        # Endpoint for the specific post
        api_url = 'https://dawn-test.xyz/wp-json/wp/v2/posts'
        url = f"{api_url}/{post_id}"
        
        # Data payload to update the category

        category_id = 1 if show_post else 30
        data = {
            'categories': [category_id]  # 1 for show, 2 for hide
        }

        print(category_id, data)
        
        # Making the PUT request to update the post
        response = requests.put(
            url,
            json=data,
            headers=header
        )
        
        return response.json()


