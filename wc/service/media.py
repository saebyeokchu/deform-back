import base64, requests, json

def header(user, password):
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header_json = {'Authorization': 'Basic ' + token.decode('utf-8')}
    return header_json

def upload_image_to_wordpress(file_path, url, header_json, mediaData):
    print("[media]")
    media = {
        'file': open(file_path,"rb"),
        'caption':  mediaData['imgUrl']
    }
    print(media)
    #'author' : mediaData['author']
    responce = requests.post(url + "wp-json/wp/v2/media", headers = header_json, files = media)
    print("responce",responce)
    return json.loads(responce.text)

class Media : 
    def upload(mediaData) :
        hed = header("user","MUBS 2xOA PboP dwK4 hpHQ DlK1") #username, application password       
        #'C://Users//cuu02//OneDrive//바탕 화면//deform//img//PIKA.png'    

        file_path = "C://Users//cuu02//Downloads//"+mediaData['imgUrl']+".jpeg"           
        return upload_image_to_wordpress(file_path, 'https://dawn-test.xyz/',hed,mediaData)

