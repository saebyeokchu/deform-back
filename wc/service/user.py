from woocommerce import API

from .api import sendWoocommerceAPI

from ..models import auth
from ..serializers import authSerializer
from ..enums import Constant

from dotenv import load_dotenv
load_dotenv()
import os

class UserService :
    def get(userId) :
        wcapi = sendWoocommerceAPI()
        print(wcapi)
        return wcapi.get("customers/"+userId).json()

    def get_auth(userId, token) :
        try : 
            item = auth.objects.filter(userid = userId, token=token, verified = False)
            serializer = authSerializer(item, many=True)
            return serializer.data
        except :
            return RuntimeError
    
    def update_auth(userId, token) :
        try :
            print("userId",userId,token)
            item = auth.objects.filter(userid=userId,token=token).first()
            if item :
                item.verified = True
                item.save()
                serializer = authSerializer(item)
                return serializer.data
        except :
            return RuntimeError
    
    def add_auth(auth_input : auth) :
        try :
            auth_input.save()
            serializer = authSerializer(auth_input)
            return serializer.data
        except :
            return RuntimeError
    
    def delete_auth(userId) :
        try :
            item = auth.objects.get(
                userid = userId, 
                verified = True
            )
            if item :
                item.delete()
            return True
        except :
            return RuntimeError
    
    def delete_auth_all(userId) :
        try :
            auth.objects.filter(userid=userId).delete()
            return True
        except :
            return RuntimeError