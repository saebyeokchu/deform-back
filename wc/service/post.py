import json
import requests
import base64

from .api import wordpressPostAPI, wordpressPutAPI
from ..enums import Constant

class PostService : 
    def create(newPost) :
        data = {
            'title' : newPost['title'] ,
            'author' : newPost['author'],
            'status': 'publish',
            'slug' : 'custom-work',
            # 'content': newPost['content'] ,
            'content': "<img src=\""+newPost['image_url']+"\" />",
            'featured_media' : newPost['featured_media'] 
        }

        response = wordpressPostAPI('/wp-json/wp/v2/posts', data)
        # os.remove( newPost['deleteImgUrl'] )
        return json.loads(response.text)

    def read(postId):
        api_url = Constant.wordpress_url + '/wp-json/wp/v2/posts/' + postId
        response = requests.get(api_url)
        return response.json()

    def update(data):
        category_id = 1 if data["showPost"] else 2
        data = {
            'categories': [category_id]  # 1 for show, 2 for hide
        }

        # Making the PUT request to update the post
        response = wordpressPutAPI( '/wp-json/wp/v2/posts/' +  data["postId"] , data )
        return response.json()


