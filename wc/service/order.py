import json
from .api import sendWoocommerceAPI, wordpressPostAPI

class OrderService : 
    def create(newPost) :
        #code
        data = {
            'title' : newPost['title'] ,
            'author' : newPost['author'],
            'status': 'publish',
            'slug' : 'custom-work',
            # 'content': newPost['content'] ,
            'content': "<img src=\""+newPost['contentImgUrl']+"\" /> <br /> <p>"+newPost['content']+"</p>",
            'featured_media' : newPost['featured_media'] 
        }

        response = wordpressPostAPI('/wp-json/wp/v2/posts', data)
        
        return json.loads(response.text)

    def make(orderData):
        wcapi = sendWoocommerceAPI()
        return wcapi.post("orders", orderData).json()

