import base64, requests, json

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def upload_image_to_wordpress(file, url, header_json, author, title):
    print("[media]")
    #  'file': open(file_path,"rb"),
    #    'file' : mediaData['imgUrl'],

    media = {
        'file': file,
        'caption':  'custom-work' #고유 구분 값을 해야할까?
    }

    data = {
        'title' : title,
        'author': author,  # Set the author ID
    }
    #'author' : mediaData['author']
    responce = requests.post(url + "wp-json/wp/v2/media", headers = header_json, files = media, data = data)
    print("responce",responce)
    return json.loads(responce.text)

class Media : 
    def __init__(self):
        self.hed = header("user","MUBS 2xOA PboP dwK4 hpHQ DlK1")
        self.url = 'https://dawn-test.xyz'

    def delete_media(mediaId) :
        hed = header("user","MUBS 2xOA PboP dwK4 hpHQ DlK1")
        url = 'https://dawn-test.xyz'
        responce = requests.delete(url + "/wp-json/wp/v2/media/"+mediaId, headers = hed)
        return responce

    def upload(mediaData) :
        hed = header("user","MUBS 2xOA PboP dwK4 hpHQ DlK1")
        url = 'https://dawn-test.xyz'
        return upload_image_to_wordpress(mediaData["file"], 'https://dawn-test.xyz/',hed,mediaData["author"],mediaData["title"])
    
    def getByAuthor(author):
        api_url = 'https://dawn-test.xyz/wp-json/wp/v2/media?author='+author
        print(api_url)
        response = requests.get(api_url)
        response_json = response.json()
        print(response_json)
        return response_json

