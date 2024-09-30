import json
import requests
import base64

from .api import wordpressDeleteAPI, wordpressPostAPI, wordpressPutAPI
from ..enums import Constant

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode(''))
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

class PostService : 
    def create(newPost) :
        data = {
            'title' : newPost['title'],
            'author' : newPost['author'],
            'status': 'publish',
            'slug' : 'custom-work-hide',
            # 'content': newPost['content'] ,newPost['author']
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
        category_id = Constant.user_share_category if data["showPost"] == 1 else Constant.user_order_category  # 1 for 사용자공유작품, 2 for 사용자주문작품

        # Making the PUT request to update the post
        print("1",data)
        print("2",{ 'categories': [category_id] })
        response = wordpressPutAPI( '/wp-json/wp/v2/posts/' +  str(data["postId"]) , { 'categories': [category_id] })
        print(response)

        return response.json()
    
    def delete(postId):
        print(postId)

        response = wordpressDeleteAPI( '/wp-json/wp/v2/posts/'+postId)
        return response.json()
    

