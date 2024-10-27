import base64, requests, json
from ..enums import Constant
from dotenv import load_dotenv
load_dotenv()
import os

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def upload_image_to_wordpress(file, url, header_json, author, title):
    media = {
        'file': file,
        'caption':  'custom-work' 
    }

    data = {
        'title' : title,
        'author': author,  
    }

    responce = requests.post(url + "/wp-json/wp/v2/media", headers = header_json, files = media, data = data)
    return json.loads(responce.text)

class MediaService : 
    def __init__(self):
        self.hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
        self.url = Constant.wordpress_url

    def delete_media(mediaId) :
        hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
        url = Constant.wordpress_url
        responce = requests.delete(url + "/wp-json/wp/v2/media/"+mediaId, headers = hed)
        print(responce)
        return responce

    def upload(mediaData) :
        print(mediaData)
        hed = header(os.environ.get('WORDPRESS_USER_NAME'),os.environ.get('WORDPRESS_USER_KEY'))
        print(mediaData)
        return upload_image_to_wordpress(mediaData["file"], Constant.wordpress_url ,hed,mediaData["author"],mediaData["title"])
    
    def getByAuthor(author):
        api_url = Constant.wordpress_url + '/wp-json/wp/v2/media?author=' + author
        print(api_url)
        response = requests.get(api_url)
        return response.json()

