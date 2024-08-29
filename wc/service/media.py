import base64, requests, json

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def upload_image_to_wordpress(file, url, header_json, userId):
    print("[media]")
    #  'file': open(file_path,"rb"),
    #    'file' : mediaData['imgUrl'],

    media = {
        'file': file,
        'caption':  'custom-work' #고유 구분 값을 해야할까?
    }

    data = {
        'author': userId,  # Set the author ID
    }
    #'author' : mediaData['author']
    responce = requests.post(url + "wp-json/wp/v2/media", headers = header_json, files = media, data = data)
    print("responce",responce)
    return json.loads(responce.text)

class Media : 
    def upload(mediaData) :
        hed = header("user","MUBS 2xOA PboP dwK4 hpHQ DlK1") #username, application password       
        #'C://Users//cuu02//OneDrive//바탕 화면//deform//img//PIKA.png'    

        # file_path = "C://Users//cuu02//Downloads//"+mediaData['imgUrl']+".jpeg"           
        return upload_image_to_wordpress(mediaData["file"], 'https://dawn-test.xyz/',hed,mediaData["userId"])
    
    def getByAuthor(userId):
        api_url = 'https://dawn-test.xyz/wp-json/wp/v2/media?author='+userId
        print(api_url)
        response = requests.get(api_url)
        response_json = response.json()
        print(response_json)
        return response_json

